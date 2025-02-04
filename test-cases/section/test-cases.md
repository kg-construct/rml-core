# Test cases

This section describes the RML-Core test cases. These descriptions are also available as RDF.
The files are available on [GitHub](https://github.com/kg-construct/rml-core/tree/main/test-cases) in the folder `test-cases`.
Each test case is contained in a single folder, containing three types of files:

 - Zero or more files containing the data sources, in the case of JSON, XML, CSV, or containing the SQL statements to create the necessary tables, in the case of MySQL, PostgreSQL, and SQL Server.
 - One file with the RML rules, called `mapping.ttl`, in the Turtle format.
 - Zero or more files with the expected RDF. No file is provided if an error is expected that must halt the generation of the RDF because of an error.

