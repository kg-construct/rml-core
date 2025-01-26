# RML Core test cases

Manifest of test cases can be generated as followed:

1. Add the testcase description in `descriptions.csv` or fetch it from the Google spreadsheet.
2. Execute the `make-metadata.py` script: `python3 make-metadata.py http://w3id.org/rml/core/`
3. Generate the manifest with RMLMapper: `java -jar rmlmapper.jar -m manifest.rml.ttl -o manifest.ttl -s turtle`


