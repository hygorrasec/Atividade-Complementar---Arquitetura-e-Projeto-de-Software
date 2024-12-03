import pytest  # type: ignore
from FibonacciGenerator import FibonacciGenerator  # Importa a classe que será testada.

# Decorator com uma fixture para inicializar um objeto da classe FibonacciGenerator.
@pytest.fixture
def fib():
    return FibonacciGenerator()  # Retorna uma instância de FibonacciGenerator para ser usada nos testes.

def test_generate_sequence(fib):
    assert fib.generate_sequence(0) == []  # Verifica se o método retorna uma lista vazia para entrada 0.
    assert fib.generate_sequence(1) == [0]  # Verifica se o método retorna [0] para entrada 1.
    assert fib.generate_sequence(5) == [0, 1, 1, 2, 3]  # Verifica se o método retorna os primeiros 5 números da sequência de Fibonacci.

def test_get_nth_number(fib):
    assert fib.get_nth_number(0) is None  # Verifica se retorna None para entrada inválida (0).
    assert fib.get_nth_number(1) == 0  # Verifica se o primeiro número da sequência é 0.
    assert fib.get_nth_number(2) == 1  # Verifica se o segundo número da sequência é 1.
    assert fib.get_nth_number(5) == 3  # Verifica se o quinto número da sequência é 3.
