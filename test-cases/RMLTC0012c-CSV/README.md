## RMLTC0012c-CSV

**Title**: "TriplesMap without subjectMap"

**Description**: "Tests a RML with missing information, TriplesMap without subjectMap."

**Error expected?** Yes

**Input**
```
fname,lname,amount
Bob,Smith,30
Sue,Jones,20
Bob,Smith,30

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "persons.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "{fname} {lname}";
          rml:termType rml:Literal
        ];
      rml:predicate foaf:name
    ], [
      rml:objectMap [
          rml:reference "amount"
        ];
      rml:predicate ex:amount
    ] .

```

