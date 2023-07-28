RPA - Robotic Process Automation

Introdução:

Programa para automatização de processos repetitivos que faríamos manualmente.

Sendo o computador clicando e digitando por nós, por meio de um Script programado previamente para isso.

O código foi criado com Python, no Windows.

---

Objetivo do programa:

Entrar em um site (site criado especialmente para esse projeto), fazer seu login
e fazer o cadastro de todos os produtos de forma automática.

---

Conteúdo do projeto:

1 - app.exe --> o programa já compilado em linguaem de máquina para ser executado.

2 - codigo.py --> o código criado em Python com descrição técnica do que foi feito e devidamente formatado no meu computador e sistema operacional Windows.

3 - produtos.csv --> a base de dados que o programa irá inserir no site que o mesmo está automatizado para abrir, logar e inserir os dados automaticamente.

4 - auxiliar_posição.py --> comando para quem quiser criar seu código a partir do meu, personalizado para o seu computador. E ver a posição do mouse.

5 - auxiliar_scroll.py --> comando para quem quiser criar seu código a partir do meu, personalizado para o seu computador. E subir ou descer o scroll da tela.

6 - vídeoapresentação.mp4 - apresentação exclusivamente do projeto
ou via Youtube (https://www.youtube.com/watch?v=4PA9ha6WC4k&ab_channel=RodolfoFM)

---

Requisitos:

1 - O App.exe só pode ser executado devidamente se estiver com a base de dados na mesma pasta que ele estiver também.

2 - O App.exe foi criado de acordo com meu codigo.py, que foi feito no meu computador, com minha configurações padrões de Windows 10,
e nas dimensões do meu monitor.

Outro computador que não tiver as dimensões ou configurações exatas do meu, irá quebrar o código, pois se trata de um RPA,
que simula a interação humana com a máquina, automatizando o local de cada click de mouse.

3 - Para quem quiser reproduzir o código como o meu, precisa primeiramente testar. Se o app.exe der problema, precisa recompilar o código
do seu computador, tento o Python instalado.

Para isso ensinarei como executar o programa a seguir.

---

Instalando a biblioteca do Pyautogui:

Para fazer a instalação da biblioteca basta escrever:
pip install pyautogui no seu terminal

Vou deixar aqui o link para a documentação dessa biblioteca, caso tenha dúvidas ou queira saber o que mais é possível fazer com essa biblioteca.
https://pyautogui.readthedocs.io/en/latest/

Nesse projeto nós vamos utilizar basicamente 3 comandos da biblioteca Pyautogui:
• Pyautogui.press – Serve para pressionar uma tecla
do seu teclado
• Pyautogui.write – Serve para escrever com o
teclado (como se fosse você digitando)
• Pyautogui.click – Serve para clicar com o mouse

Há comandos bem utilizados em outros projetos como:

#maximizar
pyautogui.hotkey('win','up')

#selecionar linha
Clique no começo da linha e digite
pyautogui.hotkey('shift','down')

---

Criando seu código:

Baixe meu código para o seu coomputador e em outra aba do editor, copie e cole o código a seguir para saber onde está seu mouse,
podendo assim pegar o gabarito de dimensões do local do mouse em seu monitor, para que os comandos de click (press), funcionem nos locais corretos.

import time
import pyautogui

time.sleep(5)
print(pyautogui.position())

Após isso, dará o resultado, como:

>import time
>import pyautogui
>time.sleep(5)
>print(pyautogui.position())
>Point(x=1313, y=418)

Basta copiar o resultado (x=1313, y=418) e colar no seu código.

---

Para mais informações, podem seguir meu instagram:

@rolftech

Agradeço a colaboração!

