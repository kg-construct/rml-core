## RMLTC0010c-SQLServer

**Title**: "Template with table columns with special chars and backslashes"

**Description**: "Tests a template with special chars in column value and backslash escapes in string templates"

**Error expected?** No

**Input**
```
USE TestDB;
DROP TABLE IF EXISTS country_info;

CREATE TABLE country_info (
  "Country Code" INTEGER,
  "Name" VARCHAR(100),
  "ISO 3166" VARCHAR(10)
);
INSERT INTO country_info values ('1', 'Bolivia, Plurinational State of', 'BO');
INSERT INTO country_info values ('2', 'Ireland', 'IE');
INSERT INTO country_info values ('3', 'Saint Martin (French part)', 'MF');

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
      rml:iterator "country_info"
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "\\{\\{\\{ {ISO 3166} \\}\\}\\}";
          rml:termType rml:Literal
        ];
      rml:predicate ex:code
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Country Code}/{Name}"
    ] .

<http://example.com/base/#DB_source> a d2rq:Database;
  d2rq:jdbcDSN "CONNECTIONDSN";
  d2rq:jdbcDriver "com.microsoft.sqlserver.jdbc.SQLServerDriver";
  d2rq:password "YourSTRONG!Passw0rd;";
  d2rq:username "sa" .

```

**Output**
```
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/code> "{{{ BO }}}" .
<http://example.com/2/Ireland> <http://example.com/code> "{{{ IE }}}" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/code> "{{{ MF }}}" .


```

