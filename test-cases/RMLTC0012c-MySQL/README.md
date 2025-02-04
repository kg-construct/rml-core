## RMLTC0012c-MySQL

**Title**: "TriplesMap without subjectMap"

**Description**: "Tests a RML with missing information, TriplesMap without subjectMap."

**Error expected?** Yes

**Input**
```
USE test;
DROP TABLE IF EXISTS test.IOUs;
DROP TABLE IF EXISTS test.Lives;

CREATE TABLE IOUs (
      fname VARCHAR(20),
      lname VARCHAR(20),
      amount FLOAT);
INSERT INTO IOUs (fname, lname, amount) VALUES ('Bob', 'Smith', 30);
INSERT INTO IOUs (fname, lname, amount) VALUES ('Sue', 'Jones', 20);
INSERT INTO IOUs (fname, lname, amount) VALUES ('Bob', 'Smith', 30);

CREATE TABLE Lives (
      fname VARCHAR(20),
      lname VARCHAR(20),
      city VARCHAR(20));
INSERT INTO Lives (fname, lname, city) VALUES ('Bob', 'Smith', 'London');
INSERT INTO Lives (fname, lname, city) VALUES ('Sue', 'Jones', 'Madrid');
INSERT INTO Lives (fname, lname, city) VALUES ('Bob', 'Smith', 'London');

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
      rml:iterator "IOUs"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "{fname} {lname}";
          rml:termType rml:Literal
        ];
      rml:predicate foaf:name
    ], [
      rml:objectMap [
          rml:reference "amount"
        ];
      rml:predicate ex:amount
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

