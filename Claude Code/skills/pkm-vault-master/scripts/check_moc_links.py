#!/usr/bin/env python3
"""
Check all wikilinks in MOC files to identify broken links.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

def extract_wikilinks(content):
    """Extract all wikilinks from markdown content."""
    # Pattern matches [[link]] or [[link|alias]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]'
    matches = re.findall(pattern, content)
    return matches

def find_file_in_vault(vault_path, filename):
    """Search for a file in the vault (case-insensitive, handles .md extension)."""
    vault_path = Path(vault_path)

    # Remove .md extension if present in search term
    search_name = filename.replace('.md', '')

    # Search for exact match with .md
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if not file.endswith('.md'):
                continue

            file_without_ext = file.replace('.md', '')

            # Case-insensitive match
            if file_without_ext.lower() == search_name.lower():
                return os.path.join(root, file)

    return None

def check_moc_links(vault_path, moc_files=None):
    """Check all links in MOC files."""
    vault_path = Path(vault_path)

    # Find all MOC files if not provided
    if moc_files is None:
        moc_files = list(vault_path.rglob("MOC*.md"))
    else:
        moc_files = [Path(f) for f in moc_files]

    results = {
        'total_mocs': len(moc_files),
        'total_links': 0,
        'broken_links': defaultdict(list),  # {moc_file: [broken_links]}
        'valid_links': 0,
        'unique_broken': set()
    }

    print(f"🔍 Checking links in {len(moc_files)} MOC files...\n")

    for moc_file in sorted(moc_files):
        try:
            with open(moc_file, 'r', encoding='utf-8') as f:
                content = f.read()

            links = extract_wikilinks(content)
            results['total_links'] += len(links)

            broken_in_this_moc = []

            for link in links:
                # Check if file exists
                found = find_file_in_vault(vault_path, link)

                if found is None:
                    broken_in_this_moc.append(link)
                    results['unique_broken'].add(link)
                else:
                    results['valid_links'] += 1

            if broken_in_this_moc:
                results['broken_links'][str(moc_file.relative_to(vault_path))] = broken_in_this_moc

        except Exception as e:
            print(f"❌ Error reading {moc_file}: {e}")

    return results

def print_results(results):
    """Print formatted results."""
    print("=" * 70)
    print("📊 MOC LINK ANALYSIS RESULTS")
    print("=" * 70)
    print(f"\n✅ Valid links: {results['valid_links']}")
    print(f"❌ Broken links: {len(results['unique_broken'])}")
    print(f"📝 Total links checked: {results['total_links']}")
    print(f"📁 MOCs analyzed: {results['total_mocs']}")

    if results['broken_links']:
        print("\n" + "=" * 70)
        print("🔴 BROKEN LINKS BY MOC")
        print("=" * 70)

        for moc_file, broken_links in sorted(results['broken_links'].items()):
            print(f"\n📄 {moc_file}")
            print(f"   {len(broken_links)} broken link(s):")
            for link in sorted(broken_links):
                print(f"   • [[{link}]]")

    if results['unique_broken']:
        print("\n" + "=" * 70)
        print("🔴 UNIQUE BROKEN LINKS (alphabetical)")
        print("=" * 70)
        for link in sorted(results['unique_broken']):
            print(f"• [[{link}]]")

    print("\n" + "=" * 70)

    # Calculate health score
    if results['total_links'] > 0:
        health_score = (results['valid_links'] / results['total_links']) * 100
        print(f"\n💚 MOC Link Health Score: {health_score:.1f}%")

        if health_score >= 95:
            print("   Excellent! Very few broken links.")
        elif health_score >= 80:
            print("   Good, but some links need attention.")
        else:
            print("   ⚠️  Many broken links - needs cleanup.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_moc_links.py <vault_path>")
        sys.exit(1)

    vault_path = sys.argv[1]

    if not os.path.exists(vault_path):
        print(f"❌ Error: Vault path does not exist: {vault_path}")
        sys.exit(1)

    results = check_moc_links(vault_path)
    print_results(results)

if __name__ == "__main__":
    main()
