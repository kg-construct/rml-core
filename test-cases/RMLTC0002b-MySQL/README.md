## RMLTC0002b-MySQL

**Title**: "Two columns mapping, generation of a BlankNode subject by using rr:template and rr:termType"

**Description**: "Tests: (1) two column mapping, no primary key; (2) generation of a BlankNode subject by using rr:template; (3) one column to one property"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.student;
CREATE TABLE student (
  ID INTEGER,
  Name VARCHAR(50)
);
INSERT INTO student values ('10', 'Venus');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:referenceFormulation rml:SQL2008Table;
      rml:source <http://example.com/base/#DB_source>;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "students{ID}";
      rml:termType rml:BlankNode
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
_:students10 <http://xmlns.com/foaf/0.1/name> "Venus" .


```

