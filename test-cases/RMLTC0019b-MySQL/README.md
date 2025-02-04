## RMLTC0019b-MySQL

**Title**: "Generation of triples by using IRI value in columns, with data error"

**Description**: "Test the generation of triples by using IRI value in columns, conforming RML mapping with data error (and limited results)"

**Error expected?** Yes

**Input**
```
USE test;
DROP TABLE IF EXISTS test.Employee;

CREATE TABLE Employee (
ID INTEGER,
FirstName VARCHAR(50),
LastName VARCHAR(50)
);
INSERT INTO Employee (ID,FirstName,LastName) VALUES (10,'http://example.com/ns#Jhon','Smith');
INSERT INTO Employee (ID,FirstName,LastName) VALUES (20,'Carlos','Mendoza');
INSERT INTO Employee (ID,FirstName,LastName) VALUES (30,'Juan Daniel','Crespo');

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
      rml:iterator "Employee"
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

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

