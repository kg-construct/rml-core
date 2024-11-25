# Datatype conversions

For each [=reference formulation=] there may be a set of defined <dfn data-lt="natural mapping">natural RDF mappings</dfn> that are applied to the [=expression evaluation results=] on the [=data source=]. These [=natural mappings=] are defined in the [[RML-IO-Registry]] and are used to convert the values of the [=expression evaluation result=] to the appropriate [=natural RDF literal=] corresponding with the [=reference formulation=].

## Natural mapping of source values

The <dfn>natural RDF literal</dfn> is a [=literal=] that is the result of applying a [=natural mapping=] on a value of a [=data source=], which produces a [=literal=] that is the most appropriate representation of the value in RDF. The [=natural RDF literal=] has a [=natural RDF lexical form=].

The <dfn>natural RDF lexical form</dfn> produces only the [=lexical form=] of the [=literal=] and recommends that implementations SHOULD apply the [=XSD canonical mapping=], making it a [=canonical RDF lexical form=]. It is used in RML when non-string [=expression evaluation results=] are used in a string context, for example when a timestamp is used in an [=template-valued term map=] with [=term type=] [=IRI=].

The <dfn>canonical RDF lexical form</dfn> produces only the [=lexical form=] of the [=literal=] and requires that the [=XSD canonical mapping=] MUST be applied. 

<dfn>Cast to string</dfn> is an implementation-dependent function that maps values from [=expression evaluation results=] to equivalent Unicode strings. The specifics of [=cast to string=] per [=reference formulation=] are defined in the [[RML-IO-Registry]].

Additionally, the [=natural mapping=] determines the [=natural RDF datatype=] of the [=literal=].

The <dfn>natural RDF datatype</dfn> is the [=datatype=] corresponding to the [=natural RDF literal=] that is the result of the [=natural mapping=]. The [=natural RDF datatype=] is an [=IRI=] that represents the [=datatype=] of the value in RDF.

## Datatype-override mapping of source values

The <dfn>datatype-override RDF literal</dfn> corresponding to an [=expression evaluation result=] value `v` and a [=datatype IRI=] `dt`, is a [=literal=] whose [=lexical form=] is the [=natural RDF lexical form=] corresponding to `v`, and whose [=datatype IRI=] is `dt`. If the [=literal=] is [=ill-typed=], then a [=data error=] is raised.

A [=literal=] is <dfn data-lt="ill-typed literal">ill-typed</dfn> in RML if its [=datatype IRI=] denotes a [=validatable RDF datatype=] and its [=lexical form=] is not in the [=lexical space=] of the [=RDF datatype=] identified by its [=datatype IRI=].

The set of <dfn>validatable RDF datatypes</dfn> includes all [=datatypes=] in the RDF datatype column of [[[#table-lexical-forms]]], as defined in [[XMLSCHEMA11-2]]. This set MAY include implementation-defined additional RDF datatypes.

For example, `"X"^^xsd:boolean` is [=ill-typed=] because `xsd:boolean` is a validatable [=RDF datatype=] in RML, and `"X"` is not in the [=lexical space=] of `xsd:boolean` [[XMLSCHEMA11-2]].

<section class="informative">
<h2>Summary of XSD Lexical Forms</h2>

The [=natural mappings=] make reference to various [=XSD datatypes=] and require that values from [=expression evaluation results=] be converted to strings that are appropriate as [=lexical forms=] for these [=datatypes=]. This subsection gives examples of these [=lexical forms=] in order to aid implementers of the mappings. This subsection is non-normative; the normative definitions of the [=lexical spaces=] as well as the [=canonical mappings=] are found in [[XMLSCHEMA11-2]].

A general approach that may be used for implementing the natural mappings is as follows:

1. Identify the source datatype of value of the [=expression evaluation result=] on the [=data source=].
1. Look up its corresponding [=natural RDF datatype=] for the [=reference formulation=] in the [[RML-IO-Registry]].
1. Apply [=cast to string=] to the value.
1. Ensure that the resulting string is in the [=lexical space=] of the target [=RDF datatype=]; that is, it must be in a form such as those listed in either column of [[[#table-lexical-forms]]] below. This may require some transformations of the string, in particular for `xsd:hexBinary`, `xsd:dateTime` and `xsd:boolean`.
1. If the goal is to obtain a [=canonical RDF lexical form=], then further string transformations may be required to obtain a form such as those listed in the Canonical lexical forms column of [[[#table-lexical-forms]]] below.

<table class="numbered" id="table-lexical-forms">
<caption>Table of canonical and non-canonical lexical forms for some XSD datatypes</caption>
<tbody>
  <tr>
    <th>RDF datatype</th>
    <th>Non-canonical lexical forms</th>
    <th>Canonical lexical forms</th>
    <th>Comments</th>
  </tr>
  <tr>
    <td><code><a href="https://www.w3.org/TR/xmlschema11-2/#hexBinary">xsd:hexBinary</a></code></td>
    <td><code>5232524d4c</code></td>
    <td><code>5232524D4C</code></td>
    <td>Convert from SQL by applying <a href="https://www.w3.org/TR/xmlschema11-2/#hexBinary"><code>xsd:hexBinary</code> lexical mapping</a>.</td>
  </tr>
  <tr>
    <td rowspan="4"><code><a href="https://www.w3.org/TR/xmlschema11-2/#decimal">xsd:decimal</a></code></td>
    <td><code>.224</code></td>
    <td><code>0.224</code></td>
    <td rowspan="4"></td>
  </tr>
  <tr>
    <td><code>+001</code></td>
    <td><code>1</code></td>
  </tr>
  <tr>
    <td><code>42.0</code></td>
    <td><code>42</code></td>
  </tr>
  <tr>
    <td><code>-5.9000</code></td>
    <td><code>-5.9</code></td>
  </tr>
  <tr>
    <td rowspan="3"><code><a href="https://www.w3.org/TR/xmlschema11-2/#integer">xsd:integer</a></code></td>
    <td><code>-05</code></td>
    <td><code>-5</code></td>
    <td rowspan="3"></td>
  </tr>
  <tr>
    <td><code>+333</code></td>
    <td><code>333</code></td>
  </tr>
  <tr>
    <td><code>00</code></td>
    <td><code>0</code></td>
  </tr>
  <tr>
    <td rowspan="5"><code><a href="https://www.w3.org/TR/xmlschema11-2/#double">xsd:double</a></code></td>
    <td><code>-5.90</code></td>
    <td><code>-5.9E0</code></td>
    <td rowspan="5">Also supports <code>INF</code>, <code>-INF</code>, <code>NaN</code> and <code>-0.0E0</code>,<br>but these do not appear in standard SQL.</td>
  </tr>
  <tr>
    <td><code>+0.00014770215000</code></td>
    <td><code>1.4770215E-4</code></td>
  </tr>
  <tr>
    <td><code>+01E+3</code></td>
    <td><code>1.0E3</code></td>
  </tr>
  <tr>
    <td><code>100.0</code></td>
    <td><code>1.0E2</code></td>
  </tr>
  <tr>
    <td><code>0</code></td>
    <td><code>0.0E0</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code><a href="https://www.w3.org/TR/xmlschema11-2/#boolean">xsd:boolean</a></code></td>
    <td><code>1</code></td>
    <td><code>true</code></td>
    <td rowspan="2">Must be lowercase.</td>
  </tr>
  <tr>
    <td><code>0</code></td>
    <td><code>false</code></td>
  </tr>
  <tr>
    <td><code><a href="https://www.w3.org/TR/xmlschema11-2/#date">xsd:date</a></code></td>
    <td></td>
    <td><code>2011-08-23</code></td>
    <td>Dates in SQL don't have timezone offsets.<br>They are optional in XSD.</td>
  </tr>
  <tr>
    <td rowspan="3"><code><a href="https://www.w3.org/TR/xmlschema11-2/#time">xsd:time</a></code></td>
    <td><code>22:17:34.885+00:00</code></td>
    <td><code>22:17:34.885Z</code></td>
    <td rowspan="3">May or may not have timezone offset.</td>
  </tr>
  <tr>
    <td><code>22:17:34.000</code></td>
    <td><code>22:17:34</code></td>
  </tr>
  <tr>
    <td><code>22:17:34.1+01:00</code></td>
    <td><code>22:17:34.1+01:00</code></td>
  </tr>
  <tr>
    <td><code><a href="https://www.w3.org/TR/xmlschema11-2/#dateTime">xsd:dateTime</a></code></td>
    <td><code>2011-08-23T22:17:00.000+00:00</code></td>
    <td><code>2011-08-23T22:17:00Z</code></td>
    <td>May or may not have timezone offset.<br>Convert from SQL by replacing space with "<code>T</code>".</td>
  </tr>
</tbody>
</table>

</section>
