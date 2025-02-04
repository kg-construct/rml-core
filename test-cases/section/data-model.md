# Data model

The test cases are semantically described for re-usability and shareability following the [W3C Test case description](https://www.w3.org/2006/03/test-description).
Each `test:Testcase` as the following properties:

- `dcterms:identifier`: unique ID of the test case.
- `rmltest:hasError`: if an error of the RML Processor is expected or not.
- `rmltest:input`: One or more input data of the test case.
- `rmltest:output`: One or more output data of the test case.
- `rmltest:inputFormat`: the input data format.
- `rmltest:outputFormat`: the output data format.
- `rmltest:mappingDocument`: the RML mapping rules in Turtle.
