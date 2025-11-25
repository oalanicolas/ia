#!/usr/bin/env python3
"""
Link Finder - Finds related notes in vault based on content similarity

Usage:
    python link_finder.py <note_path> <vault_folder> [--top N]

Examples:
    python link_finder.py ~/vault/Anotações/IA.md ~/vault/Anotações
    python link_finder.py ~/vault/Anotações/Hábitos.md ~/vault/Anotações --top 5
"""

import os
import sys
import re
import argparse
from pathlib import Path
from collections import Counter
import math


def extract_keywords(content, min_length=4):
    """Extract meaningful keywords from markdown content"""
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Remove links
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    # Remove markdown symbols
    content = re.sub(r'[#*`_\-]', ' ', content)

    # Extract words
    words = re.findall(r'\b[a-záàâãéêíóôõúçA-ZÁÀÂÃÉÊÍÓÔÕÚÇ]+\b', content.lower())

    # Filter stopwords (Portuguese and English common words)
    stopwords = {
        'que', 'de', 'para', 'com', 'um', 'uma', 'os', 'as', 'do', 'da', 'em', 'por',
        'na', 'no', 'se', 'ou', 'como', 'mais', 'mas', 'são', 'dos', 'das', 'ao', 'aos',
        'the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was',
        'for', 'on', 'are', 'with', 'as', 'this', 'be', 'at', 'by', 'from', 'or',
        'não', 'ser', 'ter', 'estar', 'fazer', 'poder', 'dar', 'ir', 'ver', 'dizer',
        'pelo', 'pela', 'pelos', 'pelas', 'seu', 'sua', 'seus', 'suas', 'esse', 'essa'
    }

    # Filter and return keywords
    keywords = [w for w in words if len(w) >= min_length and w not in stopwords]
    return keywords


def calculate_similarity(keywords1, keywords2):
    """Calculate similarity score between two lists of keywords using TF-IDF-like approach"""
    counter1 = Counter(keywords1)
    counter2 = Counter(keywords2)

    # Get common keywords
    common = set(counter1.keys()) & set(counter2.keys())

    if not common:
        return 0.0

    # Simple cosine similarity
    numerator = sum(counter1[k] * counter2[k] for k in common)

    sum1 = sum(count ** 2 for count in counter1.values())
    sum2 = sum(count ** 2 for count in counter2.values())

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator == 0:
        return 0.0

    return numerator / denominator


def find_related_notes(note_path, vault_folder, top_n=10):
    """Find notes most similar to the given note"""

    note_file = Path(note_path)
    vault = Path(vault_folder)

    if not note_file.exists():
        return {"error": f"Note not found: {note_path}"}

    if not vault.exists():
        return {"error": f"Vault folder not found: {vault_folder}"}

    # Read target note
    try:
        target_content = note_file.read_text(encoding='utf-8')
    except:
        return {"error": f"Could not read note: {note_path}"}

    target_keywords = extract_keywords(target_content)
    target_name = note_file.stem

    # Scan vault for similar notes
    similarities = []
    md_files = list(vault.glob("*.md"))

    for md_file in md_files:
        # Skip the target note itself (use samefile to handle unicode normalization)
        try:
            if md_file.samefile(note_file):
                continue
        except:
            pass  # If samefile fails, continue comparing

        # Skip Index files
        if md_file.stem.startswith('📇 Index') or md_file.stem == 'Index':
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
        except:
            continue

        keywords = extract_keywords(content)
        similarity = calculate_similarity(target_keywords, keywords)

        if similarity > 0:
            similarities.append({
                "note": md_file.stem,
                "score": round(similarity, 3),
                "path": str(md_file)
            })

    # Sort by similarity score
    similarities.sort(key=lambda x: x['score'], reverse=True)

    return {
        "target_note": target_name,
        "total_candidates": len(md_files) - 1,
        "related_notes": similarities[:top_n],
        "top_keywords": Counter(target_keywords).most_common(15)
    }


def print_results(results):
    """Print results in a readable format"""

    if "error" in results:
        print(f"\n❌ Error: {results['error']}\n")
        return

    print(f"\n{'='*70}")
    print(f"🔗 RELATED NOTES FOR: {results['target_note']}")
    print(f"{'='*70}\n")

    print(f"📊 Analyzed {results['total_candidates']} notes\n")

    print(f"🎯 Top Keywords in Target Note:")
    for keyword, count in results['top_keywords'][:10]:
        print(f"   - {keyword} ({count}x)")
    print()

    print(f"📝 Top {len(results['related_notes'])} Related Notes:\n")
    for i, note in enumerate(results['related_notes'], 1):
        score_bar = '█' * int(note['score'] * 50)
        print(f"   {i:2d}. [[{note['note']}]] — {score_bar} {note['score']:.3f}")

    print(f"\n{'='*70}\n")

    print(f"💡 Suggested Links to Add:")
    for note in results['related_notes'][:5]:
        print(f"   - [[{note['note']}]] — {note['score']:.3f} similarity")

    print()


def main():
    parser = argparse.ArgumentParser(description='Find notes related to a target note')
    parser.add_argument('note', help='Path to target note')
    parser.add_argument('vault', help='Path to vault folder')
    parser.add_argument('--top', type=int, default=10, help='Number of top results to show')

    args = parser.parse_args()

    results = find_related_notes(args.note, args.vault, args.top)
    print_results(results)


if __name__ == "__main__":
    main()
