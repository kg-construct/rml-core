# 5. RML Processors, Validators and Generators


### RML Processor

An RML processor is a system that, given an RML mapping and an input data source,
provides access to the output dataset.

There are no constraints on the method of access to the output dataset
provided by a conforming [RML processor]().
An [RML processor]() MAY materialize the output dataset into a file,
or offer virtual access through an interface,
or offer any other means of providing access to the output dataset.

An [RML processor]() also has access to an execution environment consisting of:
* A [Logical Source]()
* a base IRI used in resolving relative IRIs produced by the RML mapping.

How the [Logical Source]() is accessed,
or how users are authenticated against the database,
is outside of the scope of this document.

The [base IRI]() MUST be a valid [IRI]().
It SHOULD NOT contain question mark (“?”) or hash (“#”) characters and
SHOULD end in a slash (“/”) character.

**NOTE**
To obtain an absolute IRI from a relative IRI,
the [term generation rules]() of RML use simple string concatenation,
rather than the more complex algorithm for resolution of relative URIs
defined in [Section 5.2]() of [RFC3986]().
This ensures that the original database value can be reconstructed from the generated absolute IRI.
Both algorithms are equivalent if all of the following are true:


1. The base IRI does not contain question marks or hashes,
2. the base IRI ends in a slash,
3. the relative IRI does not start with a slash, and
4. the relative IRI does not contain any “.” or “..” path segments.

### RML Validator

An RML data validator is a system that takes as its input
an [RML mapping](), a [base IRI](), and a [SQL connection]() to an [input database](),
and checks for the presence of [data errors]().
When checking the input database,
a data validator MUST report any data errors
that are raised in the process of generating the output dataset.

An [RML processor]() MAY include an [RML data validator](), but this is not required.


### Generators

An [RML processor]() MAY include an **_RML default mapping generator_**.
This is a facility that introspects the schema of the [input data source]()
and generates an [RML mapping](), 
possibly in the form of an [RML mapping document](),
intended for further customization by a mapping author.
Such a mapping is known as a _**default mapping**_.



## 5.1 Data Errors

A **_data error_** is a condition of the data in the [input data]()
that would lead to the generation of an invalid [RDF term]().
The following conditions give rise to data errors:


1. A [term map]() with term type `rr:IRI` results in the generation of an invalid [IRI]().
2. A [term map]() whose natural RDF datatype is overridden with a specified datatype
produces an [ill-typed literal]() (see [datatype-override RDF literal]()).

When providing access to the output dataset,
an [RML processor]() MUST abort any operation
that requires inspecting or returning an [RDF term]()
whose generation would give rise to a data error,
and report an error to the agent invoking the operation.
A conforming [RML processor]() MAY, however,
allow other operations that do not require inspecting or returning these [RDF terms](),
and thus MAY provide partial access to an output dataset that contains data errors.
Nevertheless, an [RML processor]() SHOULD report data errors as early as possible.

The presence of data errors does not make an [RML mapping]() non-conforming.

**NOTES**
Data errors cannot generally be detected by analyzing the schema of the input data,
but only by scanning the data in the data source.
For large and rapidly changing databases, this can be impractical.
Therefore, [RML processors] are allowed to answer queries
that do not “touch” a data error,
and the behavior of such operations is well-defined. For the same reason,
the conformance of [RML mappings]() is defined without regard for the presence of data errors.

[RML data validators]() can be used to explicitly scan a database for data errors.









