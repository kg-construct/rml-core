## RMLTC0007e-SPARQL

**Title**: "One object mapping, using rr:graphMap and rr:class"

**Description**: "Tests subjectmap with rr:graphMap and rr:class"

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
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

<http://example.com/base#Country> rml:logicalSource [
      rml:iterator """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?FirstName ?LastName ?ID
            WHERE {
                ?x  foaf:firstName ?FirstName ;
                    foaf:lastName  ?LastName ;
                    rdf:ID         ?ID .
            } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source <http://example.com/base#InputSPARQL>
    ];
  rml:subjectMap [
      rml:class foaf:Person;
      rml:graph ex:PersonGraph;
      rml:template "http://example.com/Student/{ID.value}/{FirstName.value}"
    ] .

<http://example.com/base#InputSPARQL> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

```

**Output**
```
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.com/PersonGraph> .


```

