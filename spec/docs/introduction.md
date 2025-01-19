# Base IRIs
The base IRI of the [=mapping document=] is used to resolve relative [=IRIs=] in the RML document following the specification of the Turtle serialisaiton.

## Base IRI for mapping rules

The [=base IRI=] of the [=Triples Map=] is used in resolving relative [=IRIs=] produced by the [=RML mapping=].


<pre class="ex-mapping nohighlight">
# Triples Map that has a declared base IRI
<#TriplesMap>
    a rml:TriplesMap;
    rml:baseIri <http://example.com/> .
</pre>

The [=base IRI=] MUST be a valid [=IRI=]. It SHOULD NOT contain question mark ("`?`") or hash ("`#`") characters and SHOULD end in a slash ("`/`") character.

To obtain an absolute [=IRI=] from a relative [=IRI=], the term generation rules of RML use simple string concatenation, rather than the more complex algorithm for resolution of relative URIs defined in Section 5.2 of [RFC3986]. This ensures that the original database value can be reconstructed from the generated absolute [=IRI=]. Both algorithms are equivalent if all of the following are true:

    1. The base IRI does not contain question marks or hashes,
    2. the base IRI ends in a slash,
    3. the relative [=IRI=] does not start with a slash, and
    4. the relative [=IRI=] does not contain any "`.`" or "`..`" path segments.


