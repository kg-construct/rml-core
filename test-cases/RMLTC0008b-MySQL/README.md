## RMLTC0008b-MySQL

**Title**: "Generation of triples referencing object map"

**Description**: "Tests the mapping specification referencing object map without join"

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
@prefix activity: <http://example.com/activity/> .
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:objectMap <http://example.com/base/RefObjectMap1>;
      rml:predicate ex:Sport
    ], [
      rml:object foaf:Person;
      rml:predicate rdf:type
    ], [
      rml:objectMap [
          rml:reference "ID"
        ];
      rml:predicate ex:id
    ], [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

<http://example.com/base/RefObjectMap1> a rml:RefObjectMap;
  rml:parentTriplesMap <http://example.com/base/TriplesMap2> .

<http://example.com/base/TriplesMap2> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "student"
    ];
  rml:predicateObjectMap [
      rml:object activity:Sport;
      rml:predicate rdf:type
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Sport}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person>  .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer>  . 
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> <http://example.com/Tennis> . 
<http://example.com/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/activity/Sport> .



```

