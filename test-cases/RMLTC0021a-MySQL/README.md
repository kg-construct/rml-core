## RMLTC0021a-MySQL

**Title**: "Generation of triples referencing object map"

**Description**: "Tests the mapping specification referencing object map with same logical source and join condition"

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
INSERT INTO student values ('20', 'Serena Williams', 'Tennis');
INSERT INTO student values ('30', 'Loena Hendrickx', 'Figure skating');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

<http://example.com/base/RefObjectMap1> a rml:RefObjectMap;
  rml:joinCondition [
      rml:child "Sport";
      rml:parent "Sport"
    ];
  rml:parentTriplesMap <http://example.com/base/TriplesMap1> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:objectMap <http://example.com/base/RefObjectMap1>;
      rml:predicate ex:sameSportAs
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/10/Venus%20Williams> . 
<http://example.com/Student/10/Venus%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/20/Serena%20Williams> . 
<http://example.com/Student/20/Serena%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/20/Serena%20Williams> . 
<http://example.com/Student/20/Serena%20Williams> <http://example.com/sameSportAs> <http://example.com/Student/10/Venus%20Williams> . 
<http://example.com/Student/30/Loena%20Hendrickx> <http://example.com/sameSportAs> <http://example.com/Student/30/Loena%20Hendrickx> . 



```

