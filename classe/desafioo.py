class Carro:
    def __init__(self,v_maxima) -> None:
        self.v_atual = 0
        self.maxima = v_maxima
      
       

    def acelerar(self,delta=5) ->int:

        maxima = self.maxima
        nova  =  self.v_atual + delta
        self.v_atual = nova if nova <= maxima else maxima

        return f' A celerando Carro: {self.v_atual} km'

                    
        

                  
    def frear(self, delta=10):
        maxima = self.maxima

        nova = self.v_atual - delta

        self.v_atual = nova if nova >= 0 else 0

        return f' Ferando Carro: {self.v_atual} km'



if __name__=='__main__':
    c1 = Carro(180)

    for _ in range(2):
        print(c1.acelerar(91))
    
    for _ in range(2):
        print(c1.frear(98))