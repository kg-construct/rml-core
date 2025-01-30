## RMLTC0003c-CSV

**Title**: "Three columns mapping, by using a rr:template to produce literal"

**Description**: "Tests: (1) three column mapping; and (2) the use of rr:template to produce literal"

**Error expected?** No

**Input**
```
ID,FirstName,LastName
10,Venus,Williams

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
          rml:template "{FirstName} {LastName}";
          rml:termType rml:Literal
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student{ID}"
    ] .

```

**Output**
```
<http://example.com/Student10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .

```

