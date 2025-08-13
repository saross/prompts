CC, looking at the FAIMS3 repository, especially the codebase but also your previously generated documentation and any examples you can find, tell me everything you can about how relationships between entities / forms ('RelatedRecorSelector') works. I'm particularly interested in 'link' relationships and how 'Linking Pairs' work, including when there are multiple pairs.

```markdown
  Overview of RelatedRecordSelector

  The RelatedRecordSelector is a custom FAIMS3 component that creates relationships between records/forms. It supports two main relationship types:

  1. Child relationships (faims-core::Child) - One-to-many parent-child hierarchies
  2. Linked relationships (faims-core::Linked) - Many-to-many bidirectional links

  Key Component Parameters

  {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "related_type": "TargetFormID",        // Which form type to link to
      "relation_type": "faims-core::Linked", // Type of relationship
      "multiple": true,                      // Allow multiple links
      "relation_linked_vocabPair": [...],    // Relationship labels (key feature!)
      "related_type_label": "Display Name",  // Human-readable form name
      "allowLinkToExisting": true            // Can link existing records
    }
  }

  How Linking Pairs Work

  The relation_linked_vocabPair parameter is crucial for link relationships. It defines bidirectional relationship labels:

  For Child Relationships

  - Default: ["is child of", "is parent of"]
  - Only ONE pair allowed
  - First element: How child describes relationship to parent
  - Second element: How parent describes relationship to child

  For Linked Relationships

  - Can have MULTIPLE pairs
  - Each pair represents a different type of relationship
  - Users select which relationship type when creating the link

  Example with multiple pairs:
  "relation_linked_vocabPair": [
    ["exports to", "imports from"],
    ["supplies", "is supplied by"],
    ["is above", "is below"],
    ["is related to", "is related to"]
  ]

  How It Works Internally

  1. Data Structure:
    - Child relationships store a single parent reference
    - Linked relationships store an array of linked references
    - Each reference includes: record_id, field_id, and relation_type_vocabPair
  2. Bidirectional Updates:
    - When creating a link, BOTH records are updated
    - Record A gets link to B with first vocab term
    - Record B gets link to A with second vocab term
  3. Link Management Functions:
    - AddLink() - Adds a new link to the linked array
    - RemoveLink() - Removes a link from both records
    - Links are identified by combination of record_id and field_id

  Real-World Example

  From the Relation-Sampler notebook:
  "Factories": {
    "component-namespace": "faims-custom",
    "component-name": "RelatedRecordSelector",
    "type-returned": "faims-core::Relationship",
    "component-parameters": {
      "label": "Factories",
      "related_type": "Form",
      "relation_type": "faims-core::Linked",
      "multiple": true,
      "relation_linked_vocabPair": [
        ["exports to", "imports from"],
        ["supplies", "is supplied by"]
      ]
    }
  }

  This creates a field where:
  - Factory A can be linked to Factory B
  - User chooses relationship type (exports/supplies)
  - Factory A shows "exports to Factory B"
  - Factory B shows "imports from Factory A"

  Key Features

  1. Multiple Relationship Types: Link fields can offer multiple relationship types via vocabPair arrays
  2. Bidirectional Labels: Each relationship type has forward and reverse labels
  3. Many-to-Many: Linked relationships support multiple connections
  4. User Selection: For links with multiple pairs, users select the relationship type via dropdown
  5. Automatic Updates: Both records are updated to maintain bidirectional consistency

  UI Behavior

  - Displays a dropdown to select relationship type (if multiple pairs)
  - Shows "Add New" and "Link to Existing" buttons
  - Lists current relationships with ability to unlink
  - For single-value fields, disables after one link is made
  - Shows relationship labels in the UI (e.g., "exports to Widget-001")

  The linking pairs system provides semantic richness to relationships, allowing archaeological/research databases to express meaningful connections between records rather than just generic "is related to" links.

  ```


