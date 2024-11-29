import requests
import re
from bs4 import BeautifulSoup
from collections import OrderedDict

response = requests.get('https://www.bible.com/pt/verse-of-the-day')
 
content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML
assunto = site.find('a',attrs={'class': 'w-full no-underline dark:text-text-dark text-text-light'})
assunto_sub = site.find('p',attrs={'class': 'dark:text-text-dark text-15 font-aktiv-grotesk uppercase font-bold mbs-2 text-gray-25'})

# Limpeza do texto raspado
if assunto:
    # Pegando o texto bruto
    versiculo_texto_bruto = assunto.text
    referencia_bilbica = assunto_sub.text
    
    # Removendo espaços extras e quebras de linha
    versiculo_formatado = re.sub(r'\s+', ' ', versiculo_texto_bruto).strip()
    referencia_bilbica_formatada = re.sub(r'\s+', ' ', referencia_bilbica).strip()

    # Remover palavras repetidas (opcional)
    #versiculo_formatado = " ".join(OrderedDict.fromkeys(versiculo_formatado.split()))

# Imprimir o assunto formatado
#print("Opa Campeão, Bem-vindo, nada melhor que começar o dia com a palavra de Deus, Versículo do dia:")
print()
print('Versículo:{} {}'.format(versiculo_formatado, referencia_bilbica_formatada), end='')
print()


input('')