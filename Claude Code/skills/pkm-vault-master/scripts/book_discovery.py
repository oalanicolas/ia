#!/usr/bin/env python3
"""
Book Discovery - Auto-discovery de livros no vault.

Busca automaticamente:
- Livro existente no vault
- Menções e citações
- Perfil do autor
- Menções em Vida Lendária

Usage:
    python book_discovery.py "<título>" --author "<autor>" --vault <path>

Output:
    JSON com todas as descobertas para uso pelo command
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional


def find_book_file(vault_path: str, title: str) -> Optional[Dict]:
    """Busca arquivo do livro no vault."""
    # Normalizar título para busca
    title_lower = title.lower()
    title_normalized = re.sub(r'[^\w\s]', '', title_lower)

    # Pastas onde livros podem estar
    book_dirs = [
        os.path.join(vault_path, 'Livros'),
        os.path.join(vault_path, 'Recursos', 'Livros'),
    ]

    for book_dir in book_dirs:
        if not os.path.exists(book_dir):
            continue

        for filename in os.listdir(book_dir):
            if not filename.endswith('.md'):
                continue

            file_title = filename.replace('.md', '').lower()
            file_normalized = re.sub(r'[^\w\s]', '', file_title)

            # Match exato ou parcial
            if title_normalized in file_normalized or file_normalized in title_normalized:
                filepath = os.path.join(book_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                word_count = len(content.split())

                # Extrair seções existentes
                sections = []
                if 'Ideia Principal' in content: sections.append('IP')
                if 'Para quem' in content: sections.append('PQ')
                if 'Impactou' in content: sections.append('IMP')
                if 'Sumário' in content or 'Ideias Chave' in content: sections.append('SUM')
                if 'Citações' in content: sections.append('CIT')
                if 'Críticas' in content: sections.append('CRIT')
                if 'Vida Lendária' in content: sections.append('VL')

                return {
                    'found': True,
                    'path': filepath,
                    'word_count': word_count,
                    'sections': sections,
                    'complete': len(sections) >= 6,
                    'location': 'Livros' if 'Livros' in filepath and 'Recursos' not in filepath else 'Recursos/Livros'
                }

    return {'found': False}


def find_mentions(vault_path: str, search_term: str, exclude_paths: List[str] = None) -> List[Dict]:
    """Busca menções de um termo no vault."""
    mentions = []
    exclude_paths = exclude_paths or []

    # Pastas prioritárias
    priority_dirs = [
        'Vida Lendária',
        'Conhecimento',
        'Cursos',
        'Anotações',
        'MOCs',
    ]

    for root, dirs, files in os.walk(vault_path):
        # Skip hidden directories and excluded paths
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]

        rel_root = os.path.relpath(root, vault_path)
        if any(excl in rel_root for excl in exclude_paths):
            continue

        for filename in files:
            if not filename.endswith('.md'):
                continue

            filepath = os.path.join(root, filename)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if search_term.lower() in content.lower():
                    # Extrair linhas com menções
                    lines = content.split('\n')
                    matching_lines = []
                    for i, line in enumerate(lines):
                        if search_term.lower() in line.lower():
                            matching_lines.append({
                                'line_num': i + 1,
                                'content': line.strip()[:200]
                            })

                    # Determinar prioridade
                    priority = 99
                    for idx, pdir in enumerate(priority_dirs):
                        if pdir in filepath:
                            priority = idx
                            break

                    mentions.append({
                        'file': os.path.relpath(filepath, vault_path),
                        'matches': len(matching_lines),
                        'lines': matching_lines[:5],  # Primeiras 5
                        'priority': priority
                    })
            except Exception:
                continue

    # Ordenar por prioridade e número de matches
    mentions.sort(key=lambda x: (x['priority'], -x['matches']))
    return mentions[:20]  # Top 20


def find_author_profile(vault_path: str, author: str) -> Optional[Dict]:
    """Verifica se autor tem perfil completo."""
    authors_dir = os.path.join(vault_path, 'Autores & Pensadores')

    if not os.path.exists(authors_dir):
        return {'found': False}

    author_lower = author.lower()

    for item in os.listdir(authors_dir):
        item_path = os.path.join(authors_dir, item)
        if os.path.isdir(item_path):
            if author_lower in item.lower():
                # Contar módulos
                modules = [f for f in os.listdir(item_path) if f.endswith('.md')]
                overview = [f for f in modules if '00 -' in f or 'Overview' in f]

                return {
                    'found': True,
                    'path': item_path,
                    'name': item,
                    'modules': len(modules),
                    'has_overview': len(overview) > 0
                }

    return {'found': False}


def check_vl_index(vault_path: str, title: str, author: str) -> Dict:
    """Verifica menções no ÍNDICE_LIVROS.md de Vida Lendária."""
    index_path = os.path.join(vault_path, 'Vida Lendária', 'ÍNDICE_LIVROS.md')

    result = {
        'found': False,
        'episodes': []
    }

    if not os.path.exists(index_path):
        # Tentar caminho alternativo
        index_path = os.path.join(vault_path, 'Vida Lendária', 'Episódios VL', 'ÍNDICE_LIVROS.md')

    if not os.path.exists(index_path):
        return result

    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Buscar por título ou autor
        lines = content.split('\n')
        for line in lines:
            if title.lower() in line.lower() or author.lower() in line.lower():
                # Extrair referência de episódio (VL/XXX)
                match = re.search(r'VL[/\\]?(\d+)', line)
                if match:
                    result['episodes'].append({
                        'episode': f"VL/{match.group(1)}",
                        'context': line.strip()[:100]
                    })
                    result['found'] = True
    except Exception:
        pass

    return result


def extract_citations(vault_path: str, title: str, author: str) -> List[str]:
    """Extrai citações já existentes sobre o livro/autor."""
    citations = []

    # Padrões de citação
    citation_patterns = [
        r'>[^\n]+',  # Blockquotes
        r'"[^"]{20,}"',  # Aspas duplas com conteúdo significativo
        r'「[^」]+」',  # Aspas japonesas
    ]

    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]

        for filename in files:
            if not filename.endswith('.md'):
                continue

            filepath = os.path.join(root, filename)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Verificar se arquivo menciona o livro/autor
                if title.lower() not in content.lower() and author.lower() not in content.lower():
                    continue

                # Extrair citações
                for pattern in citation_patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        clean = match.strip('>"「」').strip()
                        if len(clean) > 30 and clean not in citations:
                            citations.append(clean)
            except Exception:
                continue

    return citations[:10]  # Top 10


def run_discovery(title: str, author: str, vault_path: str) -> Dict:
    """Executa descoberta completa."""

    result = {
        'title': title,
        'author': author,
        'vault_path': vault_path,
        'book': find_book_file(vault_path, title),
        'author_profile': find_author_profile(vault_path, author),
        'vl_mentions': check_vl_index(vault_path, title, author),
        'vault_mentions': find_mentions(vault_path, title, exclude_paths=['Recursos/Livros', 'Livros']),
        'author_mentions': find_mentions(vault_path, author, exclude_paths=['Autores & Pensadores']),
        'citations': extract_citations(vault_path, title, author),
    }

    # Determinar modo
    if result['book']['found']:
        if result['book']['complete']:
            result['mode'] = 'SKIP'
            result['mode_reason'] = 'Livro já existe e está completo'
        else:
            result['mode'] = 'UPDATE'
            result['mode_reason'] = f"Livro existe mas falta seções: {7 - len(result['book']['sections'])}"
    else:
        result['mode'] = 'CREATE'
        result['mode_reason'] = 'Livro não encontrado no vault'

    return result


def main():
    parser = argparse.ArgumentParser(description='Auto-discovery de livros no vault')
    parser.add_argument('title', help='Título do livro')
    parser.add_argument('--author', '-a', required=True, help='Nome do autor')
    parser.add_argument('--vault', '-v', required=True, help='Caminho do vault')
    parser.add_argument('--output', '-o', choices=['json', 'summary'], default='summary', help='Formato de saída')

    args = parser.parse_args()

    if not os.path.exists(args.vault):
        print(f"Erro: Vault não encontrado: {args.vault}", file=sys.stderr)
        sys.exit(1)

    result = run_discovery(args.title, args.author, args.vault)

    if args.output == 'json':
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Summary format
        print(f"\n{'='*60}")
        print(f"📚 BOOK DISCOVERY: {result['title']}")
        print(f"👤 Autor: {result['author']}")
        print(f"{'='*60}\n")

        # Livro
        book = result['book']
        if book['found']:
            print(f"📖 Livro no vault: ✅ {book['path']}")
            print(f"   Palavras: {book['word_count']}")
            print(f"   Seções: {', '.join(book['sections'])}")
            print(f"   Completo: {'✅' if book['complete'] else '❌'}")
        else:
            print("📖 Livro no vault: ❌ Não encontrado")

        # Perfil do autor
        profile = result['author_profile']
        if profile['found']:
            print(f"\n🧠 Perfil do autor: ✅ {profile['name']} ({profile['modules']} módulos)")
        else:
            print("\n🧠 Perfil do autor: ❌ Não existe")

        # Vida Lendária
        vl = result['vl_mentions']
        if vl['found']:
            print(f"\n🎙️ Vida Lendária: ✅ {len(vl['episodes'])} episódios")
            for ep in vl['episodes'][:3]:
                print(f"   - {ep['episode']}: {ep['context'][:50]}...")
        else:
            print("\n🎙️ Vida Lendária: ❌ Não mencionado")

        # Menções
        mentions = result['vault_mentions']
        if mentions:
            print(f"\n📝 Menções no vault: {len(mentions)} arquivos")
            for m in mentions[:3]:
                print(f"   - {m['file']} ({m['matches']} matches)")

        # Citações
        citations = result['citations']
        if citations:
            print(f"\n💬 Citações encontradas: {len(citations)}")
            for c in citations[:2]:
                print(f"   \"{c[:80]}...\"")

        # Modo
        print(f"\n{'='*60}")
        print(f"🎯 MODO: {result['mode']}")
        print(f"   {result['mode_reason']}")
        print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
