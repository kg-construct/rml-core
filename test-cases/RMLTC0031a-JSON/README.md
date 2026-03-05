## RMLTC0031a-JSON

**Title**: "Generating of triples with langaugeMap with custom language"

**Description**: "Test triples with a custom language from the data"

**Default Base IRI**: http://example.com/

**Error expected?** No

**Input**
```
[
  { "FOO": 1, "BAR": "string"},
  { "FOO": 2, "BAR": "integer"}
]
```

**Mapping**
```
@prefix ex: <http://example.com/> .
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
          rml:languageMap [
              rml:constant "en"
            ];
          rml:reference "$.FOO"
        ];
      rml:predicate ex:x
    ];
  rml:subjectMap [
      rml:template "http://example.com/{$.FOO}"
    ] .
```

**Output**
```
<http://example.com/1> <http://example.com/x> "string"@en .
<http://example.com/2> <http://example.com/x> "integer"@en .
```