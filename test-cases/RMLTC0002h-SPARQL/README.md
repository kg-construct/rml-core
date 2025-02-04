## RMLTC0002h-SPARQL

**Title**: "Two tripples mapping, duplicate variable name in SELECT"

**Description**: "Tests the presence of duplicate variable names in the SELECT list of the SPARQL query"

**Error expected?** Yes

**Input**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] rdf:ID "10" ;
    foaf:name "Venus" .


```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

<http://example.com/base#Country> rml:logicalSource [
      rml:iterator """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?Name ?Name
            WHERE {
                ?x foaf:name ?Name ;
            } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source <http://example.com/base#InputSPARQL>
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "IDs"
        ];
      rml:predicate ex:id
    ];
  rml:subjectMap [
      rml:template "http://example.com/{ID.value}/{Name.value}"
    ] .

<http://example.com/base#InputSPARQL> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

```

