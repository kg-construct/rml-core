## RMLTC0008a-XML

**Title**: "Generation of triples to a target graph by using rr:graphMap and rr:template"

**Description**: "Test that results of the mapping can be directed to a target graph by using rr:graphMap and rr:template"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <ID>10</ID>
    <Name>Venus Williams</Name>
    <Sport>Tennis</Sport>
  </student>
</students>

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
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
    ], [
      rml:objectMap [
          rml:reference "Sport"
        ];
      rml:predicate ex:Sport
    ];
  rml:subjectMap [
      rml:graphMap [
          rml:template "http://example.com/graph/Student/{ID}/{Name}"
        ];
      rml:template "http://example.com/Student/{ID}/{Name}"
    ] .

```

**Output**
```
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.com/graph/Student/10/Venus%20Williams> .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" <http://example.com/graph/Student/10/Venus%20Williams> .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10" <http://example.com/graph/Student/10/Venus%20Williams> . 
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> "Tennis" <http://example.com/graph/Student/10/Venus%20Williams> . 


```

