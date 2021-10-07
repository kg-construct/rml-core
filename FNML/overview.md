## Overview

Instead of integrating a specific set of functions in <a>RML</a>,
we combine <a>RML</a> with declarative function descriptions in <a>FnO</a>.

<a>FnO</a> consists of -- among others -- <a>function descriptions</a> and <a>execution</a> descriptions.
We describe these <a>executions</a> -- which link to specific <a>function descriptions</a> -- within the <a>RML mapping</a>.

A [=triples map=] generates triples from input data.
An [=RML mapping=] uses [=output triples map=]s to generate output triples from input data.
We use an intermediate [=function triples map=] to generate [=execution triples=] from input data,
and then use a [=function term map=] to link the output of those execution triples to the actual [=output triples map=],
so that input data is transformed via a [=function triples map=] and then integrated in the output using a [=function term map=].

The <a>RML processor</a> thus needs to interpret these [=execution=] triples correctly to know which input data values to assign to the parameters of the function.
After executing the correct function, the <a>RML processor</a> SHOULD link the resulting value(s) to the right [=output triples map=]s.

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
    rr:objectMap <#FunctionTermMap> .                 # Specify the object-map

<#FunctionTermMap>
    fnml:functionValue <#FunctionTriplesMap> .        # The object is taken from the output of the execution triples of the function

<#FunctionTriplesMap a fnml:FunctionTriplesMap ;      # Generating the execution triples
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
The execution result triples of that function are then referred to have the object
within the `<#NameMapping>`.
