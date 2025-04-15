from implementacao_psycopg.db.connect import connect

class RelatorioPedidoDAO:
    def buscarPedido(self, orderId):
        conn = connect()
        cur = conn.cursor()
        try:
            # Buscando os dados da atividade nas tabelas orders, customers e employees (Dados da venda)
            cur.execute("""
                SELECT 
                    o.orderid,
                    o.orderdate,
                    c.companyname AS nome_cliente,
                    e.firstname || ' ' || e.lastname AS nome_vendedor
                FROM northwind.orders o
                JOIN northwind.customers c ON o.customerid = c.customerid
                JOIN northwind.employees e ON o.employeeid = e.employeeid
                WHERE o.orderid = %s
            """, (orderId,))
            pedido = cur.fetchone()

            if not pedido:
                return None

            # Buscando o resto dos dados da atividade nas tabelas order_details, e products (Itens)
            cur.execute("""
                SELECT 
                    p.productname,
                    od.quantity,
                    od.unitprice
                FROM northwind.order_details od
                JOIN northwind.products p ON od.productid = p.productid
                WHERE od.orderid = %s
            """, (orderId,))
            itens = cur.fetchall()

            return {
                "orderid": pedido[0],
                "orderdate": pedido[1],
                "cliente": pedido[2],
                "vendedor": pedido[3],
                "itens": [{"produto": i[0], "quantidade": i[1], "preco": i[2]} for i in itens]
            }

        except Exception as e:
            print("Erro ao buscar pedido:", repr(e))
            return None
        finally:
            cur.close()
            conn.close()
