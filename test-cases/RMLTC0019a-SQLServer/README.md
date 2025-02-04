## RMLTC0019a-SQLServer

**Title**: "Generation of triples by using IRI value in columns"

**Description**: "Test the generation of triples by using IRI value in columns"

**Error expected?** No

**Input**
```
USE TestDB;
DROP TABLE IF EXISTS Employee;

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
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator """
        SELECT ID, FirstName, LastName
        FROM Employee
        WHERE ID < 30
     """;
      rml:source <http://example.com/base/#DB_source>;
      rml:referenceFormulation rml:SQL2008Query
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
  d2rq:jdbcDriver "com.microsoft.sqlserver.jdbc.SQLServerDriver";
  d2rq:password "YourSTRONG!Passw0rd;";
  d2rq:username "sa" .

```

**Output**
```
<http://example.com/ns#Jhon> <http://xmlns.com/foaf/0.1/name> "http://example.com/ns#Jhon" .
<http://example.com/base/Carlos> <http://xmlns.com/foaf/0.1/name> "Carlos" .

```

