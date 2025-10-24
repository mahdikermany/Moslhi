import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# توکن ربات - استفاده از توکن ارائه شده توسط شما
BOT_TOKEN = "8288803141:AAF-devMPyXjbcXHjHfrzkitoEqddMkNZt4"

def create_main_keyboard():
    keyboard = [
        ["📊 تابلو طلاجواهر مهران مصلحی"],
        ["🧮 ماشین حساب گالری", "🏺 گالری طلای مستعمل"],
        ["💰 صندوق طلای گالری مهران مصلحی"],
        ["📞 ارتباط با ما"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, input_field_placeholder="لطفاً یک گزینه انتخاب کنید...")

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_message = f"""سلام {user.first_name}!
به ربات طلاجواهر مهران مصلحی خوش آمدید.

🛍️ **گالری طلا و جواهر مهران مصلحی**
لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"""
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=create_main_keyboard(),
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    
    if text == "📊 تابلو طلاجواهر مهران مصلحی":
        response = """📊 **تابلو طلاجواهر مهران مصلحی**

💎 اطلاعات قیمت طلا و جواهر
📈 نمودارهای به‌روز
💰 محاسبات آنلاین

این بخش به زودی فعال خواهد شد..."""
    
    elif text == "🧮 ماشین حساب گالری":
        response = """🧮 **ماشین حساب گالری**

برای محاسبه قیمت طلا و جواهر از این بخش استفاده کنید.

لطفاً وزن طلا را به گرم وارد کنید:"""
    
    elif text == "🏺 گالری طلای مستعمل":
        response = """🏺 **گالری طلای مستعمل**

📸 عکس محصولات مستعمل
💰 قیمت‌های ویژه
🎁 شرایط پرداخت

محصولات مستعمل در این بخش نمایش داده می‌شوند."""
    
    elif text == "💰 صندوق طلای گالری مهران مصلحی":
        response = """💰 **صندوق طلای گالری مهران مصلحی**

💼 مدیریت سرمایه طلا
📊 تحلیل بازار
🛡️ خدمات امنیتی

اطلاعات صندوق طلای گالری در اینجا نمایش داده خواهد شد."""
    
    elif text == "📞 ارتباط با ما":
        response = """📞 **ارتباط با ما**

🏢 **گالری طلا و جواهر مهران مصلحی**
📞 تلفن: ۰۲۱-۱۲۳۴۵۶۷۸
📧 ایمیل: info@mohammad-masooli.com
📍 آدرس: تهران، خیابان اصلی، پلاک ۱۲۳

🕒 **ساعات کاری:**
شنبه تا چهارشنبه: ۹:۰۰ - ۱۸:۰۰
پنجشنبه: ۹:۰۰ - ۱۴:۰۰

برای دریافت مشاوره رایگان در خدمت شما هستیم."""
    
    else:
        response = "⚠️ لطفاً یکی از گزینه‌های موجود در منو را انتخاب کنید."
    
    await update.message.reply_text(response, parse_mode='Markdown')

async def error_handler(update: Update, context: CallbackContext):
    logger.error(f"خطا رخ داد: {context.error}")

def main():
    try:
        # ساخت اپلیکیشن
        application = Application.builder().token(BOT_TOKEN).build()
        
        # اضافه کردن هندلرها
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # هندلر خطا
        application.add_error_handler(error_handler)
        
        print("🤖 ربات طلاجواهر مهران مصلحی در حال راه‌اندازی...")
        print("✅ ربات آماده دریافت درخواست‌ها است!")
        
        # اجرای ربات
        application.run_polling()
        
    except Exception as e:
        print(f"❌ خطا در راه‌اندازی ربات: {e}")

if __name__ == "__main__":
    main()