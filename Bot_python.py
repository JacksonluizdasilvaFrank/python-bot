from datetime import datetime, timedelta #
import json,requests #
from telebot.types import InlineKeyboardMarkup
import random #
import telebot #
import json,requests #
import time #
import bd #
from pytz import timezone #

api_key = "6125385985:AAHk1FbntGK-gQswpt_rkQFGjmixQupv-1U"
chat_id = "5933713530"

LINK_SITE1 = '[📲 Clique para abrir a corretora](https://www.betsul.com/)'
LINK_SITE2 = '[🐯 Clique aqui para abrir o Fortune Tiger](https://www.betsul.com/cassino/jogo/fortune-tiger)'
bot = telebot.TeleBot(token=api_key)

def DELET_GALE1():
        if bd.mensage_delete1 == True:
            bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
            bd.mensage_delete1 = False

    
while True:
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = datetime.now().hour
    m = datetime.now().minute+4
    s = datetime.now().second

    if m > 59:
        h += 1
        m = 0
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')
    #hora = datetime.datetime.now().strftime("%H:%M")
    numero_aleatorio1 = random.randint(1, 10)
    numero_aleatorio2 = random.randint(1, 10)
    numero_aleatorio3 = random.randint(88,97)
    for i in range(1,10):
        print(numero_aleatorio1,numero_aleatorio2)
        
    dados  = bot.send_message(chat_id=chat_id, text=(f'''
💰 Entrada Confirmada 💰
🐯 Fortune Tiger
💻 Site: AGJogos
✅ Probabilidade do algortímo: {(numero_aleatorio3)}%
🕑 Válido por 4min
                                                                                           
👉 {(numero_aleatorio1)}X Normal
⚡ {(numero_aleatorio2)}X Turbo
🚥 Intercalando

{LINK_SITE1} 
{LINK_SITE2}

'''),
parse_mode='MARKDOWN', disable_web_page_preview=True)
    time.sleep(240)#240
    bot.send_message(chat_id=chat_id, text=(f'''
❌ Sinal Finalizado ❌
🐯 Fortune Tiger
🕑 Finalizado
''', dados . chat . id , dados . message_id), 
parse_mode='MARKDOWN', disable_web_page_preview=True)
    time.sleep(60)#60
    #ALERT_GALE1()
    time.sleep(10)#10
    #DELET_GALE1()
    time.sleep(50)#50