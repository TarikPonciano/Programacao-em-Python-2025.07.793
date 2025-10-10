INSERT INTO categorias (nome_categoria)
VALUES ('Alimentos'), ('Eletrônico'), ('Limpeza');

INSERT INTO produtos
VALUES (default, 'Banana', 1.99, 200, 1),
(default, 'Maçã', 2.99, 100, 1),
(default, 'Mouse de Computador', 10.99, 50, 2),
(default, 'Detergente 500ml', 2.19, 100, 3),
(default, 'Água Sanitária Dragão Verde', 3.50, 50, 3);

INSERT INTO clientes (nome_cliente)
VALUES('Marquinhos'), ('Josefina');

INSERT INTO pedidos
VALUES (default, 1, default);

INSERT INTO itens
VALUES (default, 2, 1, 10, 1.99), (default, 4, 1, 1, 10.99);

--Visualizando as informações
SELECT * FROM pedidos;
SELECT nome_produto, quantidade_item, preco_item, quantidade_item*preco_item FROM itens 
INNER JOIN produtos ON id_produto = produto_id
WHERE pedido_id =1;