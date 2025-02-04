## RMLTC0002b-XML

**Title**: "Two columns mapping, generation of a BlankNode subject by using rr:template and rr:termType"

**Description**: "Tests: (1) two column mapping, no primary key; (2) generation of a BlankNode subject by using rr:template; (3) one column to one property"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<students>
  <student>
    <ID>10</ID>
    <Name>Venus</Name>
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
          rml:reference "Name"
        ];
      rml:predicate foaf:name
    ];
  rml:subjectMap [
      rml:template "students{ID}";
      rml:termType rml:BlankNode
    ] .

```

**Output**
```
_:students10 <http://xmlns.com/foaf/0.1/name> "Venus" .


```

