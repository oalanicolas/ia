#!/usr/bin/env python3
"""
Vault Analyzer - Analyzes Obsidian vault folders and provides PKM insights

Usage:
    python vault_analyzer.py <folder_path> [--detailed]

Examples:
    python vault_analyzer.py ~/vault/Anotações
    python vault_analyzer.py ~/vault/Anotações --detailed
"""

import os
import sys
import re
from pathlib import Path
from collections import defaultdict, Counter
import argparse


def count_links(content):
    """Count [[wiki-links]] in markdown content"""
    return len(re.findall(r'\[\[([^\]]+)\]\]', content))


def extract_links(content):
    """Extract all [[wiki-links]] from markdown content"""
    return re.findall(r'\[\[([^\]]+)\]\]', content)


def count_headings(content):
    """Count markdown headings"""
    return len(re.findall(r'^#{1,6}\s+.+', content, re.MULTILINE))


def estimate_word_count(content):
    """Estimate word count (excluding frontmatter and code blocks)"""
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Count words
    words = content.split()
    return len(words)


def analyze_vault_folder(folder_path, detailed=False):
    """Analyze a vault folder and return statistics"""

    folder = Path(folder_path)
    if not folder.exists():
        return {"error": f"Folder not found: {folder_path}"}

    stats = {
        "folder": str(folder),
        "total_notes": 0,
        "total_links": 0,
        "orphan_notes": [],
        "hub_notes": [],  # Notes with many links
        "empty_notes": [],
        "large_notes": [],  # Notes with 500+ words
        "notes_by_word_count": {},
        "link_distribution": Counter(),
        "all_notes": []
    }

    # Scan all markdown files
    md_files = list(folder.glob("*.md"))
    stats["total_notes"] = len(md_files)

    note_links = {}  # note_name: [outgoing_links]
    backlinks = defaultdict(list)  # note_name: [notes_that_link_to_it]

    for md_file in md_files:
        note_name = md_file.stem

        try:
            content = md_file.read_text(encoding='utf-8')
        except:
            continue

        # Extract metrics
        links = extract_links(content)
        link_count = len(links)
        word_count = estimate_word_count(content)
        heading_count = count_headings(content)

        stats["total_links"] += link_count
        stats["link_distribution"][link_count] += 1

        note_links[note_name] = links

        # Track backlinks
        for target in links:
            # Remove aliases (e.g., [[Note|Alias]] -> Note)
            clean_target = target.split('|')[0]
            backlinks[clean_target].append(note_name)

        # Categorize notes
        if word_count == 0 or word_count < 10:
            stats["empty_notes"].append(note_name)

        if word_count > 500:
            stats["large_notes"].append((note_name, word_count))

        if link_count >= 10:
            stats["hub_notes"].append((note_name, link_count))

        # Store note info
        stats["all_notes"].append({
            "name": note_name,
            "words": word_count,
            "links": link_count,
            "headings": heading_count,
            "path": str(md_file)
        })

    # Find orphan notes (no incoming or outgoing links)
    for note_name in note_links.keys():
        outgoing = len(note_links[note_name])
        incoming = len(backlinks.get(note_name, []))

        if outgoing == 0 and incoming == 0:
            stats["orphan_notes"].append(note_name)

    # Sort hub notes by link count (descending)
    stats["hub_notes"].sort(key=lambda x: x[1], reverse=True)
    stats["large_notes"].sort(key=lambda x: x[1], reverse=True)

    # Summary stats
    stats["orphan_count"] = len(stats["orphan_notes"])
    stats["hub_count"] = len(stats["hub_notes"])
    stats["empty_count"] = len(stats["empty_notes"])
    stats["large_count"] = len(stats["large_notes"])
    stats["avg_links_per_note"] = round(stats["total_links"] / stats["total_notes"], 2) if stats["total_notes"] > 0 else 0

    return stats


def print_report(stats, detailed=False):
    """Print analysis report"""

    if "error" in stats:
        print(f"❌ Error: {stats['error']}")
        return

    print(f"\n{'='*70}")
    print(f"📊 VAULT ANALYSIS: {Path(stats['folder']).name}")
    print(f"{'='*70}\n")

    print(f"📝 Total Notes: {stats['total_notes']}")
    print(f"🔗 Total Links: {stats['total_links']}")
    print(f"📈 Avg Links/Note: {stats['avg_links_per_note']}")
    print()

    print(f"🔴 Orphan Notes (no links in/out): {stats['orphan_count']}")
    if detailed and stats["orphan_notes"]:
        for note in stats["orphan_notes"][:10]:
            print(f"   - {note}")
        if len(stats["orphan_notes"]) > 10:
            print(f"   ... and {len(stats['orphan_notes']) - 10} more")
    print()

    print(f"⭐ Hub Notes (10+ links): {stats['hub_count']}")
    if stats["hub_notes"]:
        for note, link_count in stats["hub_notes"][:5]:
            print(f"   - {note} ({link_count} links)")
        if len(stats["hub_notes"]) > 5:
            print(f"   ... and {len(stats['hub_notes']) - 5} more")
    print()

    print(f"📄 Empty/Stub Notes: {stats['empty_count']}")
    if detailed and stats["empty_notes"]:
        for note in stats["empty_notes"][:5]:
            print(f"   - {note}")
    print()

    print(f"📚 Large Notes (500+ words): {stats['large_count']}")
    if stats["large_notes"]:
        for note, word_count in stats["large_notes"][:5]:
            print(f"   - {note} ({word_count} words)")
    print()

    print(f"📊 Link Distribution:")
    for link_count in sorted(stats["link_distribution"].keys())[:8]:
        count = stats["link_distribution"][link_count]
        bar = '█' * min(count, 40)
        print(f"   {link_count:2d} links: {bar} ({count} notes)")

    print(f"\n{'='*70}\n")


def main():
    parser = argparse.ArgumentParser(description='Analyze Obsidian vault folder')
    parser.add_argument('folder', help='Path to folder to analyze')
    parser.add_argument('--detailed', action='store_true', help='Show detailed breakdown')

    args = parser.parse_args()

    stats = analyze_vault_folder(args.folder, args.detailed)
    print_report(stats, args.detailed)


if __name__ == "__main__":
    main()
