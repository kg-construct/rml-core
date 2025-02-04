## RMLTC0001a-SPARQL

**Title**: "One tripple mapping, subject URI generation by using rr:template"

**Description**: "Tests: (1) one tripple mapping; (2) generation of a BlankNode subject by using rr:termType; (3) one tripple to one property"

**Error expected?** No

**Input**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

[] foaf:name "Venus" .


```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix formats: <http://www.w3.org/ns/formats/> .
@prefix rml: <http://w3id.org/rml/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .

<http://example.com/base#Country> rml:logicalSource [
      rml:iterator """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            SELECT ?name
            WHERE {
                ?x foaf:name ?name .
            } """;
      rml:referenceFormulation formats:SPARQL_Results_JSON;
      rml:source <http://example.com/base#InputSPARQL>
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "name.value"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{name.value}"
    ] .

<http://example.com/base#InputSPARQL> a sd:Service;
  sd:endpoint <http://HOST:PORT/ds1/sparql>;
  sd:supportedLanguage sd:SPARQL11Query .

```

**Output**
```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .

```

