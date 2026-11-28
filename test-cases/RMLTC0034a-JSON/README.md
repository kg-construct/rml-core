## RMLTC0034a-JSON

**Title**: "Generation of IRIs from values with non-ASCII characters"

**Description**: "Test that the IRI-safe version of a value in a template keeps non-ASCII characters and percent-encodes reserved characters"

**Default Base IRI**: http://example.com/

**Error expected?** No

**Input**
```
[
  {"name": "Zoë"},
  {"name": "Périgord"},
  {"name": "São Paulo"},
  {"name": "Ærøskøbing"},
  {"name": "東京"},
  {"name": "Line:42/A"}
]

```

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:JSONPath;
      rml:iterator "$[*]";
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "data.json"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "$.name"
        ];
      rml:predicate <http://example.com/ontology/name>
    ];
  rml:subjectMap [
      rml:template "http://example.com/place/{$.name}"
    ] .

```

**Output**
```
<http://example.com/place/Zoë> <http://example.com/ontology/name> "Zoë" .
<http://example.com/place/Périgord> <http://example.com/ontology/name> "Périgord" .
<http://example.com/place/São%20Paulo> <http://example.com/ontology/name> "São Paulo" .
<http://example.com/place/Ærøskøbing> <http://example.com/ontology/name> "Ærøskøbing" .
<http://example.com/place/東京> <http://example.com/ontology/name> "東京" .
<http://example.com/place/Line%3A42%2FA> <http://example.com/ontology/name> "Line:42/A" .

```

