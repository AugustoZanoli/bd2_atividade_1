from implementacao_psycopg.db.connect import connect

class PedidoDAO:
    def inserirPedido(self, nomeCliente, nomeVendedor, dataPedido, itens):
        conn = connect()
        cur = conn.cursor()

        try:
            cur.execute("SELECT customerid FROM northwind.customers WHERE contactname = %s", (nomeCliente,))
            cliente = cur.fetchone()

            cur.execute("SELECT employeeid FROM northwind.employees WHERE firstname || ' ' || lastname = %s", (nomeVendedor,))
            vendedor = cur.fetchone()

            if not cliente or not vendedor:
                print("Cliente ou vendedor não encontrado.")
                return
            
            # Adicionei aqui a busca pra buscar o orderid, pra não precisar mexer no banco
            cur.execute("SELECT COALESCE(MAX(orderid), 0) + 1 FROM northwind.orders")
            orderId = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate)
                VALUES (%s, %s, %s, %s)
                RETURNING orderid
            """, (orderId, cliente[0], vendedor[0], dataPedido))
            order_id = cur.fetchone()[0]
            print("Pedido criado com ID:", order_id)

            for i, item in enumerate(itens, start=1):
                print(f"Inserindo item #{i}: {item}")
                cur.execute("""
                    INSERT INTO northwind.order_details (orderid, productid, unitprice, quantity, discount)
                    VALUES (%s, %s, %s, %s, %s)
                """, (order_id, item["productid"], item["unitprice"], item["quantity"], 0))

            conn.commit()
            print("Commit feito com sucesso! Pedido inserido.")

        except Exception as e:
            conn.rollback()
            print("ERRO:")
            print(repr(e)) 
            raise

        finally:
            cur.close()
            conn.close()
            print("Conexão encerrada.")