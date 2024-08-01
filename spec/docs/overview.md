# [R2]RML Overview and Example (Informative)


Each [=logical source=] is mapped to RDF using a [triples map]().
The [triples map]() is a rule that maps each iteration in the [=logical source=]
to a number of [=RDF triples=].
The rule has two main parts:


 1. A [subject map]() that generates the subject of all [=RDF triples=]
 that will be generated from a logical source iteration.
 The subjects often are [=IRIs=].
 2. Multiple [predicate-object maps]() that
 in turn consist of [predicate maps]() and [object maps]()
 (or [referencing object maps]()).
 
By default, all [=RDF triples=] are in the [=default graph=] of the [output dataset]().
A [triples map]() can contain [graph maps]() that
place some or all of the triples into [=named graphs=] instead. 

**TODO: Add updated figure here**
