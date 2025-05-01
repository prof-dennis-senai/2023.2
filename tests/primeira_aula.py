import datetime

class Calculadora:

    @staticmethod
    def soma(num1, num2):
        return int(num1) + int(num2)
    
    @staticmethod
    def calcular_idade_em_dias(data_nascimento):
        hoje = datetime.datetime.now()
        data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')

        if data_nascimento > hoje:
            raise ValueError("A data de nascimento nao pode ser maior que a data atual")


        idade_em_dias = (hoje - data_nascimento).days

        if idade_em_dias == 0:
            idade_em_dias = 1
            
        return idade_em_dias