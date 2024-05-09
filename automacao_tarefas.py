# 01 -Abrir o Chrome
# 02 - Entrar no Site Sitema
# 03 - Inserir usuario e senha
# 04 - cadastrar produto

import pyautogui as pa
import pandas as pd
import time

pa.PAUSE = 2


# Variaveis

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# IMPORTANDO A TABELA PRODUTOS
tabela = pd.read_csv("produtos.csv") 

# 01

pa.press("Win")
pa.write("Chrome")
pa.press("Enter")

# 02
pa.position(x=395, y=63)
pa.doubleClick()
pa.write(site)
pa.press("Enter")

# 03 

time.sleep(4)
pa.click(x=738, y=403)
# Usuário
pa.write("teste")
pa.press("Tab")
#senha
pa.write("xicara")
pa.press("Tab")
pa.press("Enter")

# 04

#for linha in tabela.index:

pa.click(x=973, y=296)
    # Codigo
pa.write(str((tabela.loc["codigo"])))
Pa.press("Tab")
    # Marca
pa.write(str((tabela.loc["marca"])))
pa.press("Tab")
    # Tipo
pa.write(str((tabela.loc["tipo"])))
pa.press("Tab")
    # Categoria
pa.write(str((tabela.loc["categoria"])))
pa.press("Tab")
    # Preco Unitario
pa.write(str((tabela.loc["preco_unitario"])))
pa.press("Tab")
    # Custo
pa.write(str((tabela.loc["custo"])))
pa.press("Tab")
    # Obs
obs = str((tabela.loc["obs"]))
if obs != "nan":
    pa.write(obs)
pa.press("Tab")
pa.press("Enter")
pa.scroll(5000)
