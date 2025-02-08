# The Output Dataset

The <dfn>output dataset</dfn> of an [=RML mapping=] is an [=RDF dataset=] that contains the [=generated RDF triples=] for each of the [=triples maps=] of the [=RML mapping=]. The [=output dataset=] MUST NOT contain any other [=RDF triples=] or [=named graphs=] besides these. However, [=RML processors=] MAY provide access to datasets that contain additional triples or graphs beyond those in the [=output dataset=], such as inferred triples or provenance information.

Conforming [=RML processors=] MAY rename [=blank nodes=] when providing access to the [=output dataset=]. This means that client applications may see actual [=blank node identifiers=] that differ from those produced by the [=RML mapping=]. Client applications SHOULD NOT rely on the specific text of the blank node identifier for any purpose.

<aside class="note">
RDF syntaxes and RDF APIs generally represent [=blank nodes=] with [=blank node identifiers=]. But the characters allowed in [=blank node identifiers=] differ between syntaxes, and not all characters occurring in the values produced by a [=term map=] may be allowed, so a bijective mapping function from values to valid [=blank node identifiers=] may be required. The details of this mapping function are implementation-dependent, and [=RML processors=] may have to use different functions for different output syntaxes or access interfaces. Strings matching the regular expression `[a-zA-Z_][a-zA-Z_0-9-]*` are valid [=blank node identifiers=] in all W3C-recommended RDF syntaxes (as of this document's publication).
</aside>

<aside class="note">
[=RDF datasets=] may contain empty [=named graphs=]. RML cannot generate such [=output datasets=].
</aside>
