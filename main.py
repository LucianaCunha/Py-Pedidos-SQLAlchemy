from models import Base, Pedido, ItemPedido
from database import engine
from control import PedidoControl

# Criar tabelas no banco, se não existirem
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    control = PedidoControl()
    
    try:
        # 1. INSERÇÃO
        print("=== 1. INSERÇÃO ===")
        # Criar pedido (REMOVIDO parâmetro data_pedido)
        pedido_novo = Pedido(cliente="João Santos")
        
        # Criar itens (ADICIONADO parâmetro categoria)
        item1 = ItemPedido(
            produto="Smartphone Samsung",
            quantidade=1,
            preco=1200.00,
            categoria="Eletrônicos"  # ADICIONADO
        )
        
        item2 = ItemPedido(
            produto="Capa Protetora",
            quantidade=1,
            preco=45.00,
            categoria="Acessórios"  # ADICIONADO
        )
        
        item3 = ItemPedido(
            produto="Carregador USB-C",
            quantidade=2,
            preco=35.00,
            categoria="Cabos"  # ADICIONADO
        )
        
        # Adicionar itens ao pedido
        pedido_novo.itens.extend([item1, item2, item3])
        
        # Salvar pedido
        pedido_salvo = control.salvar_pedido(pedido_novo)
        print(f"Pedido {pedido_salvo.id} inserido com sucesso!")
        
        # 2. LISTAGEM
        print("\n=== 2. LISTAGEM ===")
        pedidos = control.listar_pedidos_com_itens()
        for pedido in pedidos:
            print(f"Pedido {pedido.id} - Cliente: {pedido.cliente}")
            for item in pedido.itens:
                # ADICIONADO exibição da categoria
                print(f"  Produto: {item.produto}, Qtd: {item.quantidade}, "
                      f"Preço: R$ {item.preco}, Categoria: {item.categoria}")
            print()
        
        # 3. ATUALIZAÇÃO
        print("=== 3. ATUALIZAÇÃO ===")
        if pedido_salvo.id:
            # REMOVIDO parâmetro nova_data
            pedido_atualizado = control.atualizar_pedido(
                pedido_salvo.id,
                novo_cliente="João Santos Silva"
            )
            print(f"Pedido {pedido_atualizado.id} atualizado!")
            print(f"Novo cliente: {pedido_atualizado.cliente}")
        
        # 4. DELEÇÃO
        print("\n=== 4. DELEÇÃO ===")
        if pedido_salvo.id:
            control.deletar_pedido(pedido_salvo.id)
            print(f"Pedido {pedido_salvo.id} deletado!")
            
            # Confirmar deleção
            pedidos_restantes = control.listar_pedidos_com_itens()
            print("Pedidos restantes:")
            if not pedidos_restantes:
                print("Nenhum pedido encontrado.")
            else:
                for pedido in pedidos_restantes:
                    print(f"Pedido {pedido.id} - Cliente: {pedido.cliente}")
    
    except Exception as e:
        print(f"Erro durante execução: {e}")
    
    finally:
        control.fechar()


