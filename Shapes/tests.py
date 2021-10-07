#!/usr/bin/env python
#
# (c) Dylan Van Assche (2020-2021)
# IDLab - Ghent University - imec
# MIT license
#

import argparse
import unittest
import logging
from parameterized import parameterized
from glob import glob
from os.path import abspath
from typing import Tuple, List
from rdflib import Graph

from mapping_validator import MappingValidator

VALIDATION_MAPPING_RULES_DIR = abspath('tests/assets/validation') + '/*/*.ttl'
RML_RULES_SHAPE = abspath('rml_v1_shape.ttl')


class MappingValidatorTests(unittest.TestCase):
    def _validate_rules(self, path: str) -> None:
        rules = Graph().parse(path, format='turtle')
        mapping_validator = MappingValidator(RML_RULES_SHAPE)
        mapping_validator.validate(rules)

    def test_non_existing_mapping_rules(self) -> None:
        with self.assertRaises(FileNotFoundError):
            p = abspath('tests/assets/io/mapping_files/mapping_does_not_exist.ttl')
            self._validate_rules(p)

    @parameterized.expand([(p,) for p in sorted(glob(VALIDATION_MAPPING_RULES_DIR))])
    def test_validation_rules(self, path: str) -> None:
        """
        Test if our SHACL shapes are able to validate our validation mapping
        rules test cases.
        """
        print(f'Testing validation with: {path}')
        # All test cases with 'success' in their path should succeed.
        if 'validation_duplicate_columns.ttl' in path:
            self.skipTest('Duplicate CSVW column checks are not added yet')

        if 'success' in path:
            self._validate_rules(path)
        # The other test cases shouldn't validate
        else:
            with self.assertRaises(ValueError):
                self._validate_rules(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute tests for SHACL shapes on RML mapping rules.')
    parser.add_argument('--verbose', '-v', action='count', default=1,
                        help='Set verbosity level of messages. Example: -vvv')
    args = parser.parse_args()

    args.verbose = 70 - (10 * args.verbose) if args.verbose > 0 else 0
    logging.basicConfig(level=args.verbose,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    unittest.main(failfast=True)
