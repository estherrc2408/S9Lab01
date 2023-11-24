import unittest
import sys

from calculadora import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        # Resultado > 0
        self.assertEqual(dividir(3, 3), 1)
        # Resultado = 0
        self.assertEqual(dividir(0, 3), 0)
        # Resultado != 0
        with self.assertRaises(ZeroDivisionError):
            dividir(3, 0)
        # Resultado < 0
        self.assertEqual(dividir(3, -3), -1)
        # Pruebas adicionales de tipos
        self.assertEqual(dividir(3.5, 2), "Ambos deben ser números enteros")
        self.assertEqual(dividir("3", 2), "Ambos deben ser números enteros")
        # Dividir un límite
        self.assertEqual(dividir(sys.maxsize, 2), sys.maxsize / 2)

if __name__ == '__main__':
    unittest.main()
