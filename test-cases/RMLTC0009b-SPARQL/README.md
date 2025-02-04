## RMLTC0009b-SPARQL

**Title**: "Generation of triples to multiple graphs"

**Description**: "Test that results from distinct parts of the mapping can be directed to different target graphs."

**Error expected?** No

**Input**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://example.com/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] ns1:plays [ a ns1:Sport ;
            rdf:ID "100" ] ;
    rdf:ID "10" ;
    foaf:name "Venus Williams" .

[] ns1:plays [ a ns1:Sport ] ;
    rdf:ID "20" ;
    foaf:name "Demi Moore" .


```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator """
              PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
              PREFIX foaf: <http://xmlns.com/foaf/0.1/>
              PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
              SELECT ?Name ?ID ?Sport
              WHERE {
                  ?x  foaf:name ?Name ;
                      rdf:ID    ?ID ;
                      <http://example.com/plays> ?sportObject .
                  OPTIONAL { ?sportObject a <http://example.com/Sport> ;
                                            rdf:ID ?Sport . }
              } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path <http://example.com/base/#InputSPARQL1>
        ]
    ];
  rml:predicateObjectMap [
      rml:graph <http://example.com/graph/students>;
      rml:objectMap [
          rml:reference "Name.value"
        ];
      rml:predicate foaf:name
    ], [
      rml:graph <http://example.com/graph/practise>;
      rml:objectMap [ a rml:RefObjectMap;
          rml:joinCondition [
              rml:child "Sport.value";
              rml:parent "ID.value"
            ];
          rml:parentTriplesMap <http://example.com/base/TriplesMap2>
        ];
      rml:predicate <http://example.com/ontology/practises>
    ];
  rml:subjectMap [
      rml:class <http://example.com/ontology/Student>;
      rml:graph <http://example.com/graph/students>;
      rml:template "http://example.com/resource/student_{ID.value}"
    ] .

<http://example.com/base/#InputSPARQL1> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

<http://example.com/base/#InputSPARQL2> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds2/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator """
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT ?ID ?Name
                WHERE {
                    ?x  foaf:name ?Name ;
                        rdf:ID    ?ID ;
                } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path <http://example.com/base/#InputSPARQL2>
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name.value"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:class <http://example.com/ontology/Sport>;
      rml:graph <http://example.com/graph/sports>;
      rml:template "http://example.com/resource/sport_{ID.value}"
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

