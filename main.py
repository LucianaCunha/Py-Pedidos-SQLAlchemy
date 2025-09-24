from database import Database
from models import Pedido, ItemPedido
from control import PedidoControl

if __name__ == "__main__":
    db = Database(host='localhost', user='root', password='', database='db_pedidos')
    control = PedidoControl(db)
    #pedido=Pedido(cliente="Claudio Ulisse")
    #pedido.id=7
    #control.atualizar_pedido(pedido)
    
   # control.salvar_pedido(pedido)

   #1. Inserção - Criar novo pedido
print("=== 1. Inserção ===")
pedido_novo = Pedido(cliente="Luciana Cunha")

# Criar itens com categoria
item1 = ItemPedido("Notebook Dell", 1, 2800.00, "Eletrônicos")
item2 = ItemPedido("Mouse Logitech", 1, 85.00, "Periféricos")
item3 = ItemPedido("Cabo HDMI", 2, 25.00, "Cabos")

pedido_novo.add_item(item1)
pedido_novo.add_item(item2)
pedido_novo.add_item(item3)

control.salvar_pedido(pedido_novo)
print(f"Pedido {pedido_novo.id} inserido com sucesso!")

#2. Listagem - Mostrar todos os pedidos
print("\n=== 2. LISTAGEM ===")
pedidos = control.listar_pedidos_com_itens()
for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Qtd: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")
        print()

    # 3. ATUALIZAÇÃO - Modificar cliente do último pedido inserido
print("=== 3. ATUALIZAÇÃO ===")
if pedido_novo.id:
        pedido_novo.cliente = "Maria Silva Santos"
        control.atualizar_pedido(pedido_novo)
        print(f"Pedido {pedido_novo.id} atualizado!")
        
        # Mostrar resultado da atualização
        pedidos = control.listar_pedidos_com_itens()
        for p in pedidos:
            if p.id == pedido_novo.id:
                print(f"Pedido atualizado: {p.id} - Cliente: {p.cliente}")
    
    # 4. DELEÇÃO - Remover o pedido criado
print("\n=== 4. DELEÇÃO ===")
if pedido_novo.id:
        control.deletar_pedido(pedido_novo.id)
        print(f"Pedido {pedido_novo.id} deletado!")
        
        # Confirmar deleção
        pedidos = control.listar_pedidos_com_itens()
        print("Pedidos restantes:")
        if not pedidos:
            print("Nenhum pedido encontrado.")
        else:
            for p in pedidos:
                print(f"Pedido {p.id} - Cliente: {p.cliente}")
    
db.close()


 
