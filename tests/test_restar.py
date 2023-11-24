import unittest
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

if __name__ == '__main__':
    unittest.main()