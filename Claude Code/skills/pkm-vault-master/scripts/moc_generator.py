#!/usr/bin/env python3
"""
MOC Generator - Generates Map of Content (MOC) structure from a folder of notes

Usage:
    python moc_generator.py <folder_path> <moc_name> [--stage {1,2,3}]

Examples:
    python moc_generator.py ~/vault/Anotações "IA & Tecnologia"
    python moc_generator.py ~/vault/Anotações "Filosofia" --stage 2
"""

import os
import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime


def extract_keywords(content, min_length=4):
    """Extract meaningful keywords (reused from link_finder)"""
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    content = re.sub(r'[#*`_\-]', ' ', content)

    words = re.findall(r'\b[a-záàâãéêíóôõúçA-ZÁÀÂÃÉÊÍÓÔÕÚÇ]+\b', content.lower())

    stopwords = {
        'que', 'de', 'para', 'com', 'um', 'uma', 'os', 'as', 'do', 'da', 'em', 'por',
        'na', 'no', 'se', 'ou', 'como', 'mais', 'mas', 'são', 'dos', 'das', 'ao', 'aos',
        'the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was',
        'for', 'on', 'are', 'with', 'as', 'this', 'be', 'at', 'by', 'from', 'or'
    }

    keywords = [w for w in words if len(w) >= min_length and w not in stopwords]
    return keywords


def cluster_notes_by_keywords(notes_data, num_clusters=5):
    """Simple keyword-based clustering to suggest sub-themes"""
    # Collect all keywords
    all_keywords = Counter()
    for note in notes_data:
        all_keywords.update(note['keywords'])

    # Get top keywords as cluster seeds
    top_keywords = [kw for kw, _ in all_keywords.most_common(num_clusters * 3)]

    # Assign notes to clusters
    clusters = defaultdict(list)

    for note in notes_data:
        best_cluster = None
        best_score = 0

        # Find which top keyword appears most in this note
        for keyword in top_keywords:
            score = note['keyword_counts'].get(keyword, 0)
            if score > best_score:
                best_score = score
                best_cluster = keyword

        if best_cluster:
            clusters[best_cluster].append(note['name'])

    # Return top N clusters with most notes
    sorted_clusters = sorted(clusters.items(), key=lambda x: len(x[1]), reverse=True)
    return sorted_clusters[:num_clusters]


def generate_moc_stage1(folder_path, moc_name):
    """Generate Stage 1 MOC (simple list)"""
    folder = Path(folder_path)
    md_files = sorted(list(folder.glob("*.md")))

    # Skip Index files
    md_files = [f for f in md_files if not (f.stem.startswith('📇 Index') or f.stem == 'Index')]

    moc_content = f"""# MOC - {moc_name}

*Última atualização: {datetime.now().strftime('%Y-%m-%d')}*
*Stage: 1 - List*

---

## 📍 Visão Geral
[Adicione 1-2 parágrafos: O que é este tema? Por que importa para você?]

---

## 🗺 Notas Relacionadas

"""

    for md_file in md_files:
        moc_content += f"- [[{md_file.stem}]]\n"

    moc_content += """
---

## 🔗 MOCs Relacionados
- [[MOC - Tema Relacionado 1]]
- [[MOC - Tema Relacionado 2]]

---

## 🏠 Voltar para

[[⭐ Home]] (ATLAS/Home) — Dashboard principal do vault
"""

    return moc_content


def generate_moc_stage2(folder_path, moc_name):
    """Generate Stage 2 MOC (workbench with groups)"""
    folder = Path(folder_path)
    md_files = list(folder.glob("*.md"))

    # Skip Index files
    md_files = [f for f in md_files if not (f.stem.startswith('📇 Index') or f.stem == 'Index')]

    # Analyze notes
    notes_data = []
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            keywords = extract_keywords(content)
            keyword_counts = Counter(keywords)

            notes_data.append({
                "name": md_file.stem,
                "keywords": keywords,
                "keyword_counts": keyword_counts
            })
        except:
            continue

    # Cluster into sub-themes
    clusters = cluster_notes_by_keywords(notes_data, num_clusters=4)

    moc_content = f"""# MOC - {moc_name}

*Última atualização: {datetime.now().strftime('%Y-%m-%d')}*
*Stage: 2 - Workbench*

---

## 📍 Visão Geral
[Adicione 1-2 parágrafos desenvolvidos: O que está explorando neste tema?]

---

## 🗺 Estrutura de Notas

"""

    for i, (theme_keyword, note_list) in enumerate(clusters, 1):
        moc_content += f"### {theme_keyword.capitalize()}\n"
        moc_content += f"*[Adicione comentário sobre este aspecto]*\n\n"
        for note_name in sorted(note_list):
            moc_content += f"- [[{note_name}]]\n"
        moc_content += "\n"

    # Add uncategorized notes
    all_clustered = set()
    for _, notes in clusters:
        all_clustered.update(notes)

    uncategorized = [n['name'] for n in notes_data if n['name'] not in all_clustered]

    if uncategorized:
        moc_content += f"### Outras Notas\n"
        moc_content += f"*[A categorizar]*\n\n"
        for note_name in sorted(uncategorized):
            moc_content += f"- [[{note_name}]]\n"
        moc_content += "\n"

    moc_content += """---

## 💭 Pensamentos em Desenvolvimento
*Seu thinking atual sobre este tema*

[Escreva parágrafos conectando as ideias. Este é seu workbench.]

---

## ❓ Questões a Explorar
- [ ] Pergunta não respondida 1
- [ ] Pergunta não respondida 2

---

## 🔗 MOCs Relacionados
- [[MOC - Tema Relacionado 1]]
- [[MOC - Tema Relacionado 2]]

---

## 🏠 Voltar para

[[⭐ Home]] (ATLAS/Home) — Dashboard principal do vault
"""

    return moc_content


def main():
    parser = argparse.ArgumentParser(description='Generate MOC from folder of notes')
    parser.add_argument('folder', help='Path to folder containing notes')
    parser.add_argument('name', help='Name for the MOC')
    parser.add_argument('--stage', type=int, choices=[1, 2], default=1,
                        help='MOC stage (1=List, 2=Workbench)')

    args = parser.parse_args()

    if args.stage == 1:
        moc_content = generate_moc_stage1(args.folder, args.name)
    else:
        moc_content = generate_moc_stage2(args.folder, args.name)

    # Print to stdout (can be redirected to file)
    print(moc_content)


if __name__ == "__main__":
    main()
