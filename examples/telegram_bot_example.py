"""
مثال لبوت تليجرام يستخدم مكتبة italymusic
"""

import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

from italymusic.telegram.TelegramYoutubeBot import TelegramYoutubeBot

# معلومات API لتليجرام (يجب استبدالها بالقيم الخاصة بك)
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

# إنشاء كائن البوت
bot = TelegramYoutubeBot(API_ID, API_HASH, BOT_TOKEN)

# إنشاء كائن عميل Pyrogram
app = Client("italymusic_example_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# معالجة أمر البداية
@app.on_message(filters.command("start"))
async def start_command(client, message):
    """
    معالجة أمر البداية
    """
    await message.reply_text(
        "👋 مرحباً بك في بوت تحميل يوتيوب!\n\n"
        "يمكنك استخدام هذا البوت لتحميل فيديوهات وملفات صوتية من يوتيوب.\n\n"
        "الأوامر المتاحة:\n"
        "/search [كلمات البحث] - البحث في يوتيوب\n"
        "/audio [رابط يوتيوب] - تحميل ملف صوتي\n"
        "/video [رابط يوتيوب] - تحميل فيديو\n"
        "/help - عرض المساعدة\n\n"
        "مثال: /search شيلة حماسية"
    )

# معالجة أمر المساعدة
@app.on_message(filters.command("help"))
async def help_command(client, message):
    """
    معالجة أمر المساعدة
    """
    await message.reply_text(
        "🔍 **أوامر البوت:**\n\n"
        "/search [كلمات البحث] - البحث في يوتيوب\n"
        "/audio [رابط يوتيوب] - تحميل ملف صوتي\n"
        "/video [رابط يوتيوب] - تحميل فيديو\n"
        "/help - عرض المساعدة\n\n"
        "يمكنك أيضاً إرسال رابط يوتيوب مباشرة وسيتم سؤالك عن نوع التحميل."
    )

# معالجة أمر البحث
@app.on_message(filters.command("search"))
async def search_command(client, message):
    """
    معالجة أمر البحث
    """
    # استخراج كلمات البحث
    query = message.text.split(" ", 1)
    if len(query) < 2:
        await message.reply_text("❌ يرجى تحديد كلمات البحث.\n\nمثال: /search شيلة حماسية")
        return
    
    query = query[1]
    
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # البحث في يوتيوب
        await bot.search_youtube(message.chat.id, query, limit=5, low_quality=True)
    finally:
        # إيقاف البوت
        await bot.stop()

# معالجة أمر تحميل الصوت
@app.on_message(filters.command("audio"))
async def audio_command(client, message):
    """
    معالجة أمر تحميل الصوت
    """
    # استخراج رابط يوتيوب
    url = message.text.split(" ", 1)
    if len(url) < 2:
        await message.reply_text("❌ يرجى تحديد رابط يوتيوب.\n\nمثال: /audio https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        return
    
    url = url[1]
    
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # تحميل الصوت
        await bot.download_from_url(message.chat.id, url, is_audio=True, low_quality=True)
    finally:
        # إيقاف البوت
        await bot.stop()

# معالجة أمر تحميل الفيديو
@app.on_message(filters.command("video"))
async def video_command(client, message):
    """
    معالجة أمر تحميل الفيديو
    """
    # استخراج رابط يوتيوب
    url = message.text.split(" ", 1)
    if len(url) < 2:
        await message.reply_text("❌ يرجى تحديد رابط يوتيوب.\n\nمثال: /video https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        return
    
    url = url[1]
    
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # تحميل الفيديو
        await bot.download_from_url(message.chat.id, url, is_audio=False, low_quality=True)
    finally:
        # إيقاف البوت
        await bot.stop()

# معالجة الروابط المباشرة
@app.on_message(filters.regex(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+'))
async def direct_link_handler(client, message):
    """
    معالجة الروابط المباشرة
    """
    url = message.text
    
    # سؤال المستخدم عن نوع التحميل
    response = await message.reply_text(
        "🎬 تم اكتشاف رابط يوتيوب!\n\n"
        "يرجى اختيار نوع التحميل:\n"
        "/audio " + url + " - تحميل ملف صوتي\n"
        "/video " + url + " - تحميل فيديو"
    )

# معالجة استجابات الأزرار
@app.on_callback_query()
async def callback_handler(client, callback_query: CallbackQuery):
    """
    معالجة استجابات الأزرار
    """
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # معالجة الاستجابة
        await bot.handle_callback(callback_query, low_quality=True)
    finally:
        # إيقاف البوت
        await bot.stop()

# تشغيل البوت
async def main():
    """
    الدالة الرئيسية لتشغيل البوت
    """
    await app.start()
    print("✅ البوت قيد التشغيل!")
    
    # الانتظار حتى يتم إيقاف البوت
    await pyrogram.idle()
    
    # إيقاف البوت
    await app.stop()

# تشغيل البوت
if __name__ == "__main__":
    asyncio.run(main())
