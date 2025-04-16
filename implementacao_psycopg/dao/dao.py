from implementacao_psycopg.db.connect import connect

class PedidoDAO:

    # SQL Injection, passando os parametros direto na query
    def inserirPedidoInjection(self, nomeCliente, nomeVendedor, dataPedido, itens):
        conn = connect()
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        try:
            queryCliente = f"SELECT customerid FROM northwind.customers WHERE contactname = '{nomeCliente}'"

            cur.execute(queryCliente)
            cliente = cur.fetchone()

            queryVendedor = f"SELECT employeeid FROM northwind.employees WHERE firstname || ' ' || lastname = '{nomeVendedor}'"
            cur.execute(queryVendedor)
            vendedor = cur.fetchone()

            if not cliente or not vendedor:
                print("Cliente ou vendedor não encontrado.")
                return

            cur.execute("SELECT COALESCE(MAX(orderid), 0) + 1 FROM northwind.orders")
            orderId = cur.fetchone()[0]

            print("Pedido criado com ID:", orderId)

            queryParaInserir = f"""
                INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate)
                VALUES ({orderId}, '{cliente[0]}', {vendedor[0]}, '{dataPedido}')
            """
            cur.execute(queryParaInserir)

            for item in itens:
                print(f"Inserindo item: {item}")
                insert_item_query = f"""
                    INSERT INTO northwind.order_details (orderid, productid, unitprice, quantity, discount)
                    VALUES ({orderId}, {item['productid']}, {item['unitprice']}, {item['quantity']}, 0)
                """
                cur.execute(insert_item_query)

            print("Pedido e itens inseridos com sucesso (autocommit ativo).")

        except Exception as e:
            print("Erro ao inserir pedido (nenhum rollback pois autocommit está ativado):", e)

        finally:
            cur.close()
            conn.close()
            print("Conexão encerrada.")

    # Passando os parametros sem utilizar injection
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
            orderIdFetch = cur.fetchone()[0]
            print("Pedido criado com ID:", orderIdFetch)

            for item in itens:
                print(f"Inserindo item: {item}")
                cur.execute("""
                    INSERT INTO northwind.order_details (orderid, productid, unitprice, quantity, discount)
                    VALUES (%s, %s, %s, %s, %s)
                """, (orderIdFetch, item["productid"], item["unitprice"], item["quantity"], 0))

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