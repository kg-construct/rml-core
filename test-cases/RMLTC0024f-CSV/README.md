## RMLTC0024f-CSV

**Title**: "Invalid IRI template 6"

**Description**: "Test handling of invalid IRI template"

**Error expected?** No

**Input**
```
N\ame
Venus

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.csv"
        ]
    ];
  rml:subjectMap [
      rml:template "http://example.com/{N\\\ame}";
      rml:class foaf:Person;
    ] .

```

**Output**
```
<http://example.com/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .


```

