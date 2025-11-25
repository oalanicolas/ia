#!/usr/bin/env python3
"""
Book Analyzer - Analisa livros do vault e identifica prioridades para perfis de autores.

Usage:
    python book_analyzer.py <vault_path> [--output report.md]

Example:
    python book_analyzer.py ~/vault --output _reports/book_analysis.md
"""

import os
import sys
import re
import argparse
from datetime import datetime
from collections import defaultdict

# Seções esperadas no template de livro
EXPECTED_SECTIONS = {
    'IP': ['Ideia Principal', 'ideia principal'],
    'PQ': ['Para quem', 'para quem'],
    'IMP': ['Como o Livro me Impactou', 'Como me Impactou', 'impactou'],
    'SUM': ['Sumário', 'Ideias Chave', 'sumário', 'ideias chave'],
    'CIT': ['Citações', 'Citação', 'citações'],
    'CRIT': ['Críticas', 'críticas'],
    'VL': ['Vida Lendária', 'Mencionado em']
}

# Níveis de profundidade
DEPTH_LEVELS = {
    1: {'name': 'STUB', 'min': 0, 'max': 200},
    2: {'name': 'BÁSICO', 'min': 200, 'max': 500},
    3: {'name': 'INTERMEDIÁRIO', 'min': 500, 'max': 1500},
    4: {'name': 'COMPLETO', 'min': 1500, 'max': 3000},
    5: {'name': 'EXEMPLAR', 'min': 3000, 'max': float('inf')}
}


def count_words(text):
    """Conta palavras no texto."""
    return len(text.split())


def extract_author(content):
    """Extrai autor do frontmatter."""
    match = re.search(r'^autor:\s*["\[]?([^"\]\n]+)["\]]?', content, re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    match = re.search(r'^author:\s*["\[]?([^"\]\n]+)["\]]?', content, re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def check_sections(content):
    """Verifica quais seções estão presentes."""
    found = []
    for key, patterns in EXPECTED_SECTIONS.items():
        for pattern in patterns:
            if pattern.lower() in content.lower():
                found.append(key)
                break
    return found


def get_depth_level(word_count):
    """Retorna o nível de profundidade baseado na contagem de palavras."""
    for level, info in DEPTH_LEVELS.items():
        if info['min'] <= word_count < info['max']:
            return level, info['name']
    return 5, 'EXEMPLAR'


def analyze_books(vault_path):
    """Analisa todos os livros no vault."""
    books = []
    book_dirs = [
        os.path.join(vault_path, 'Livros'),
        os.path.join(vault_path, 'Recursos', 'Livros')
    ]

    for book_dir in book_dirs:
        if not os.path.exists(book_dir):
            continue

        for filename in os.listdir(book_dir):
            if not filename.endswith('.md') or filename == 'INDEX.md':
                continue

            filepath = os.path.join(book_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            title = filename.replace('.md', '')
            word_count = count_words(content)
            author = extract_author(content)
            sections = check_sections(content)
            level, level_name = get_depth_level(word_count)

            books.append({
                'title': title,
                'author': author or 'N/A',
                'words': word_count,
                'sections': sections,
                'level': level,
                'level_name': level_name,
                'path': filepath
            })

    return books


def get_existing_profiles(vault_path):
    """Lista autores com perfis existentes."""
    profiles_dir = os.path.join(vault_path, 'Autores & Pensadores')
    profiles = {}

    if not os.path.exists(profiles_dir):
        return profiles

    for item in os.listdir(profiles_dir):
        item_path = os.path.join(profiles_dir, item)
        if os.path.isdir(item_path):
            files = [f for f in os.listdir(item_path) if f.endswith('.md')]
            profiles[item] = len(files)

    return profiles


def generate_report(books, profiles, output_path=None):
    """Gera relatório de análise."""

    # Estatísticas por nível
    level_counts = defaultdict(int)
    for book in books:
        level_counts[book['level']] += 1

    # Autores com múltiplos livros
    author_books = defaultdict(list)
    for book in books:
        if book['author'] != 'N/A':
            author_books[book['author']].append(book)

    # Gerar relatório
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    report = f"""# Análise de Livros e Perfis de Autores

**Data:** {now}
**Total de Livros:** {len(books)}
**Perfis de Autores:** {len(profiles)}

---

## Distribuição por Nível

| Nível | Nome | Quantidade | % |
|-------|------|------------|---|
"""

    for level in range(1, 6):
        count = level_counts[level]
        pct = (count / len(books) * 100) if books else 0
        name = DEPTH_LEVELS[level]['name']
        report += f"| {level} | {name} | {count} | {pct:.0f}% |\n"

    report += """
---

## Autores com Múltiplos Livros

| Autor | Livros | Total Palavras | Perfil? |
|-------|--------|----------------|--------|
"""

    # Ordenar por número de livros
    multi_authors = [(a, b) for a, b in author_books.items() if len(b) > 1]
    multi_authors.sort(key=lambda x: len(x[1]), reverse=True)

    for author, author_book_list in multi_authors:
        total_words = sum(b['words'] for b in author_book_list)
        has_profile = '✅' if any(author.lower() in p.lower() for p in profiles) else '❌'
        report += f"| {author} | {len(author_book_list)} | {total_words:,} | {has_profile} |\n"

    report += """
---

## Livros STUB (Precisam Desenvolvimento)

| Livro | Autor | Palavras |
|-------|-------|----------|
"""

    stubs = [b for b in books if b['level'] == 1]
    for book in stubs:
        report += f"| {book['title']} | {book['author']} | {book['words']} |\n"

    report += """
---

## Livros EXEMPLARES (Referência)

| Livro | Autor | Palavras | Perfil? |
|-------|-------|----------|--------|
"""

    exemplars = sorted([b for b in books if b['level'] == 5], key=lambda x: x['words'], reverse=True)
    for book in exemplars:
        has_profile = '✅' if any(book['author'].lower() in p.lower() for p in profiles) else '❌'
        report += f"| {book['title']} | {book['author']} | {book['words']:,} | {has_profile} |\n"

    report += f"""
---

*Relatório gerado em {now}*
"""

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Relatório salvo em: {output_path}")

    return report


def main():
    parser = argparse.ArgumentParser(description='Analisa livros do vault Obsidian')
    parser.add_argument('vault_path', help='Caminho para o vault')
    parser.add_argument('--output', '-o', help='Arquivo de saída para o relatório')

    args = parser.parse_args()

    if not os.path.exists(args.vault_path):
        print(f"Erro: Caminho não encontrado: {args.vault_path}")
        sys.exit(1)

    print(f"Analisando vault: {args.vault_path}")

    books = analyze_books(args.vault_path)
    profiles = get_existing_profiles(args.vault_path)

    print(f"Livros encontrados: {len(books)}")
    print(f"Perfis existentes: {len(profiles)}")

    report = generate_report(books, profiles, args.output)

    if not args.output:
        print("\n" + report)


if __name__ == '__main__':
    main()
