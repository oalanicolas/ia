---
name: pkm-vault-master
description: This skill should be used when organizing and structuring Personal Knowledge Management (PKM) vaults, particularly Obsidian vaults using the Linking Your Thinking (LYT) methodology. Use this skill when the user asks to analyze notes, create MOCs (Maps of Content), find related notes, organize folders, generate Index.md files, or improve vault structure. This skill provides Python scripts for vault analysis, link finding, and MOC generation, along with LYT methodology references and templates.
---

# PKM Vault Master

## Overview

Provide expert assistance for organizing and structuring Personal Knowledge Management (PKM) systems, specifically Obsidian vaults following the Linking Your Thinking (LYT) framework by Nick Milo.

This skill enables:
- **Vault analysis**: Analyze folders to identify orphan notes, hub notes, and link patterns
- **Link discovery**: Find related notes based on content similarity
- **MOC generation**: Create structured Maps of Content from collections of notes
- **Structure guidance**: Apply LYT best practices to improve vault organization

---

## When to Use This Skill

Trigger this skill when the user asks to:
- "Analyze my Anotações folder"
- "Find notes related to [topic]"
- "Create a MOC for my notes about [theme]"
- "Organize these notes"
- "Which notes should I link?"
- "Generate an Index.md for this folder"
- "Help me structure my vault"
- "Find orphan notes"
- "What are my hub notes?"
- "Improve my PKM system"
- "Analyze my books" / "Analyze book library"
- "Which authors need profiles?"
- "Prioritize authors" / "Author priorities"
- "Book depth analysis"

---

## Core Capabilities

### 1. Vault Analysis

Analyze a folder of markdown notes to understand structure and identify improvements.

**Use the script:**
```bash
python scripts/vault_analyzer.py <folder_path> [--detailed]
```

**What it provides:**
- Total notes and links count
- Average links per note
- Orphan notes (no incoming/outgoing links)
- Hub notes (10+ links - central concepts)
- Empty/stub notes
- Large notes (500+ words)
- Link distribution patterns

**When to analyze:**
- User wants overview of folder health
- Before organizing/restructuring
- To identify which notes need attention
- To find disconnected content

**How to interpret results:**
- **Orphan notes** → Need linking or may be deletable
- **Hub notes** → Central concepts, consider Evergreens
- **Low avg links/note** → Under-connected vault
- **Empty notes** → Stubs to develop or remove

**Example workflow:**
```
User: "Analyze my Anotações folder"

1. Run: python scripts/vault_analyzer.py ~/vault/Anotações --detailed
2. Review output: orphan count, hub notes, link density
3. Suggest:
   - Link orphan notes to relevant concepts
   - Develop hub notes into MOCs
   - Archive or develop empty stubs
   - Create MOCs for clusters of 7+ related notes
```

---

### 2. Finding Related Notes

Discover which notes should be linked based on content similarity.

**Use the script:**
```bash
python scripts/link_finder.py <note_path> <vault_folder> [--top N]
```

**What it provides:**
- Top N most similar notes by content
- Similarity scores (0-1 range)
- Top keywords in target note
- Suggested links to add

**How it works:**
- Extracts keywords from markdown (filters stopwords)
- Calculates cosine similarity between keyword vectors
- Ranks notes by similarity

**When to use:**
- User asks "What should I link to this note?"
- Creating atomic notes that need connections
- Developing existing notes
- Before creating MOCs (find natural clusters)

**Example workflow:**
```
User: "Find notes related to Hábitos.md"

1. Run: python scripts/link_finder.py ~/vault/Anotações/Hábitos.md ~/vault/Anotações --top 10
2. Review top matches with scores
3. Suggest adding [[links]] to top 3-5 most relevant notes
4. Explain WHY they're related (based on shared keywords)
```

**Best practices:**
- Scores >0.3 = strong relation worth linking
- Scores 0.1-0.3 = moderate relation, link if contextually relevant
- Scores <0.1 = weak relation, usually skip
- Always explain the relationship when suggesting links

---

### 3. MOC Generation

Create Maps of Content (MOCs) from folders of related notes.

**Use the script:**
```bash
python scripts/moc_generator.py <folder_path> "<moc_name>" [--stage {1,2}]
```

**Stage 1 (List):**
- Simple list of all notes in folder
- 1-paragraph intro placeholder
- Takes ~10 minutes to create
- Use when: First organizing a theme

**Stage 2 (Workbench):**
- Groups notes by keyword clusters
- Adds structure with sub-themes
- Includes thinking prompts
- Use when: Actively developing theme

**When to create MOCs:**
- Folder has 7-10+ related notes
- User wants to organize a theme
- Starting new project (Effort)
- Theme needs structure

**After generation:**
1. Customize the intro paragraphs
2. Refine sub-theme groupings
3. Add contextual comments
4. Link to related MOCs
5. Add to Home.md if major theme

**Example workflow:**
```
User: "Create a MOC for my IA notes"

1. Analyze: How many notes? (scripts/vault_analyzer.py)
2. If 7-10+:
   - Generate Stage 1: python scripts/moc_generator.py ~/vault/Anotações "IA & Tecnologia" --stage 1
   - Or Stage 2 if user is actively working theme
3. Save output to: ~/vault/ATLAS/MOC - IA & Tecnologia.md
4. Suggest:
   - Customize intro
   - Review groupings
   - Link to [[Home]]
   - Link to related MOCs
```

---

### 4. Applying LYT Methodology

Reference the LYT framework when advising on vault organization.

**Load reference when needed:**
```
Read: references/lyt-methodology.md
```

**Key principles to apply:**

**Linking:**
- Minimum 2-3 links per note
- Explain WHY linking (add context)
- "Linking IS Thinking" - each link is cognitive work

**MOCs:**
- Non-destructive (note can be in multiple MOCs)
- Evolve through stages (List → Workbench → Hub)
- Create when 7-10+ related notes

**Structure:**
- Keep folders minimal (ACE: ATLAS, CALENDAR, EXTRAS)
- Use Index.md as MOC for each folder
- Home.md as dashboard
- 3-7 active Efforts (projects) max

**Note-making:**
- Atomic notes (one idea = one note)
- Evergreens for concepts refined over time
- Develop ideas in your own words (not just highlights)

**Avoid:**
- Collector's Fallacy (collecting ≠ knowing)
- Over-categorization (let structure emerge)
- Too many Efforts (dilutes focus)
- Perfectionism (70% done is enough to share)

**Reference templates:**
```
Read: references/moc-templates.md
```

Use templates for:
- MOC Stage 1, 2, 3
- Effort/Project MOCs
- Index.md files
- Customized for user's vault style

---

### 5. Creating Index.md Files

Generate Index.md MOCs for folders to improve navigation.

**Structure for Index.md:**
1. Overview of folder purpose
2. Stats (total notes, last updated)
3. Notes organized by theme/category
4. Navigation table (if folder is large)
5. Connections to other sections
6. Link back to Home

**Example workflow:**
```
User: "Create an Index.md for my Recursos folder"

1. Analyze folder:
   - python scripts/vault_analyzer.py ~/vault/Recursos
2. Identify natural categories (Templates, Livros, Autores, etc)
3. Use Template 5 from references/moc-templates.md
4. Customize:
   - Add real stats
   - List actual categories found
   - Link to specific notes
   - Connect to other sections
5. Save as: ~/vault/Recursos/📇 Index.md
```

---

## Workflow Decision Tree

**User request → Decision path:**

```
REQUEST: "Analyze my vault/folder"
→ Use: scripts/vault_analyzer.py
→ Report: stats, orphans, hubs, suggestions

REQUEST: "Find related notes" or "What should I link?"
→ Use: scripts/link_finder.py
→ Report: top similar notes with scores
→ Suggest: specific [[links]] to add with reasoning

REQUEST: "Create/organize MOC" or "Structure these notes"
→ Check: How many notes? (>7-10?)
→ Use: scripts/moc_generator.py (stage 1 or 2)
→ Customize: intro, groupings, connections
→ Advise: where to save, how to evolve

REQUEST: "Organize folder" or "Create Index"
→ Analyze folder first
→ Use: Template 5 (Index.md) from references
→ Customize: with actual categories and notes
→ Link: to other sections

REQUEST: "How do I [PKM concept]?" or "What's the best way to..."
→ Load: references/lyt-methodology.md
→ Advise: based on LYT principles
→ Suggest: concrete next steps

REQUEST: Multiple steps (analyze + organize + create MOCs)
→ Break into sequential tasks
→ Use appropriate scripts/templates per step
→ Provide holistic recommendation at end
```

---

## Best Practices

### Always:
- ✅ Explain WHY suggesting changes (not just what)
- ✅ Use concrete examples from user's vault
- ✅ Reference LYT principles when advising
- ✅ Suggest 3-5 actionable next steps
- ✅ Explain the relationship when suggesting links
- ✅ Customize templates to user's style/voice

### Avoid:
- ❌ Over-organizing (let structure emerge)
- ❌ Suggesting perfect structure upfront
- ❌ Generic advice without vault-specific context
- ❌ Creating MOCs with <7 notes
- ❌ Overwhelming user with 20+ suggestions

### When uncertain:
- Ask clarifying questions
- Start with analysis (scripts/vault_analyzer.py)
- Propose options rather than dictating structure
- Reference methodology for guidance

---

## Typical Workflows

### Complete Folder Organization

```
1. ANALYZE
   → python scripts/vault_analyzer.py ~/vault/Anotações --detailed
   → Understand: total notes, orphans, hubs, patterns

2. FIND CONNECTIONS
   → For orphan notes: python scripts/link_finder.py <orphan_path> ~/vault/Anotações
   → Suggest links to integrate them

3. IDENTIFY CLUSTERS
   → Group related notes (7-10+) into themes
   → Use link_finder to validate clusters

4. CREATE MOCS
   → For each cluster: python scripts/moc_generator.py
   → Generate Stage 1 or 2 depending on user's engagement

5. CREATE INDEX
   → Use Template 5 to create Index.md
   → Link all MOCs and major notes
   → Add navigation table

6. UPDATE HOME
   → Add major MOCs to Home.md
   → Link Index.md from Home
```

### Developing a Single Note

```
1. ANALYZE CURRENT STATE
   → Check: links, word count, development

2. FIND RELATED
   → python scripts/link_finder.py <note_path> ~/vault/folder
   → Identify top 5 related notes

3. SUGGEST LINKS
   → Explain relationship for each suggested link
   → Recommend minimum 3 links

4. CHECK FOR MOC
   → If note has 10+ links → consider Evergreen
   → If theme has 7-10 related → suggest MOC

5. EVOLVE
   → Suggest how to develop further
   → Connect to Efforts if relevant
```

### Creating New MOC

```
1. VALIDATE NEED
   → Check: >7-10 related notes?
   → If yes, proceed

2. CHOOSE STAGE
   → Stage 1: just starting to explore theme
   → Stage 2: actively working on theme

3. GENERATE
   → python scripts/moc_generator.py ~/folder "Theme Name" --stage N
   → Save output to ATLAS/MOC - Theme Name.md

4. CUSTOMIZE
   → Write personalized intro (1-2 paragraphs)
   → Refine sub-theme groups
   → Add thinking/questions sections

5. INTEGRATE
   → Link from Home.md (if major)
   → Link from related MOCs
   → Link from Effort if project-related
```

---

## Resources

### Scripts (scripts/)

**vault_analyzer.py**
- Analyzes folders for PKM health metrics
- Identifies orphan notes, hubs, empty stubs
- Provides link distribution patterns
- Execute without loading into context for speed

**link_finder.py**
- Finds content-similar notes using keyword extraction
- Calculates cosine similarity scores
- Suggests specific [[links]] to add
- Helps combat "orphan note" problem

**moc_generator.py**
- Generates MOC templates (Stage 1 or 2)
- Clusters notes by keywords into sub-themes
- Creates ready-to-customize markdown
- Saves hours of manual MOC creation

**book_analyzer.py**
- Analyzes book library depth and completeness
- Identifies authors with multiple books (profile priorities)
- Cross-references with existing author profiles
- Generates prioritized reports for content planning
- Outputs to `_reports/` with timestamp

### Workflows (workflows/)

**book-analysis.md**
- Complete workflow for book/author analysis
- Depth level criteria (Stub → Exemplar)
- Prioritization formula for new author profiles
- Integration with other vault systems

### References (references/)

**lyt-methodology.md**
- Complete LYT framework reference
- Core principles (Linking IS Thinking, MOCs, Idea Emergence)
- MOC evolution stages explained
- Best practices and common pitfalls
- Decision framework for linking/MOC creation
- Load when user asks conceptual PKM questions

**moc-templates.md**
- 5 production-ready templates:
  - MOC Stage 1 (List)
  - MOC Stage 2 (Workbench)
  - MOC Stage 3 (Hub)
  - Effort/Project MOC
  - Index.md (Folder MOC)
- Selection guide for choosing right template
- Customization guidelines

---

## Examples

### Example 1: Analyzing a folder

**User:** "Analyze my Anotações folder and tell me what needs work"

**Response:**
```
Analyzing ~/vault/Anotações...

[Run: python scripts/vault_analyzer.py ~/vault/Anotações --detailed]

📊 Results:
- 267 notes total
- 3.2 avg links/note (❌ below target of 3-5)
- 47 orphan notes (❌ 17% - should be <5%)
- 12 hub notes (✅ good central concepts)

🎯 Recommendations:

1. **Link orphan notes** (47 need connections)
   - Run link_finder on top 10 orphans
   - Add minimum 2-3 links each

2. **Develop hub notes into MOCs**
   - [[LLMs]] (18 links) → Create "MOC - IA & Tecnologia"
   - [[Hábitos]] (15 links) → Create "MOC - Produtividade"

3. **Increase link density**
   - Target: 3-5 links/note average
   - Currently: 3.2 (add ~50 more links total)

4. **Create Index.md**
   - Organize 267 notes into themes
   - Add navigation table

Want me to start with any of these?
```

### Example 2: Finding related notes

**User:** "What notes should I link to my note about Procrastinação?"

**Response:**
```
Finding related notes...

[Run: python scripts/link_finder.py ~/vault/Anotações/Procrastinação.md ~/vault/Anotações --top 10]

🔗 Top Related Notes:

1. [[Hábitos]] — 0.42 similarity
   Both discuss behavioral patterns and change

2. [[Decisão]] — 0.38 similarity
   Shared concepts: mental energy, willpower, choice

3. [[Atenção]] — 0.35 similarity
   Both about managing cognitive resources

4. [[Foco Lazer]] — 0.31 similarity
   Related via focus, distraction, time management

5. [[Se tá pesado está errado]] — 0.28 similarity
   Both address when tasks feel difficult

💡 Suggested Links to Add:

Add these to [[Procrastinação]]:
- [[Hábitos]] — procrastination is often habit-driven
- [[Decisão]] — procrastination as decision avoidance
- [[Atenção]] — attention management prevents procrastination

Consider creating MOC if you have 7-10 related notes on productivity/behavior.
```

### Example 3: Creating a MOC

**User:** "Create a MOC for my notes about IA"

**Response:**
```
Creating MOC for IA theme...

[Step 1: Analyze]
Found 49 notes related to IA in ~/vault/Anotações

[Step 2: Generate Stage 2 Workbench]
[Run: python scripts/moc_generator.py ~/vault/Anotações "IA & Tecnologia" --stage 2]

✅ Created: MOC - IA & Tecnologia (Stage 2)

📊 Structure:
- 49 notes organized into 4 sub-themes:
  - Fundamentos (LLMs, embeddings, fine-tuning)
  - Aplicações (Aurora, ChatVolt, Finch)
  - Desenvolvimento (Git, Web, Interface)
  - Análise (reflexões, perigos, mercado)

🎯 Next Steps:

1. Save to: ~/vault/ATLAS/MOC - IA & Tecnologia.md

2. Customize:
   - Write intro (what you're exploring in IA)
   - Review sub-theme groupings
   - Add "Pensamentos em Desenvolvimento" section

3. Link from:
   - [[Home]] (main MOC section)
   - [[MOC - Prompts e GPTs]] (related theme)

4. Link to:
   - [[/IA/📇 Index|IA & Prompts section]]

Want me to save this and update your Home.md?
```

---

### 6. Book Analysis & Author Prioritization

Analyze the book library to assess depth of summaries and identify authors who should have profiles created.

**Use the script:**
```bash
python scripts/book_analyzer.py <vault_path> [--output report.md]
```

**What it provides:**
- Distribution of books by depth level (Stub → Exemplar)
- Authors with multiple books (priority for profiles)
- Cross-reference with existing author profiles
- List of books needing development

**Depth Levels:**
| Level | Name | Words | Description |
|-------|------|-------|-------------|
| 1 | STUB | <200 | Needs urgent development |
| 2 | BÁSICO | 200-500 | Partial template |
| 3 | INTER | 500-1500 | Complete but superficial |
| 4 | COMPLETO | 1500-3000 | Complete and detailed |
| 5 | EXEMPLAR | 3000+ | Reference quality |

**When to use:**
- Planning author profile creation
- Reviewing book library health
- Preparing Vida Lendária content
- Quarterly content strategy review

**Example workflow:**
```
User: "Analyze my books and tell me which authors need profiles"

1. Run: python scripts/book_analyzer.py ~/vault --output _reports/book_analysis.md
2. Review output:
   - Authors with 3+ books → High priority for profile
   - Authors with exemplar summaries → High engagement
   - Cross-reference with existing profiles
3. Suggest priorities based on:
   - Number of books
   - Total word count
   - Theme alignment
   - VL mentions

🎯 Prioritization Formula:
Score = (Num_Books × 3) + (Words/1000 × 2) + (Theme_Aligned × 2)
```

**Workflow documentation:** `workflows/book-analysis.md`

---

This skill follows the Linking Your Thinking (LYT) methodology by Nick Milo and provides practical tools for vault organization.
