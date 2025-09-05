# Documentation State & Decisions Record
## Fieldmark LLM-First Documentation Project

**Last Updated**: January 2025  
**Purpose**: Maintain continuity across chat sessions during documentation development  
**Status**: Active development - Phase 1 (Consolidation & Gap Analysis)

---

## 1. Project Context

### System Overview
- **Current brand**: Fieldmark (electronic field notebook platform)
- **Legacy references**: FAIMS3, FAIMS (may appear in older documentation)
- **Company**: Electronic Field Notebooks Pty Ltd
- **Project history**: Open-source research infrastructure project at Australian universities, now commercialised as COSS (Commercial Open Source Software)

### Component Architecture
- **Control Centre**: Web application for administration
- **Designer**: Web application for notebook creation (modal overlay 95vw × 95vh)
- **Notebook**: Web and mobile applications for data collection (iOS, Android, PWA)

### Technical Environment
- JSON as primary configuration format
- Web-based Designer with real-time preview
- Cross-platform mobile applications (iOS, Android)
- Progressive web application for desktop use
- Redux-based state management within Designer sessions
- Automatic JSON migration and validation on notebook load
- Clean JSON export with internal tracking identifiers stripped

### Terminology Alignment
**Critical**: The system employs dual terminology that must be reconciled:
- **User-facing terms**: Forms → Sections → Fields
- **Technical implementation**: Viewsets → Views → Fields
- Documentation must bridge these perspectives seamlessly

### JSON-GUI Duality
Fieldmark supports multiple creation pathways:
- GUI-based design through Designer web application
- Direct JSON manipulation through text editors
- AI-assisted generation via Claude Code
- Hybrid approaches combining all methods
This flexibility must be reflected in all documentation and examples.

---

## 2. Format Decisions

### LLM-First Documentation Philosophy
**Core Principle**: Single comprehensive master document optimised for LLM parsing
- Master document serves as single source of truth
- Downstream documentation generated via extraction/transformation
- Interactive knowledge base when loaded into LLM
- **Status**: Experimental approach requiring iterative refinement through testing

### Three-Tier Documentation Model
As agreed, all documentation follows a three-tier stratification:
1. **{essential}** Quick Start (5-minute comprehension target)
   - Essential concepts only
   - Most common use cases
   - Minimal viable examples

2. **{important}** Reference (working documentation)
   - Complete property listings
   - Standard patterns
   - Troubleshooting procedures

3. **{comprehensive}** Deep Dive (complete understanding)
   - Implementation rationales
   - Performance implications
   - Edge cases and limitations

### Multi-Audience Format
Documentation written once, tagged for multiple audiences:
- **{designer}**: GUI-focused, visual workflow emphasis
- **{developer}**: Technical JSON, API details, performance
- **{end-user}**: Data entry guidance, platform-specific instructions
- **{claude-code}**: Decision trees, validation rules, anti-patterns

### Documentation Structure Requirements
- Lead with Quick Reference providing immediate practical value
- Include working JSON examples that Claude Code can use
- Explicitly state what fields DON'T do (negative space definition)
- Provide copy-paste JSON examples
- Include mobile-specific guidance
- Reference related fields bidirectionally
- Contain troubleshooting guidance for common errors