## RMLTC0007g-CSV

**Title**: "Assigning triples to the default graph"

**Description**: "Tests the generation of triples to the default graph"

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
          rml:reference "FirstName"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:graph rml:defaultGraph;
      rml:template "http://example.com/Student/{ID}/{FirstName}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .


```

