import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.sql import functions


engine = db.create_engine("mysql+pymysql://root@localhost:3306/frigobar")
Base = declarative_base()

class Frigobar(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    quantidade = Column(Numeric)
    preco = Column(Numeric(6,2))

Base.metadata.create_all(engine)

i1 = Frigobar(nome = "agua", quantidade = 2.00, preco= 4.00)
i2 = Frigobar(nome = "refrigerante", quantidade = 2.00, preco=5.00)
i3 = Frigobar(nome = "cerveja", quantidade = 2.00, preco= 10.00)
i4 = Frigobar(nome = "amendoim", quantidade = 2.00, preco=4.50)

Session = sessionmaker(bind=engine)
session = Session()

#session.add_all([i1, i2, i3, i4])
#session.commit()

print("MENU DE OPÇÕES:\n"
      "- Digite 1 para consumo\n"
      "- Digite 2 para alterar\n"
      "- Digite 3 para deletar\n"
      "- Digite 4 para inserir\n")

opcao = int(input("Informe a opção desejada: "))


def consumo():
    item = session.query(Frigobar).all()
    for itens in item:
        print(itens.id,itens.nome)
    itens_cons_nome = []
    itens_cons_preco = []
    conta = {}
    op = 0
    while True:
        if op == 0:
            consumo = int(input('digite o ID do produto consumido: '))
            impressao_consumo = session.query(Frigobar).filter(Frigobar.id == consumo).first()
            itens_cons_nome.append(impressao_consumo.nome)
            itens_cons_preco.append(impressao_consumo.preco)
            resposta = input('deseja continuar [Y] sim\n [N] não: ').upper()
            if resposta == 'Y':
                op = 0
            elif resposta == 'N':
                op = 1
        elif op == 1:
            conta['itens_cons_nome']= [itens_cons_preco]
            print(conta)
            break

    

def alterar():
    consumo()
    id_item = int(input('Digite qual item foi reposto: '))
    itens = session.query(Frigobar).filter(Frigobar.id == id_item).one()
    Quantidade = int(input('informe a quantidade de itens repostos: '))
    itens.quantidade = Quantidade
    session.add(itens)
    session.commit()

def deletar():
    produtos = session.query(Frigobar).filter(Frigobar.id == 4).one()
    session.delete(produtos)
    session.commit()

def inserir():
    N_produto =input('digite o nome')
    preco = int(input('digite o preço'))
    new_produto = Frigobar(nome=N_produto, preco=preco)
    session.add(new_produto)
    session.commit()


if opcao == 1:
    print("Você quer consultar.")
    consumo()
elif opcao == 2:
    print("Você quer alterar.")
    alterar()
elif opcao == 3:
    print("Você quer deletar.")
    deletar()
elif opcao == 4:
    print("Você quer inserir.")
    inserir()