import unittest
from parameterized import parameterized
from tool_string import ToolString

class TestPractica(unittest.TestCase):
    @parameterized.expand([
        ('neuquen'),
        ('agita falsos usos la fatiga')
    ])
    def test_palindromo(self, phrase):
        tool_string = ToolString()
        self.assertTrue(tool_string.is_palindromo(phrase))

    @parameterized.expand([
        ('mendoza'),
        ('la programacion requiere muchas horas de practica')
    ])
    def test_no_palindromo(self, phrase):
        tool_string = ToolString()
        self.assertFalse(tool_string.is_palindromo(phrase))

    @parameterized.expand([
        ('SAN LUIS'),
        ('PYTHON')
    ])
    def test_mayusculas(self, phrase):
        tool_string = ToolString()
        self.assertTrue(tool_string.is_upper(phrase))

    @parameterized.expand([
        ('cordoba'),
        ('flask')
    ])
    def test_no_mayusculas(self, phrase):
        tool_string = ToolString()
        self.assertFalse(tool_string.is_upper(phrase))

if __name__ == '__main__':
    unittest.main()