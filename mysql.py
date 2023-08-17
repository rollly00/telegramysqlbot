# -*- coding: utf-8 -*-
import telebot
import MySQLdb
bot = telebot.TeleBot("")
new string = 'test'
@bot.message_handler(commands=['auth'])
def send_auth(message):
    #создаем пустую переменную 
    answer = ""
    ###
    con = MySQLdb.connect(host="", user="", passwd="", db="")
    cur = con.cursor()
    cur.execute("""SELECT * FROM vk""")
    for row in cur.fetchall():
        ## перенос кода, добавляем код в переменную
        answer = answer +\
        '1: ' + str(row[0]) + '\n' +\
        '2: ' + str(row[1]) + '\n' +\
        '3: ' + str(row[2]) + '\n' +\
        '4: ' + str(row[3]) + '\n' +\
        '5: ' + str(row[4]) + '\n' +\
        '6 ответа: ' + str(row[5]) + '\n' 
        print(answer)
    bot.send_message(message.chat.id,answer)
    con.close()
bot.polling()
