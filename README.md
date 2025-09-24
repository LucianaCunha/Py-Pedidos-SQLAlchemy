# Py-Pedidos-SQLAlchemy
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/LucianaCunha/Py-Pedidos-SQLAlchemy/blob/main/LICENSE)
[![MySQL Connector](https://img.shields.io/badge/Connector-MySQL-blue.svg)](https://pypi.org/project/mysql-connector-python/)
[![ORM: SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-darkgreen.svg)](https://www.sqlalchemy.org/)

## 📝 Descrição do Projeto

Este projeto é uma aplicação Python para gerenciamento de pedidos que utiliza o SQLAlchemy, um poderoso ORM (Object-Relational Mapper), para interagir com um banco de dados MySQL. Ele demonstra como mapear classes Python para tabelas de banco de dados e realizar operações CRUD de forma orientada a objetos, abstraindo a complexidade das queries SQL diretas.

## ✨ Funcionalidades
- **Mapeamento ORM:** Define modelos Python (Pedido, ItemPedido) que representam as tabelas do banco de dados.
- **Criação Automática de Tabelas:** O SQLAlchemy pode criar as tabelas no banco de dados com base nos modelos definidos.
- **Criação de Pedidos:** Adiciona novos pedidos com informações do cliente e seus itens associados.
- **Listagem de Pedidos:** Recupera e exibe todos os pedidos e seus respectivos itens através de relacionamentos ORM.
- **Atualização de Pedidos:** Modifica informações de pedidos existentes.
- **Exclusão de Pedidos:** Remove pedidos e todos os seus itens relacionados de forma transparente via ORM.
  
## 🚀 Tecnologias Utilizadas
- **Python 3.x:** Linguagem de programação principal.
- **MySQL:** Sistema de gerenciamento de banco de dados relacional.
- **SQLAlchemy:** Toolkit SQL e Object-Relational Mapper.
- **PyMySQL:** Driver MySQL para Python, utilizado pelo SQLAlchemy para conexão.
  
## 📦 Estrutura do Projeto
- database.py: Configura a conexão com o banco de dados MySQL e a sessão do SQLAlchemy.
- models.py: Define as classes de modelo (Pedido, ItemPedido) e seus mapeamentos para as tabelas do banco de dados.
- control.py: Contém a lógica de negócio para realizar as operações CRUD, utilizando a sessão do SQLAlchemy.
- main.py: Ponto de entrada da aplicação, onde as operações de teste são executadas e as tabelas são criadas automaticamente.

## ⚙️ Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

- **1. Clonar o Repositório**
```Bash
git clone https://github.com/seu-usuario/Py-Pedidos-SQLAlchemy.git
cd Py-Pedidos-SQLAlchemy
```

- **2. Instalar Dependências Python**

Certifique-se de ter o pip instalado e execute:

```Bash

pip install SQLAlchemy pymysql
````

- **3. Configurar o Banco de Dados MySQL**
  
 **1. Crie o Banco de Dados (Opcional):** Você pode criar o banco de dados db_pedidos manualmente no MySQL. O SQLAlchemy criará as tabelas pedido e item_pedido automaticamente na primeira execução do main.py.
  
```Sql

    CREATE DATABASE IF NOT EXISTS db_pedidos;
```

  **2. Atualizar Credenciais:** Edite o arquivo database.py (ou onde a DATABASE_URL é definida) com suas credenciais de conexão MySQL.

```Python

    # Exemplo de database.py
    # ...
    # Formato: "mysql+pymysql://USUARIO:SENHA@HOST/NOME_DO_BANCO"
    DATABASE_URL = "mysql+pymysql://root:@localhost/db_pedidos" 
    # Altere 'root' e '' (senha) conforme seu setup. Se tiver senha, adicione-a.
    # Ex: "mysql+pymysql://root:minhasenha@localhost/db_pedidos"
    # ...
```
 - **4. Executar o Projeto**

Para testar as operações CRUD, execute o arquivo main.py:
```Bash

python main.py
```

Ao executar main.py, o SQLAlchemy criará as tabelas pedido e item_pedido no banco de dados db_pedidos (se elas não existirem) e, em seguida, realizará uma inserção, uma listagem, uma atualização e uma deleção, imprimindo os resultados no console.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
