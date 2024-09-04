def pertence_fibonacci(n):
    if n < 0:
        return False
    
    
    a, b = 0, 1
    
    if n == a or n == b:
        return True
    
    while b < n:
        a, b = b, a + b
        
    return b == n

entrada = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if pertence_fibonacci(entrada):
    print(f"O número {entrada} pertence à sequência de Fibonacci.")
else:
    print(f"O número {entrada} não pertence à sequência de Fibonacci.")

