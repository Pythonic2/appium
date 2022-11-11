from datetime import datetime
from desafio import Cliente,Vendedor,Compra


def main():
    cliente = Cliente('Maria Lima',44)
    vendedor = Vendedor('Pedro Garrido',36,5000)
    compra1 = Compra(cliente,datetime.now(),512)
    compra2 = Compra(cliente, datetime(2022,6,4), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    
    print(f'Cliente: {cliente}','(Adulto)' if cliente.is_Adulto() else '(Menor)')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()

    qtd_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtd_compras} compras')
    print(f'Ultima compra: {cliente.get_data_ultima_compra()}')

if __name__=='__main__':
    main()