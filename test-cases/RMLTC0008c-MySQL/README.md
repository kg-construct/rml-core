## RMLTC0008c-MySQL

**Title**: "Generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Description**: "Tests the generation of triples by using multiple predicateMaps within a rr:predicateObjectMap"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.student;

CREATE TABLE student (
  ID INTEGER,
  Name VARCHAR(50),
  Sport VARCHAR(50)
);
INSERT INTO student values ('10', 'Venus Williams', 'Tennis');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
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
      rml:predicate ex:name, foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams"  .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams"  .


```

