
from datetime import datetime

class Projeto:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
        return self.tarefas.__iter__()

    def _add_tarefa(self,tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _nova_tarefa(self,descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento',None)))

    def add_tarefa(self, tarefa, vencimento = None,**kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa,Tarefa) else self._nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

        #self.tarefas.append(Tarefa(descricao))
    
    def pendentes(self):
        return [Tarefa for Tarefa in self.tarefas if not Tarefa.feito]

    def procurar(self,descricao):
        return [Tarefa for Tarefa in self.tarefas if Tarefa.descricao == descricao][0]
    
    def __str__(self) -> str:
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) Pendente(s))'

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
   
    casa = Projeto('Tarefas de casa')
    casa.add_tarefa('Passar Pano')
    casa.add_tarefa('Lavar prato')

    mercado = Projeto('Mercado')
    mercado.add_tarefa('comprar poupa de fruta')
    mercado.add_tarefa('comprar banana')
    casa.procurar('Lavar prato').concluir()
    
    for tarefa in mercado:
        print(tarefa)
   

    
    # mercado.add_tarefa('comprar poupa de fruta')
    # mercado.add_tarefa('comprar banana')

    

if __name__=='__main__':    
    main()

# percorrer lista de forma otimizada e chame o método concluir tarefa qnd a tarefa for lavar prato
