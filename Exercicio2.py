# Função para calcular a sequência de Fibonacci até um limite
def pertence_fibonacci(num):
    # Definindo os dois primeiros números da sequência
    fib1, fib2 = 0, 1
    # Lista para armazenar a sequência
    fibonacci_sequence = [fib1, fib2]

    # Gera a sequência de Fibonacci até que o próximo número seja maior ou igual ao número informado
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
        fibonacci_sequence.append(fib2)

    # Verifica se o número informado pertence à sequência
    if num in fibonacci_sequence:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")


# Teste da função com um número informado
pertence_fibonacci(50)
