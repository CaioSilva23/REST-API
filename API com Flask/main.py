from flask import Flask
import pandas as pd

app = Flask(__name__)  # cria o site
tabela = pd.read_excel("Vendas - Dez.xlsx")  # importa a tabela do excel(banco de dados)


@app.route("/")  # decorator -> diz em qual link a função vai rodar
def faturamento():  # função
    fat = float(tabela['Valor Final'].sum())  # soma a coluna valor final
    return {'Faturamento': fat}


@app.route("/vendas/produtos")
def vendas_produtos():
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()  # agrupa a tabela produtos e
    # soma a tabela valor final
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()  # transforma a a variavel tabela_vendas_produtos(tabela)
    # em um dicionário e atribue a dic_vendas_produtos para ser retornado na funcao vendas_produtos
    return dic_vendas_produtos


@app.route("/vendas/produtos/<produto>")
def fat_produto(produto):
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    if produto in tabela_vendas_produtos.index:  # verifica se o produto está no indice ta tabela_vendas_produtos
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    else:
        return {produto: "Inexistente"}


app.run()
