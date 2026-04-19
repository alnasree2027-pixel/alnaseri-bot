import telebot
from telebot import types

API_TOKEN = '8688829272:AAGQ4snoefT53JygsGj2NtamMsvmwhbPV3M'
bot = telebot.TeleBot(API_TOKEN)

PASSWORDS = {
    "FIRST": "NR-770",
    "SECOND": "BT-550",
    "THIRD": "MN-110"
}

def main_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("الفايز الاول 🎁", "الفايز الثاني 🎁")
    markup.add("الفايز الثالث 🎁")
    return markup

def first_winner_sections():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("1️⃣ 4 أرقام وهمية", callback_data="p1_1"),
        types.InlineKeyboardButton("2️⃣ كيبورد معدل", callback_data="p1_2"),
        types.InlineKeyboardButton("3️⃣ نسخة توثيق حظر", callback_data="p1_3"),
        types.InlineKeyboardButton("4️⃣ توثيق رقم ميتا", callback_data="p1_4"),
        types.InlineKeyboardButton("5️⃣ 100 بوت اختراق", callback_data="p1_5"),
        types.InlineKeyboardButton("6️⃣ 5 طرق تفنيش", callback_data="p1_6"),
        types.InlineKeyboardButton("7️⃣ 10 بوتات أرقام", callback_data="p1_7"),
        types.InlineKeyboardButton("8️⃣ صورة ملغمة", callback_data="p1_8"),
        types.InlineKeyboardButton("9️⃣ بند حظر نسخة", callback_data="p1_9"),
        types.InlineKeyboardButton("🔟 أداة بلاغات Python", callback_data="p1_10")
    ]
    markup.add(*btns)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    welcome_text = f"مرحباً بك يا {user_name} في بوت الجوائز الرسمي 🏆.\n\nالرجاء اختيار المركز لإدخال كود التحقق الخاص بك:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_markup())

@bot.message_handler(func=lambda m: True)
def handle_selections(message):
    text = message.text
    if "الاول" in text:
        msg = bot.send_message(message.chat.id, "🔐 أرسل كود التحقق للمركز الأول:")
        bot.register_next_step_handler(msg, verify_first)
    elif "الثاني" in text:
        msg = bot.send_message(message.chat.id, "🔐 أرسل كود التحقق للمركز الثاني:")
        bot.register_next_step_handler(msg, verify_second)
    elif "الثالث" in text:
        msg = bot.send_message(message.chat.id, "🔐 أرسل كود التحقق للمركز الثالث:")
        bot.register_next_step_handler(msg, verify_third)

def verify_first(message):
    if message.text.strip().upper() == PASSWORDS["FIRST"]:
        bot.send_message(message.chat.id, "✅ تم التحقق بنجاح! إليك أقسام الجوائز:", reply_markup=first_winner_sections())
    else:
        bot.send_message(message.chat.id, "❌ كود التحقق خاطئ!")

def verify_second(message):
    if message.text.strip().upper() == PASSWORDS["SECOND"]:
        bot.send_message(message.chat.id, "✅ تم التحقق للمركز الثاني! (المحتوى قيد التجهيز)")
    else:
        bot.send_message(message.chat.id, "❌ كود خاطئ.")

def verify_third(message):
    if message.text.strip().upper() == PASSWORDS["THIRD"]:
        bot.send_message(message.chat.id, "✅ تم التحقق للمركز الثالث! (المحتوى قيد التجهيز)")
    else:
        bot.send_message(message.chat.id, "❌ كود خاطئ.")

@bot.callback_query_handler(func=lambda call: True)
def handle_prizes(call):
    bot.answer_callback_query(call.id, text="جاري جلب المحتوى...")
    bot.send_message(call.message.chat.id, f"فتحت القسم: {call.data}\nسيتم إرسال الجائزة هنا قريباً.")

if __name__ == "__main__":
    bot.infinity_polling()
