"""
مثال بسيط لاستخدام مكتبة italymusic للبحث والتحميل من يوتيوب
"""

import asyncio
from italymusic.services.SearchService import SearchService
from italymusic.services.DownloadService import DownloadService

async def main():
    """
    الدالة الرئيسية للمثال
    """
    print("🔍 مثال على استخدام مكتبة italymusic للبحث والتحميل من يوتيوب")
    
    # البحث في يوتيوب
    query = "أغنية عربية"
    print(f"\n🔎 جاري البحث عن: {query}")
    
    results = await SearchService.search_youtube(query, limit=3, low_quality=True)
    
    if not results:
        print("❌ لم يتم العثور على نتائج")
        return
    
    # عرض نتائج البحث
    print("\n📋 نتائج البحث:")
    for i, result in enumerate(results):
        print(f"{i+1}. {result['title']}")
        print(f"   ⏱️ {result['duration_text']} | 👤 {result['channel']}")
        print(f"   🔗 {result['url']}")
        print()
    
    # اختيار الفيديو الأول للتحميل
    if results:
        video_url = results[0]['url']
        print(f"⬇️ جاري تحميل الفيديو الأول: {results[0]['title']}")
        
        # إنشاء مسار للتحميل
        download_path = "/tmp"
        
        # تحميل الفيديو
        download_service = DownloadService(
            url=video_url,
            path=download_path,
            quality="low",
            is_audio=True
        )
        
        try:
            # تنفيذ التحميل
            video, video_id, _, video_audio, _ = download_service.download_preparing()
            audio_filename = download_service.download_audio(video, video_audio, video_id)
            
            print(f"✅ تم تحميل الملف الصوتي بنجاح: {audio_filename}")
            print(f"📂 مسار الملف: {download_path}/{audio_filename}")
        except Exception as e:
            print(f"❌ حدث خطأ أثناء التحميل: {str(e)}")

# تشغيل المثال
if __name__ == "__main__":
    asyncio.run(main())
