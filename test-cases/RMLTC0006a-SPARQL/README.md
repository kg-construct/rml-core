## RMLTC0006a-SPARQL

**Title**: "rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap"

**Description**: "Tests the use of rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap"

**Error expected?** No

**Input**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] rdf:ID "10" ;
    foaf:firstName "Venus" ;
    foaf:lastName "Williams" .


```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

ex:TriplesMap1 a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?BadStudent ?LastName ?ID
            WHERE {

            } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path <http://example.com/base#InputSPARQL>
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

<http://example.com/base#InputSPARQL> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

```

**Output**
```
<http://example.com/BadStudent> <http://example.com/description> "Bad Student" <http://example.com/graph/student> .
```

