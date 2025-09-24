CREATE DATABASE db_pedidos;
use db_pedidos;

CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100)
    -- Removi data_pedido
    
);

CREATE TABLE item_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    produto VARCHAR(100),
    quantidade INT,
    preco DECIMAL(10,2),
    categoria varchar(100), --Adicionei categoria
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);

-- Remover coluna data_pedido da tabela pedido
alter table pedido drop column data_pedido;

-- Adicionar coluna categoria na tabela item_pedido
alter table item_pedido add column categoria varchar (100);