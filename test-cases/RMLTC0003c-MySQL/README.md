## RMLTC0003c-MySQL

**Title**: "Three columns mapping, by using a rr:template to produce literal"

**Description**: "Tests: (1) three column mapping; and (2) the use of rr:template to produce literal"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.student;

CREATE TABLE student (
  ID INTEGER,
  FirstName VARCHAR(50),
  LastName VARCHAR(50)
);
INSERT INTO student values ('10', 'Venus', 'Williams');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
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
          rml:template "{FirstName} {LastName}";
          rml:termType rml:Literal
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student{ID}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/Student10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .

```

