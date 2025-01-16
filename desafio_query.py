from sqlalchemy import create_engine, select, func
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

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

with Session(engine) as session:

    stmt = select(fornecedor.c.nome, 
                  func.sum(produto.c.preco)).join(
                      fornecedor, produto.c.fornecedor_id == fornecedor.c.id
                  ).group_by(fornecedor.c.nome)

    result = session.execute(stmt)

    for row in result:
        print(row)