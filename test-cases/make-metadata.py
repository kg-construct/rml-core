#!/usr/bin/env python3

import os
import sys
import glob
import csv

def get_title_description(testcase: str):
    with open ('descriptions.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == testcase:
                return row[1], row[2]
    print(f'{testcase} not found in descriptions.csv')
    sys.exit(1)

def main(spec: str):
    with open ('metadata.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'title', 'description', 'specification',
                         'mapping', 'input_format1', 'input_format2',
                         'input_format3', 'output_format1', 'output_format2',
                         'output_format3', 'input1', 'input2', 'input3',
                         'output1', 'output2', 'output3', 'error'])
        for testcase in glob.glob('RML*'):
            title, description = get_title_description(testcase)
            title = '"' + title + '"'
            description = '"' + description + '"'
            error = 'false'
            input1 = ''
            input2 = ''
            input3 = ''
            input_format1 = ''
            input_format2 = ''
            input_format3 = ''
            output1 = ''
            output2 = ''
            output3 = ''
            output_format1 = ''
            output_format2 = ''
            output_format3 = ''

            # Input file
            if os.path.exists(os.path.join(testcase, 'student.json')):
                input1 = 'student.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'student_sport.json')):
                if testcase == 'RMLTC0009a-JSON' or testcase == 'RMLTC0009b-JSON':
                    input3 = 'student_sport.json'
                    input_format3 = 'application/json'
                else:
                    input1 = 'student_sport.json'
                    input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'sport.json')):
                input2 = 'sport.json'
                input_format2 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'ious.json')):
                input1 = 'ious.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'country_info.json')):
                input1 = 'country_info.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'persons.json')):
                if testcase == 'RMLTC0012b-JSON':
                    input2 = 'persons.json'
                    input_format2 = 'application/json'
                else:
                    input1 = 'persons.json'
                    input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'country_en.json')):
                input1 = 'country_en.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'country_es.json')):
                input1 = 'country_es.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'data.json')):
                input1 = 'data.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'lives.json')):
                input1 = 'lives.json'
                input_format1 = 'application/json'
            elif os.path.exists(os.path.join(testcase, 'student.xml')):
                input1 = 'student.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'student_sport.xml')):
                if testcase == 'RMLTC0009a-XML' or testcase == 'RMLTC0009b-XML':
                    input3 = 'student_sport.xml'
                    input_format3 = 'text/xml'
                else:
                    input1 = 'student_sport.xml'
                    input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'sport.xml')):
                input2 = 'sport.xml'
                input_format2 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'ious.xml')):
                input1 = 'ious.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'country_info.xml')):
                input1 = 'country_info.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'persons.xml')):
                if testcase == 'RMLTC0012b-XML':
                    input2 = 'persons.xml'
                    input_format2 = 'text/xml'
                else:
                    input1 = 'persons.xml'
                    input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'country_en.xml')):
                input1 = 'country_en.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'country_es.xml')):
                input1 = 'country_es.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'data.xml')):
                input1 = 'data.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'lives.xml')):
                input1 = 'lives.xml'
                input_format1 = 'text/xml'
            elif os.path.exists(os.path.join(testcase, 'student.csv')):
                input1 = 'student.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'student_sport.csv')):
                if testcase == 'RMLTC0009a-CSV' or testcase == 'RMLTC0009b-CSV':
                    input3 = 'student_sport.csv'
                    input_format3 = 'text/csv'
                else:
                    input1 = 'student_sport.csv'
                    input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'sport.csv')):
                input2 = 'sport.csv'
                input_format2 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'ious.csv')):
                input1 = 'ious.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'country_info.csv')):
                input1 = 'country_info.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'persons.csv')):
                if testcase == 'RMLTC0012b-CSV':
                    input2 = 'persons.csv'
                    input_format2 = 'text/csv'
                else:
                    input1 = 'persons.csv'
                    input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'country_en.csv')):
                input1 = 'country_en.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'country_es.csv')):
                input1 = 'country_es.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'data.csv')):
                input1 = 'data.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'lives.csv')):
                input1 = 'lives.csv'
                input_format1 = 'text/csv'
            elif os.path.exists(os.path.join(testcase, 'resource.sql')):
                input1 = 'resource.sql'
                if 'MySQL' in testcase:
                    input_format1 = 'application/sql+mysql'
                elif 'PostgreSQL' in testcase:
                    input_format1 = 'application/sql+postgresql'
                elif 'SQLServer' in testcase:
                    input_format1 = 'application/sql+sqlserver'
                elif 'MariaDB' in testcase:
                    input_format1 = 'application/sql+mariadb'
                elif 'SQLite' in testcase:
                    input_format1 = 'application/sql+sqlite'
                else:
                    input_format1 = 'application/sql'
            elif os.path.exists(os.path.join(testcase, 'resource.ttl')):
                input1 = 'resource.ttl'
                input_format1 = 'text/turtle'
            elif os.path.exists(os.path.join(testcase, 'resource1.ttl')):
                input1 = 'resource1.ttl'
                input_format1 = 'text/turtle'
            elif os.path.exists(os.path.join(testcase, 'resource2.ttl')):
                input2 = 'resource2.ttl'
                input_format2 = 'text/turtle'

            # Mapping file
            if os.path.exists(os.path.join(testcase, 'mapping.ttl')):
               mapping_file = 'mapping.ttl'
            else:
                raise ValueError('Mapping file missing!')

            # Output files
            if os.path.exists(os.path.join(testcase, 'output.nq')):
                output1 = 'output.nq'
                output_format1 = 'application/n-quads'
            else:
                error = 'true';

            writer.writerow([testcase, title, description, spec, mapping_file,
                             input_format1, input_format2, input_format3,
                             output_format1, output_format2, output_format3,
                             input1, input2, input3, output1, output2,
                             output3, error])
            lines = []
            # Title and description
            lines.append(f'## {testcase}\n\n')
            lines.append(f'**Title**: {title}\n\n')
            lines.append(f'**Description**: {description}\n\n')
            if error == 'true':
                error_html = 'Yes'
            else:
                error_html = 'No'
            lines.append(f'**Error expected?** {error_html}\n\n')

            # Input
            inputCount = ''

            for index, i in enumerate([input1, input2, input3]):
                if not i:
                    break

                if 'http://w3id.org/rml/resources' in i:
                    input_html = f'**Input{inputCount}**\n [{i}]({i})\n\n'
                else:
                    try:
                        with open(os.path.join(testcase, i)) as f:
                            input_html = f'**Input{inputCount}**\n```\n{f.read()}\n```\n\n'
                    except UnicodeDecodeError:
                        try:
                            with open(os.path.join(testcase, i), encoding='utf-16') as f:
                                input_html = f'**Input{inputCount}**\n```\n{f.read()}\n```\n\n'
                        except UnicodeDecodeError:
                            input_html = f'**Input{inputCount}**\n `{i}`\n\n'

                lines.append(input_html)
                inputCount = f' {index + 1}'

            # Mapping
            with open(os.path.join(testcase, mapping_file)) as f:
                mapping_html = f'**Mapping**\n```\n{f.read()}\n```\n\n'
                lines.append(mapping_html)

            # Output
            outputCount = ''
            if output2 or output3:
                outputCount = ' 1'

            for index, i in enumerate([output1, output2, output3]):
                if not i:
                    break

                if 'http://w3id.org/rml/resources' in i:
                    output_html = f'**Output{outputCount}**\n [{i}]({i})\n\n'
                else:
                    try:
                        with open(os.path.join(testcase, i)) as f:
                            output_html = f'**Output{outputCount}**\n```\n{f.read()}\n```\n\n'
                    except UnicodeDecodeError:
                        try:
                            with open(os.path.join(testcase, i), encoding='utf-16') as f:
                                output_html = f'**Output{outputCount}**\n```\n{f.read()}\n```\n\n'
                        except UnicodeDecodeError:
                            output_html = f'**Output{outputCount}**\n `{i}`\n\n'

                lines.append(output_html)
                outputCount = f' {index + 2}'


            with open(os.path.join(testcase, 'README.md'), 'w') as f:
                f.writelines(lines)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./make-metadata.py <IRI OF SPEC>')
        sys.exit(1)
    main(sys.argv[1])
