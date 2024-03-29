# Joins

A <dfn>Referencing Object Map</dfn> (`rml:ReferencingObjectMap`) allows
using the subject generated by the [Subject Map]() (`rml:SubjectMap`)
of the referenced [Triples Map]() (`rml:TriplesMap`).
Since the two triples maps (`rml:TriplesMap`) may be based on
different logical sources (`rml:LogicalSource`),
this may require a join between the logical sources (`rml:LogicalSource`).
This is not restricted to 1:1 joins.

## Referencing Object Map

A [Referencing Object Map] (`rml:ReferencingObjectMap`) is represented by a resource that:

* has exactly one [Parent Triples Map]() (`rml:parentTriplesMap`) property,
  whose value MUST be a Triples Map (`rml:TriplesMap`).
* MAY have one or more [Join Conditions]()  (`rml:joinCondition`) properties.

The [Referencing Object Map]() (`rml:ReferencingObjectMap`)
is constructed with the subject of the [Parent Triples Map]() (`rml:parentTriplesMap`).

```
<#TM1> 
    rml:logicalSource <LS1> ;
    rml:subjectMap <#SM1> ;
    rml:predicateObjectMap [
        rml:predicateMap <#PM1> ;
        rml:objectMap [ rml:parentTriplesMap <#TM2> ] ]. 

<#TM2> 
    rml:logicalSource <LS2> ;
    rml:subjectMap <#SM2> ;
    rml:predicateObjectMap [
        rml:predicateMap <#PM2> ;
        rml:objectMap <#OM2> ] .
```

## Join Condition

A [Join Condition]() is represented by a resource that
has exactly one value for each of the following two properties:

* a [child map]() (`rml:childMap`),
  whose value is an [Expression Map]() (`rml:ExpressionMap`), which
  MUST include references that exists in the [Logical Source]()
  of the [Parent Triples Map]() that contains the [Referencing Object Map]()
  or it should have a constant value.

* a [parent map]() (`rml:parentMap`),
  whose value is an [Expression Map]() (`rml:ExpressionMap`), which,
  as the join condition's parent map,
  MUST include references that exists in the [Logical Source]()
  of the [Referencing Object Map]()'s [Parent Triples Map]()
  or it should have a constant value.

```
<#TM1> 
    rml:logicalSource <LS1> ;
    rml:subjectMap <#SM1> ;
    rml:predicateObjectMap [
        rml:predicateMap <#PM1> ;
        rml:objectMap [ 
            rml:parentTriplesMap <#TM2> ;
            rml:joinCondition [
                rml:childMap [ rml:reference "..."];
                rml:parentMap [ rml:template "..."]; 
            ] ] ]. 

<#TM2> 
    rml:logicalSource <LS2> ;
    rml:subjectMap <#SM2> .
```

### Shortcuts

If the [Child Map]() (`rml:ChildMap`) is a reference-valued [Expression Map]() (`rml:ExpressionMap`),
then the `rml:child` shortcut could be used.

Similarly, if the [Parent Map]() (`rml:ParentMap`) is a reference-valued [Expression Map]() (`rml:ExpressionMap`),
then the `rml:child` shortcut could be used.

```
<#TM1> 
    rml:logicalSource <LS1> ;
    rml:subjectMap <#SM1> ;
    rml:predicateObjectMap [
        rml:predicateMap <#PM1> ;
        rml:objectMap [ 
            rml:parentTriplesMap <#TM2> ;
            rml:joinCondition [
                rml:child "..." ;
                rml:parent "..."]; 
            ] ] ]. 

<#TM2> 
    rml:logicalSource <LS2> ;
    rml:subjectMap <#SM2> .
```
