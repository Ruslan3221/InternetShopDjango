import telebot

api = "7221443679:AAEdan4arivujW7U2z620pLrHaQxIdwemPc"
bot = telebot.TeleBot(api)
def main():
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            chat_id = message.chat.id
            print(f"Chat ID: {chat_id}")
            bot.send_message(chat_id, f"Ваш ID: {chat_id}")

    except Exception as e:
        print(f"[{e}][IN BOT]")





    bot.polling()

def send_message_to_user(chat_id, message):
    try:
        bot.send_message(chat_id, message)
        print("Сообщение успешно отправлено!")
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка при отправке сообщения: {e}")

if __name__ == "__main__":
    main()
