# 📚 Pratica Conexão com Banco de Dados

Este projeto tem como objetivo integrar Python com um banco de dados PostgreSQL, explorando conceitos como conexão direta via `psycopg`, segurança contra SQL Injection, uso de ORM com SQLAlchemy e geração de relatórios a partir de dados reais.

---

## 🚀 **Recursos principais**
- Conexão com banco de dados via `psycopg`.
- Simulação de SQL Injection (modo vulnerável e modo seguro).
- Versão alternativa usando ORM com SQLAlchemy.
- Implementação dos padrões MVC + DAO.
- Relatórios detalhados com dados do banco Northwind.

---

## 🛠️ **Funcionalidades**

### 1. Inserção de Pedidos
O sistema permite o cadastro de novos pedidos com:
- Nome do cliente
- Nome do vendedor
- Data do pedido
- Lista de produtos com quantidade e preço unitário

### 2. Modos de Conexão
- **Modo Driver (`psycopg`)**: utiliza queries SQL puras.
- **Modo ORM (`SQLAlchemy`)**: utiliza classes Python para abstrair o banco.

### 3. Segurança
- **SQL Injection**: o sistema possui dois modos de backend para inserção de dados:
  - Um modo propositalmente vulnerável para simular ataques.
  - Um modo seguro que usa queries parametrizadas.

### 4. Relatórios
- **Relatório de Pedido**:
  - Número e data do pedido
  - Nome do cliente e do vendedor
  - Lista de itens (produto, quantidade, preço)
- **Ranking de Funcionários**:
  - Nome do funcionário
  - Total de pedidos realizados
  - Soma dos valores vendidos

---

## 📦 **Estrutura do Projeto**

```
implementacao_psycopg/
  |- controller/
  |- dao/
  |- db/
  |- models/
  |- view/
  |- questionario.py

relatorioFuncionario/
  |- controller/
  |- dao/
  |- view/

relatorioPedido/
  |- controller/
  |- dao/
  |- view/

orm_sqlalchemy/
  |- implementacao_orm/
    |- controller/
    |- dao/
    |- db/
    |- models/
    |- view/
  |- questionario.py
```

---

## 📋 **Como executar?**

1. Crie e configure o banco de dados Northwind no PostgreSQL.
2. Execute o script de criação de chaves estrangeiras, se necessário.
3. Certifique-se de que o arquivo `connect.py` tenha as credenciais corretas.
4. Execute o projeto com:

```bash
python main.py
```


---

## ✅ **Checklist da Entrega**

- [x] Inserção de pedido com `psycopg`
- [x] Simulação de SQL Injection (modo vulnerável e seguro)
- [x] Implementação com `SQLAlchemy`
- [x] Relatório de pedido
- [x] Relatório de ranking de funcionários
- [x] Documento com nomes dos integrantes, link do repositório e vídeo

---

## 👥 **Integrantes do Grupo**
- Augusto de Camargos Zanoli
- Lucas Silva Pinheiro

