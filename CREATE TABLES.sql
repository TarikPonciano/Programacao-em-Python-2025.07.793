CREATE DATABASE "Ecommerce";

CREATE TABLE IF NOT EXISTS categorias(
id_categoria integer GENERATED ALWAYS AS IDENTITY 
PRIMARY KEY,
nome_categoria varchar(255) NOT NULL
);

CREATE TABLE produtos(
id_produto integer GENERATED ALWAYS AS IDENTITY PRIMARY
KEY,
nome_produto varchar(255) NOT NULL,
preco_produto NUMERIC(7,2) NOT NULL DEFAULT 0.00,
estoque_produto integer NOT NULL DEFAULT 0,
categoria_id integer NOT NULL,
CONSTRAINT fk_produto_categoria FOREIGN KEY (categoria_id)
REFERENCES categorias (id_categoria)
);

CREATE TABLE clientes(
id_cliente integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_cliente varchar(255) NOT NULL
);

CREATE TABLE pedidos(
id_pedido integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cliente_id integer NOT NULL,
data_pedido date DEFAULT current_date,
CONSTRAINT fk_pedido_cliente FOREIGN KEY (cliente_id) REFERENCES
clientes(id_cliente)
);

CREATE TABLE itens(
id_item integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
produto_id integer NOT NULL,
pedido_id integer NOT NULL,
quantidade_item integer NOT NULL DEFAULT 1,
preco_item NUMERIC(7,2) NOT NULL DEFAULT 0.00,
CONSTRAINT fk_item_produto FOREIGN KEY (produto_id) REFERENCES
produtos(id_produto),
CONSTRAINT fk_item_pedido FOREIGN KEY (pedido_id) REFERENCES
pedidos(id_pedido)
);

