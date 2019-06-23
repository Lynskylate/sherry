import os
import unittest

from lark import Lark

PACKAGE_PATH = os.path.join(os.path.dirname(__file__), "..")
GRAMMER_PATH = os.path.join(PACKAGE_PATH, "sherry", "grammer", "sh.lark")

class ParserTest(unittest.TestCase):
    def test_redirection(self):
        parser = Lark.open(GRAMMER_PATH, start="redirection_list")
        res1 = parser.parse("> test")
        self.assertEqual(res1.children[0].data, 'redirection')

    def test_simple_command(self):
        parser = Lark.open(GRAMMER_PATH, start="simple_command")
        res = parser.parse("res = 1")
        self.assertEqual(res.children[0].data, "assignment_word")