# Importa os tipos de dados e base para os modelos
from sqlalchemy import Column, Integer, String, Date, Numeric, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Cria a base para os modelos (é tipo a herança que todas as tabelas vão usar)
Base = declarative_base()

# Tabela de categorias de produtos
class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'northwind'}  # Usa o schema 'northwind'
    category_id = Column('categoryid', Integer, primary_key=True)  # ID único da categoria
    category_name = Column('categoryname', String(50))  # Nome da categoria
    description = Column('description', String(100))  # Descrição da categoria

# Tabela de clientes
class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'northwind'}
    customer_id = Column('customerid', String(5), primary_key=True)  # ID do cliente
    company_name = Column('companyname', String(50))  # Nome da empresa
    contact_name = Column('contactname', String(30))  # Nome da pessoa de contato
    contact_title = Column('contacttitle', String(30))  # Cargo da pessoa de contato
    address = Column('address', String(50))  # Endereço do cliente
    city = Column('city', String(20))  # Cidade
    region = Column('region', String(15))  # Região/estado
    postal_code = Column('postalcode', String(9))  # CEP
    country = Column('country', String(15))  # País
    phone = Column('phone', String(17))  # Telefone
    fax = Column('fax', String(17))  # Fax

# Tabela de funcionários (vendedores)
class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'northwind'}
    employee_id = Column('employeeid', Integer, primary_key=True)  # ID do funcionário
    last_name = Column('lastname', String(10))  # Sobrenome
    first_name = Column('firstname', String(10))  # Nome
    title = Column('title', String(25))  # Cargo
    title_of_courtesy = Column('titleofcourtesy', String(5))  # Tratamento (Sr., Sra., etc.)
    birth_date = Column('birthdate', Date)  # Data de nascimento
    hire_date = Column('hiredate', Date)  # Data de contratação
    address = Column('address', String(50))  # Endereço
    city = Column('city', String(20))  # Cidade
    region = Column('region', String(2))  # Região
    postal_code = Column('postalcode', String(9))  # CEP
    country = Column('country', String(15))  # País
    home_phone = Column('homephone', String(14))  # Telefone residencial
    extension = Column('extension', String(4))  # Ramal
    reports_to = Column('reportsto', Integer)  # ID do chefe direto
    notes = Column('notes', Text)  # Observações

# Tabela de produtos
class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'northwind'}
    product_id = Column('productid', Integer, primary_key=True)  # ID do produto
    product_name = Column('productname', String(35))  # Nome do produto
    supplier_id = Column('supplierid', Integer)  # ID do fornecedor
    category_id = Column('categoryid', Integer)  # ID da categoria
    quantity_per_unit = Column('quantityperunit', String(20))  # Quantidade por unidade
    unit_price = Column('unitprice', Numeric(13, 4))  # Preço unitário
    units_in_stock = Column('unitsinstock', Integer)  # Quantidade em estoque
    units_on_order = Column('unitsonorder', Integer)  # Quantidade em pedido
    reorder_level = Column('reorderlevel', Integer)  # Nível de reposição
    discontinued = Column('discontinued', String(1))  # Produto descontinuado? (S/N)

# Tabela de pedidos
class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}
    order_id = Column('orderid', Integer, primary_key=True)  # ID do pedido
    customer_id = Column('customerid', String(5), ForeignKey('northwind.customers.customerid'))  # FK para o cliente
    employee_id = Column('employeeid', Integer, ForeignKey('northwind.employees.employeeid'))  # FK para o funcionário (vendedor)
    order_date = Column('orderdate', Date)  # Data do pedido
    required_date = Column('requireddate', Date)  # Data requerida
    shipped_date = Column('shippeddate', Date)  # Data de envio
    freight = Column('freight', Numeric(15, 4))  # Valor do frete
    ship_name = Column('shipname', String(35))  # Nome do destinatário
    ship_address = Column('shipaddress', String(50))  # Endereço de entrega
    ship_city = Column('shipcity', String(15))  # Cidade de entrega
    ship_region = Column('shipregion', String(15))  # Região de entrega
    ship_postal_code = Column('shippostalcode', String(9))  # CEP de entrega
    ship_country = Column('shipcountry', String(15))  # País de entrega
    shipper_id = Column('shipperid', Integer)  # ID da transportadora

    # Relacionamentos
    customer = relationship("Customer")
    employee = relationship("Employee")
    order_details = relationship("OrderDetail", backref="order")

# Tabela de detalhes de pedidos
class OrderDetail(Base):
    __tablename__ = 'order_details'
    __table_args__ = {'schema': 'northwind'}
    order_id = Column('orderid', Integer, ForeignKey('northwind.orders.orderid'), primary_key=True)  # FK para o pedido
    product_id = Column('productid', Integer, ForeignKey('northwind.products.productid'), primary_key=True)  # FK para o produto
    unit_price = Column('unitprice', Numeric(13, 4))  # Preço do item
    quantity = Column('quantity', Integer)  # Quantidade comprada
    discount = Column('discount', Numeric(10, 4))  # Desconto aplicado

    # Relacionamentos
    product = relationship("Product")

# Tabela de transportadoras
class Shipper(Base):
    __tablename__ = 'shippers'
    __table_args__ = {'schema': 'northwind'}
    shipper_id = Column('shipperid', Integer, primary_key=True)  # ID da transportadora
    company_name = Column('companyname', String(20))  # Nome da transportadora
    phone = Column('phone', String(14))  # Telefone de contato

# Tabela de fornecedores
class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column('supplierid', Integer, primary_key=True)  # ID do fornecedor
    company_name = Column('companyname', String(50))  # Nome da empresa fornecedora
    contact_name = Column('contactname', String(30))  # Nome do contato
    contact_title = Column('contacttitle', String(30))  # Cargo do contato
    address = Column('address', String(50))  # Endereço
    city = Column('city', String(20))  # Cidade
    region = Column('region', String(15))  # Região
    postal_code = Column('postalcode', String(8))  # CEP
    country = Column('country', String(15))  # País
    phone = Column('phone', String(15))  # Telefone
    fax = Column('fax', String(15))  # Fax
    homepage = Column('homepage', String(100))  # Site do fornecedor