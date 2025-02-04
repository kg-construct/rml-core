## RMLTC0001b-MySQL

**Title**: "One column mapping, generation of a BlankNode subject by using rr:termType"

**Description**: "Tests: (1) one column mapping; (2) generation of a BlankNode subject by using rr:termType; (3) one column to one property"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.student;
CREATE TABLE student (
  Name VARCHAR(50)
);
INSERT INTO student values ('Venus');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "SELECT Name FROM student";
      rml:referenceFormulation rml:SQL2008Query;
      rml:source <http://example.com/base/#DB_source>
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Name}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .

```

