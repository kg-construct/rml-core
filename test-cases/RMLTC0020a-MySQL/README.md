## RMLTC0020a-MySQL

**Title**: "Generation of triples by using IRI value in columns"

**Description**: "Test the generation of triples by using IRI value in columns"

**Error expected?** No

**Input**
```
USE test;
DROP TABLE IF EXISTS test.Student_Sport;
DROP TABLE IF EXISTS test.Student;

CREATE TABLE Student (
Name VARCHAR(50)
);

INSERT INTO Student (Name) VALUES ('http://example.com/company/Alice');
INSERT INTO Student (Name) VALUES ('Bob');
INSERT INTO Student (Name) VALUES ('Bob/Charles');
INSERT INTO Student (Name) VALUES ('path/../Danny');
INSERT INTO Student (Name) VALUES ('Emily Smith');

```

**Mapping**
```
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Table;
      rml:iterator "Student"
    ];
  rml:predicateObjectMap [
      rml:object foaf:Person;
      rml:predicate rdf:type
    ];
  rml:subjectMap [
      rml:template "{Name}";
      rml:termType rml:IRI
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.mysql.cj.jdbc.Driver";
  d2rq:password "";
  d2rq:username "root" .

```

**Output**
```
<http://example.com/base/http%3A%2F%2Fexample.com%2Fcompany%2FAlice> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/Bob> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/Bob%2FCharles> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/path%2F..%2FDanny> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/Emily%20Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .

```

