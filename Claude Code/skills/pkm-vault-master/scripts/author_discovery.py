#!/usr/bin/env python3
"""
Author Discovery - Auto-discovery de autores no vault.

Busca automaticamente:
- Perfil do autor existente
- Livros do autor no vault
- Menções em Vida Lendária
- Citações existentes

Usage:
    python author_discovery.py "<autor>" --vault <path>

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


def find_author_profile(vault_path: str, author: str) -> Dict:
    """Verifica se autor tem perfil completo e quais módulos."""
    authors_dir = os.path.join(vault_path, 'Autores & Pensadores')

    result = {
        'found': False,
        'path': None,
        'name': None,
        'modules': [],
        'missing_modules': [],
        'has_overview': False,
        'has_analysis': False
    }

    if not os.path.exists(authors_dir):
        return result

    author_lower = author.lower()

    for item in os.listdir(authors_dir):
        item_path = os.path.join(authors_dir, item)
        if os.path.isdir(item_path):
            if author_lower in item.lower():
                result['found'] = True
                result['path'] = item_path
                result['name'] = item

                # Listar módulos
                files = os.listdir(item_path)
                md_files = [f for f in files if f.endswith('.md')]

                expected_modules = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8']

                for f in md_files:
                    if '00 -' in f or 'Overview' in f:
                        result['has_overview'] = True
                    for m in expected_modules:
                        if f.startswith(m):
                            result['modules'].append(m)

                # Verificar analysis
                analysis_dir = os.path.join(item_path, 'analysis')
                if os.path.exists(analysis_dir):
                    result['has_analysis'] = True

                # Módulos faltantes
                result['missing_modules'] = [m for m in expected_modules if m not in result['modules']]

                break

    return result


def find_author_books(vault_path: str, author: str) -> List[Dict]:
    """Busca livros do autor no vault."""
    books = []

    book_dirs = [
        os.path.join(vault_path, 'Livros'),
        os.path.join(vault_path, 'Recursos', 'Livros'),
    ]

    author_lower = author.lower()

    for book_dir in book_dirs:
        if not os.path.exists(book_dir):
            continue

        for filename in os.listdir(book_dir):
            if not filename.endswith('.md') or filename == 'INDEX.md':
                continue

            filepath = os.path.join(book_dir, filename)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Verificar se autor está no arquivo
                if author_lower not in content.lower():
                    continue

                # Verificar frontmatter para autor
                author_match = re.search(r'^autor:\s*["\[]?([^"\]\n]+)["\]]?', content, re.MULTILINE | re.IGNORECASE)
                if author_match:
                    file_author = author_match.group(1).lower()
                    if author_lower not in file_author:
                        continue

                word_count = len(content.split())
                title = filename.replace('.md', '')

                # Rating
                rating_match = re.search(r'^rating:\s*(\d)', content, re.MULTILINE)
                rating = int(rating_match.group(1)) if rating_match else None

                books.append({
                    'title': title,
                    'path': filepath,
                    'word_count': word_count,
                    'rating': rating,
                    'location': 'Livros' if 'Recursos' not in filepath else 'Recursos/Livros'
                })
            except Exception:
                continue

    # Ordenar por word_count
    books.sort(key=lambda x: x['word_count'], reverse=True)
    return books


def find_vl_mentions(vault_path: str, author: str) -> List[Dict]:
    """Busca menções do autor em Vida Lendária."""
    mentions = []

    vl_dir = os.path.join(vault_path, 'Vida Lendária', 'Episódios VL')

    if not os.path.exists(vl_dir):
        return mentions

    author_lower = author.lower()

    for filename in os.listdir(vl_dir):
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(vl_dir, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if author_lower in content.lower():
                # Extrair número do episódio
                ep_match = re.search(r'(\d+)', filename)
                ep_num = ep_match.group(1) if ep_match else '?'

                # Extrair título
                title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else filename.replace('.md', '')

                mentions.append({
                    'episode': f"VL/{ep_num}",
                    'title': title[:50],
                    'file': filename
                })
        except Exception:
            continue

    return mentions


def extract_citations(vault_path: str, author: str) -> List[str]:
    """Extrai citações do autor no vault."""
    citations = []
    author_lower = author.lower()

    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]

        for filename in files:
            if not filename.endswith('.md'):
                continue

            filepath = os.path.join(root, filename)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if author_lower not in content.lower():
                    continue

                # Extrair blockquotes
                quotes = re.findall(r'>([^\n]+)', content)
                for quote in quotes:
                    clean = quote.strip()
                    if len(clean) > 30 and clean not in citations:
                        citations.append(clean)
            except Exception:
                continue

    return citations[:15]


def run_discovery(author: str, vault_path: str) -> Dict:
    """Executa descoberta completa do autor."""

    result = {
        'author': author,
        'vault_path': vault_path,
        'author_profile': find_author_profile(vault_path, author),
        'books': find_author_books(vault_path, author),
        'vl_mentions': find_vl_mentions(vault_path, author),
        'citations': extract_citations(vault_path, author),
    }

    # Determinar modo
    profile = result['author_profile']
    if profile['found']:
        if profile['has_overview'] and len(profile['missing_modules']) == 0:
            result['mode'] = 'SKIP'
            result['mode_reason'] = 'Perfil completo já existe'
        else:
            result['mode'] = 'UPDATE'
            missing = profile['missing_modules']
            result['mode_reason'] = f"Perfil existe mas falta: {', '.join(missing) if missing else 'overview'}"
    else:
        result['mode'] = 'CREATE'
        result['mode_reason'] = 'Autor não encontrado no vault'

    # Calcular relevância
    result['relevance_score'] = (
        len(result['books']) * 3 +
        len(result['vl_mentions']) * 2 +
        len(result['citations']) * 0.5
    )

    return result


def main():
    parser = argparse.ArgumentParser(description='Auto-discovery de autores no vault')
    parser.add_argument('author', help='Nome do autor')
    parser.add_argument('--vault', '-v', required=True, help='Caminho do vault')
    parser.add_argument('--output', '-o', choices=['json', 'summary'], default='summary', help='Formato de saída')

    args = parser.parse_args()

    if not os.path.exists(args.vault):
        print(f"Erro: Vault não encontrado: {args.vault}", file=sys.stderr)
        sys.exit(1)

    result = run_discovery(args.author, args.vault)

    if args.output == 'json':
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Summary format
        print(f"\n{'='*60}")
        print(f"🧠 AUTHOR DISCOVERY: {result['author']}")
        print(f"{'='*60}\n")

        # Perfil do Autor
        profile = result['author_profile']
        if profile['found']:
            print(f"📁 Perfil do autor: ✅ {profile['name']}")
            print(f"   Módulos: {', '.join(profile['modules']) or 'nenhum'}")
            print(f"   Faltando: {', '.join(profile['missing_modules']) or 'nenhum'}")
            print(f"   Overview: {'✅' if profile['has_overview'] else '❌'}")
            print(f"   Analysis: {'✅' if profile['has_analysis'] else '❌'}")
        else:
            print("📁 Perfil do autor: ❌ Não existe")

        # Livros
        books = result['books']
        if books:
            print(f"\n📚 Livros no vault: {len(books)}")
            for b in books[:5]:
                rating = f"⭐{b['rating']}" if b['rating'] else ""
                print(f"   - {b['title']} ({b['word_count']}p) {rating}")
        else:
            print("\n📚 Livros no vault: ❌ Nenhum encontrado")

        # VL
        vl = result['vl_mentions']
        if vl:
            print(f"\n🎙️ Vida Lendária: {len(vl)} episódios")
            for ep in vl[:3]:
                print(f"   - {ep['episode']}: {ep['title']}")
        else:
            print("\n🎙️ Vida Lendária: ❌ Não mencionado")

        # Citações
        citations = result['citations']
        if citations:
            print(f"\n💬 Citações: {len(citations)}")
            for c in citations[:2]:
                print(f"   \"{c[:60]}...\"")

        # Modo
        print(f"\n{'='*60}")
        print(f"🎯 MODO: {result['mode']}")
        print(f"   {result['mode_reason']}")
        print(f"📊 Relevância: {result['relevance_score']:.1f}")
        print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
