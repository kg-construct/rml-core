## RMLTC0033a-JSON

**Title**: "Generation of triples from a join of a logical source with itself"

**Description**: "Test that, in a join of a logical source with itself, each iteration is joined with every iteration that has the same value, not only with itself"

**Default Base IRI**: http://example.com/

**Error expected?** No

**Input**
```
[
  {"trip": "T1", "stop": "S1"},
  {"trip": "T1", "stop": "S2"},
  {"trip": "T2", "stop": "S3"}
]

```

**Mapping**
```
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:JSONPath;
      rml:iterator "$[*]";
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "data.json"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [ a rml:RefObjectMap;
          rml:joinCondition [
              rml:child "$.trip";
              rml:parent "$.trip"
            ];
          rml:parentTriplesMap <http://example.com/base/TriplesMap1>
        ];
      rml:predicate <http://example.com/ontology/sameTripAs>
    ];
  rml:subjectMap [
      rml:template "http://example.com/resource/stop_{$.stop}"
    ] .

```

**Output**
```
<http://example.com/resource/stop_S1> <http://example.com/ontology/sameTripAs> <http://example.com/resource/stop_S1> .
<http://example.com/resource/stop_S1> <http://example.com/ontology/sameTripAs> <http://example.com/resource/stop_S2> .
<http://example.com/resource/stop_S2> <http://example.com/ontology/sameTripAs> <http://example.com/resource/stop_S1> .
<http://example.com/resource/stop_S2> <http://example.com/ontology/sameTripAs> <http://example.com/resource/stop_S2> .
<http://example.com/resource/stop_S3> <http://example.com/ontology/sameTripAs> <http://example.com/resource/stop_S3> .

```

