## RMLTC0003c-XML

**Title**: "Three columns mapping, by using a rr:template to produce literal"

**Description**: "Tests: (1) three column mapping; and (2) the use of rr:template to produce literal"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <ID>10</ID>
    <FirstName>Venus</FirstName>
    <LastName>Williams</LastName>
  </student>
</students>

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/students/student";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "{FirstName} {LastName}";
          rml:termType rml:Literal
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/Student{ID}"
    ] .

```

**Output**
```
<http://example.com/Student10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .

```

