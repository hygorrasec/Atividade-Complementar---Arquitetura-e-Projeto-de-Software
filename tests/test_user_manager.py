import pytest  # type: ignore
from UserManager import UserManager  # Importa a classe que será testada.

# Decorator com uma fixture para inicializar um objeto da classe UserManager.
@pytest.fixture
def manager():
    return UserManager()  # Retorna uma instância de UserManager para ser usada nos testes.

def test_add_user(manager):
    manager.add_user("Sidney")  # Adiciona o usuário "Sidney" e verifica se ele está na lista de usuários.
    assert "Sidney" in manager.users
    assert manager.add_user("Sidney") == "User already exists!"  # Tenta adicionar o mesmo usuário novamente e verifica se retorna a mensagem correta.

def test_remove_user(manager):
    manager.add_user("Loyola")  # Adiciona o usuário "Loyola" e verifica se ele está na lista de usuários.
    assert "Loyola" in manager.users
    assert manager.remove_user("Loyola") is None  # Remove o usuário "Loyola" e verifica se ele foi removido corretamente.
    assert "Loyola" not in manager.users
    assert manager.remove_user("Loyola") == "User not found!"  # Tenta remover um usuário inexistente e verifica se retorna a mensagem correta.
