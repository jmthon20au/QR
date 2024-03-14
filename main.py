#Dev : @DF_GD_D
#in 2023/12/8
#Channel @T62RS 
import telebot 
import qrcode

private = "7088902990:AAHZX5_hqZmDkXNDo4VAiHP6-bwExEHDzZE"
bot = telebot.TeleBot(private)

@bot.message_handler(commands=["start"])
def start(message):
  instructions = "• 👋 اهلا بك عزيزي في بوت صنع وتشفير QR \n\n ارسل النص التشفير الان ↫ 🛎️"
  bot.send_message(message.chat.id, instructions)

@bot.message_handler(func=lambda message: True)
def send_encrypted_qr(message):
  plaintext = message.text
  qr_code = qrcode.make(plaintext)
  qr_code.save("image.png")
  encrypted_message = "• تم تشفير النص هذا هو QR اعلاة 〈 👆 〉"
  bot.send_photo(message.chat.id, open("image.png", "rb"), caption=encrypted_message)

print("تم✅✅✅✅✅😈😈😈😈🖥🖥🔰😂✅😜😈〽️😔🆕✨🌹😂🌺💖💖🌹") 
bot.polling(True)
#Dev : @DF_GD_D
#in 2023/12/8
#Channel @T62RS 
