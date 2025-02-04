## RMLTC0011b-CSV

**Title**: "M to M relation, by using an additional Triples Map"

**Description**: "Tests, M to M relations, by using an additional Triples Map"

**Error expected?** No

**Input**
```
ID,FirstName,LastName
10,Venus,Williams
11,Fernando,Alonso
12,David,Villa

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/LinkMap_1_2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student_sport.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "http://example.com/sport/{ID_Sport}"
        ];
      rml:predicate ex:plays
    ];
  rml:subjectMap [
      rml:template "http://example.com/student/{ID_Student}"
    ] .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "FirstName"
        ];
      rml:predicate ex:firstName
    ], [
      rml:objectMap [
          rml:reference "LastName"
        ];
      rml:predicate ex:lastName
    ];
  rml:subjectMap [
      rml:template "http://example.com/student/{ID}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "sport.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Description"
        ];
      rml:predicate ex:description
    ], [
      rml:objectMap [
          rml:reference "ID"
        ];
      rml:predicate ex:id
    ];
  rml:subjectMap [
      rml:template "http://example.com/sport/{ID}"
    ] .

```

**Output**
```
<http://example.com/student/10> <http://example.com/lastName> "Williams" .
<http://example.com/student/10> <http://example.com/firstName> "Venus" .
<http://example.com/student/12> <http://example.com/lastName> "Villa" .
<http://example.com/student/12> <http://example.com/firstName> "David" .
<http://example.com/student/11> <http://example.com/lastName> "Alonso" .
<http://example.com/student/11> <http://example.com/firstName> "Fernando" .
<http://example.com/sport/110> <http://example.com/description> "Tennis" .
<http://example.com/sport/110> <http://example.com/id> "110" .
<http://example.com/sport/111> <http://example.com/description> "Football" .
<http://example.com/sport/111> <http://example.com/id> "111" .
<http://example.com/sport/112> <http://example.com/description> "Formula1" .
<http://example.com/sport/112> <http://example.com/id> "112" .
<http://example.com/student/10> <http://example.com/plays> <http://example.com/sport/110> .
<http://example.com/student/12> <http://example.com/plays> <http://example.com/sport/111> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/112> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/111> .


```

