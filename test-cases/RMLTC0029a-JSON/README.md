## RMLTC0029a-JSON

**Title**: "Generation of the right datatype for a constant in the mapping"

**Description**: "Test the honoring of the datatype specified by the constant term in the mapping"

**Error expected?** No

**Input**
```
[ { "id": "0", "foo": "bar"  } ] 

```

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .

 [
    a rml:TriplesMap;
    rml:logicalSource [
      rml:source "data.json" ;
      rml:referenceFormulation rml:JSONPath ;
      rml:iterator "$[*]";
    ];
    rml:subjectMap [
      rml:template "https://example.org/instances/{id}";
    ];
    rml:predicateObjectMap [
      rml:predicate <http://example.org/ns/p> ;
      rml:object true ; # datatype is boolean
    ];
  ] .

```

**Output**
```
<https://example.org/instances/0> <http://example.org/ns/p> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .

```

