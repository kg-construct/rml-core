## RMLTC0010b-CSV

**Title**: "Template with table columns with special chars"

**Description**: "Tests a template with special chars in column value"

**Error expected?** No

**Input**
```
Country Code,Name,ISO 3166
1,"Bolivia, Plurinational State of",BO
2,Ireland,IE
3,"Saint Martin (French part)",MF

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:referenceFormulation rml:CSV;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_info.csv"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:reference "Name"
        ];
      rml:predicate ex:name
    ];
  rml:subjectMap [
      rml:template "http://example.com/{Country Code}/{Name}"
    ] .

```

**Output**
```
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2/Ireland> <http://example.com/name> "Ireland" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/name> "Saint Martin (French part)" .


```

