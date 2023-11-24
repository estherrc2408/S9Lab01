Puedes ejecutar todas las pruebas con el siguiente comando en el directorio principal del proyecto:
- python -m unittest discover -s tests -p "test_*.py"
NOTA: *-s tests* indica que unittest debe buscar pruebas en el directorio "tests", y *-p* "test_*.py" especifica que solo debe considerar los archivos cuyos nombres comienzan con "test_".

