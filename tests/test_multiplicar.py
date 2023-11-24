import unittest
from calculadora import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        #Resultado > 0
        self.assertEqual(multiplicar(3,2), 6)
        #Resultado = 0
        self.assertEqual(multiplicar(2,0), 0)
        self.assertEqual(multiplicar(0,2), 0)
        #Resultado < 0
        self.assertEqual(multiplicar(3,-2), -6)
        # Pruebas adicionales de tipos
        self.assertEqual(multiplicar(3.5, 2), "Ambos deben ser números enteros")
        self.assertEqual(multiplicar("3", 2), "Ambos deben ser números enteros")

if __name__ == '__main__':
    unittest.main()