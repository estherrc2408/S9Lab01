import unittest
import sys

from calculadora import sumar

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        #Resultado > 0
        self.assertEqual(sumar(3, 5), 8)
        #Resultado = 0
        self.assertEqual(sumar(-1, 1), 0)
        #Resultado < 0
        self.assertEqual(sumar(-1,-1), -2)
        # Pruebas adicionales de tipos
        self.assertEqual(sumar(3.5, 2), "Ambos deben ser números enteros")
        self.assertEqual(sumar("3", 2), "Ambos deben ser números enteros")
        # Pruebas limites
        self.assertEqual(sumar(sys.maxsize, 1), sys.maxsize+1)
        

if __name__ == '__main__':
    unittest.main()
