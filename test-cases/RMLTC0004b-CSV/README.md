## RMLTC0004b-CSV

**Title**: "One column mapping, presence of rr:termType rr:Literal on rr:subjectMap"

**Description**: "Tests: (1) one column mapping (2) the presence of rr:termType rr:Literal on rr:subjectMap, which is invalid"

**Error expected?** Yes

**Input**
```
Name
Venus

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Name}";
      rml:termType rml:Literal
    ] .

```

