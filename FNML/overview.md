## Overview

Instead of integrating a specific set of functions in <a>RML</a>,
we combine <a>RML</a> with declarative function descriptions in <a>FnO</a>.

<a>FnO</a> consists of -- among others -- <a>function descriptions</a> and <a>execution</a> descriptions.
We describe these <a>executions</a> -- which link to specific <a>function descriptions</a> -- within the <a>RML mapping</a>.

A [=triples map=] "specifies the rules for translating each record" in input data into the output triples. We define [=function triples map=], a specific type of triplesMap (following the same semantics) to generate output of the function from input data. [=function triples map=] includes:
- Exactly one rml:logicalSource
- Exactly one fnml:functionTermMap to define the output of the function which is the output of the triplesMap.
- Exactly one rml:predicateObjectMap to define the execution of the function
- At least one rml:predicateObjectMap to define the input of the function
 to generate the 
 it has exactly one rml:logicalSource and one fnml:functionTermMap. 

Based on the definitions above, linking from any [=triples map=] to [=function triples map=] follows exactly the same semantic and rule as linking between any two [=triples map=] i.e. using rr:parentTriplesMap and in case of having different [=logical sources=], applying rr:joinCondition.


### Example

We use [Example 1](#example-rml-mapping-without-data-transformations),
where we want to perform an uppercase operation to a set of fields.

The FnO description of the function [toUppercase](https://github.com/OpenRefine/OpenRefine/wiki/GREL-String-Functions#touppercasestring-s) is as follows:

```turtle "example": "toUppercase FnO description"
grel:toUppercase a fno:Function ;
    fno:name "upper case" ;
    dcterms:description "return the input string in upper case" ;
    fno:expects ( [ fno:predicate grel:stringInput ] ) ;
    fno:output ( [ fno:predicate grel:stringOutput ] ) .
```

The execution of such function would be described as follows:

```turtle "example": "toUppercase FnO execution description"
:exe a fno:Execution ;
    fno:executes grel:toUppercase ;
    grel:stringInput "This is an input STRING." ;
    grel:stringOutput "THIS IS AN INPUT STRING." .
```

To connect this function with the RML mapping document, we make use of a `fnml:FunctionMap`

```turtle "example": "using toUppercase in an RML mapping"
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;              # Specify the data source
    rr:subjectMap <#SubjectMap> ;                     # Specify the subject
    rr:predicateObjectMap <#NameMapping> .            # Specify the predicate-object-map

<#NameMapping>
    rr:predicate dbo:title ;                          # Specify the predicate
    rr:objectMap [ rr:parentTriplesMap <#FunctionTriplesMap> ].                                                # Specify the object-map

<#FunctionTermMap>
    fnml:outputValue grel:stringOutput.               # grel:stringOutput

<#FunctionTriplesMap a fnml:FunctionTriplesMap ;      # Generating the execution triples

    rml:logicalSource <#LogicalSource> ;              # Specify the data source

    fnml:outputValue <#FunctionTermMap>;              # Specify the output of the triplesMap

    rr:predicateObjectMap [
        rr:predicate fno:executes ;                   # Execute the function&hellip;
        rr:objectMap [ rr:constant grel:toUppercase ] # grel:toUppercase
    ] ;
    rr:predicateObjectMap [
        rr:predicate grel:inputString ;
        rr:objectMap [ rr:reference "name" ]          # Use as input the "name" reference
    ] .
```

The `name`-value is not referenced directly,
instead, its value is used as `grel:inputString`-parameter
for the `grel:toUppercase`-function.

