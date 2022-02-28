## Overview

Instead of integrating a specific set of functions in [=RML=],
we combine [=RML=] with declarative function descriptions in [=FnO=].

<a>FnO</a> consists of -- among others -- <a>function descriptions</a> and <a>execution</a> descriptions.
We describe these <a>executions</a> -- which link to specific <a>function descriptions</a> -- within the <a>RML mapping</a>.

A [=triples map=] is a rule that maps each iteration in the logical source to a number of RDF triples.
An [=RML mapping=] uses [=triples map=]s to generate output triples from input data.
We use an intermediate [=FnML execution=] to refer to an FnO [=execution=] from input data,
and then use an [=execution term map=] to link some specific output of an [=execution=] to the actual [=triples map=],
so that input data is transformed via an [=FnML execution=] and then integrated in the output using an [=execution term map=].

The <a>RML processor</a> thus needs to interpret these [=execution=] triples correctly to know which input data values to assign to the parameters of the function.
After executing the correct function, the <a>RML processor</a> SHOULD link the resulting value(s) to the right [=triples map=]s.

<figure>
<pre class="mermaid nohighlight override">
graph LR
    A([triples map]) -->|subject map| B([execution term map]):::fnml
    A([triples map]) -->|predicateobject map| C([predicateobject map])
    C -->|predicate map| B
    C -->|object map| B
    B -->|execution| D([FnML execution]):::fnml
    D -->|function| F([function]):::fno
    D -->|inputParameters| G([parameter term map]):::fnml
    B -->|output| E([output predicate]):::fno
    G -->|predicate| H([parameter predicate]):::fno
    classDef fnml fill:#8F9
    classDef fno fill:#F89
</pre>
<figcaption>FNML construction, in relation to RML</figcaption>
</figure>

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

To connect this function with the RML mapping document, we make use of a `fnml:Execution`

```turtle "example": "using toUppercase in an RML mapping"
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;       # Specify the data source
    rr:subjectMap <#SubjectMap> ;              # Specify the subject
    rr:predicateObjectMap <#NameMapping> .     # Specify the predicate-object-map

<#NameMapping>
    rr:predicate dbo:title ;                   # Specify the predicate
    rr:objectMap <#ExecutionTermMap> .         # Specify the object-map

<#ExecutionTermMap> a fnml:ExecutionTermMap ;  # A Term Map: the link between RML and an FnO Execution
    fnml:execution <#Execution> ;              # Link to the execution
    fnml:output grel:stringOutput .            # Specify which output of the execution is taken

<#Execution> a fnml:Execution ;                # A new class, unrelated to existing RML constructs
    fnml:function grel:toUppercase ;           # Specify which FnO function
    fnml:inputParameters                       # Specify the input parameters
        [
            fnml:predicate grel:stringInput ;  # Specify this specific parameter
            rr:reference "name" .              # Specify the value using existing Term Map constructions
        ] .
```

The `name`-value is not referenced directly,
instead, its value is used as `grel:inputString`-parameter
for the `grel:toUppercase`-function.
After execution, the `grel:stringOutput` result of that function is returned to generate the object
within the `<#NameMapping>`.
We make use of an intermediate `<#ExecutionTermMap>` so that we can reuse the output of an execution in multiple TermMaps.
