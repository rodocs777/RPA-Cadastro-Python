# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# site tal

import time
import pyautogui
import pandas as pd

# pyautogui.write
# pyautogui.press
# pyautogui.click
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3
# abrir navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
# selecionar convidado do chrome
pyautogui.click(x=305, y=911)
# maximizar
pyautogui.hotkey('win', 'up')
# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=935, y=546)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")  # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=962, y=793)  # clique no botao de login
time.sleep(3)
# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")
print(tabela)
# Passo 4: Cadastrar um produto
for linha in tabela.index:
  pyautogui.PAUSE = 0.1
  # clicar no campo de código
  pyautogui.click(x=745, y=362)
  # pegar da tabela o valor que quero preencher
  codigo = tabela.loc[linha, "codigo"]
  # preencher campo
  pyautogui.write(str(codigo))
  # passar para o próximo campo
  pyautogui.press("tab")
  # preencher campo
  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  obs = tabela.loc[linha, "obs"]
  if not pd.isna(obs):
      pyautogui.write(str(tabela.loc[linha, "obs"]))
  pyautogui.press("tab")
  pyautogui.press("enter") # cadastra o produto
  pyautogui.scroll(5000)
  # Passo 5: Repetir o processo de cadastro até o fim