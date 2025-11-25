#!/usr/bin/env python3
"""
Gemini Research - Pesquisa via Gemini API para autores/livros.

Usa modelo gemini-3-pro-preview com:
- Sistema de cache (30 dias)
- Fallback indicator para WebSearch

Usage:
    python gemini_research.py author "<nome>" [--output json|markdown]
    python gemini_research.py book "<título>" --author "<autor>"
    python gemini_research.py --clear-cache  # Limpa cache expirado

Requer:
    GEMINI_API_KEY no ambiente
"""

import os
import sys
import json
import argparse
import hashlib
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional


# Configuração do modelo
GEMINI_MODEL = "gemini-3-pro-preview"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

# Cache configuration
CACHE_DIR = Path(__file__).parent.parent.parent.parent.parent / "_utils" / "cache"
CACHE_EXPIRY_DAYS = 30


def get_cache_path(query: str, query_type: str) -> Path:
    """Gera path do cache baseado no tipo e query."""
    # Normalizar nome para filename seguro
    safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in query.lower())
    safe_name = safe_name.replace(' ', '_')[:50]

    subdir = "authors" if query_type == "author" else "books"
    return CACHE_DIR / subdir / f"{safe_name}.json"


def check_cache(query: str, query_type: str) -> Optional[Dict]:
    """Verifica se existe cache válido."""
    cache_path = get_cache_path(query, query_type)

    if not cache_path.exists():
        return None

    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            cached = json.load(f)

        # Verificar expiração
        cached_date = datetime.fromisoformat(cached.get('cached_at', '2000-01-01'))
        if datetime.now() - cached_date > timedelta(days=CACHE_EXPIRY_DAYS):
            print(f"⚠️ Cache expirado para: {query}", file=sys.stderr)
            return None

        print(f"✅ Usando cache para: {query} (de {cached_date.strftime('%Y-%m-%d')})", file=sys.stderr)
        return cached

    except Exception as e:
        print(f"⚠️ Erro lendo cache: {e}", file=sys.stderr)
        return None


def save_cache(query: str, query_type: str, result: Dict) -> None:
    """Salva resultado no cache."""
    cache_path = get_cache_path(query, query_type)

    # Garantir diretório existe
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    result['cached_at'] = datetime.now().isoformat()
    result['cache_query'] = query
    result['cache_type'] = query_type

    try:
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"💾 Cache salvo: {cache_path.name}", file=sys.stderr)
    except Exception as e:
        print(f"⚠️ Erro salvando cache: {e}", file=sys.stderr)


def clear_expired_cache() -> int:
    """Remove arquivos de cache expirados."""
    removed = 0

    for subdir in ['authors', 'books']:
        cache_subdir = CACHE_DIR / subdir
        if not cache_subdir.exists():
            continue

        for cache_file in cache_subdir.glob('*.json'):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cached = json.load(f)

                cached_date = datetime.fromisoformat(cached.get('cached_at', '2000-01-01'))
                if datetime.now() - cached_date > timedelta(days=CACHE_EXPIRY_DAYS):
                    cache_file.unlink()
                    removed += 1
                    print(f"🗑️ Removido: {cache_file.name}", file=sys.stderr)
            except Exception:
                continue

    return removed


def get_api_key() -> Optional[str]:
    """Obtém API key do ambiente."""
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        print("⚠️ GEMINI_API_KEY não definida - fallback para WebSearch", file=sys.stderr)
        return None
    return key


def call_gemini(prompt: str, max_tokens: int = 8192, temperature: float = 0.7) -> Optional[Dict]:
    """Faz chamada para Gemini API."""
    api_key = get_api_key()

    if not api_key:
        return None

    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }
    }

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={api_key}",
            headers={'Content-Type': 'application/json'},
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            print(f"⚠️ Erro API Gemini: {response.status_code}", file=sys.stderr)
            print(f"   Response: {response.text[:200]}", file=sys.stderr)
            return None

        data = response.json()

        # Extrair texto da resposta
        if 'candidates' in data and data['candidates']:
            content = data['candidates'][0].get('content', {})
            parts = content.get('parts', [])
            if parts:
                return {
                    'success': True,
                    'text': parts[0].get('text', ''),
                    'model': GEMINI_MODEL
                }

        return None

    except requests.exceptions.Timeout:
        print("⚠️ Timeout na chamada Gemini API", file=sys.stderr)
        return None
    except Exception as e:
        print(f"⚠️ Erro na chamada Gemini: {e}", file=sys.stderr)
        return None


def research_author(author: str, use_cache: bool = True) -> Dict:
    """Pesquisa completa sobre um autor."""

    # 1. Verificar cache
    if use_cache:
        cached = check_cache(author, "author")
        if cached:
            cached['from_cache'] = True
            return cached

    # 2. Tentar Gemini
    prompt = f"""Provide comprehensive research on {author} including:

1. BIOGRAPHY:
   - Full name, birth date and place
   - Education and academic background
   - Career milestones and key life events
   - Current status/activities

2. WORKS:
   - All major books with publication years
   - Key articles, papers, or other contributions
   - Most influential/popular works

3. PHILOSOPHY & IDEAS:
   - Core concepts and frameworks
   - Main methodologies
   - Worldview and beliefs
   - Key principles

4. COMMUNICATION STYLE:
   - Writing style characteristics
   - Rhetoric and tone of voice
   - Signature phrases or expressions

5. VALUES & PRINCIPLES:
   - Stated values
   - Ethical positions
   - Life philosophy

6. CONTEXT:
   - Influences and mentors
   - Contemporaries and peers
   - Critics and controversies
   - Impact and legacy

7. TOP 10 QUOTES:
   - Most famous or representative quotes
   - With context when possible

8. RESOURCES:
   - Official website
   - Wikipedia page
   - Key interviews or podcasts
   - Social media presence

Be comprehensive, accurate, and cite sources where possible.
Format the response in clear sections with markdown headers."""

    result = call_gemini(prompt)

    if result and result['success']:
        output = {
            'success': True,
            'author': author,
            'research': result['text'],
            'model': result['model'],
            'from_cache': False
        }
        # Salvar no cache
        save_cache(author, "author", output)
        return output

    # 3. Fallback - indicar para usar WebSearch
    return {
        'success': False,
        'author': author,
        'error': 'Gemini indisponível',
        'fallback': True,
        'fallback_action': 'USE_WEBSEARCH',
        'fallback_queries': [
            f'"{author}" biography books philosophy',
            f'"{author}" quotes interviews podcasts',
            f'"{author}" wikipedia'
        ]
    }


def research_book(title: str, author: str, use_cache: bool = True) -> Dict:
    """Pesquisa informações sobre um livro."""

    cache_key = f"{title}_{author}"

    # 1. Verificar cache
    if use_cache:
        cached = check_cache(cache_key, "book")
        if cached:
            cached['from_cache'] = True
            return cached

    # 2. Tentar Gemini
    prompt = f"""Provide comprehensive information about the book "{title}" by {author}:

1. BASIC INFO:
   - Full title
   - Author(s)
   - Publication year
   - Publisher
   - Number of pages
   - ISBN if available
   - Genre/Category

2. SUMMARY:
   - Main thesis/argument (2-3 paragraphs)
   - Key concepts introduced
   - Structure overview (chapters/parts)

3. KEY IDEAS (5-10):
   - Most important concepts
   - Frameworks or models
   - Memorable insights

4. QUOTES (10-15):
   - Most impactful quotes from the book
   - With page numbers if possible

5. AUTHOR CONTEXT:
   - Why the author wrote this book
   - How it fits in their body of work
   - Background that influenced it

6. RECEPTION:
   - Critical reception
   - Awards or recognition
   - Controversies if any

7. RELATED:
   - Similar books
   - Books that influenced it
   - Books it influenced

8. RESOURCES:
   - Official page
   - Author's website
   - Key reviews or interviews about the book

Be accurate and cite sources where possible.
Format with clear markdown sections."""

    result = call_gemini(prompt)

    if result and result['success']:
        output = {
            'success': True,
            'title': title,
            'author': author,
            'research': result['text'],
            'model': result['model'],
            'from_cache': False
        }
        # Salvar no cache
        save_cache(cache_key, "book", output)
        return output

    # 3. Fallback - indicar para usar WebSearch
    return {
        'success': False,
        'title': title,
        'author': author,
        'error': 'Gemini indisponível',
        'fallback': True,
        'fallback_action': 'USE_WEBSEARCH',
        'fallback_queries': [
            f'"{title}" "{author}" book summary review',
            f'"{title}" key ideas quotes',
            f'"{title}" "{author}" goodreads amazon'
        ]
    }


def main():
    parser = argparse.ArgumentParser(description='Pesquisa via Gemini API com cache')
    parser.add_argument('type', nargs='?', choices=['author', 'book'], help='Tipo de pesquisa')
    parser.add_argument('name', nargs='?', help='Nome do autor ou título do livro')
    parser.add_argument('--author', '-a', help='Autor do livro (obrigatório para type=book)')
    parser.add_argument('--output', '-o', choices=['json', 'markdown', 'text'], default='text')
    parser.add_argument('--no-cache', action='store_true', help='Ignorar cache e buscar fresh')
    parser.add_argument('--clear-cache', action='store_true', help='Limpar cache expirado')

    args = parser.parse_args()

    # Comando para limpar cache
    if args.clear_cache:
        removed = clear_expired_cache()
        print(f"✅ Cache limpo: {removed} arquivos removidos")
        sys.exit(0)

    # Validações
    if not args.type or not args.name:
        parser.print_help()
        sys.exit(1)

    if args.type == 'book' and not args.author:
        print("Erro: --author é obrigatório para pesquisa de livro", file=sys.stderr)
        sys.exit(1)

    print(f"🔍 Pesquisando via Gemini ({GEMINI_MODEL})...\n", file=sys.stderr)

    use_cache = not args.no_cache

    if args.type == 'author':
        result = research_author(args.name, use_cache=use_cache)
    else:
        result = research_book(args.name, args.author, use_cache=use_cache)

    # Output
    if args.output == 'json':
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.output == 'markdown':
        if result['success']:
            print(result['research'])
        else:
            print(f"# Erro\n\n{result.get('error', 'Falha desconhecida')}")
            if result.get('fallback'):
                print(f"\n## Fallback: WebSearch\n")
                print("Use estas queries:")
                for q in result.get('fallback_queries', []):
                    print(f"- `{q}`")
    else:
        if result['success']:
            cache_status = "📦 DO CACHE" if result.get('from_cache') else "🌐 FRESH"
            print(f"✅ Pesquisa concluída para: {args.name} {cache_status}")
            print(f"📊 Modelo: {result['model']}")
            print(f"\n{'-'*60}\n")
            print(result['research'])
        else:
            print(f"❌ Falha na pesquisa: {result.get('error')}")
            if result.get('fallback'):
                print(f"\n💡 FALLBACK: Use WebSearch do Claude com estas queries:")
                for q in result.get('fallback_queries', []):
                    print(f"   → {q}")


if __name__ == '__main__':
    main()
