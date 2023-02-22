import unittest
from serlib import serlib


class TestPrimitives(unittest.TestCase):
    def test_int(self):
        original = [1, 5, 3]
        expected = "[1, 5, 3]"
        serialized = serlib.to_json(original)
        self.assertEqual(expected, serialized)
        final = serlib.from_json(serialized)
        self.assertEqual(original, final)

    def test_float(self):
        original = [1.0, 5.3, 3.999999]
        expected = "[1.0, 5.3, 3.999999]"
        serialized = serlib.to_json(original)
        self.assertEqual(expected, serialized)
        final = serlib.from_json(serialized)
        self.assertEqual(original, final)

    def test_str(self):
        original = ["one", "two", "three"]
        expected = """["one", "two", "three"]"""
        serialized = serlib.to_json(original)
        self.assertEqual(expected, serialized)
        final = serlib.from_json(serialized)
        self.assertEqual(original, final)

    def test_bool(self):
        original = [True, False, True]
        expected = "[true, false, true]"
        serialized = serlib.to_json(original)
        self.assertEqual(expected, serialized)
        final = serlib.from_json(serialized)
        self.assertEqual(original, final)


class TestStub(unittest.TestCase):

    def test_parser(self):
        # Given
        input = ["--name", "Davo"]

        # When
        result = serlib.setup(input)

        # Then
        self.assertFalse(result.verbose)
        self.assertEqual(result.name, input[1])

    def test_no_name(self):
        # When
        result = serlib.run()

        # Then
        self.assertEqual(result, "Hello, world!")

    def test_name(self):
        # When
        result = serlib.run("Davo")

        # Then
        self.assertEqual(result, "Hello, Davo!")
