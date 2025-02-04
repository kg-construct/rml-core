## RMLTC0006a-CSV

**Title**: "Long form of R2RML by using rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap"

**Description**: "Tests the use of rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap"

**Error expected?** No

**Input**
```
ID,FirstName,LastName
10,Venus,Williams

```

**Mapping**
```
@prefix ex: <http://example.com/> .
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
          rml:constant "Bad Student"
        ];
      rml:predicateMap [
          rml:constant ex:description
        ]
    ];
  rml:subjectMap [
      rml:constant ex:BadStudent;
      rml:graphMap [
          rml:constant <http://example.com/graph/student>
        ]
    ] .

```

**Output**
```
<http://example.com/BadStudent> <http://example.com/description> "Bad Student" <http://example.com/graph/student> .
```

