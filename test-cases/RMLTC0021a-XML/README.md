## RMLTC0021a-XML

**Title**: "Generation of triples referencing object map"

**Description**: "Tests the mapping specification referencing object map with same logical source and join condition"

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
  <student>
    <ID>20</ID>
    <Name>Serena Williams</Name>
    <Sport>Tennis</Sport>
  </student>
  <student>
    <ID>30</ID>
    <Name>Loena Hendrickx</Name>
    <Sport>Figure skating</Sport>
  </student>
</students>

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/RefObjectMap1> a rml:RefObjectMap;
  rml:joinCondition [
      rml:child "Sport";
      rml:parent "Sport"
    ];
  rml:parentTriplesMap <http://example.com/base/TriplesMap1> .

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

