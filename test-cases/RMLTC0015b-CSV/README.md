## RMLTC0015b-CSV

**Title**: "Generation of language tags from a table with language information, and a term map with invalid rr:language value"

**Description**: "Tests a term map with an invalid rr:language value, which is an error"

**Error expected?** Yes

**Input**
```
Code,Name
BO,"Bolivia, Plurinational State of"
IE,Ireland

```

**Mapping**
```
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_en.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "a-english";
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Code}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_es.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:language "a-spanish";
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Code}"
    ] .

```

