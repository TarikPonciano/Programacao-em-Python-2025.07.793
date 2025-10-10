SELECT * FROM produtos
WHERE estoque_produto <= 50;

SELECT * FROM pedidos
WHERE id_pedido = 1;

SELECT * FROM clientes
WHERE id_cliente = 1;

SELECT * FROM pedidos
INNER JOIN clientes ON cliente_id = id_cliente
WHERE id_pedido = 1;

SELECT id_pedido, cliente_id, data_pedido,SUM(preco_item * quantidade_item) as "Total" FROM pedidos
INNER JOIN itens ON pedido_id = id_pedido
WHERE id_pedido = 1
GROUP BY id_pedido;