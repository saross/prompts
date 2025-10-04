# Template Workflow Principle
**Created**: 2025-10-04
**Purpose**: Core principle about template creation in Fieldmark
**Audience**: LLMs and documentation authors

---

## Core Principle {essential}

**Templates are an advanced feature, not the primary workflow.**

Most Fieldmark users:
1. Create a notebook directly
2. Use and refine the notebook
3. Later (optionally) convert it to a template for reuse

**NOT**:
1. ~~Design template first~~
2. ~~Deploy notebooks from template~~

---

## Two Ways to Create Templates

### Method 1: From Existing Notebook (Most Common) {essential}

**Workflow**:
1. User creates and uses a notebook
2. Notebook proves useful and well-designed
3. User converts notebook to template via Dashboard
4. Template can be used to create new notebooks with same structure

**UI Process**:
- Dashboard → Select notebook → Actions → "Convert to Template"
- No special editor or interface
- Simple conversion operation

**Priority**: Document this as the primary template creation method

---

### Method 2: From Scratch (Advanced Users) {important}

**Workflow**:
1. User goes to Templates interface
2. Clicks "Create Template"
3. Template Designer opens → **This is just the Notebook Editor**
4. Design works exactly like designing a notebook
5. Save template (instead of notebook)

**Key Insight**: Template Designer = Notebook Editor with different save target

**UI Identity**: Same interface, same workflows, same modal dialogs, same field configuration

**Documentation Implication**: Don't create separate Template Designer UI documentation. Reference Notebook Editor documentation and note the minimal differences.

---

## Documentation Priorities

### High Priority {essential}

1. **Notebook Editor UI** - Core interface for creating notebooks (and templates)
2. **Notebook-to-Template Conversion** - Most common template creation path
3. **Template Usage** - How to create notebooks from templates

### Low Priority {comprehensive}

4. **Template-from-Scratch UI** - Just reference Notebook Editor with note: "Template Designer uses the same interface as Notebook Editor"

---

## Common Documentation Mistake to Avoid

❌ **DON'T**: Treat templates as the foundation of Fieldmark workflow
❌ **DON'T**: Document Template Designer as a separate major UI component
❌ **DON'T**: Prioritize template creation over notebook creation in user guides

✅ **DO**: Show notebook creation first, template conversion as optional advanced step
✅ **DO**: Reference Notebook Editor when discussing Template Designer UI
✅ **DO**: Emphasize templates as reusable patterns, not required workflow

---

## UI Documentation Impact

### For Screenshot Sessions

**Notebook Editor**: Full documentation needed
- Complete workflow capture
- All modal dialogs
- Field configuration patterns
- Form/section creation
- Settings panels

**Template Designer**: Minimal documentation needed
- Screenshot: "Create Template" button location
- Screenshot: Template list interface
- Note: "Editor interface identical to Notebook Editor, see [link]"
- Screenshot: Template-to-notebook creation workflow

**Estimated savings**: ~10-15 hours by not re-documenting Template Designer as separate component

---

## Cross-References

- Dashboard documentation: `/dashboard/templates-interface.md`
- Notebook Editor: (To be documented in Tier 1)
- Template conversion: (To be documented in Dashboard session)

---

## For LLM Instruction Generation

When asked to generate template-related documentation:

1. **Check context**: Is user creating template from scratch or from existing notebook?
2. **Reference appropriately**:
   - From scratch → "Use Notebook Editor (see [link]), save as template"
   - From notebook → "Convert existing notebook via Dashboard → Actions"
3. **Don't duplicate**: Don't regenerate Notebook Editor UI instructions for Template Designer

---

**Remember**: Templates are powerful but optional. Most users start with notebooks, not templates.
