# Project Standards

## Spelling and Localisation

- Always use UK/Australian English spelling (colour, behaviour, organisation, centre, analyse, optimise, etc.)
- Apply UK/Australian spelling to all documentation, code comments, and file names
- Convert US spellings to UK/Australian equivalents when editing existing files

## Documentation System Architecture

### CRITICAL: Never Edit Concatenated Files Directly

- `production/reference.md` is a CONCATENATED file built from source files
- **NEVER update reference.md directly** - always update the source files
- Source files are located in `production/` subdirectories:
  - `production/dashboard/` - Dashboard interface documentation
  - `production/field-categories/` - Field type documentation
  - `production/references/` - Cross-cutting references and patterns
  - `production/patterns/` - UI and workflow patterns
  - `production/human-facing/` - User-facing guides
- After updating source files, rebuild reference.md using the build script
- **Violation of this rule corrupts the entire documentation system**

## Markdown Standards

- All markdown files must pass markdownlint validation
- Before committing markdown files, check for linting issues using the IDE diagnostics
- Common rules to follow:
  - MD022: Blank lines around headings
  - MD031: Blank lines around fenced code blocks
  - MD032: Blank lines around lists
  - MD040: Language specifiers for code blocks (use ```text for plain text)
- Fix all linting warnings before committing

## Git Commit Messages

- Use UK/Australian spelling in commit messages
- Include descriptive brief and detailed commit messages with context
- Always include the Claude Code co-authorship footer
