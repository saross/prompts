Hi CC, I need help migrating field notebook definitions from FAIMS2.x to FAIMS3.x format.

## Context
- FAIMS2.x: Legacy system using XML, beanshell, and text files
- FAIMS3.x (Fieldmark): Modern system using single JSON files
- Expected feature parity: ~85%
- Known limitations: 
  - Geospatial features significantly reduced in 3.x
  - Custom coding capabilities reduced in 3.x

## Resources
- `/faims-android/` - FAIMS2.x source code
- `/UserToDev/` - FAIMS2.x notebook (module) creation documentation
- `/FAIMS2-modules/` - Example 2.x modules (one per subfolder with definition files and documentation)
- `/FAIMS3/Notebooks/Documentation/` - FAIMS3.x JSON specifications

## Overview of Migration Process
For each FAIMS2.x module, you will:
1. Analyse the module's structure, features, and documentation
2. Create a functionally equivalent FAIMS3.x JSON notebook
3. Generate user documentation for the new notebook
4. Document the migration process and any limitations

## Migration Guidelines
- **Feature gaps**: Implement the closest simplified version, documenting what was lost
- **Geospatial features**: Use only capabilities available in FAIMS3.x (basic points/polygons)
- **Custom code**: Convert to FAIMS3.x patterns where possible, document if functionality is lost
- **Field relationships**: Preserve all data relationships and validation rules
- **Metadata**: Maintain all field names, descriptions, and hierarchies

## Output Structure
For each migrated module, create three files in `/FAIMS3/Notebooks/JSON-definition-files-migrations/`:

1. **`[module-name]-faims3.json`** - The converted notebook definition
2. **`[module-name]-documentation.md`** - User documentation that:
   - Describes the notebook's purpose and workflow (adapted from original)
   - Explains how to use each section/field
   - Notes any behavioural changes from the original
3. **`[module-name]-migration-report.md`** - Technical migration details:
   - Conversion decisions and rationale
   - Features successfully migrated (with mapping table)
   - Features simplified (with explanation)
   - Features omitted (with justification)
   - Any assumptions or interpretations made

## Process
I will guide you through this migration one module at a time, with each module typically requiring 2-3 steps:
1. Analysis and planning
2. Implementation and documentation
3. Review and refinement (if needed)

Please confirm you understand this overview then pause. We'll begin with the first module shortly and take it step by step.