## RMLTC0021a-SPARQL

**Title**: "Generation of triples referencing object map"

**Description**: "Tests the mapping specification referencing object map with same logical source and join condition"

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

[] ns1:plays [ a ns1:Sport ;
            foaf:name "Tennis" ] ;
    rdf:ID "20" ;
    foaf:name "Serena Williams" .

[] ns1:plays [ a ns1:Sport ;
            foaf:name "Figure skating" ] ;
    rdf:ID "30" ;
    foaf:name "Loena Hendrickx" .


```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

ex:RefObjectMap1 a rml:RefObjectMap;
  rml:joinCondition [
      rml:child "Sport.value";
      rml:parent "Sport.value"
    ];
  rml:parentTriplesMap ex:TriplesMap1 .

ex:TriplesMap1 a rml:TriplesMap;
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
          rml:path <http://example.com/base#InputSPARQL>
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap ex:RefObjectMap1;
      rml:predicate ex:sameSportAs
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID.value}/{Name.value}"
    ] .

<http://example.com/base#InputSPARQL> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/10/Venus%20Williams> . 
<http://example.com/Student/10/Venus%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/20/Serena%20Williams> . 
<http://example.com/Student/20/Serena%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/20/Serena%20Williams> . 
<http://example.com/Student/20/Serena%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/10/Venus%20Williams> . 
<http://example.com/Student/30/Loena%20Hendrickx> <http://example.com/sameSportAs> <http://example.com/Student/30/Loena%20Hendrickx> . 



```

