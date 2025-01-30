## RMLTC0009a-XML

**Title**: "Generation of triples from foreign key relations"

**Description**: "Test foreign key relationships among logical tables"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <ID>10</ID>
    <Name>Venus Williams</Name>
    <Sport>100</Sport>
  </student>
  <student>
    <ID>20</ID>
    <Name>Demi Moore</Name>
  </student>
</students>

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/students/student";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ], [
      rml:objectMap [ a rml:RefObjectMap;
          rml:joinCondition [
              rml:child "Sport";
              rml:parent "ID"
            ];
          rml:parentTriplesMap <http://example.com/base/TriplesMap2>
        ];
      rml:predicate <http://example.com/ontology/practises>
    ];
  rml:subjectMap [
      rml:template "http://example.com/resource/student_{ID}"
    ] .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/sports/sport";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "sport.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate rdfs:label
    ];
  rml:subjectMap [
      rml:template "http://example.com/resource/sport_{ID}"
    ] .

```

**Output**
```
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore"  .
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100>  .

```

