# Defining Logical Iterables and Logical Sources

A <dfn>logical iterable</dfn> is an abstract construct to describe data access and iteration for a [=data source=].

A [=logical iterable=] (`rml:LogicalIterable`) MUST have:
* exactly one `rml:referenceFormulation` property, whose value is a <dfn>reference formulation</dfn> which defines how the underlying [=data source=] is to be accessed, and which [=expressions=] can be evaluated on [=logical iterations=],
* zero or one `rml:iterator` property, whose value is a <dfn data-lt="iterator">logical iterator</dfn> that defines a sequence of [=logical iterations=] on the [=data source=]. If no [=iterator=] is provided, a <dfn class="lint-ignore">default iterator</dfn> MUST be associated with the [=reference formulation=].

A <dfn data-lt="iteration">logical iteration</dfn> is an item in the sequence produced by the [=logical iterable=], on which [=expressions=] can be evaluated.

A <dfn>data source</dfn> is an abstract concept that represents a source of data that can be accessed via a [=logical iterable=]. A [=data source=] can be a file, a database, a web service, or any other source of data, depending on the type of [=logical iterable=].

<aside class="note">
There can be many different types of [=reference formulation=]. The known types, and the details of how a reference formulation is handled and implemented for each data format, are specified in [[RML-IO-Registry]].
</aside>

A <dfn>logical source</dfn> (`rml:LogicalSource`) is a sub class of [=logical iterable=] that can be associated with a [=triples map=] such that a [=data source=] can be mapped to [=RDF triples=].
