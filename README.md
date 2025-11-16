# مصنف الأوزان / Morphological Pattern Classifier

<div dir="rtl">

## نظرة عامة

أداة متقدمة لتصنيف الكلمات العربية وفق الأوزان الصرفية. تستخدم خوارزميات متقدمة للمطابقة والتصنيف مع دعم معالجة متوازية.

## المميزات

- 🏷️ **تصنيف الأوزان**: تصنيف الكلمات وفق الأوزان الصرفية
- 🔍 **مطابقة متقدمة**: استخدام أنماط regex متقدمة
- ⚡ **معالجة متوازية**: معالجة متعددة الخيوط للأداء العالي
- 📊 **تصدير Excel**: تصدير النتائج بصيغة Excel
- 🗺️ **دعم الخرائط**: استخدام خرائط الرموز العربية

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- openpyxl
- pandas

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/pattern-classifier.git
cd pattern-classifier
```

2. قم بتثبيت المتطلبات:
```bash
pip install openpyxl pandas
```

## الاستخدام

### الإصدار 0.4 (الأحدث)

```bash
python "0.4 مصنف الأوزان الصرفية/0.4 مصنف الكلمات صرفيا.py"
```

### الإصدارات السابقة

```bash
python "0.1 مصنف الأوزان الصرفية/0.1 مصنف الكلمات صرفيا.py"
python "0.2 مصنف الأوزان الصرفية/0.2 مصنف الكلمات صرفيا.py"
python "0.3 مصنف ابلأوزان الصرفية/0.3 مصنف الكلمات صرفيا.py"
```

## هيكل المشروع

```
مصنف الأوزان/
├── 0.1 مصنف الأوزان الصرفية/
│   ├── 0.1 مصنف الكلمات صرفيا.py
│   └── [ملفات الأوزان والخرائط]
├── 0.2 مصنف الأوزان الصرفية/
│   └── [ملفات محسنة]
├── 0.3 مصنف ابلأوزان الصرفية/
│   └── [ملفات محسنة]
└── 0.4 مصنف الأوزان الصرفية/
    ├── 0.4 مصنف الكلمات صرفيا.py
    ├── الأوزان.txt
    └── الخريطة.txt
```

## الملفات الرئيسية

- **0.4 مصنف الكلمات صرفيا.py**: الإصدار الأحدث والأكثر تطوراً
- **الأوزان.txt**: ملف الأوزان الصرفية
- **الخريطة.txt**: خريطة الرموز العربية

## ملاحظات مهمة

⚠️ **ملاحظة**: 
- ضع الكلمات المراد تصنيفها في ملف Excel
- ملف الأوزان يجب أن يحتوي على الأوزان الصرفية
- ملف الخريطة يحتوي على رموز العربية للتحويل

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] تحسين دقة التصنيف
- [ ] دعم المزيد من الأوزان
- [ ] تحسين الأداء

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## عن المطور

**أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

خبير لغوي في معجم الدوحة التاريخي للغة العربية، مهتم بالأدوات والبرامج اللغوية، ومبرمج Vibe Coding.

🌐 **الموقع الشخصي**: [aymannji.com](https://www.aymannji.com/)

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

An advanced tool for classifying Arabic words according to morphological patterns. Uses advanced matching and classification algorithms with parallel processing support.

## Features

- 🏷️ **Pattern Classification**: Classify words according to morphological patterns
- 🔍 **Advanced Matching**: Use advanced regex patterns
- ⚡ **Parallel Processing**: Multi-threaded processing for high performance
- 📊 **Excel Export**: Export results in Excel format
- 🗺️ **Map Support**: Use Arabic symbol maps

## Installation

### Requirements

- Python 3.7 or later
- openpyxl
- pandas

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/pattern-classifier.git
cd pattern-classifier
```

2. Install requirements:
```bash
pip install openpyxl pandas
```

## Usage

### Version 0.4 (Latest)

```bash
python "0.4 مصنف الأوزان الصرفية/0.4 مصنف الكلمات صرفيا.py"
```

### Previous Versions

```bash
python "0.1 مصنف الأوزان الصرفية/0.1 مصنف الكلمات صرفيا.py"
python "0.2 مصنف الأوزان الصرفية/0.2 مصنف الكلمات صرفيا.py"
python "0.3 مصنف ابلأوزان الصرفية/0.3 مصنف الكلمات صرفيا.py"
```

## Project Structure

```
pattern-classifier/
├── 0.1 مصنف الأوزان الصرفية/
│   ├── 0.1 مصنف الكلمات صرفيا.py
│   └── [Pattern and map files]
├── 0.2 مصنف الأوزان الصرفية/
│   └── [Enhanced files]
├── 0.3 مصنف ابلأوزان الصرفية/
│   └── [Enhanced files]
└── 0.4 مصنف الأوزان الصرفية/
    ├── 0.4 مصنف الكلمات صرفيا.py
    ├── الأوزان.txt
    └── الخريطة.txt
```

## Main Files

- **0.4 مصنف الكلمات صرفيا.py**: Latest and most advanced version
- **الأوزان.txt**: Morphological patterns file
- **الخريطة.txt**: Arabic symbols map

## Important Notes

⚠️ **Note**: 
- Place words to classify in Excel file
- Pattern file must contain morphological patterns
- Map file contains Arabic symbols for conversion

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Improve classification accuracy
- [ ] Support for more patterns
- [ ] Performance improvements

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## About the Developer

**Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

Linguistic expert at the Historical Dictionary of the Arabic Language of Qatar (Doha Dictionary), interested in linguistic tools and software, and a Vibe Coding programmer.

🌐 **Personal Website**: [aymannji.com](https://www.aymannji.com/)

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

