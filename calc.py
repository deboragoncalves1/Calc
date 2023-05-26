class Calculadora:

    def __init__(self):

        self.__numero1 = 0

        self.__numero2 = 0

    def soma(self):

        numero1 = int(input("Digite o primeiro 1° inteiro positivo: "))

        numero2 = int(input("Digite o 2° número inteiro positivo: "))

        if numero1 > 0 and numero2 > 0:

            self.__numero1 = numero1

            self.__numero2 = numero2

            return self.__numero1 + self.__numero2

        else:

            return "Os números devem ser inteiros positivos."

    def multiplicar(self):

        numero1 = int(input("Digite o 1° número (pode ser negativo): "))

        numero2 = int(input("Digite o 2° número (deve ser positivo): "))

        if numero1 < 0 and numero2 > 0:

            self.__numero1 = numero1

            self.__numero2 = numero2

            return self.__numero1 * self.__numero2

        else:

            return "O primeiro número deve ser negativo e o segundo número deve ser positivo."

    def desconto(self):

        valor = float(input("Digite o valor: "))

        taxa_desconto = float(
            input("Digite a taxa de desconto em porcentagem: "))

        if valor > 0 and taxa_desconto > 0:

            self.__numero1 = valor

            self.__numero2 = taxa_desconto

            desconto = self.__numero1 * (self.__numero2 / 100)

            return self.__numero1 - desconto

        else:

            return "O valor e a taxa de desconto devem ser maiores que zero."


# Exemplo de uso da calculadora

calculadora = Calculadora()

# Saída: resultado da soma dos números digitados pelo usuário
print(calculadora.soma())
# Saída: resultado da multiplicação dos números digitados pelo usuário
print(calculadora.multiplicar())
# Saída: valor com desconto calculado a partir dos valores digitados pelo usuário
print(calculadora.desconto())
