## RMLTC0009b-CSV

**Title**: "Generation of triples to multiple graphs"

**Description**: "Test that results from distinct parts of the mapping can be directed to different target graphs."

**Error expected?** No

**Input**
```
ID,Sport,Name
10,100,Venus Williams
20,,Demi Moore

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
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
      rml:graph <http://example.com/graph/students>;
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ], [
      rml:graph <http://example.com/graph/practise>;
      rml:objectMap [ a rml:RefObjectMap;
          rml:joinCondition [
              rml:child "Sport";
              rml:parent "ID"
            ];
          rml:parentTriplesMap <http://example.com/base/TriplesMap2>
        ];
      rml:predicate <http://example.com/ontology/practises>
    ];
  rml:subjectMap [
      rml:class <http://example.com/ontology/Student>;
      rml:graph <http://example.com/graph/students>;
      rml:template "http://example.com/resource/student_{ID}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "sport.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:class <http://example.com/ontology/Sport>;
      rml:graph <http://example.com/graph/sports>;
      rml:template "http://example.com/resource/sport_{ID}"
    ] .

```

**Output**
```
<http://example.com/resource/student_10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Student> <http://example.com/graph/students> .
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" <http://example.com/graph/students> .
<http://example.com/resource/student_20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Student> <http://example.com/graph/students> .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore" <http://example.com/graph/students> .
<http://example.com/resource/sport_100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Sport> <http://example.com/graph/sports> .
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" <http://example.com/graph/sports> .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100> <http://example.com/graph/practise> .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100> <http://example.com/graph/students> .

```

