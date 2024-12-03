# Trabalho de Graduação: Testes Automatizados em Python

**Repositório**: [Atividade Complementar - Arquitetura e Projeto de Software](https://github.com/hygorrasec/Atividade-Complementar---Arquitetura-e-Projeto-de-Software)

**Universidade de Vassouras – Campus Maricá**  
**Disciplina**: Arquitetura e Projeto de Software  
**Curso**: Engenharia de Software – 6º período  
**Professora**: Sidney Loyola  
**Estudante**: Hygor Rasec  

---

## Instruções do que precisa ser feito

1. Você receberá três arquivos Python com classes implementadas.  
2. Cada classe contém métodos que possuem bugs.  
3. Seu objetivo é:  
   - Identificar os bugs nas implementações.  
   - Corrigir os métodos para que funcionem conforme esperado.  
   - Escrever testes automatizados para verificar se os métodos corrigidos estão funcionando corretamente.  
4. Utilize a biblioteca **unittest** ou **pytest** para criar os testes automatizados.

## Como rodar os testes

1. Certifique que o Python esteja instalado no seu sistema.
2. Crie o ambiente virtual em cada pasta (auth_service) e (orders_service): ```python -m venv venv```
- Iniciando Ambiente Virtual (Linux): ```. venv/bin/activate```
- Iniciando Ambiente Virtual (Windows PowerShell): ```.\venv\Scripts\Activate.ps1```
- Iniciando Ambiente Virtual (Windows CMD): ```.\venv\Scripts\activate.bat```
3. Instalando bibliotecas: ```pip install -r requirements.txt```
4. Rode o comando para testar: ```pytest```
