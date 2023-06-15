#!/usr/bin/env python
#
# (c) Dylan Van Assche (2020 - 2023)
# IDLab - Ghent University - imec
# MIT license
#

import os
import argparse
import unittest
import logging
from parameterized import parameterized
from glob import glob
from rdflib import Graph

from mapping_validator import MappingValidator

TEST_CASES_DIR = os.path.join(os.path.abspath('../test-cases'),
                              '*/mapping.ttl')
CORE_SHAPE_FILE = os.path.abspath('core.ttl')
SHACL_SHAPE_FILE = os.path.abspath('shacl.ttl')


class MappingValidatorTests(unittest.TestCase):
    def _validate_rules(self, path: str) -> None:
        rules = Graph().parse(path, format='turtle')
        mapping_validator = MappingValidator(CORE_SHAPE_FILE)
        mapping_validator.validate(rules)

    def _validate_shapes(self, path: str) -> None:
        rules = Graph().parse(path, format='turtle')
        mapping_validator = MappingValidator(SHACL_SHAPE_FILE)
        mapping_validator.validate(rules)

    def test_non_existing_mapping_rules(self) -> None:
        with self.assertRaises(FileNotFoundError):
            p = os.path.abspath('does_not_exist.ttl')
            self._validate_rules(p)

    @parameterized.expand([(p,) for p in sorted(glob(TEST_CASES_DIR))],
                          skip_on_empty=True)
    def test_validation_rules(self, path: str) -> None:
        """
        Test if our SHACL shapes are able to validate our validation mapping
        rules test cases.
        """
        print(f'Testing validation with: {path}')
        if 'RMLTC0004b' in path or 'RMLTC0007h' in path or \
                'RMLTC0012c' in path or 'RMLTC0012d' in path or \
                'RMLTC0015b' in path:
            with self.assertRaises(Exception):
                self._validate_rules(path)
        # ShapeRecursionWarning
        elif 'RMLTC0008b' in path or 'RMLTC0009a' in path or \
                'RMLTC0009b' in path:
            with self.assertRaises(Exception):
                self._validate_rules(path)
        else:
            self._validate_rules(path)

    @unittest.skip('pySHACL validation is broken for Core')
    def test_validation_shapes(self) -> None:
        """
        Test if our SHACL shapes are valid according to the W3C Recommdendation
        of SHACL. Validation with the official SHACL shapes for SHACL.

        See https://www.w3.org/TR/shacl/#shacl-shacl
        """
        self._validate_shapes('./core.ttl')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute tests for SHACL '
                                     'shapes on RML mapping rules.')
    parser.add_argument('--verbose', '-v', action='count', default=1,
                        help='Set verbosity level of messages. Example: -vvv')
    args = parser.parse_args()

    args.verbose = 70 - (10 * args.verbose) if args.verbose > 0 else 0
    logging.basicConfig(level=args.verbose,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    print(TEST_CASES_DIR)
    unittest.main(failfast=True)
