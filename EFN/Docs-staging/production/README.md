# Fieldmark v3 Production Documentation

## Quick Start

### For LLM/Claude Code Usage
```bash
# Use the concatenated reference for complete context
cat reference.md
```

### For Human Navigation
Start with [field-type-index.md](field-type-index.md) - the master navigation index.

### To Rebuild Reference
```bash
./scripts/build-reference.sh
```

## What's Here

This is the authoritative documentation for Fieldmark v3's field system, optimized for both LLM consumption and human reference.

### 📁 `/field-categories/` - Field Type Documentation
8 comprehensive guides covering all 23 field components:
- **Text fields** - TextField, TemplatedString, QRCode, etc.
- **Selection fields** - Select, RadioGroup, AdvancedSelect, etc.
- **DateTime fields** - DatePicker, DateTimeNow, DateTimePicker
- **Number fields** - NumberInput, BasicAutoIncrementer
- **Display field** - RichText for instructions
- **Location fields** - TakePoint, MapFormField
- **Media fields** - FileUploader, TakePhoto
- **Relationship field** - RelatedRecordSelector

### 📁 `/patterns/` - Cross-Field Patterns
4 guides showing how fields work together:
- **field-selection-guide.md** - Choosing the right field types
- **form-structure-guide.md** - Form architecture and navigation
- **dynamic-forms-guide.md** - Validation and conditional logic
- **implementation-patterns-guide.md** - Common patterns and troubleshooting

### 📁 `/references/` - Technical References
4 consolidated technical guides:
- **component-reference.md** - Namespaces, types, Formik integration
- **platform-reference.md** - Platform behaviors, performance, accessibility
- **operations-reference.md** - Migration, export, troubleshooting
- **constraints-reference.md** - Designer limitations, security considerations

### 📄 Key Files
- **field-type-index.md** - Master navigation with categorized links
- **reference.md** - 24,400-line concatenated reference for LLM consumption
- **MANIFEST.md** - Complete inventory of all documentation

## Documentation Features

### LLM Optimization
- **Depth tags**: `{essential}`, `{important}`, `{comprehensive}` for filtering
- **Clean JSON**: All examples are executable (no inline comments)
- **Concatenated reference**: Single file for complete context loading
- **Consistent structure**: Every document follows the same template

### Human Navigation
- **Master index**: Start from field-type-index.md
- **Cross-references**: Bidirectional links between related topics
- **Component mapping**: Designer UI names → JSON names → Code files
- **Quick diagnosis tables**: Problem → Cause → Solution format

### Security & Best Practices
- **Contextualized risks**: Security concerns with nuanced explanations
- **Privacy vs security**: Clear distinction for research features
- **Platform behaviors**: Device-specific considerations
- **Performance boundaries**: Documented limits and thresholds

## Key Improvements from Original

### Before (78 files)
- Scattered across 7 directories
- Significant duplication
- Inconsistent formatting
- Difficult navigation
- Non-executable JSON examples

### After (17 docs)
- Clear three-tier architecture
- No duplication
- Standardized format
- Easy navigation
- Clean, executable JSON

## Using This Documentation

### For Development
1. Check field-type-index.md for navigation
2. Read relevant field category doc
3. Review patterns for workflows
4. Consult references for technical details

### For LLM/Claude Code
1. Load reference.md for complete context
2. Use depth tags to filter content
3. All JSON examples are copy-paste ready
4. Security considerations are contextualized

### For Troubleshooting
1. Start with Quick Diagnosis tables
2. Check platform-specific behaviors
3. Review constraints for Designer limitations
4. Consult operations reference for solutions

## Maintenance Status

### ✅ Complete
- All structural consolidation
- Navigation infrastructure
- Security standardization
- JSON cleanup for LLM use
- Technical validation

### 🔄 Ongoing
- Monthly Designer limitation reviews
- Security advisory updates
- Performance threshold adjustments

### 📝 Planned Enhancements
- 60-80 production JSON examples
- Expanded platform behaviors
- Enhanced troubleshooting sections

## Build Information

- **Source**: 78 original documentation files
- **Consolidated**: Into 17 production documents
- **Reference size**: 868KB (~24,400 lines)
- **Last updated**: 2025-01-06
- **Version**: v05

## Related Resources

- **Archive**: `/archive/` contains all source documentation
- **Housekeeping**: `housekeeping-tasks.md` tracks remaining work
- **GitHub**: Full version history available

## Contributing

When updating documentation:
1. Edit the appropriate file in `/field-categories/`, `/patterns/`, or `/references/`
2. Run `./scripts/build-reference.sh` to regenerate reference.md
3. Update MANIFEST.md if adding new files
4. Commit with clear message describing changes

## License & Attribution

Documentation for Fieldmark v3 (formerly FAIMS3)  
Maintained by the Fieldmark development team