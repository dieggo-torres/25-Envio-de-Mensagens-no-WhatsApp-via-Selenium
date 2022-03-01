# Importa a biblioteca pandas com o apelido pd
import pandas as pd

# Importa métodos da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Importa a biblioteca urllib para codificação de URL
import urllib

# Importa a biblioteca time
import time

# Criação de dataframe com a planilha
df_contatos = pd.read_excel('Enviar.xlsx')


def esperar_elemento(elemento):
    '''Aguarda o elemento aparecer na tela.'''
    while len(elemento) == 0:
        time.sleep(1)

    # Agurada mais 1s
    time.sleep(1)


# Cria uma instância do Google Chrome
navegador = webdriver.Chrome()

# Acessa o site do WhatsApp
navegador.get('https://web.whatsapp.com/')

# A partir deste ponto, espera-se que o usuário escaneie o QR code
barra_lateral = navegador.find_elements(By.ID, 'side')
esperar_elemento(barra_lateral)

# Percorre a lista de pessoas
for i, pessoa in enumerate(df_contatos['Pessoa']):
    # Dados de contato da pessoa
    numero = df_contatos.loc[i, 'Número']
    mensagem = df_contatos.loc[i, 'Mensagem']

    # Codificação da mensagem para passar no URL
    texto = urllib.parse.quote(f'Oi, {pessoa}! {mensagem}')

    # Link para enviar a mensagem
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'

    # Navega para o link
    navegador.get(link)

    # Aguarda a barra lateral aparecer
    esperar_elemento(barra_lateral)

    # Localiza o campo de texto
    campo_mensagem = navegador.find_element(
        By.CSS_SELECTOR, 'footer._2cYbV div._2lMWa div._13NKt')

    # Envia a mensgem
    campo_mensagem.send_keys(Keys.RETURN)

    # Aguarda 10s antes de enviar a próxima mensagem
    time.sleep(10)
