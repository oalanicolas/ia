#!/usr/bin/env python3
"""
Fix broken wikilinks in MOC files based on vault structure.
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

def fix_episode_links(content, moc_path, vault_path):
    """
    Fix episode links in MOC - Episódios VL.md

    Changes [[001 - Por quê?]] to [[Episódios VL/001 - Por quê?]]
    """
    vault_path = Path(vault_path)
    moc_path = Path(moc_path)

    # Pattern for episode links: [[001 - Title]] through [[024 - Title]]
    # Also matches PN episodes
    episode_pattern = r'\[\[((?:PN - |0[0-2][0-9] - )[^\]]+)\]\]'

    def replace_episode(match):
        episode_name = match.group(1)
        # Check if it already has the folder path
        if 'Episódios VL/' in episode_name or '../Vida Lendária/Episódios VL/' in episode_name:
            return match.group(0)  # Already has path, don't modify

        # Check if file exists in Episódios VL
        episode_file = vault_path / "Vida Lendária" / "Episódios VL" / f"{episode_name}.md"
        if episode_file.exists():
            return f"[[Episódios VL/{episode_name}]]"

        return match.group(0)  # File doesn't exist, keep as is

    fixed_content = re.sub(episode_pattern, replace_episode, content)
    changes = len(re.findall(episode_pattern, content)) - len(re.findall(episode_pattern, fixed_content))

    return fixed_content, changes

def fix_moc_cross_references(content, moc_path, vault_path):
    """
    Fix cross-references between MOCs.

    Changes [[../Anotações/MOC - Title]] to [[MOC - Title]]
    """
    vault_path = Path(vault_path)

    # Pattern for MOC cross-references
    moc_ref_pattern = r'\[\[\.\.\/Anotações\/(MOC - [^\]]+)\]\]'

    fixed_content = re.sub(moc_ref_pattern, r'[[\1]]', content)
    changes = content.count('../Anotações/MOC')

    return fixed_content, changes

def fix_vida_lendaria_references(content, moc_path, vault_path):
    """
    Fix references to Vida Lendária content from MOCs folder.

    Changes [[../Vida Lendária/...]] to [[Vida Lendária/...]]
    """
    # For MOCs in /MOCs/ folder
    if '/MOCs/' in str(moc_path):
        pattern = r'\[\[\.\.\/Vida Lendária\/([^\]]+)\]\]'
        fixed_content = re.sub(pattern, r'[[Vida Lendária/\1]]', content)
        changes = content.count('../Vida Lendária/')
        return fixed_content, changes

    return content, 0

def fix_anotacoes_index(content, moc_path, vault_path):
    """
    Fix reference to Anotações index.

    Changes [[/Anotações/📇 Index]] to [[Anotações/📇 Index]]
    """
    fixed_content = content.replace('[[/Anotações/📇 Index]]', '[[Anotações/📇 Index]]')
    changes = content.count('[[/Anotações/📇 Index]]')
    return fixed_content, changes

def fix_moc_file(moc_path, vault_path, dry_run=False):
    """Apply all fixes to a MOC file."""
    moc_path = Path(moc_path)

    try:
        with open(moc_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        content = original_content
        total_changes = 0
        fixes_applied = []

        # Apply fixes
        if 'MOC - Episódios VL' in moc_path.name:
            content, changes = fix_episode_links(content, moc_path, vault_path)
            if changes > 0:
                fixes_applied.append(f"Fixed {changes} episode links")
                total_changes += changes

        content, changes = fix_moc_cross_references(content, moc_path, vault_path)
        if changes > 0:
            fixes_applied.append(f"Fixed {changes} MOC cross-references")
            total_changes += changes

        content, changes = fix_vida_lendaria_references(content, moc_path, vault_path)
        if changes > 0:
            fixes_applied.append(f"Fixed {changes} Vida Lendária references")
            total_changes += changes

        content, changes = fix_anotacoes_index(content, moc_path, vault_path)
        if changes > 0:
            fixes_applied.append(f"Fixed {changes} Anotações index references")
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
                    'fixes': fixes_applied,
                    'backup': backup_path,
                    'modified': True
                }
            else:
                return {
                    'file': str(moc_path.relative_to(vault_path)),
                    'changes': total_changes,
                    'fixes': fixes_applied,
                    'modified': False
                }

        return None

    except Exception as e:
        print(f"❌ Error processing {moc_path}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_moc_links.py <vault_path> [--dry-run]")
        sys.exit(1)

    vault_path = Path(sys.argv[1])
    dry_run = '--dry-run' in sys.argv

    if not vault_path.exists():
        print(f"❌ Error: Vault path does not exist: {vault_path}")
        sys.exit(1)

    # Find all MOC files
    moc_files = list(vault_path.rglob("MOC*.md"))

    print(f"🔧 {'[DRY RUN] ' if dry_run else ''}Fixing links in {len(moc_files)} MOC files...\n")

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
        print(f"🔗 Fixed {total_changes} total links\n")

        for result in results:
            print(f"\n📄 {result['file']}")
            print(f"   Changes: {result['changes']}")
            for fix in result['fixes']:
                print(f"   • {fix}")
            if not dry_run and 'backup' in result:
                print(f"   Backup: {Path(result['backup']).name}")
    else:
        print("\n✅ No fixes needed - all links are already correct!")

    print("\n" + "=" * 70)

    if dry_run:
        print("\n💡 This was a dry run. Run without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
