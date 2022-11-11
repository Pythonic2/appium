MAIOR_IDADE = 18
class Pessoa:
    def __init__(self, nome:str, idade:int) ->None:
        self.nome = nome
        self.idade = idade


    def __str__(self) -> str:
        if not self.idade:
            return f'{self.nome}'
        return f'Nome da Pessoa: {self.nome} com: {self.idade} anos de Idade.'

    def is_Adulto(self) -> bool:
        return (self.idade or 0) >= MAIOR_IDADE


if __name__ =='__main__':
    p1 = Pessoa('Igor',27)
    print(p1.is_Adulto())