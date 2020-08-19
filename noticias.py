import requests
from bs4 import BeautifulSoup as bs
import PySimpleGUI as sg
import win32com.client as wincl
import time
speak = wincl.Dispatch('SAPI.SpVoice')

def tela():

	resp = requests.get('https://g1.globo.com/')

	page = bs(resp.text, 'html.parser')

	noticias_lista = []

	noticias = page.find_all('div', {'class':"feed-post-body-resumo"})
	for noticia in noticias:
		noticias_lista.append(noticia.text)

	sg.change_look_and_feel('DarkBlue10')
	

	layout = [
		
		[sg.Text(noticias_lista[0]+'\n',size=(30,0))],
		[sg.Text(noticias_lista[1]+'\n',size=(30,0))],
		[sg.Text(noticias_lista[2]+'\n',size=(30,0))],
		[sg.Text(noticias_lista[3]+'\n',size=(30,0))],
		[sg.Text(noticias_lista[4]+'\n',size=(30,0))],
		[sg.Text('\n',size=(30,0))],
		[sg.Button('Ouvir Podcast')]
	]

	janela = sg.Window('Noticias G1').layout(layout)
	while True:
		
		Button, values = janela.Read()
		if Button == None:
			quit()

		elif Button == 'Ouvir Podcast':
			for noticia in noticias:
				speak.Speak(noticia)
				time.sleep(1)

tela()