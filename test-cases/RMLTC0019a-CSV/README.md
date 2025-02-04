## RMLTC0019a-CSV

**Title**: "Generation of triples by using IRI value in columns"

**Description**: "Test the generation of triples by using IRI value in columns"

**Error expected?** No

**Input**
```
ID,FirstName,LastName
10,http://example.com/ns#Jhon,Smith
20,Carlos,Mendoza

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

**Output**
```
<http://example.com/ns#Jhon> <http://xmlns.com/foaf/0.1/name> "http://example.com/ns#Jhon" .
<http://example.com/base/Carlos> <http://xmlns.com/foaf/0.1/name> "Carlos" .

```

