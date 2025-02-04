## RMLTC0007c-XML

**Title**: "One row mapping, using rr:class"

**Description**: "Tests subjectmap with more than one class IRIs, rr:class"

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
@prefix ex: <http://example.com/> .
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
          rml:reference "ID"
        ];
      rml:predicate ex:id
    ], [
      rml:objectMap [
          rml:reference "FirstName"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:class ex:Student, foaf:Person;
      rml:template "http://example.com/Student/{ID}/{FirstName}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
<http://example.com/Student/10/Venus> <http://example.com/id> "10" . 
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .


```

