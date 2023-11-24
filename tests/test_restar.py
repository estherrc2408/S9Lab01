import unittest
import sys

from calculadora import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        #Resultado > 0
        self.assertEqual(restar(5,2), 3)
        #Resultado = 0
        self.assertEqual(restar(5,5), 0)
        #Resultado < 0
        self.assertEqual(restar(2,5), -3)
        # Pruebas adicionales de tipos
        self.assertEqual(restar(3.5, 2), "Ambos deben ser números enteros")
        self.assertEqual(restar("3", 2), "Ambos deben ser números enteros")
        # Pruebas limites
        self.assertEqual(restar(sys.maxsize, 1), sys.maxsize-1)

if __name__ == '__main__':
    unittest.main()