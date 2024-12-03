import pytest  # type: ignore
from StringUtils import StringUtils  # Importa a classe que será testada.

# Decorator com uma fixture para inicializar um objeto da classe StringUtils.
@pytest.fixture
def utils():
    return StringUtils()  # Retorna uma instância de StringUtils para ser usada nos testes.

def test_reverse_string(utils):
    assert utils.reverse_string("hygor") == "rogyh"  # Verifica se a string "hygor" é revertida corretamente.
    assert utils.reverse_string("") == ""  # Verifica se a string vazia retorna ela mesma.
    assert utils.reverse_string("a") == "a"  # Verifica se uma string com um único caractere retorna ela mesma.

def test_is_palindrome(utils):
    assert utils.is_palindrome("osso") is True  # Verifica se "osso" é identificado como um palíndromo.
    assert utils.is_palindrome("hygor") is False  # Verifica se "hygor" não é identificado como um palíndromo.
    assert utils.is_palindrome("") is True  # Verifica se uma string vazia é identificada como um palíndromo.
