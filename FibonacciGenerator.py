class FibonacciGenerator:
    def generate_sequence(self, n):
        """
        Gera os primeiros n números da sequência de Fibonacci.
        :param n: Número de elementos na sequência.
        :return: Lista contendo a sequência de Fibonacci.
        """
        if n <= 0:
            return []  # OK: Sequência vazia para entrada inválida.
        
        sequence = [0, 1]
        for _ in range(n):  
            next_number = sequence[-1] + sequence[-1]  # BUG: Deve ser sequence[-1] + sequence[-2].
            sequence.append(next_number)
        return sequence[:n]  # OK: Retorna apenas os primeiros n números.

    def get_nth_number(self, n):
        """
        Retorna o enésimo número da sequência de Fibonacci (baseado em índice 1).
        :param n: Posição do número na sequência (1-indexed).
        :return: Número correspondente na sequência.
        """
        if n <= 0:
            return None  # OK: Entrada inválida retorna None.
        elif n == 1:
            return 0  # OK: Primeiro número da sequência é 0.
        elif n == 2:
            return 1  # OK: Segundo número da sequência é 1.
        
        a, b = 0, 1
        for _ in range(n - 2):  # BUG: Deve ser range(n - 1).
            a = b  
            b = b + a
        return b
