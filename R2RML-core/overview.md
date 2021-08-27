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

# 4. [R2]RML Processors, Validators and Mapping Documents

### RML Mapping

An [RML mapping]() defines a mapping from a data source to RDF.
It is a structure that consists of one or more [triples maps]().

The input to an RML mapping is called the [input data source]().

### RML Processor

An RML processor is a system that, given an R2RML mapping and an input database,
provides access to the output dataset.

There are no constraints on the method of access to the output dataset provided by a conforming R2RML processor.
An R2RML processor MAY materialize the output dataset into a file,
or offer virtual access through an interface that queries the input database,
or offer any other means of providing access to the output dataset.

An [RML processor]() also has access to an execution environment consisting of:
* A [Logical Source]()
* a base IRI used in resolving relative IRIs produced by the R2RML mapping.

How the [Logical Source]() is accessed,
or how users are authenticated against the database,
is outside of the scope of this document.

The [base IRI]() MUST be a valid [IRI]().
It SHOULD NOT contain question mark (“?”) or hash (“#”) characters and
SHOULD end in a slash (“/”) character.

**NOTE**
To obtain an absolute IRI from a relative IRI,
the [term generation rules]() of R2RML use simple string concatenation,
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

## 4.1 Mapping Graphs and the RML Vocabulary

An [RML mapping]() is represented as an [RDF graph]().
In other words, RDF is used not just as the target data model of the mapping,
but also as a formalism for representing the R2RML mapping itself.

An [RDF graph]() that represents an [RML mapping]() is called an **_RML mapping graph_**.

The **_RML vocabulary_** is the set of IRIs defined in this specification
that start with the rr: namespace IRI: +++TODO:ADD IRI+++

An R2RML mapping graph:

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
A resource SHOULD NOT be typed as an R2RML class
if it does not meet the definition of that class.


## 


















