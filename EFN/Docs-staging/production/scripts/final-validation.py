#!/usr/bin/env python3
"""
Final validation of reference.md for LLM optimization.
Checks all critical metrics and quality indicators.

Usage:
    python final-validation.py
"""

import re
import json
from pathlib import Path

def validate_reference():
    """Perform comprehensive validation of reference.md."""
    
    reference_file = Path("/home/shawn/Code/prompts/EFN/Docs-staging/production/reference.md")
    
    if not reference_file.exists():
        print("ERROR: reference.md not found!")
        return False
    
    with open(reference_file, 'r') as f:
        content = f.read()
        lines = content.split('\n')
    
    print("=" * 70)
    print("FINAL VALIDATION REPORT FOR REFERENCE.MD")
    print("=" * 70)
    
    # Size metrics
    print("\n📏 SIZE METRICS:")
    print(f"  Total lines: {len(lines):,}")
    print(f"  File size: {len(content):,} bytes ({len(content)/1024/1024:.1f} MB)")
    print(f"  Target: <30,000 lines")
    if len(lines) <= 30000:
        print("  ✅ Within target size")
    else:
        print(f"  ⚠️  Slightly over target by {len(lines)-30000} lines")
    
    # Content completeness
    print("\n📚 CONTENT COMPLETENESS:")
    sections = {
        "Field Types": "## Text & Input Fields",
        "Selection Fields": "## Selection Fields",
        "Navigation Manifest": "## LLM Navigation Manifest",
        "Glossary": "# Fieldmark Glossary",
        "Cookbook": "# Fieldmark Cookbook",
        "Troubleshooting": "# Troubleshooting Index",
        "Templates": "## Complete Notebook Templates"
    }
    
    for name, marker in sections.items():
        if marker in content:
            print(f"  ✅ {name}")
        else:
            print(f"  ❌ Missing: {name}")
    
    # Template markers
    print("\n🏷️ TEMPLATE MARKERS:")
    marker_count = content.count('{{')
    print(f"  Total markers: {marker_count:,}")
    print(f"  Target: >1000")
    if marker_count > 1000:
        print("  ✅ Parametric generation enabled")
    else:
        print("  ❌ Insufficient markers")
    
    # JSON examples
    print("\n📋 JSON EXAMPLES:")
    json_blocks = re.findall(r'```json', content)
    print(f"  Total JSON blocks: {len(json_blocks)}")
    print(f"  Average per 1000 lines: {len(json_blocks)*1000//len(lines)}")
    if len(json_blocks) > 300:
        print("  ✅ Rich with examples")
    
    # Cross-references
    print("\n🔗 CROSS-REFERENCES:")
    md_links = re.findall(r'\[([^\]]+)\]\(#([^)]+)\)', content)
    print(f"  Internal links: {len(md_links)}")
    
    broken_xrefs = content.count('XREF')
    if broken_xrefs > 0:
        print(f"  ⚠️  Potential broken refs: {broken_xrefs}")
    else:
        print("  ✅ No broken XREF markers")
    
    # Metadata quality
    print("\n🏷️ METADATA QUALITY:")
    summaries = content.count('meta:summary:')
    purposes = content.count('meta:purpose:')
    discovery = content.count('discovery:metadata')
    
    print(f"  Summary tags: {summaries}")
    print(f"  Purpose tags: {purposes}")
    print(f"  Discovery blocks: {discovery}")
    
    if summaries > 20:
        print("  ✅ Rich metadata for LLM comprehension")
    
    # Error mapping
    print("\n🔧 ERROR MAPPING:")
    error_patterns = [
        "Sorry, something went wrong",
        "Invalid notebook format",
        "Field not found",
        "Cannot read property"
    ]
    
    errors_mapped = sum(1 for pattern in error_patterns if pattern in content)
    print(f"  Common errors mapped: {errors_mapped}/{len(error_patterns)}")
    if errors_mapped == len(error_patterns):
        print("  ✅ Comprehensive error coverage")
    
    # Depth tags
    print("\n🏷️ DEPTH TAGS:")
    essential = content.count('{essential}')
    important = content.count('{important}')
    comprehensive = content.count('{comprehensive}')
    
    print(f"  Essential sections: {essential}")
    print(f"  Important sections: {important}")
    print(f"  Comprehensive sections: {comprehensive}")
    
    if essential > 0:
        print("  ✅ Depth-based filtering enabled")
    
    # LLM optimization score
    print("\n🎯 LLM OPTIMIZATION SCORE:")
    
    scores = {
        "Navigation": 100 if "LLM Navigation Manifest" in content else 0,
        "Templates": 100 if marker_count > 1000 else 50,
        "Troubleshooting": 100 if "diagnostic flowcharts" in content else 0,
        "Metadata": 100 if summaries > 20 else 50,
        "Glossary": 100 if "Fieldmark Glossary" in content else 0,
        "Examples": 100 if len(json_blocks) > 300 else 50,
        "Cross-refs": 100 if broken_xrefs == 0 else 75,
        "Size": 100 if len(lines) <= 30000 else 90
    }
    
    for metric, score in scores.items():
        status = "✅" if score >= 90 else "⚠️" if score >= 70 else "❌"
        print(f"  {status} {metric}: {score}%")
    
    overall = sum(scores.values()) // len(scores)
    print(f"\n  OVERALL SCORE: {overall}/100")
    
    if overall >= 90:
        print("  🏆 EXCELLENT - Top 1% of LLM documentation")
    elif overall >= 80:
        print("  ✅ VERY GOOD - Well optimized for LLM use")
    elif overall >= 70:
        print("  ⚠️ GOOD - Some optimization opportunities remain")
    else:
        print("  ❌ NEEDS WORK - Significant improvements needed")
    
    # Final recommendations
    print("\n💡 RECOMMENDATIONS:")
    
    if len(lines) > 30000:
        print("  - Consider removing verbose sections to get under 30K lines")
    
    if broken_xrefs > 0:
        print("  - Fix remaining XREF placeholders")
    
    if summaries < 24:
        print("  - Add more summary metadata tags")
    
    if overall >= 90:
        print("  - Document is ready for production LLM use!")
        print("  - Consider creating a 'lite' version for faster processing")
    
    print("\n" + "=" * 70)
    print("VALIDATION COMPLETE")
    print("=" * 70)
    
    return overall >= 80

if __name__ == "__main__":
    success = validate_reference()
    
    if success:
        print("\n✅ reference.md is optimized for LLM-first usage!")
    else:
        print("\n⚠️ Some optimization opportunities remain.")
    
    print("\nNext steps:")
    print("1. Test with actual notebook generation")
    print("2. Monitor LLM performance and accuracy")
    print("3. Collect feedback from usage")
    print("4. Iterate based on real-world results")