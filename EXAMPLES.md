# أمثلة استخدام مكتبة italymusic

هذا الملف يحتوي على أمثلة مفصلة لاستخدام مكتبة italymusic للبحث والتحميل من يوتيوب والتكامل مع تليجرام.

## البحث في يوتيوب

### البحث البسيط

```python
import asyncio
from italymusic.services.SearchService import SearchService

async def search_example():
    # البحث في يوتيوب
    results = await SearchService.search_youtube("أغنية عربية", limit=5)
    
    # عرض النتائج
    for result in results:
        print(f"العنوان: {result['title']}")
        print(f"الرابط: {result['url']}")
        print(f"المدة: {result['duration_text']}")
        print(f"القناة: {result['channel']}")
        print()

# تشغيل المثال
asyncio.run(search_example())
```

### البحث بجودة منخفضة لتسريع التحميل

```python
import asyncio
from italymusic.services.SearchService import SearchService

async def search_low_quality_example():
    # البحث في يوتيوب بجودة منخفضة
    results = await SearchService.search_youtube("أغنية عربية", limit=5, low_quality=True)
    
    # عرض النتائج
    for result in results:
        print(f"العنوان: {result['title']}")
        print(f"الرابط: {result['url']}")
        print(f"المدة: {result['duration_text']}")
        print(f"القناة: {result['channel']}")
        print()

# تشغيل المثال
asyncio.run(search_low_quality_example())
```

## تحميل فيديوهات يوتيوب

### تحميل فيديو

```python
from italymusic.services.DownloadService import DownloadService

# تحميل فيديو
download_service = DownloadService(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    path="/path/to/save",
    quality="best",
    is_audio=False
)

# تنفيذ التحميل
download_service.download()
```

### تحميل صوت فقط

```python
from italymusic.services.DownloadService import DownloadService

# تحميل صوت
download_service = DownloadService(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    path="/path/to/save",
    quality="best",
    is_audio=True
)

# تنفيذ التحميل
download_service.download()
```

### تحميل بجودة منخفضة لتسريع التحميل

```python
from italymusic.services.DownloadService import DownloadService

# تحميل فيديو بجودة منخفضة
download_service = DownloadService(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    path="/path/to/save",
    quality="low",  # استخدام جودة منخفضة
    is_audio=False
)

# تنفيذ التحميل
download_service.download()
```

## استخدام المكتبة مع تليجرام

### تهيئة خدمة تليجرام

```python
import asyncio
from italymusic.services.TelegramService import TelegramService

async def telegram_service_example():
    # إنشاء كائن خدمة تليجرام
    telegram_service = TelegramService(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"  # اختياري، استخدم فقط إذا كنت تريد استخدام بوت
    )
    
    # تهيئة الخدمة
    await telegram_service.initialize()
    
    try:
        # استخدام الخدمة هنا
        pass
    finally:
        # إيقاف الخدمة
        await telegram_service.stop()

# تشغيل المثال
asyncio.run(telegram_service_example())
```

### تحميل وإرسال صوت إلى تليجرام

```python
import asyncio
from italymusic.services.TelegramService import TelegramService

async def download_and_send_audio_example():
    # إنشاء كائن خدمة تليجرام
    telegram_service = TelegramService(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"
    )
    
    # تهيئة الخدمة
    await telegram_service.initialize()
    
    try:
        # تحميل وإرسال صوت
        await telegram_service.download_and_send_audio(
            chat_id=123456789,
            youtube_url="https://www.youtube.com/watch?v=VIDEO_ID",
            caption="تم التحميل بواسطة italymusic",
            low_quality=True  # استخدام جودة منخفضة لتسريع التحميل
        )
    finally:
        # إيقاف الخدمة
        await telegram_service.stop()

# تشغيل المثال
asyncio.run(download_and_send_audio_example())
```

### تحميل وإرسال فيديو إلى تليجرام

```python
import asyncio
from italymusic.services.TelegramService import TelegramService

async def download_and_send_video_example():
    # إنشاء كائن خدمة تليجرام
    telegram_service = TelegramService(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"
    )
    
    # تهيئة الخدمة
    await telegram_service.initialize()
    
    try:
        # تحميل وإرسال فيديو
        await telegram_service.download_and_send_video(
            chat_id=123456789,
            youtube_url="https://www.youtube.com/watch?v=VIDEO_ID",
            caption="تم التحميل بواسطة italymusic",
            low_quality=True  # استخدام جودة منخفضة لتسريع التحميل
        )
    finally:
        # إيقاف الخدمة
        await telegram_service.stop()

# تشغيل المثال
asyncio.run(download_and_send_video_example())
```

## استخدام بوت تليجرام للبحث والتحميل

### إنشاء بوت تليجرام

```python
import asyncio
from italymusic.telegram.TelegramYoutubeBot import TelegramYoutubeBot

async def telegram_bot_example():
    # إنشاء كائن البوت
    bot = TelegramYoutubeBot(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"
    )
    
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # استخدام البوت هنا
        pass
    finally:
        # إيقاف البوت
        await bot.stop()

# تشغيل المثال
asyncio.run(telegram_bot_example())
```

### البحث وإرسال النتائج إلى تليجرام

```python
import asyncio
from italymusic.telegram.TelegramYoutubeBot import TelegramYoutubeBot

async def search_and_send_example():
    # إنشاء كائن البوت
    bot = TelegramYoutubeBot(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"
    )
    
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # البحث وإرسال النتائج
        await bot.search_youtube(
            chat_id=123456789,
            query="أغنية عربية",
            limit=5,
            low_quality=True  # استخدام جودة منخفضة لتسريع التحميل
        )
    finally:
        # إيقاف البوت
        await bot.stop()

# تشغيل المثال
asyncio.run(search_and_send_example())
```

### تحميل من رابط وإرساله إلى تليجرام

```python
import asyncio
from italymusic.telegram.TelegramYoutubeBot import TelegramYoutubeBot

async def download_from_url_example():
    # إنشاء كائن البوت
    bot = TelegramYoutubeBot(
        api_id="YOUR_API_ID",
        api_hash="YOUR_API_HASH",
        bot_token="YOUR_BOT_TOKEN"
    )
    
    # تهيئة البوت
    await bot.initialize()
    
    try:
        # تحميل من رابط وإرساله
        await bot.download_from_url(
            chat_id=123456789,
            youtube_url="https://www.youtube.com/watch?v=VIDEO_ID",
            is_audio=True,  # استخدم False لتحميل فيديو
            low_quality=True  # استخدام جودة منخفضة لتسريع التحميل
        )
    finally:
        # إيقاف البوت
        await bot.stop()

# تشغيل المثال
asyncio.run(download_from_url_example())
```

## بوت تليجرام كامل

للحصول على مثال لبوت تليجرام كامل، يرجى الاطلاع على ملف `examples/telegram_bot_example.py` في المشروع.
