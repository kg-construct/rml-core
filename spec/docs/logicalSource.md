# Defining Iterables and Logical Sources

An <dfn>iterable</dfn> is an abstract construct to describe data access and iteration for a [=data source=].

An [=iterable=] (`rml:Iterable`) MUST have:
* zero or one `rml:referenceFormulation` property, whose value is a <dfn>reference formulation</dfn> which defines how to reference parts of the underlying [=data source=], and which [=expressions=] can be evaluated on [=logical iterations=]. If no `rml:referenceFormulation` is provided, it MUST be inferred as defined for the specific type of [=Iterable=].
* zero or one `rml:iterator` property, whose value is a <dfn data-lt="iterator">logical iterator</dfn> that defines a sequence of [=logical iterations=] on the [=data source=]. If no [=iterator=] is provided, a <dfn class="lint-ignore">default iterator</dfn> MUST be associated with the [=reference formulation=].

A <dfn data-lt="iteration">logical iteration</dfn> is an item in the sequence produced by the [=iterable=], on which [=expressions=] can be evaluated.

A <dfn>data source</dfn> is an abstract concept that represents a source of data that can be accessed via a [=iterable=]. A [=data source=] can be a file, a database, a web service, or any other source of data, depending on the type of [=iterable=].

<aside class="note">
There can be many different types of [=reference formulation=]. The known types, and the details of how a reference formulation is handled and implemented for each data format, are specified in [[RML-IO-Registry]].
</aside>

An <dfn data-lt="logical source">abstract logical source</dfn> (`rml:AbstractLogicalSource`) is a sub-class of [=iterable=] that can be associated with a [=triples map=] such that a [=data source=] can be mapped to [=RDF triples=].
