from twilio.rest import Client 
from bs4 import BeautifulSoup
import requests

#data para twilio
account_sid = 'AC9f0f07e160edfbf8bb156718e6a70b66' 
auth_token = 'dbfffdbae8fe437a4af797a36131cc54' 
client = Client(account_sid, auth_token) 

#cosas de beautifulsoup
#todo esto de lanacion hasta q diga lo contrario
#   primero agarrar el url madre y hacerlo sopa
urlrey="https://www.lanacion.com.ar/economia"
pagerey=requests.get(urlrey).text
souprey=BeautifulSoup(pagerey,features="html.parser")
#   de la sopa sacar todos los gois q sean titulos y ese objeto raro hacerlo string y chuparle los URLs
stringgigante=str(souprey.findAll(class_="titulo"))
listaURLs=['https://www.lanacion.com.ar'+oracion for oracion in stringgigante.split('"') if "/economia" in oracion]
#ahora usar la lista de URLs para sacarle los headlines y parrafos
headlines=[]
content=[]
for i in range(len(listaURLs)):
    page=requests.get(listaURLs[i]).text
    soup=BeautifulSoup(page,features="html.parser")
    headline=soup.find('h1').get_text()
    headlines.append(headline)
    p_tags=soup.find_all('p')
    p_tags_text=[tag.get_text().strip() for tag in p_tags]
    sentence_list=[sentence for sentence in p_tags_text if '.' in sentence]
    sentence_list2=sentence_list[0:2]
    sentence_list2=[sentence.replace('\r','') for sentence in sentence_list2]
    sentence_list2=[sentence.replace('\n','') for sentence in sentence_list2]
    article = ''.join(sentence_list2)
    content.append(article)
#armar lista con cada titulo y contenido
listajuntadora=[h+'\n'+c+"\n"+'*La Nacion*'+'\n\n' for h,c in zip(headlines,content)]
#aca vendrian otros diarios
#funcion de twilio hace lo suyo
def send_message(mensajestring):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                 body=mensajestring,      
                                 to='whatsapp:+5491156541925' 
                             ) 
def send_message2(mensajestring):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                 body=mensajestring,      
                                 to='whatsapp:+5491169784988' 
                             ) 
def send_message3():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                 body="averga",      
                                 to='whatsapp:+5491169784988' 
                             ) 
#funcion q itera send_message 3 veces con strings de listajuntadora
def mandarvariosmensajes():
    for i in range(2):
        send_message(listajuntadora[i])
        send_message2(listajuntadora[i])
        send_message3()
#mandarvariosmensajes()