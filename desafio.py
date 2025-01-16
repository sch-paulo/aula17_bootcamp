# Desafio Intermediário de SQLAlchemy: Tabelas de Produto e Fornecedor
# Este desafio focará na criação de duas tabelas relacionadas, Produto e Fornecedor, 
# utilizando SQLAlchemy. Cada produto terá um fornecedor associado, demonstrando o 
# uso de chaves estrangeiras para estabelecer relações entre tabelas. Além disso, 
# você realizará inserções nessas tabelas para praticar a manipulação de dados.

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///desafio.db')

metadata_obj = MetaData()

produto = Table(
    'produtos',
    metadata_obj,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('preco', Float, nullable=False),
    Column('descricao', String(100)),
    Column('fornecedor_id', Integer, ForeignKey('fornecedores.id'))
)

fornecedor = Table(
    'fornecedores',
    metadata_obj,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome', String(100))
)

metadata_obj.create_all(engine)

itens_insercao = {
    "fornecedores": [
        {"nome": "Fornecedor A"},
        {"nome": "Fornecedor B"},
        {"nome": "Fornecedor C"},
        {"nome": "Fornecedor D"},
        {"nome": "Fornecedor E"}
    ],
    "produtos": [
        {"preco": 25.99, "descricao": "Produto 1", "fornecedor_id": 1},
        {"preco": 15.50, "descricao": "Produto 2", "fornecedor_id": 2},
        {"preco": 42.75, "descricao": "Produto 3", "fornecedor_id": 3},
        {"preco": 8.99, "descricao": "Produto 4", "fornecedor_id": 4},
        {"preco": 19.99, "descricao": "Produto 5", "fornecedor_id": 5},
        {"preco": 33.49, "descricao": "Produto 6", "fornecedor_id": 1},
        {"preco": 12.00, "descricao": "Produto 7", "fornecedor_id": 2},
        {"preco": 27.30, "descricao": "Produto 8", "fornecedor_id": 3},
        {"preco": 6.89, "descricao": "Produto 9", "fornecedor_id": 4},
        { "preco": 50.00, "descricao": "Produto 10", "fornecedor_id": 5}
    ]
}

Session = sessionmaker(bind=engine)

with Session() as session:
    session.execute(
        fornecedor.insert(),
        itens_insercao['fornecedores']
    )
    session.execute(
        produto.insert(),
        itens_insercao['produtos']
    )
    session.commit()