from time import sleep
import time
import requests
import os
import telebot
from PyPDF2 import PdfReader
from io import BytesIO
print("\033[97;1m[\033[92;1m+\033[97;1m] \x1b[1;38;5;121m MY INFO https://t.me/KING_OF_ENG")


try:
    from cfonts import render, say
except:
    os.system("pip install python-cfonts")
    os.system("pip install render")


Z = "\033[1;31m"
F = "\033[2;32m"
B = "\033[2;36m"
X = "\033[1;33m"
C = "\033[2;35m"


def SAJ(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)


output = render("PDF2TEXT", colors=["white", "red"], align="center")
print(output)
SAJ(
    F
    + f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D \n                            ᴄʜᴀɴɴᴇʟ : https://t.me/KING_OF_ENG  』",
    0.00,
    True,
)


TOKEN = "7144691782:AAGN_HN75TEQ5Se1bDy25E_kVr9OP8_mHp0"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "اهلا بك في بوت استخراج النص من الPDF.")


@bot.message_handler(content_types=['document'])
def handle_pdf(message):
    file_info = bot.get_file(message.document.file_id)
    file_extension = os.path.splitext(file_info.file_path)[-1]

    if file_extension.lower() == '.pdf':
        downloaded_file = bot.download_file(file_info.file_path)

        extracted_text = extract_text_from_pdf(downloaded_file)

        reversed_text = extracted_text[::-1]

        bot.send_message(message.chat.id, reversed_text)
    else:
        bot.send_message(message.chat.id, "من فضلك ارسل ملف PDF.")


def extract_text_from_pdf(pdf_bytes):
    text = ""
    with BytesIO(pdf_bytes) as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


bot.polling()
