
from datetime import datetime


class Tarefa:
    
    def __init__(self, descricao) -> None:
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def concluir(self):
        self.feito = True
    
    def __str__(self) -> str:
         return self.descricao + (' (Concluída)' if self.feito else '')

def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('lavar prato'))
    casa.append(Tarefa('cozinhar'))
    casa.append(Tarefa('estender roupa'))

    nova = [Tarefa.concluir() for Tarefa in casa if Tarefa.descricao == 'lavar prato']

    for tarefas in casa:
        print(f'- {tarefas}')
      


if __name__=='__main__':    
    main()

# percorrer lista de forma otimizada e chame o método concluir tarefa qnd a tarefa for lavar prato
