from bs4 import BeautifulSoup
from lxml import etree
from urllib.request import urlopen, Request
import time, schedule
from datetime import datetime as dt_time
import pywhatkit as kt
import telegram, telebot
from telegram.ext import Updater, CommandHandler




def EstrategiaTDA(): 
    
    requisicao7 = Request('https://br.investing.com/currencies/xau-usd', headers={'User-Agent': 'Mozilla/5.0'})
    response7 = urlopen(requisicao7).read()
    soup7 = BeautifulSoup(response7, 'html.parser')
    if soup7.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        ouro_usd = soup7.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print(f'OURO= {ouro_usd}')
    if soup7.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        ouro_usd = soup7.find('span','instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print(f'OURO= {ouro_usd}')
    #USD/EUR
    requisicao = Request('https://br.investing.com/currencies/usd-eur', headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(requisicao).read()
    soup = BeautifulSoup(response, "html.parser")
    if soup.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        usd_eur = soup.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print('USD/EUR= ' + usd_eur)
    # usd_eur = soup.find('span', class_=f'instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
    if soup.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        usd_eur = soup.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print('USD/EUR= ' + usd_eur)

    # USD/JPY
    requisicao2 = Request('https://br.investing.com/currencies/usd-jpy', headers={'User-Agent': 'Mozilla/5.0'})
    response2 = urlopen(requisicao2).read()
    soup2 = BeautifulSoup(response2, "html.parser")
    if soup2.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        usd_jpy = soup2.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print('USD/JPY= ' + usd_jpy)
    if soup2.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        usd_jpy = soup2.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print('USD/JPY= ' + usd_jpy)

    # USD/AUD
    requisicao3 = Request('https://br.investing.com/currencies/usd-aud', headers={'User-Agent': 'Mozilla/5.0'})
    response3 = urlopen(requisicao3).read()
    soup3 = BeautifulSoup(response3, "html.parser")
    if soup3.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        usd_aud = soup3.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print('USD/AUD= ' + usd_aud)
    if soup3.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        usd_aud = soup3.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print('USD/AUD= ' + usd_aud)

    # USD/CHF
    requisicao4 = Request('https://br.investing.com/currencies/usd-chf', headers={'User-Agent': 'Mozilla/5.0'})
    response4 = urlopen(requisicao4).read()
    soup4 = BeautifulSoup(response4, "html.parser")
    if soup4.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        usd_chf = soup4.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print('USD/CHF= ' + usd_chf)
    if soup4.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        usd_chf = soup4.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print('USD/CHF= ' + usd_chf)

    #USD/TRY
    requisicao5 = Request('https://br.investing.com/currencies/usd-try', headers={'User-Agent': 'Mozilla/5.0'})
    response5 = urlopen(requisicao5).read()
    soup5 = BeautifulSoup(response5, 'html.parser')
    if soup5.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        usd_try = soup5.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print(f'USD/TRY= {usd_try}')
    if soup5.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        usd_try = soup5.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print(f'USD/TRY= {usd_try}')

    #BTC/USD
    requisicao6 = Request('https://br.investing.com/crypto/bitcoin/btc-usd?cid=1035793', headers={'User-Agent': 'Mozilla/5.0'})
    response6 = urlopen(requisicao6).read()
    soup6 = BeautifulSoup(response6, 'html.parser')
    if soup6.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main'):
        btc_usd = soup6.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-negative-main').text
        print(f'BTC/USD= {btc_usd}')
    if soup6.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main'):
        btc_usd = soup6.find('span', class_='instrument-price_change-percent__bT4yt ml-2.5 text-positive-main').text
        print(f'BTC/USD= {btc_usd}')

    #DX/USD
    requisicao8 = Request('https://br.investing.com/currencies/us-dollar-index', headers={'User-Agent': 'Mozilla/5.0'})
    response8 = urlopen(requisicao8).read()
    soup8 = BeautifulSoup(response8, 'html.parser')
    soup8.find('div', class_='top bold inlineblock')
    dx = soup8.find('div', class_='top bold inlineblock').text
    dx= dx.split()
    dx = dx[2]
    print(f'DX= ({dx})')

    requisicao9 = Request('https://br.financas.yahoo.com/quote/BZ%3DF/', headers={'User-Agent': 'Mozilla/5.0'})
    response9 = urlopen(requisicao9).read()
    soup9 = BeautifulSoup(response9, 'html.parser')
    if soup9.find('span', class_='C($negativeColor)'):
        oil_usd = soup9.find('span', class_='C($negativeColor)').text
        print(f'OIL/USD= {oil_usd}')
    if soup9.find('span', class_='C($positiveColor)'):
        oil_usd = soup9.find('span', class_='C($positiveColor)').text
        print(f'OIL/USD= ({oil_usd})')

    time.sleep(5)
    
    hora_atual = dt_time.now()
    hora = hora_atual.strftime('%H:%M:%S')
    global mensagem_cotaçao
    mensagem_cotaçao = f'HORA SENDO COTADA= {hora}\nUSD-EUR= {usd_eur}\nUSD-JPY= {usd_jpy}\nUSD-AUD= {usd_aud}\nUSD-CHF= {usd_chf}\nUSD-TRY= {usd_try}\nBTC-USD= {btc_usd}\nOURO= {ouro_usd}\nDX= ({dx})\nOIL-USD= ({oil_usd})'
    # kt.sendwhatmsg_to_group_instantly('BQuVgaAhUmHFkHNxxierjk',mensagem)

def enviar_cotacao():
    token = '6068841134:AAEyglly0sj9UWewIcksNeU-8HkFcGs1v8g'
    bot = telebot.TeleBot(token)
    def verificar(mensagem):
        if mensagem.text == 'cotaçao' or 'cotacao' or 'cotação':
            return True
        else:
            return False
    @bot.message_handler(func=verificar)
    def responder(mensagem):
        bot.reply_to(mensagem, 'COTALÇÃO ATUALIZADA')   
        EstrategiaTDA()
        bot.reply_to(mensagem, mensagem_cotaçao)
    bot.polling() 

enviar_cotacao()

# schedule.every().monday.at("08:59").do(EstrategiaTDA)
# schedule.every().tuesday.at("08:57").do(EstrategiaTDA)
# schedule.every().wednesday.at("08:57").do(EstrategiaTDA)
# schedule.every().thursday.at("08:57").do(EstrategiaTDA)
# schedule.every().friday.at("08:57").do(EstrategiaTDA)
# # schedule.every(5).minutes.monday.do(EstrategiaTDA())

# while 1:
#     schedule.run_pending()
#     time.sleep(1)