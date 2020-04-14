import unittest
from src.lib import Foo


class TestFoo(unittest.TestCase):

    def test_bar(self):
        foo = Foo()

        expected_result = 'Hello, World!'
        result = foo.bar()

        self.assertEqual(result, expected_result, 'Should as expected')
