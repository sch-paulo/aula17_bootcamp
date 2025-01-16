from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo=True)

print('Conexão com SQLite estabelecida.')

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# novo_usuario = Usuario(nome='João', idade=28)
# session.add(novo_usuario)
# session.commit()

# print('Usuário adicionado com sucesso')

usuario = session.query(Usuario).filter_by(nome='João').first()
print(f'Usuário encontrado: {usuario.nome}. Idade: {usuario.idade}')

# Gerenciador de contexto. Sem with:
try:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

# O with cuida de todos esses processos, de abertura e fechamento de sessão e rollback
# Com with:

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)

