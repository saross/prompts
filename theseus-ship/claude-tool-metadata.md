# Archaeological Research Software Tools Metadata Collection

## Research Approach
- **Accuracy & Evidence**: Base all claims on supporting evidence. Extrapolate from evidence, but do not speculate or guess; indicate uncertainty clearly. Prioritize if sources are in conflict: official documentation → peer-reviewed publications → community consensus.
- **Thoroughness**: Examine at least 20 search results, official documentation, source repositories, and scholarly literature. Research until you reach information saturation.
- **Recency Focus**: Metadata should reflect the most recent software version as of today's date.
- **Missing Information**: For unavailable data: leave URL fields empty, use controlled vocabulary only when reasonably certain, and clearly indicate limitations in assessments. 
- **Methodical approach**: Double-check your work even if that requires more time. Follow a systematic research process and document findings carefully.
- **Research Depth**: Prioritize exhaustive investigation over efficiency. Seek multiple confirming sources for each claim. Research primary (repositories, documentation), secondary (academic literature), and tertiary sources (community discussions) until reaching true information saturation. Actively search for contradictory evidence. Identify potential archaeological applications not explicitly documented. No upper limit on research time—thoroughness is paramount.
- **Field Length Guidance**: Target 200-250 words for descriptive/interpretive fields (Description, Technical-discussion, History, Strengths, Weaknesses, Survivability). Prioritize information quality over length constraints. For abundant information, emphasize significance; for sparse information, document what exists. Technical-discussion may extend to 300-350 words for complex tools. Ensure comprehensive coverage of all evaluation criteria regardless of length requirements.

## Version Clarity
- **Explicit Version Identification**: Always specify which version is being described (use version names/numbers) in all fields.
- **Current Version Priority**: Begin descriptions with current version capabilities before discussing previous versions.
- **Consistent Signposting**: Use clear markers ("current version," "previous versions") throughout all evaluative fields.
- **Comparative Context**: Where relevant, note how current versions improve upon or address limitations of earlier iterations.

## Tool disambiguation
When encountering tools with ambiguous names that could refer to multiple software systems, always prioritize the software most relevant to archaeological/historical research. If multiple archaeological or historical applications share the same name, or other ambiguity remains, focus on the one with the most substantial documentation and usage, then briefly note the potential alternatives in the Description field.

## Content Guidelines
- **Description vs. Technical**: Description explains what it does in non-technical terms; Technical-discussion explains how it works (architecture, dependencies, requirements, data models, UI/UX, deployment, performance, scalability, limitations, APIs, etc.)
- **Timeline Research**: Prioritize repository tags, release notes, and changelogs. Fall back to official statements or community discussions. Use "Abandoned" only if repository is inactive >2 years without explanation.
- **Usage Metrics**: Capture GitHub metrics (stars, forks, contributors), citations, community activity (Stack Overflow; community sites), extensions, publications, and documented institutional adoption (use specific numbers and examples when availalbe). Indicate changes over time and distinguish between major versions where possible.

## CSV Output Format
- Present complete findings as a markdown fenced code block with quoted CSV with the following columns:
"Tool", "Description", "History", "Technical-discussion", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "License", "Tags", "AI-tags", "First-release-date", "Last-update-date", "Current-version", "Development-status", "Institutional-backing", "Authors", "Development-team-size", "Original-discipline", "Original-purpose", "Documentation-quality", "Usage-indicators", "Lifecycle-stage", "Type", "Category", "Language", "Platform", "Open-Archaeo-Platform",  "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives".
- Include header row and a single properly escaped data row.
- Format multiple values with pipe (|) separators and ensure no newlines or citations within fields.
- For quoted text within fields, use single quotes ('example') rather than escaped double quotes (""example"" or \"example\").
- Before submitting your  CSV, verify that the number of columns in your data row exactly matches the number in the header row (count them). Confirm that all fields are accounted for, even if empty (shown as "")

## Column Specifications

### Essential Information
- **Tool**: Exact name as provided.
- **Description**: overview of purpose and functionality, focusing on what it does. If the tool was oringinally developed for another discipline, discuss that, but also look for and present any archaeological/historical uses. Focus on the current version; when describing historical versions, explicitly note them as previous or earlier versions.
- **History**: Chronological development account including major versions and updates.
- **Technical-discussion**: Detailed technical implementation examination. Begin with the current version's technical implementation, followed by relevant information about previous versions with explicit version identification.
- **Access-date**: Today's date (YYYY-MM-DD).
- **Tool-status**: "yes"/"maybe"/"no" based on evaluation framework. 
- **Tool-status-reasoning**: Detailed classification explanation referencing specific criteria. If "maybe", then describe uncertainties or borderline aspects.
- **DVCS-repo/CRAN/PyPi**: Relevant repository URLs.
- **Other-URL**: Primary homepage or documentation
- **License**: Current verified license
- **Tags**: Categorization tags from controlled list below.
- **AI-tags**: Five tags you generate to characterise the tool.

### Development and Organization
- **First-release/Last-update-date**: Initial release and most recent update dates, (use repositories, release notes, change logs, etc.).
- **Current-version**: Most recent version identifier.
- **Development-status**: From controlled list: "Active"/"Maintenance-only"/"Deprecated"/"Abandoned"/"Unknown".
- **Institutional-backing**: Formal supporting organizations.
- **Authors**: Major contributors to the software.
- **Development-team-size**: Categorised size of team: "Solo"/"Small (2-5)"/"Medium (6-20)"/"Large (20+)".
- **Original-discipline**: Academic field of origin.
- **Original-purpose**: From controlled list: "Project-specific"/"General-purpose"/"Unknown"
- **Documentation-quality**: From controlled list: "Minimal"/"Basic"/"Comprehensive"/"Excellent"
- **Usage-indicators**: Usage metrics paragraph. 

### Technical and Assessment 
- **Lifecycle-stage**: Supported research stages from controlled list
- **Type**: "mass-market"/"research-specific"
- **Category**: From controlled list: "Packages and libraries"/"Stand-alone software"/"Scripts".
- **Language**: Programming language(s) of current version.
- **Platform**: Operating systems/environments supported by current version.
- **Open-Archaeo-Platform**: Must be completed if and only if "Category" is "Packages and libraries", otherwise leave empty. When used, select value from the controlled list below. For tools that extend existing platforms (e.g., ArcGIS, QGIS, etc.), this field should reflect the parent software.
- **Interoperability**: Data formats and exchange capabilities. When differences exist, specify which version(s) each observation applies to.
- **Strengths/Weaknesses**: Evidence-based assessment of advantages and opportunities enabled versus limitations, challenges, or potential risks. Include consideration of transparency and reproducibility (source availability, algorithm transparency, documentation completeness, version control, test data, etc.). Whenever possible, specify which version(s) each capability or limitation applies to.
- **Survivability**: Long-term viability assessment.
- **Alternatives**: Similar tools comparison.

## Research Software Tool Evaluation

### Core Definition & Essential Criteria
Research software supports scholarly inquiry through data collection, processing, analysis, visualization, or dissemination. Tools qualify regardless of origin discipline if they meet ALL:
1. **Research-Specific Purpose**: Supports research activities
2. **Research Data Engagement**: Transforms research materials meaningfully
3. **Methodological Alignment**: Compatible with recognized methodologies

### Supporting Criteria (Must Meet ≥2)
1. **Domain Knowledge Integration**: Incorporates relevant terminology/classifications/procedures
2. **Research Lifecycle Support**: Addresses one or more research stages
3. **Data Transformation**: Converts between formats or representations; assists data preparation and cleaning
4. **Analytical Capabilities**: Performs calculations/comparisons/pattern recognition
5. **Visualization Functions**: Renders data in meaningful visual formats
6. **Documentation Focus**: Documentaiton addresses research applications
7. **Data Collection**: Supports gathering data in field or laboratory settings
8. **Data Dissemination**: Supports sharing/publication/reuse of research data (beyond simple storage)

### Classification Process
1. Identify primary functions and use cases
2. Verify all Essential Criteria
3. Count satisfied Supporting Criteria (need ≥2)
4. Determine classification: "Yes"/"Maybe"/"No"

### Classification Examples
- "Yes" example: A tool that implements statistical analysis methods originally developed for ecology but applicable to archaeological data, or software for spatial analysis initially created for geography but useful for archaeological site mapping.
- "Maybe" example: A general database system that requires substantial customization before being useful for research.
- "No" example: A basic spreadsheet program with no research-specific features.

## Controlled Vocabulary Lists
### Category Controlled List
- **Packages and libraries**: Sets of functions assembled with clear purpose, and made accessible using standards established by an underlying platform. Templates, plugins, and extensions for existing platforms should be classifed as 'Packages and libraries'.
- **Stand-alone software**: Software that may be operated without needing to first access an underlying platform.
- **Scripts**: Sets of pragmatically assembled mutable functions, often lacking complete documentation or adherence to protocols that would otherwise facilitate secondary use outside their original contexts of creation.

### Open-Archaeo-Platform Controlled List
ArcGIS
AutoCAD
JavaScript
LibreOffice Calc
Lisp
Meshlab
Microsoft Excel
Nextflow
Open Data Kit
Piwigo
Python
QGIS
R
Stellarium

### Lifecycle-stage Controlled List
Planning
Data Acquisition
Processing
Analysis
Interpretation
Publication
Preservation and Reuse

### Tags Controlled List
Statistical analysis
Spatial analysis
Viewshed analysis
Site mapping
Harrix matrix
Chronological modelling
Seriation
Zooarchaeology
Palaeobotany
Artefact morphology
Literary analysis and epigraphy
Iconography
Shape recognition
3D modelling
Photogrammetry
Virtual reality
Augmented reality
Drones
Aerial and satellite imagery
Luminescence dating
X-Ray Fluorescence
Instrumental Neutron activation analysis
Radiocarbon dating, calibration and sequencing
Geophysical survey
Data management
Data collection
Lithic analysis
API interfaces and web scrapers
Datasets
Diagrams and visualizations
Platforms and publications
Schemas and ontologies
Templates
Drivers and IO
Educational resources and practical guides
Public archaeology
Public policy and civic action
Games
Writing
Lists
LiDAR
Museums
Bibliography
Archaeogenetics
Bits and bobs
Biological anthropology
Archaeoastronomy
Dendrochronology
Photography
Cultural evolution
Ethics and professional development
Simulation
Stable isotope analysis
Network analysis
Geoarchaeology
Machine learning
Palaeoclimate modelling
Ceramic analysis
