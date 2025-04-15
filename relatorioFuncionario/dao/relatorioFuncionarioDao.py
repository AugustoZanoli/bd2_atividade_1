from implementacao_psycopg.db.connect import connect

class RankingFuncionarioDAO:
    def buscarRanking(self, data_inicio, data_fim):
        conn = connect()
        cur = conn.cursor()
        try:
            
            # Query pra buscar os dados solicitados na atividade
            cur.execute("""
                SELECT 
                    e.firstname || ' ' || e.lastname AS nome_funcionario,
                    COUNT(DISTINCT o.orderid) AS total_pedidos,
                    SUM(od.unitprice * od.quantity * (1 - od.discount)) AS total_vendido
                FROM northwind.orders o
                JOIN northwind.employees e ON o.employeeid = e.employeeid
                JOIN northwind.order_details od ON o.orderid = od.orderid
                WHERE o.orderdate BETWEEN %s AND %s
                GROUP BY nome_funcionario
                ORDER BY total_vendido DESC
            """, (data_inicio, data_fim))
            
            return cur.fetchall()

        except Exception as e:
            print("Erro ao buscar ranking:", repr(e))
            return []
        finally:
            cur.close()
            conn.close()
