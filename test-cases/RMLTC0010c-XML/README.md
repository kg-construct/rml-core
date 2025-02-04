## RMLTC0010c-XML

**Title**: "Template with table columns with special chars and backslashes"

**Description**: "Tests a template with special chars in reference value and backslash escapes in string templates"

**Error expected?** No

**Input**
```
<?xml version="1.0"?>

<countries>
  <country>
    <CountryCode>1</CountryCode>
    <Name>Bolivia, Plurinational State of</Name>
    <ISO3166>BO</ISO3166>
  </country>
  <country>
    <CountryCode>2</CountryCode>
    <Name>Ireland</Name>
    <ISO3166>IE</ISO3166>
  </country>
  <country>
    <CountryCode>3</CountryCode>
    <Name>Saint Martin (French part)</Name>
    <ISO3166>MF</ISO3166>
  </country>
</countries>


```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/countries/country";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "country_info.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "\\{\\{\\{ {ISO3166} \\}\\}\\}";
          rml:termType rml:Literal
        ];
      rml:predicate ex:code
    ];
  rml:subjectMap [
      rml:template "http://example.com/{CountryCode}/{Name}"
    ] .

```

**Output**
```
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/code> "{{{ BO }}}" .
<http://example.com/2/Ireland> <http://example.com/code> "{{{ IE }}}" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/code> "{{{ MF }}}" .


```

