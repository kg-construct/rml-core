## RMLTC0008c-CSV

**Title**: "Generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Description**: "Tests the generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Error expected?** No

**Input**
```
ID,Name,Sport
10,Venus Williams,Tennis

```

**Mapping**
```
@prefix ex: <http://example.com/> .
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
      rml:predicate ex:name, foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams"  .


```

