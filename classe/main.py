class Data:
    
    def __init__(self,dia:int,mes:int,ano:int) -> None:
        self.dia = dia 
        self.mes = mes
        self.ano = ano

    def __str__(self) -> str:
        return f'{self.dia}/{self.mes}/{self.ano}'






