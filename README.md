# Kooora Match Scraper

هذا المشروع يحتوي على سكربت Python لسحب نتائج مباريات كرة القدم من موقع كووورة (kooora.com) وحفظها في ملف JSON. يتم تشغيل السكربت تلقائيًا باستخدام GitHub Actions.

## محتويات المشروع

- `kooora_scraper.py`: سكربت Python الذي يقوم بسحب البيانات.
- `.github/workflows/scrape_matches.yml`: ملف GitHub Actions لإعداد وتشغيل السكربت تلقائيًا.
- `matches.json`: (يتم إنشاؤه بواسطة GitHub Actions) ملف JSON يحتوي على نتائج المباريات المسحوبة.

## كيفية الاستخدام (محليًا)

1.  **استنساخ المستودع:**
    ```bash
    git clone <رابط المستودع الخاص بك>
    cd kooora-match-scraper
    ```

2.  **تثبيت الاعتمادات:**
    ```bash
    pip install requests beautifulsoup4
    ```

3.  **تشغيل السكربت:**
    ```bash
    python kooora_scraper.py
    ```
    سيقوم السكربت بطباعة نتائج المباريات في الطرفية.

## GitHub Actions

تم إعداد GitHub Actions لتشغيل السكربت يوميًا في منتصف الليل (UTC). سيقوم السكربت بسحب أحدث نتائج المباريات وحفظها في ملف `matches.json`. إذا كانت هناك أي تغييرات في النتائج، فسيتم تحديث الملف ودفع التغييرات إلى المستودع تلقائيًا.

يمكنك أيضًا تشغيل سير العمل يدويًا من خلال الذهاب إلى تبويب "Actions" في مستودع GitHub الخاص بك واختيار "Scrape Kooora Matches" ثم النقر على "Run workflow".

## هيكل البيانات (matches.json)

سيكون ملف `matches.json` عبارة عن قائمة من الكائنات، حيث يمثل كل كائن مباراة واحدة. مثال:

```json
[
  {
    "competition": "المباريات الودية",
    "round": "مباريات دولية ودية",
    "status": "RESULT",
    "start_date": "2026-03-28T12:00:00.000Z",
    "team_a": "ناميبيا",
    "team_b": "جزر القمر",
    "score_a": 0,
    "score_b": 0
  },
  // ... المزيد من المباريات
]
```
