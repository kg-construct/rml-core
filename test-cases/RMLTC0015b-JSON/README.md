## RMLTC0015b-JSON

**Title**: "Generation of language tags from a table with language information, and a term map with invalid rml:language value"

**Description**: "Tests a term map with an invalid rml:language value, which is an error"

**Error expected?** Yes

**Input**
```
{
  "countries": [
    {"Code": "BO", "Name": "Estado Plurinacional de Bolivia"},
    {"Code": "IE", "Name": "Irlanda"}
  ]
}

```

**Mapping**
```
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "$.countries[*]";
      rml:referenceFormulation rml:JSONPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_en.json"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "a-english";
          rml:reference "$.Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{$.Code}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "$.countries[*]";
      rml:referenceFormulation rml:JSONPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_en.json"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "a-spanish";
          rml:reference "$.Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{$.Code}"
    ] .

```

