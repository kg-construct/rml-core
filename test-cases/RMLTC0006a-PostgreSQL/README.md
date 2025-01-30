## RMLTC0006a-PostgreSQL

**Title**: "Long form of R2RML by using rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap"

**Description**: "Tests the use of rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap"

**Error expected?** No

**Input**
```
DROP TABLE IF EXISTS student;

CREATE TABLE student (
  "ID" INTEGER,
  "FirstName" VARCHAR(50),
  "LastName" VARCHAR(50)
);
INSERT INTO student values ('10', 'Venus', 'Williams');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:constant "Bad Student"
        ];
      rml:predicateMap [
          rml:constant ex:description
        ]
    ];
  rml:subjectMap [
      rml:constant ex:BadStudent;
      rml:graphMap [
          rml:constant <http://example.com/graph/student>
        ]
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "org.postgresql.Driver";
  d2rq:password "";
  d2rq:username "postgres" .

```

**Output**
```
<http://example.com/BadStudent> <http://example.com/description> "Bad Student" <http://example.com/graph/student> .
```

