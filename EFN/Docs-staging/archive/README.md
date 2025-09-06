# Archive Directory

## Purpose

This archive directory contains deprecated documentation that has been superseded by consolidated references. These files are maintained for:

1. **Disaster Recovery**: In case issues are discovered with consolidation
2. **Historical Reference**: Understanding documentation evolution
3. **Source Material**: Original content before reorganization
4. **Rollback Capability**: Quick restoration if needed

## Structure

```
archive/
├── reference-docs/         # Original technical reference documents
│   ├── accessibility-reference.md
│   ├── data-export-reference.md
│   ├── designer-limitations-reference.md
│   ├── migration-strategies-reference.md
│   ├── performance-thresholds-reference.md
│   ├── platform-behaviors-reference.md
│   ├── security-considerations-reference.md
│   ├── troubleshooting-framework-reference.md
│   └── validation-timing-reference.md
└── cross-field/            # Original cross-field pattern documents
    └── [Various archived pattern documents]
```

## Consolidation Map

The archived documents have been consolidated into four primary references:

### Phase 3A Consolidation
- **component-reference.md** ← Consolidated from:
  - component-namespace-reference.md
  - validation-timing-reference.md
  - meta-properties-reference.md
  - formik-integration-reference.md

- **platform-reference.md** ← Consolidated from:
  - platform-behaviors-reference.md
  - performance-thresholds-reference.md
  - accessibility-reference.md
  - troubleshooting-framework-reference.md (platform issues)

### Phase 3B Consolidation
- **operations-reference.md** ← Consolidated from:
  - migration-strategies-reference.md
  - data-export-reference.md
  - troubleshooting-framework-reference.md (operational issues)

- **constraints-reference.md** ← Consolidated from:
  - designer-limitations-reference.md
  - security-considerations-reference.md

## Important Notes

⚠️ **All files in this archive contain deprecation notices** pointing to their consolidated replacements.

⚠️ **Do not reference these files directly** - Use the consolidated references instead:
- `/references/component-reference.md`
- `/references/platform-reference.md`
- `/reference/operations-reference.md`
- `/reference/constraints-reference.md`

## Recovery Procedures

If you need to restore archived documentation:

1. **Identify the issue** with the consolidated version
2. **Locate the original** in this archive
3. **Remove deprecation notice** from the file header
4. **Move to appropriate directory** (reference-docs or references)
5. **Update build-reference.sh** to include the restored file
6. **Document the reason** for restoration

## Maintenance

This archive should be:
- **Preserved indefinitely** for disaster recovery
- **Not modified** except for deprecation notices
- **Not referenced** in active documentation
- **Included in backups** but excluded from builds

## Contact

For questions about archived documentation:
- Check the consolidated references first
- Review git history for consolidation commits
- Contact the documentation team if unclear

---

Last Updated: 2025-01-06
Purpose: Archive for Phase 3A/3B documentation consolidation