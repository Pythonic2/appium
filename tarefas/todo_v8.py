
from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass

class Projeto:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga do operador +=
    # projeto += tarefa
    # casa += ...(tarefa)
    def __iadd__(self, tarefa):
        tarefa.dono =  self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self,tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _nova_tarefa(self,descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento',None)))

    def add_tarefa(self, tarefa, vencimento = None,**kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa,Tarefa) else self._nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
    
    def pendentes(self):
        return [Tarefa for Tarefa in self.tarefas if not Tarefa.feito]

    def procurar(self,descricao):
        # possivel exeption
        try:
            return [Tarefa for Tarefa in self.tarefas if Tarefa.descricao == descricao][0]
        except IndexError as e:
            #indexerror é o tipo de erro que pode ocorrer aqui, devemos tratar erros mais especificos possvel       
            raise TarefaNaoEncontrada(str(e))


    def __str__(self) -> str:
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) Pendente(s))'

class Tarefa:
    
    def __init__(self, descricao, vencimento=None) -> None:
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.vencimento = vencimento


    def concluir(self):
        self.feito = True
    
    def __str__(self) -> str:
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'Vence em: {dias} dias')
        return f'{self.descricao} ' + ' '.join(status)

class TarefaRecrrente(Tarefa):#herança
    def __init__(self, descricao, vencimento=None, dias=7) -> None:#herança
        super().__init__(descricao, vencimento) #herança
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir() #herança
        novo_vencimento =  datetime.now() + timedelta(days=self.dias)
        nova_tarefa =  TarefaRecrrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa

        return nova_tarefa

def main():
    casa = Projeto('Tarefas de casa')
    casa.add_tarefa('Passar Pano', datetime.now())
    casa.add_tarefa('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa +=TarefaRecrrente('Trocar Lençóis', datetime.now(), 7)
    casa.procurar('Trocar Lençóis').concluir()

    try:
        casa.procurar('dale')
    except TarefaNaoEncontrada as e:
        print(f'A causa foi: {e}')

    print(casa)
    for t in casa:
        print(f'- {t}')

    mercado = Projeto('Mercado')
    mercado.add_tarefa('comprar poupa de fruta')
    mercado.add_tarefa('comprar banana')
if __name__=='__main__':    
    main()

# percorrer lista de forma otimizada e chame o método concluir tarefa qnd a tarefa for lavar prato