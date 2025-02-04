## RMLTC0009a-MySQL

**Title**: "Generation of triples from foreign key relations"

**Description**: "Test foreign key relationships among logical tables"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.student;

CREATE TABLE student (
  ID INTEGER,
  Sport VARCHAR(50),
  Name VARCHAR(50)
);
INSERT INTO student values ('10', '100', 'Venus Williams');
INSERT INTO student values ('20', NULL , 'Demi Moore');

DROP TABLE IF EXISTS test.sport;

CREATE TABLE sport (
  ID INTEGER,
  Name VARCHAR(50)
);
INSERT INTO sport values ('100', 'Tennis');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
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
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "sport"
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

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore"  .
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100>  .

```

