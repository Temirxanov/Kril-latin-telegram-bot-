from aiogram import Bot, Dispatcher, types 
from aiogram.utils import executor 
import logging 
import transliterate

# Bot tokeningizni shu yerga kiriting

TOKEN = "7533584256:AAH23_uxOLtCzsY6Ljm1Ujz4_CHeoiisg8A"

#Bot va Dispatcher obyektlarini yaratamiz

bot = Bot(token=TOKEN) 
dp = Dispatcher(bot)

# Logging sozlamalari

logging.basicConfig(level=logging.INFO)

#start va /help komandalariga javob beradigan handler

dp.register_message_handler(lambda message: message.answer("Salom! Men Telegram botman. Kirill-Lotin va Lotin-Kirill o'girish botiman."), commands=['start', 'help'])

# Matnni Kirill-Lotin yoki Lotin-Kirillga o‘girish

def transliterate_text(text):
     if any("а" <= ch <= "я" for ch in text.lower()): 
        return transliterate.to_latin(text) 
     else: return transliterate.to_cyrillic(text)

@dp.message_handler()
def translit(message: types.Message): 
    converted_text = transliterate_text(message.text) 
    message.answer(converted_text)

#Botni ishga tushirish

if __name__ == "__main__": 
    executor.start_polling(dp, skip_updates=True)