## RMLTC0008c-SPARQL

**Title**: "Generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Description**: "Tests the generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Error expected?** No

**Input**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://example.com/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] ns1:plays [ a ns1:Sport ;
            foaf:name "Tennis" ] ;
    rdf:ID "10" ;
    foaf:name "Venus Williams" .


```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator """
              PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
              PREFIX foaf: <http://xmlns.com/foaf/0.1/>
              PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
              SELECT ?Name ?ID
              WHERE {
                  ?x  foaf:name ?Name ;
                      rdf:ID    ?ID ;
              } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path <http://example.com/base/#InputSPARQL>
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name.value"
        ];
      rml:predicate ex:name, foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID.value}/{Name.value}"
    ] .

<http://example.com/base/#InputSPARQL> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams"  .


```

