## RMLTC0029b-JSON

**Title**: "Generation of all named graphs when rml:defaultGraph is involved"

**Description**: "Test if the default graph is also generated correctly."

**Error expected?** No

**Input**
```
[ { "id": "0", "name": "Alice"  } ] 

```

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .
@prefix s: <http://schema.org/> .

 [
    a rml:TriplesMap;
    rml:logicalSource [
      rml:source "data.json" ;
      rml:referenceFormulation rml:JSONPath ;
      rml:iterator "$[*]";
    ];
    rml:subjectMap [
      rml:template "https://example.org/instances/{id}";
      rml:class s:Person ;
      rml:graph <graph:1> ;
    ];
    rml:predicateObjectMap [
      rml:predicate s:givenName ;
      rml:objectMap [ rml:reference "name" ] ;
      rml:graph rml:defaultGraph ;
    ];
  ] .

```

**Output**
```
<https://example.org/instances/0> <http://schema.org/givenName> "Alice".
<https://example.org/instances/0> <http://schema.org/givenName> "Alice" <graph:1> .
<https://example.org/instances/0> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> <graph:1> .

```

