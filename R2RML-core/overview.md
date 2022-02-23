# [R2]RML Overview and Example (Informative)


Each [logical source]() is mapped to RDF using a [triples map]().
The [triples map]() is a rule that maps each iteration in the [logical source]()
to a number of RDF triples.
The rule has two main parts:


 1. A [subject map]() that generates the subject of all [RDF triples]()
 that will be generated from a logical source iteration.
 The subjects often are [IRIs]().
 2. Multiple [predicate-object maps]() that
 in turn consist of [predicate maps]() and [object maps]()
 (or [referencing object maps]()).
 
By default, all [RDF triples]() are in the [default graph]() of the [output dataset]().
A [triples map]() can contain [graph maps]() that
place some or all of the triples into [named graphs]() instead. 

**TODO: Add updated figure here**

## 2.1 Example Input

## 2.2 Desired RDF Output

## 2.3 - 2.7 Examples

# 3. Conformance

# 4. RML Mapping Documents

### RML Mapping

An [RML mapping]() defines a mapping from a data source to RDF.
It is a structure that consists of one or more [triples maps]().

The input to an RML mapping is called the [input data source]().

## 4.1 Mapping Graphs and the RML Vocabulary

An [RML mapping]() is represented as an [RDF graph]().
In other words, RDF is used not just as the target data model of the mapping,
but also as a formalism for representing the [RML mapping]() itself.

An [RDF graph]() that represents an [RML mapping]() is called an **_RML mapping graph_**.

The **_RML vocabulary_** is the set of IRIs defined in this specification
that start with the rr: namespace IRI: +++TODO:ADD IRI+++

An [RML mapping graph]():

1. SHOULD NOT include any [IRIs]() that start with the `rml:` namespace [IRI](),
but are not defined in the RML vocabulary.
2. SHOULD NOT include [IRIs]() from the [RML vocabulary]()
where such use is not explicitly allowed or required by a clause in this specification.
3. SHOULD contain only [mapping components]()
that are referenced by some triples map
(in other words, all mapping components should actually be “used” in the mapping).
4. MAY contain arbitrary additional [triples]() whose terms are not from the [RML vocabulary]().
In particular, a valid mapping graph MAY contain documentation
in the form of `rdfs:label`, `rdfs:comment` and similar properties.
5. MAY assign [IRIs]() or [blank node identifiers]() to any [mapping component]()
in order to enable reuse of [mapping components]() within the [mapping graph]().
For example, an [IRI]() that represents a [subject map]()
may be used as the [subject map]() of multiple [triples maps]();
and may even be used as an object map of another [triples map]()
if it has the right properties.

The [RML vocabulary]() also includes the following [RML classes]():

* `rml:TriplesMap` is the class of [triples maps]().
* `rml:LogicalSource` is the class of [logical sources](). 
* `rml:TermMap` is the class of [term maps](). It has four subclasses:
    * `rml:SubjectMap` is the class of [subject maps]().
    * `rml:PredicateMap` is the class of [predicate maps]().
    * `rml:ObjectMap` is the class of [object maps]().
    * `rml:GraphMap` is the class of [graph maps]().
* `rml:PredicateObjectMap` is the class of [predicate-object maps]().
* `rml:RefObjectMap` is the class of [referencing object maps]().
* `rml:Join` is the class of [join conditions]().

The members of these classes are collectively called [mapping components]().

**NOTE**
Many of these classes differ only in capitalization from properties in the [RML vocabulary]().

Explicit typing of the resources in a mapping graph with [RML classes]() is OPTIONAL
and has no effect on the behaviour of an [RML processor]().
The [mapping component]() represented by any given resource in a mapping graph
is defined by the presence or absence of certain properties,
as defined throughout this specification.
A resource SHOULD NOT be typed as an RML class
if it does not meet the definition of that class.

The [default mapping]() SHOULD be such that
its output is the [Direct Graph]() [[DM]()] corresponding to the [input data source]().


## 4.2 RDF-based Turtle Syntax; Media Type

An **_RML mapping document_** is any document written in the [Turtle]() [[TURTLE]]() RDF syntax
that encodes an [RML mapping graph]().

The media type for [RML mapping documents]() is the same as for Turtle documents in general:
`text/turtle`.
The content encoding of Turtle content is always UTF-8
and the charset parameter on the media type SHOULD always be used:
`text/turtle;charset=utf-8`. The file extension `.ttl` SHOULD be used.

A conforming [RML processor]() SHOULD accept [RML mapping documents]() in Turtle syntax.
It MAY accept [RML mapping graphs]() encoded in other RDF syntaxes.

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









