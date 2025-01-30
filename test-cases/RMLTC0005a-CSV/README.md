## RMLTC0005a-CSV

**Title**: "Typing of resources"

**Description**: "Tests the typing of resources"

**Error expected?** No

**Input**
```
fname,lname,amount
Bob,Smith,30.0E0
Sue,Jones,20.0E0
Bob,Smith,30.0E0

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
          rml:path "ious.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "amount"
        ];
      rml:predicate ex:owes
    ];
  rml:subjectMap [
      rml:class foaf:Person;
      rml:template "http://example.com/{fname};{lname}"
    ] .

```

**Output**
```
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Bob;Smith> <http://example.com/owes> "30.0E0" .
<http://example.com/Sue;Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Sue;Jones> <http://example.com/owes> "20.0E0" .


```

