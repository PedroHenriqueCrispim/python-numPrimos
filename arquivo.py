#Pedro Crispim RM:99005

def is_prime(num):
    """
    Função para verificar se um número é primo.
    Retorna True se o número for primo e False caso contrário.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nearest_prime(num):
    """
    Função para encontrar o número primo mais próximo de um determinado número.
    Retorna o número primo mais próximo encontrado.
    """
    if num == 1:
        return 2
    if is_prime(num):
        return num
    lower_prime = num - 1
    upper_prime = num + 1
    while not is_prime(lower_prime) and not is_prime(upper_prime):
        lower_prime -= 1
        upper_prime += 1
    if is_prime(lower_prime) and is_prime(upper_prime):
        return lower_prime
    elif is_prime(lower_prime):
        return lower_prime
    else:
        return upper_prime

# Loop para solicitar entrada do usuário até que o número zero seja digitado
while True:
    num = input("Digite um número entre 1 e 1000 (digite 0 para sair): ")
    try:
        num = int(num)
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue
    if num == 0:
        break
    elif num < 1 or num > 1000:
        print("Número inválido. Tente novamente.")
        continue
    else:
        nearest_prime = find_nearest_prime(num)
        print("O número primo mais próximo de", num, "é", nearest_prime)

