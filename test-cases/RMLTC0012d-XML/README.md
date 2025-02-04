## RMLTC0012d-XML

**Title**: "TriplesMap with two subjectMap"

**Description**: "Tests a RML with wrong information, TriplesMap with two subjectMap."

**Error expected?** Yes

**Input**
```
<?xml version="1.0"?>

<Persons>
  <Person>
    <fname>Bob</fname>
    <lname>Smith</lname>
    <amount>30</amount>
  </Person>
  <Person>
    <fname>Sue</fname>
    <lname>Jones</lname>
    <amount>20</amount>
  </Person>
  <Person>
    <fname>Bob</fname>
    <lname>Smith</lname>
    <amount>30</amount>
  </Person>
</Persons>

```

**Mapping**
```
@prefix ex: <http://example.com/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rml: <http://w3id.org/rml/> .

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:logicalSource [ a rml:LogicalSource;
      rml:iterator "/Persons/Person";
      rml:referenceFormulation rml:XPath;
      rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "persons.xml"
        ]
    ];
  rml:predicateObjectMap [
      rml:objectMap [
          rml:template "{fname} {lname}";
          rml:termType rml:Literal
        ];
      rml:predicate foaf:name
    ], [
      rml:objectMap [
          rml:reference "amount"
        ];
      rml:predicate ex:amount
    ];
  rml:subjectMap [
      rml:template "{fname}_{lname}_{amount}";
      rml:termType rml:BlankNode
    ], [
      rml:template "{amount}_{fname}_{lname}";
      rml:termType rml:BlankNode
    ] .

```

