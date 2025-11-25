#!/usr/bin/env python3
"""
Fix broken wikilinks in MOC files - Obsidian-aware version.

Obsidian wikilinks work globally across the vault:
- [[File Name]] searches the entire vault
- [[Folder/File Name]] uses explicit path
- [[../Relative/Path]] DOES NOT WORK in Obsidian

This script only fixes:
1. Relative paths with ../ (not supported in Obsidian)
2. Absolute paths starting with / (should be relative)
"""

import os
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

def backup_file(file_path):
    """Create backup of file before modifying."""
    backup_path = str(file_path) + f".backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def fix_relative_paths(content, moc_path, vault_path):
    """
    Fix relative paths with ../ that don't work in Obsidian.

    Obsidian searches files globally, so [[File]] is better than [[../Folder/File]]
    """
    changes = 0

    # Pattern 1: ../Vida Lendária/... → just the filename
    # Since Obsidian searches globally, we can simplify
    pattern1 = r'\[\[\.\.\/Vida Lendária\/(?:Episódios VL|Ensaios|Ideias p: Novos Episódios)\/([^\]]+)\]\]'
    matches = re.findall(pattern1, content)
    if matches:
        content = re.sub(pattern1, r'[[\1]]', content)
        changes += len(matches)

    # Pattern 2: ../Anotações/MOC - ... → MOC - ...
    pattern2 = r'\[\[\.\.\/Anotações\/(MOC - [^\]]+)\]\]'
    matches = re.findall(pattern2, content)
    if matches:
        content = re.sub(pattern2, r'[[\1]]', content)
        changes += len(matches)

    # Pattern 3: ../Vida Lendária/MOC - ... → MOC - ...
    pattern3 = r'\[\[\.\.\/Vida Lendária\/(MOC - [^\]]+)\]\]'
    matches = re.findall(pattern3, content)
    if matches:
        content = re.sub(pattern3, r'[[\1]]', content)
        changes += len(matches)

    # Pattern 4: ../IA/Prompts/... → just the filename
    pattern4 = r'\[\[\.\.\/IA\/Prompts\/([^\]]+)\]\]'
    matches = re.findall(pattern4, content)
    if matches:
        content = re.sub(pattern4, r'[[\1]]', content)
        changes += len(matches)

    # Pattern 5: /Anotações/... → just the filename
    pattern5 = r'\[\[\/Anotações\/([^\]]+)\]\]'
    matches = re.findall(pattern5, content)
    if matches:
        content = re.sub(pattern5, r'[[\1]]', content)
        changes += len(matches)

    return content, changes

def fix_moc_file(moc_path, vault_path, dry_run=False):
    """Apply fixes to a MOC file."""
    moc_path = Path(moc_path)

    try:
        with open(moc_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        content = original_content
        total_changes = 0

        # Fix relative paths
        content, changes = fix_relative_paths(content, moc_path, vault_path)
        total_changes += changes

        # Write changes
        if total_changes > 0:
            if not dry_run:
                backup_path = backup_file(moc_path)
                with open(moc_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return {
                    'file': str(moc_path.relative_to(vault_path)),
                    'changes': total_changes,
                    'backup': backup_path,
                    'modified': True
                }
            else:
                return {
                    'file': str(moc_path.relative_to(vault_path)),
                    'changes': total_changes,
                    'modified': False
                }

        return None

    except Exception as e:
        print(f"❌ Error processing {moc_path}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_moc_links_v2.py <vault_path> [--dry-run]")
        sys.exit(1)

    vault_path = Path(sys.argv[1])
    dry_run = '--dry-run' in sys.argv

    if not vault_path.exists():
        print(f"❌ Error: Vault path does not exist: {vault_path}")
        sys.exit(1)

    # Find all MOC files
    moc_files = list(vault_path.rglob("MOC*.md"))

    print(f"🔧 {'[DRY RUN] ' if dry_run else ''}Fixing relative paths in {len(moc_files)} MOC files...\n")
    print("ℹ️  Obsidian wikilinks search globally - [[File]] is preferred over [[../Folder/File]]\n")

    results = []
    for moc_file in sorted(moc_files):
        result = fix_moc_file(moc_file, vault_path, dry_run)
        if result:
            results.append(result)

    # Print summary
    print("=" * 70)
    print(f"📊 FIX SUMMARY {'(DRY RUN)' if dry_run else ''}")
    print("=" * 70)

    if results:
        total_changes = sum(r['changes'] for r in results)
        print(f"\n✅ Modified {len(results)} MOC files")
        print(f"🔗 Fixed {total_changes} relative path links\n")

        for result in results:
            print(f"\n📄 {result['file']}")
            print(f"   Fixed {result['changes']} relative paths (../)")
            if not dry_run and 'backup' in result:
                print(f"   Backup: {Path(result['backup']).name}")
    else:
        print("\n✅ No relative paths found - all links use Obsidian's global search!")

    print("\n" + "=" * 70)

    if dry_run:
        print("\n💡 This was a dry run. Run without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
