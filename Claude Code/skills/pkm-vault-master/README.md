# PKM Vault Master - Skill Documentation

**Version:** 1.0
**Status:** ✅ Production Ready
**Last Updated:** 2025-11-05

---

## Overview

PKM Vault Master is a comprehensive skill for organizing and structuring Personal Knowledge Management (PKM) vaults, specifically Obsidian vaults following the **Linking Your Thinking (LYT)** methodology by Nick Milo.

This skill provides:
- ✅ **Vault analysis** - Identify orphan notes, hub notes, and link patterns
- ✅ **Link discovery** - Find related notes based on content similarity
- ✅ **MOC generation** - Create structured Maps of Content from note collections
- ✅ **LYT guidance** - Apply best practices from Linking Your Thinking framework

---

## When to Use This Skill

Activate this skill when you ask to:
- "Analyze my vault/folder"
- "Find notes related to [topic]"
- "Create a MOC for [theme]"
- "Organize these notes"
- "Which notes should I link?"
- "Generate an Index.md"
- "Help me structure my PKM system"

---

## Quick Start

### 1. Analyze a Folder

```bash
python scripts/vault_analyzer.py ~/vault/Anotações
```

**Output:**
- Total notes and links
- Orphan notes (disconnected)
- Hub notes (highly connected)
- Link density metrics
- Empty/stub notes
- Large notes (500+ words)

### 2. Find Related Notes

```bash
python scripts/link_finder.py ~/vault/Anotações/MyNote.md ~/vault/Anotações --top 10
```

**Output:**
- Top 10 most similar notes
- Similarity scores (0-1 range)
- Top keywords in target note
- Suggested links to add

### 3. Generate a MOC

```bash
# Stage 1: Simple list
python scripts/moc_generator.py ~/vault/Anotações "Theme Name" --stage 1

# Stage 2: Grouped workbench
python scripts/moc_generator.py ~/vault/Anotações "Theme Name" --stage 2
```

**Output:**
- Formatted MOC markdown
- Notes organized by theme/keyword
- Ready-to-customize structure
- Links to related MOCs

---

## Available Resources

### Scripts (`scripts/`)

**vault_analyzer.py**
- Analyzes folder health
- Identifies orphan and hub notes
- Provides actionable metrics
- No context loading needed (fast execution)

**link_finder.py**
- Content-based similarity matching
- Keyword extraction and comparison
- Suggests specific [[wikilinks]]
- Handles Unicode characters correctly (macOS safe)

**moc_generator.py**
- Generates MOC templates (Stage 1 or 2)
- Automatic keyword clustering
- Date-stamped outputs
- Portuguese-optimized

### References (`references/`)

**lyt-methodology.md**
- Complete LYT framework
- Core principles and practices
- MOC evolution stages
- Decision frameworks
- Common pitfalls

**moc-templates.md**
- 5 production-ready templates
- Template selection guide
- Customization examples
- Portuguese formatting

---

## Tested & Validated

All scripts have been tested on real vault data:

✅ **vault_analyzer.py**
- Tested on 215-note folder
- Correctly identified 64 orphans, 6 hubs
- Link distribution visualization working
- Empty note detection accurate

✅ **link_finder.py**
- Content similarity working correctly
- Unicode filename support (macOS)
- Excludes target note from results
- Keyword extraction accurate

✅ **moc_generator.py**
- Stage 1 templates generated successfully
- Stage 2 keyword clustering working
- Handles 200+ notes efficiently
- Portuguese text formatting correct

---

## Example Workflow

### Complete Folder Organization

1. **Analyze** → Understand current state
2. **Link orphans** → Use link_finder to connect isolated notes
3. **Identify clusters** → Group related notes (7-10+)
4. **Create MOCs** → Generate Stage 1 or 2 for each cluster
5. **Create Index** → Build Index.md for folder navigation
6. **Update Home** → Link major MOCs from Home.md

### Developing a Single Note

1. **Check state** → Links, word count, development
2. **Find related** → Run link_finder
3. **Add links** → Suggest top 3-5 connections
4. **Evaluate** → Consider Evergreen status or MOC creation

---

## LYT Principles

This skill follows these core LYT concepts:

- **Linking IS Thinking** - Each link is cognitive work
- **MOCs over Folders** - Structure through links, not hierarchy
- **Emergence over Planning** - Let structure emerge naturally
- **Atomic Notes** - One idea = one note
- **Evergreens** - Develop notes over time
- **7-10 Rule** - Create MOC when theme has 7-10+ related notes

---

## Skill Metadata

**Frontmatter:**
```yaml
name: pkm-vault-master
description: This skill should be used when organizing and structuring Personal Knowledge Management (PKM) vaults, particularly Obsidian vaults using the Linking Your Thinking (LYT) methodology. Use this skill when the user asks to analyze notes, create MOCs (Maps of Content), find related notes, organize folders, generate Index.md files, or improve vault structure.
```

**Location:** `.claude/skills/pkm-vault-master/`

**Structure:**
```
pkm-vault-master/
├── SKILL.md              # Main skill instructions (15KB, comprehensive)
├── README.md             # This file
├── scripts/
│   ├── vault_analyzer.py # Analyze folder health
│   ├── link_finder.py    # Find related notes
│   └── moc_generator.py  # Generate MOCs
└── references/
    ├── lyt-methodology.md    # LYT framework reference
    └── moc-templates.md      # MOC templates library
```

---

## Future Enhancements

Potential improvements for v2.0:
- [ ] Recursive folder analysis
- [ ] Graph visualization export
- [ ] Automated link suggestions batch mode
- [ ] Custom clustering algorithms
- [ ] Integration with Obsidian plugins
- [ ] Multi-language support (beyond Portuguese)

---

## Support

For issues or questions:
- See SKILL.md for detailed usage instructions
- Check references/ for methodology guidance
- Review example workflows in this README

Created with ❤️ for the Mentelendária vault
