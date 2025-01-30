## RMLTC0021a-CSV

**Title**: "Generation of triples referencing object map"

**Description**: "Tests the mapping specification referencing object map with same logical source and join condition"

**Error expected?** No

**Input**
```
ID,Name,Sport
10,Venus Williams,Tennis
20,Serena Williams,Tennis
30,Loena Hendrickx,Figure skating

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
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.csv"
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

