import requests
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
import ttkbootstrap as ttk
from ttkbootstrap.constants import CENTER

# Função para raspar o versículo
def get_versiculo():
    response = requests.get('https://www.bible.com/pt/verse-of-the-day')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')

    assunto = site.find('a', attrs={'class': 'w-full no-underline dark:text-text-dark text-text-light'})
    assunto_sub = site.find('p', attrs={'class': 'dark:text-text-dark text-15 font-aktiv-grotesk uppercase font-bold mbs-2 text-gray-25'})

    if assunto and assunto_sub:
        versiculo_texto_bruto = assunto.text
        referencia_bilbica = assunto_sub.text

        versiculo_formatado = re.sub(r'\s+', ' ', versiculo_texto_bruto).strip()
        referencia_bilbica_formatada = re.sub(r'\s+', ' ', referencia_bilbica).strip()

        return versiculo_formatado, referencia_bilbica_formatada
    return None, None

# Função para exibir o versículo na interface
def exibir_versiculo():
    versiculo, referencia = get_versiculo()
    if versiculo and referencia:
        mensagem = f"Versículo: {versiculo} {referencia}"
        versiculo_label.config(text=mensagem)
        versiculo_label.update_idletasks()  # Atualiza o widget

# Configuração da interface
root = ttk.Window(themename="darkly")

root.title("Versículo do Dia")
root.geometry("800x200")

# Label para exibir o versículo
versiculo_label = ttk.Label(root, text="", anchor=CENTER, font=("Helvetica", 16), wraplength=750)
versiculo_label.pack(expand=True)

# Carregar e exibir o versículo
exibir_versiculo()

root.mainloop()
