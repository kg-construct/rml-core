## RMLTC0007e-CSV

**Title**: "One column mapping, using rr:graphMap and rr:class"

**Description**: "Tests subjectmap with rr:graphMap and rr:class"

**Error expected?** No

**Input**
```
ID,Name
10,Venus

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
          rml:reference "ID"
        ];
      rml:predicate ex:id
    ], [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:class foaf:Person;
      rml:graph ex:PersonGraph;
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus> <http://example.com/id> "10" <http://example.com/PersonGraph> .
<http://example.com/Student/10/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" <http://example.com/PersonGraph> .
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.com/PersonGraph> .


```

