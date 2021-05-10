## Overview

Instead of integrating a specific set of functions in <a>RML</a>,
we combine <a>RML</a> with declarative function descriptions in <a>FnO</a>.

<a>FnO</a> consists of -- among others -- <a>function descriptions</a> and <a>execution</a> descriptions.
We describe these <a>executions</a> -- which link to specific <a>function descriptions</a> -- within the <a>RML mapping</a>.

The <a>RML processor</a> then needs to interpret these <a>executions</a> correctly to know which values to assign to the parameters of the function.
After executing the correct function, the <a>RML processor</a> SHOULD return the resulting value, to be used for further processing by the <a>RML processor</a>.

### Example

We use [Example 1](#example-1-rml-mapping-without-data-transformations),
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
    rml:logicalSource <#LogicalSource> ;                  # Specify the data source
    rr:subjectMap <#SubjectMap> ;                         # Specify the subject
    rr:predicateObjectMap <#NameMapping> .                # Specify the predicate-object-map

<#NameMapping>
    rr:predicate dbo:title ;                              # Specify the predicate
    rr:objectMap <#FunctionTermMap> .                         # Specify the object-map

<#FunctionTermMap>
    fnml:functionValue [                                  # The object is the result of the function
        a fnml:FunctionTriplesMap ;
        rr:predicateObjectMap [
            rr:predicate fno:executes ;                   # Execute the function&hellip;
            rr:objectMap [ rr:constant grel:toUppercase ] # grel:toUppercase
        ] ;
        rr:predicateObjectMap [
            rr:predicate grel:inputString ;
            rr:objectMap [ rr:reference "name" ]          # Use as input the "name" reference
        ]
    ] .
```

Before the `name`-value is referenced,
the value is first used as `grel:inputString`-parameter
for the `grel:toUppercase`-function.
The output of that function is then used as object
within the `<#NameMapping>`
