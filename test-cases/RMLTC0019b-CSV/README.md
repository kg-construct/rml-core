## RMLTC0019b-CSV

**Title**: "Generation of triples by using IRI value in columns, with data error"

**Description**: "Test the generation of triples by using IRI value in columns, conforming RML mapping with data error (and limited results)"

**Error expected?** Yes

**Input**
```
ID,FirstName,LastName
10,http://example.com/ns#Jhon,Smith
20,Carlos,Mendoza
30,Juan Daniel,Crespo

```

**Mapping**
```
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
          rml:reference "FirstName"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:reference "FirstName"
    ] .

```

