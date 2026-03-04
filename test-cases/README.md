# RML Core test cases

Manifest of test cases can be generated as followed:

1. Add the testcase description in `descriptions.csv` or fetch it from the Google spreadsheet.
2. Execute the `make-metadata.py` script: `python3 make-metadata.py http://w3id.org/rml/core/`
3. Generate the manifest with RMLMapper: `java -jar rmlmapper.jar -m manifest.rml.ttl -o manifest.ttl -s turtle`
4. Run list.sh and insert output in dev.html
5. To publish the new HTML verson of the test cases, run with `python3 -m http.server`, export `dev.html` as `index.html` in ./docs and in a subfolder with the date of the publication (maybe adapt the publication date)  

