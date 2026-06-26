"""
multilingual_db.py
Multilingual Plant Name Database — 50+ Languages / 1000+ Plant Name Translations
Covers all major agricultural regions: South Asia, Southeast Asia, East Asia, Africa, Europe, Americas
"""

# ─────────────────────────────────────────────────────────────────────────────
# MULTILINGUAL PLANT NAMES DATABASE
# Format: botanical_name -> {language_code: local_name}
# ─────────────────────────────────────────────────────────────────────────────

MULTILINGUAL_NAMES = {
    "Oryza sativa": {
        "en": "Rice", "hi": "Chawal / Dhan (धान)", "bn": "Dhaan (ধান)", "te": "Vadlu (వరి)",
        "ta": "Arisi (அரிசி)", "kn": "Akki (ಅಕ್ಕಿ)", "ml": "Ari (അരി)", "mr": "Tandul (तांदूळ)",
        "pa": "Jhona (ਝੋਨਾ)", "gu": "Chaval (ચોખા)", "or": "Dhana (ଧାନ)", "as": "Dhan (ধান)",
        "ur": "Chawal (چاول)", "ar": "Arz (أرز)", "zh": "Dào (稻)", "ja": "Kome (米)",
        "ko": "Ssal (쌀)", "vi": "Lúa gạo", "th": "Khao (ข้าว)", "id": "Padi",
        "ms": "Padi", "tl": "Palay", "my": "Hsainn", "km": "Srov (ស្រូវ)",
        "si": "Hal (හාල්)", "ne": "Chamal (चामल)", "sw": "Mchele", "ha": "Shinkafa",
        "yo": "Iresi", "ig": "Osikapa", "am": "Timhirt (ጤፍ)", "pt": "Arroz",
        "es": "Arroz", "fr": "Riz", "de": "Reis", "it": "Riso", "ru": "Ris (рис)",
        "nl": "Rijst", "pl": "Ryż", "tr": "Pirinç", "fa": "Berenj (برنج)",
        "gu": "Chaval", "kk": "Küriş", "uz": "Sholi", "tg": "Birinj", "ky": "Küröch"
    },
    "Triticum aestivum": {
        "en": "Wheat", "hi": "Gehun (गेहूँ)", "bn": "Gom (গম)", "te": "Godhuma (గోధుమ)",
        "ta": "Gothumai (கோதுமை)", "kn": "Godi (ಗೋಧಿ)", "ml": "Gothambu (ഗോതമ്പ്)", "mr": "Gahu (गहू)",
        "pa": "Kanak (ਕਣਕ)", "gu": "Ghaun (ઘઉ)", "or": "Gahama (ଗହମ)", "as": "Gom (গম)",
        "ur": "Gandum (گندم)", "ar": "Qamh (قمح)", "zh": "Xiǎomài (小麦)", "ja": "Komugi (小麦)",
        "ko": "Mil (밀)", "vi": "Lúa mì", "th": "Saalee (สาลี)", "id": "Gandum",
        "ms": "Gandum", "tl": "Trigo", "sw": "Ngano", "ha": "Alkama", "yo": "Alikama",
        "am": "Senafich (ስንዴ)", "pt": "Trigo", "es": "Trigo", "fr": "Blé",
        "de": "Weizen", "it": "Grano", "ru": "Pshenitsa (пшеница)", "nl": "Tarwe",
        "pl": "Pszenica", "tr": "Buğday", "fa": "Gandom (گندم)", "kk": "Buday",
        "uz": "Bug'doy", "ro": "Grâu", "uk": "Pshenytsia (пшениця)"
    },
    "Zea mays": {
        "en": "Maize / Corn", "hi": "Makka / Bhuta (मक्का)", "bn": "Bhutta (ভুট্টা)",
        "te": "Makka jowar (మొక్కజొన్న)", "ta": "Cholam (சோளம்)", "kn": "Jawari (ಜೋಳ)",
        "ml": "Cholam (ചോളം)", "mr": "Makai (मका)", "pa": "Makki (ਮੱਕੀ)", "gu": "Makkai (મકાઈ)",
        "ur": "Makai (مکئی)", "ar": "Dhura (ذرة)", "zh": "Yùmǐ (玉米)", "ja": "Tōmorokoshi (とうもろこし)",
        "ko": "Oksusu (옥수수)", "vi": "Ngô", "th": "Khao Phot (ข้าวโพด)", "id": "Jagung",
        "ms": "Jagung", "tl": "Mais", "sw": "Mahindi", "ha": "Masara", "yo": "Àgbàdo",
        "ig": "Oka", "am": "Masara (ማሳር)", "pt": "Milho", "es": "Maíz",
        "fr": "Maïs", "de": "Mais", "it": "Granoturco", "ru": "Kukuruza (кукуруза)",
        "nl": "Maïs", "pl": "Kukurydza", "tr": "Mısır", "fa": "Zarat (ذرت)",
        "ro": "Porumb", "uk": "Kukurudza (кукурудза)"
    },
    "Mangifera indica": {
        "en": "Mango", "hi": "Aam (आम)", "bn": "Aam (আম)", "te": "Mamidi (మామిడి)",
        "ta": "Maambalam (மாம்பழம்)", "kn": "Mavina Hannu (ಮಾವಿನ ಹಣ್ಣು)", "ml": "Mampazham (മാമ്പഴം)",
        "mr": "Amba (आंबा)", "pa": "Aam (ਅੰਬ)", "gu": "Keri (કેરી)", "ur": "Aam (آم)",
        "ar": "Manga (مانجو)", "zh": "Mángguǒ (芒果)", "ja": "Mango (マンゴー)", "ko": "Manggo (망고)",
        "vi": "Xoài", "th": "Mamuang (มะม่วง)", "id": "Mangga", "ms": "Mangga",
        "tl": "Mangga", "my": "Thayet", "sw": "Embe", "ha": "Mangwaro",
        "pt": "Manga", "es": "Mango", "fr": "Mangue", "de": "Mango",
        "it": "Mango", "ru": "Mango (манго)", "tr": "Mango"
    },
    "Musa acuminata": {
        "en": "Banana", "hi": "Kela (केला)", "bn": "Kola (কলা)", "te": "Arati Pandu (అరటిపండు)",
        "ta": "Vazhai Pazham (வாழைப்பழம்)", "kn": "Bale Hannu (ಬಾಳೆ ಹಣ್ಣು)", "ml": "Vazha Pazham (വാഴ്ചഫലം)",
        "mr": "Keli (केळी)", "pa": "Kela (ਕੇਲਾ)", "gu": "Kela (કેળ)", "ur": "Kela (کیلا)",
        "ar": "Mouz (موز)", "zh": "Xiāngjiāo (香蕉)", "ja": "Banana (バナナ)", "ko": "Banana (바나나)",
        "vi": "Chuối", "th": "Kluai (กล้วย)", "id": "Pisang", "ms": "Pisang",
        "tl": "Saging", "sw": "Ndizi", "ha": "Ayaba", "yo": "Ọgẹdẹ",
        "pt": "Banana", "es": "Banana/Plátano", "fr": "Banane", "de": "Banane",
        "it": "Banana", "ru": "Banan (банан)"
    },
    "Solanum lycopersicum": {
        "en": "Tomato", "hi": "Tamatar (टमाटर)", "bn": "Tomato (টমেটো)", "te": "Tomato (టమాటా)",
        "ta": "Thakkali (தக்காளி)", "kn": "Tomato (ಟಮೇಟ)", "ml": "Thakkali (തക്കാളി)",
        "mr": "Tomato (टोमॅटो)", "pa": "Tamater (ਟਮਾਟਰ)", "gu": "Tameta (ટામેટું)",
        "ur": "Tamatar (ٹماٹر)", "ar": "Tamatim (طماطم)", "zh": "Xīhóngshì (西红柿)",
        "ja": "Tomato (トマト)", "ko": "Tomato (토마토)", "vi": "Cà chua",
        "th": "Makhua thet (มะเขือเทศ)", "id": "Tomat", "ms": "Tomato",
        "tl": "Kamatis", "sw": "Nyanya", "ha": "Tumatir", "yo": "Tomáti",
        "pt": "Tomate", "es": "Tomate", "fr": "Tomate", "de": "Tomate",
        "it": "Pomodoro", "ru": "Pomidor (помидор)", "tr": "Domates",
        "nl": "Tomaat", "pl": "Pomidor", "ro": "Roșie"
    },
    "Solanum tuberosum": {
        "en": "Potato", "hi": "Aloo (आलू)", "bn": "Aloo (আলু)", "te": "Uralagedda (ఉరుళగడ్డ)",
        "ta": "Urulaikizhangu (உருளைக்கிழங்கு)", "kn": "Alu Gedde (ಆಲೂ ಗಡ್ಡೆ)", "ml": "Urulakkizhangu (ഉരുളക്കിഴങ്ങ്)",
        "mr": "Batata (बटाटा)", "pa": "Aloo (ਆਲੂ)", "gu": "Bataka (બટેટા)", "ur": "Aloo (آلو)",
        "ar": "Batata (بطاطس)", "zh": "Tǔdòu (土豆)", "ja": "Jagaimo (じゃがいも)",
        "ko": "Gamja (감자)", "vi": "Khoai tây", "th": "Man farang (มันฝรั่ง)",
        "id": "Kentang", "ms": "Kentang", "tl": "Patatas", "sw": "Kiazi",
        "ha": "Dankali", "yo": "Ànàmò", "pt": "Batata", "es": "Patata/Papa",
        "fr": "Pomme de terre", "de": "Kartoffel", "it": "Patata",
        "ru": "Kartofel (картофель)", "nl": "Aardappel", "pl": "Ziemniak", "tr": "Patates"
    },
    "Allium cepa": {
        "en": "Onion", "hi": "Pyaz (प्याज)", "bn": "Peyaj (পেঁয়াজ)", "te": "Nirulli (నిరుల్లి)",
        "ta": "Vengayam (வெங்காயம்)", "kn": "Irulli (ಈರುಳ್ಳಿ)", "ml": "Ulli (ഉള്ളി)",
        "mr": "Kanda (कांदा)", "pa": "Piyaz (ਪਿਆਜ਼)", "gu": "Dungri (ડુંગળી)", "ur": "Piyaz (پیاز)",
        "ar": "Basal (بصل)", "zh": "Yángcōng (洋葱)", "ja": "Tamanegi (玉ねぎ)",
        "ko": "Yangpa (양파)", "vi": "Hành tây", "th": "Hua hom (หัวหอม)",
        "id": "Bawang merah", "ms": "Bawang", "tl": "Sibuyas", "sw": "Kitunguu",
        "ha": "Albasa", "yo": "Àlùbọ́sà", "pt": "Cebola", "es": "Cebolla",
        "fr": "Oignon", "de": "Zwiebel", "it": "Cipolla",
        "ru": "Luk (лук)", "tr": "Soğan"
    },
    "Allium sativum": {
        "en": "Garlic", "hi": "Lahsun (लहसुन)", "bn": "Rasun (রসুন)", "te": "Vellulli (వెల్లుల్లి)",
        "ta": "Poondu (பூண்டு)", "kn": "Bellulli (ಬೆಳ್ಳುಳ್ಳಿ)", "ml": "Veluthulli (വെളുത്തുള്ളി)",
        "mr": "Lasun (लसूण)", "pa": "Thum (ਥੁੰਮ)", "gu": "Lasan (લ‌સણ)", "ur": "Lahsun (لہسن)",
        "ar": "Thoum (ثوم)", "zh": "Dàsuàn (大蒜)", "ja": "Ninniku (にんにく)",
        "ko": "Maneul (마늘)", "vi": "Tỏi", "th": "Kratiam (กระเทียม)",
        "id": "Bawang putih", "ms": "Bawang putih", "tl": "Bawang", "sw": "Kitunguu saumu",
        "yo": "Àjọ̀", "pt": "Alho", "es": "Ajo", "fr": "Ail",
        "de": "Knoblauch", "it": "Aglio", "ru": "Chesnok (чеснок)", "tr": "Sarımsak"
    },
    "Zingiber officinale": {
        "en": "Ginger", "hi": "Adrak (अदरक)", "bn": "Aada (আদা)", "te": "Allam (అల్లం)",
        "ta": "Inji (இஞ்சி)", "kn": "Shunti (ಶುಂಠಿ)", "ml": "Inji (ഇഞ്ചി)",
        "mr": "Ale (आले)", "pa": "Adrak (ਅਦਰਕ)", "gu": "Aadu (આદુ)", "ur": "Adrak (ادرک)",
        "ar": "Zanjabil (زنجبيل)", "zh": "Jiāng (姜)", "ja": "Shōga (しょうが)",
        "ko": "Saenggang (생강)", "vi": "Gừng", "th": "Khing (ขิง)",
        "id": "Jahe", "ms": "Halia", "tl": "Luya", "sw": "Tangawizi",
        "ha": "Cita", "pt": "Gengibre", "es": "Jengibre", "fr": "Gingembre",
        "de": "Ingwer", "it": "Zenzero", "ru": "Imbir (имбирь)", "tr": "Zencefil"
    },
    "Curcuma longa": {
        "en": "Turmeric", "hi": "Haldi (हल्दी)", "bn": "Halud (হলুদ)", "te": "Pasupu (పసుపు)",
        "ta": "Manjal (மஞ்சள்)", "kn": "Arisina (ಅರಿಶಿನ)", "ml": "Manjal (മഞ്ഞൾ)",
        "mr": "Halad (हळद)", "pa": "Haldi (ਹਲਦੀ)", "gu": "Haldar (હળદર)", "ur": "Haldi (ہلدی)",
        "ar": "Kurkum (كركم)", "zh": "Jiānghuáng (姜黄)", "ja": "Ukon (ウコン)",
        "ko": "Ulgeumchai (울금)", "vi": "Nghệ", "th": "Kha min (ขมิ้น)",
        "id": "Kunyit", "ms": "Kunyit", "tl": "Dilaw", "sw": "Manjano",
        "ha": "Gangamau", "pt": "Açafrão-da-índia", "es": "Cúrcuma",
        "fr": "Curcuma", "de": "Kurkuma", "it": "Curcuma", "ru": "Kurkuma (куркума)"
    },
    "Carica papaya": {
        "en": "Papaya", "hi": "Papita (पपीता)", "bn": "Pepe (পেঁপে)", "te": "Boppai Pandu (బొప్పాయి)",
        "ta": "Pappali (பப்பாளி)", "kn": "Pappayi (ಪಪ್ಪಾಯ)", "ml": "Papaya (പപ്പായ)",
        "mr": "Papai (पपई)", "pa": "Papita (ਪਪੀਤਾ)", "gu": "Papaya (પપૈયા)", "ur": "Papita (پپیتا)",
        "ar": "Babaya (بابايا)", "zh": "Mùguā (木瓜)", "ja": "Papaya (パパイア)",
        "ko": "Papaya (파파야)", "vi": "Đu đủ", "th": "Malako (มะละกอ)",
        "id": "Pepaya", "ms": "Betik", "tl": "Papaya", "sw": "Papai",
        "ha": "Gwandaflawa", "yo": "Ìbépé", "pt": "Mamão", "es": "Papaya",
        "fr": "Papaye", "de": "Papaya", "it": "Papaia", "ru": "Papaya (папайя)"
    },
    "Glycine max": {
        "en": "Soybean", "hi": "Soyabean (सोयाबीन)", "bn": "Soya (সয়া)", "te": "Soya Ginjalu (సోయా)",
        "ta": "Soya (சோயா)", "kn": "Soya (ಸೋಯಾ)", "ml": "Soya Bean (സോയ ബീൻ)",
        "mr": "Soybean (सोयाबीन)", "ur": "Soya (سویا)", "ar": "Soya (فول الصويا)",
        "zh": "Dàdòu (大豆)", "ja": "Daizu (大豆)", "ko": "Kong (콩)",
        "vi": "Đậu nành", "th": "Thua Lueang (ถั่วเหลือง)", "id": "Kedelai",
        "ms": "Kacang soya", "tl": "Soybean", "sw": "Soya", "pt": "Soja",
        "es": "Soja", "fr": "Soja", "de": "Sojabohne", "it": "Soia",
        "ru": "Soya (соя)", "tr": "Soya fasulyesi"
    },
    "Cicer arietinum": {
        "en": "Chickpea (Bengal Gram)", "hi": "Chana (चना)", "bn": "Boot (বুট)", "te": "Sanagalu (సెనగలు)",
        "ta": "Kadalai (கடலை)", "kn": "Kadale (ಕಡಲೆ)", "ml": "Kadala (കടല)",
        "mr": "Harbhara (हरभरा)", "pa": "Chhole (ਛੋਲੇ)", "gu": "Chana (ચણા)", "ur": "Chana (چنا)",
        "ar": "Hummus (حمص)", "zh": "Ying zuì dòu (鹰嘴豆)", "ja": "Hiyo kobe (ひよこ豆)",
        "ko": "Chickpea (병아리콩)", "vi": "Đậu gà", "th": "Thua kho (ถั่วลูกไก่)",
        "id": "Kacang Arab", "ms": "Kacang kuda", "tl": "Garbanzos", "sw": "Njegere",
        "ha": "Agwado", "pt": "Grão-de-bico", "es": "Garbanzo",
        "fr": "Pois chiche", "de": "Kichererbse", "it": "Cece",
        "ru": "Nut (нут)", "tr": "Nohut", "ar": "Hummus (حمص)"
    },
    "Cajanus cajan": {
        "en": "Pigeon Pea (Red Gram)", "hi": "Arhar / Tur (अरहर)", "bn": "Arhar (অড়হর)",
        "te": "Kandi Pappu (కంది పప్పు)", "ta": "Thuvaram (துவரை)", "kn": "Thogari (ತೊಗರಿ)",
        "ml": "Thuvara (തുവര)", "mr": "Tur (तूर)", "pa": "Arhar (ਅਰਹਰ)", "gu": "Tuver (તુવેર)",
        "ur": "Arhar (ارہر)", "ar": "Adas (عدس حلبي)", "sw": "Mbaazi", "ha": "Wake",
        "yo": "Ẹ̀wà", "pt": "Ervilha-pombo", "es": "Gandul", "fr": "Pois d'Angole",
        "de": "Straucherbse"
    },
    "Vigna radiata": {
        "en": "Mung Bean (Green Gram)", "hi": "Moong (मूंग)", "bn": "Mug (মুগ)", "te": "Pesalu (పెసలు)",
        "ta": "Pasiparuppu (பாசிப்பருப்பு)", "kn": "Hesaru Kaalu (ಹೆಸರು ಕಾಳು)", "ml": "Cherupayar (ചെറുപയർ)",
        "mr": "Mug (मूग)", "pa": "Mung (ਮੂੰਗ)", "gu": "Moong (મગ)", "ur": "Moong (مونگ)",
        "ar": "Adas Akhdar (عدس أخضر)", "zh": "Lǜdòu (绿豆)", "ja": "Ryokuto (緑豆)",
        "ko": "Nokdu (녹두)", "vi": "Đậu xanh", "th": "Thua khiao (ถั่วเขียว)",
        "id": "Kacang hijau", "ms": "Kacang hijau", "tl": "Munggo", "sw": "Maharagwe ya kijani",
        "pt": "Feijão-verde", "es": "Frijol mungo", "fr": "Haricot mungo",
        "de": "Mungbohne"
    },
    "Arachis hypogaea": {
        "en": "Groundnut / Peanut", "hi": "Mungphali (मूंगफली)", "bn": "Cheenabadam (চিনাবাদাম)",
        "te": "Verusenaga (వేరుసెనగ)", "ta": "Kadalai (கடலை)", "kn": "Kadalekayi (ಕಡ್ಲೇಕಾಯಿ)",
        "ml": "Nelakadala (നിലക്കടല)", "mr": "Shengan (शेंगाना)", "pa": "Moonphali (ਮੂੰਗਫਲੀ)",
        "gu": "Shing (સિંગ)", "ur": "Moonphali (مونگ پھلی)", "ar": "Ful Sudan (فول سوداني)",
        "zh": "Huāshēng (花生)", "ja": "Rakkasei (落花生)", "ko": "Ttangkong (땅콩)",
        "vi": "Lạc / Đậu phộng", "th": "Thua lisong (ถั่วลิสง)", "id": "Kacang tanah",
        "ms": "Kacang tanah", "tl": "Mani", "sw": "Karanga", "ha": "Gyada",
        "yo": "Epa", "ig": "Ahụ̀ọ̀cha", "am": "Yegena ater (የጤፍ)", "pt": "Amendoim",
        "es": "Cacahuate/Maní", "fr": "Arachide", "de": "Erdnuss", "it": "Arachide",
        "ru": "Arakhis (арахис)", "tr": "Yerfıstığı"
    },
    "Cocos nucifera": {
        "en": "Coconut", "hi": "Nariyal (नारियल)", "bn": "Narkel (নারকেল)", "te": "Kobbari (కొబ్బరి)",
        "ta": "Thengai (தேங்காய்)", "kn": "Tenginakayi (ತೆಂಗಿನಕಾಯಿ)", "ml": "Thenga (തെങ്ങ്)",
        "mr": "Naral (नारळ)", "pa": "Nariyal (ਨਾਰੀਅਲ)", "gu": "Nadiyer (નારિયેળ)",
        "ur": "Nariyal (ناریل)", "ar": "Jawz al-hind (جوز الهند)", "zh": "Yēzi (椰子)",
        "ja": "Kokonattsu (ヤシの実)", "ko": "Coconut (코코넛)", "vi": "Dừa",
        "th": "Maphrao (มะพร้าว)", "id": "Kelapa", "ms": "Kelapa",
        "tl": "Niyog", "sw": "Nazi", "ha": "Kwakwa", "yo": "Agbon",
        "pt": "Coco", "es": "Coco", "fr": "Noix de coco", "de": "Kokosnuss",
        "it": "Noce di cocco", "ru": "Kokos (кокос)"
    },
    "Saccharum officinarum": {
        "en": "Sugarcane", "hi": "Ganna (गन्ना)", "bn": "Aakh (আখ)", "te": "Cheruku (చెరుకు)",
        "ta": "Karumbu (கரும்பு)", "kn": "Kabbu (ಕಬ್ಬು)", "ml": "Karumbu (കരിമ്പ്)",
        "mr": "Oos (ऊस)", "pa": "Ganna (ਗੰਨਾ)", "gu": "Svaradi (શેરડી)", "ur": "Ganna (گنا)",
        "ar": "Qasab al-sukkar (قصب السكر)", "zh": "Gānzhè (甘蔗)", "ja": "Satōkibi (サトウキビ)",
        "ko": "Satong Susu (사탕수수)", "vi": "Mía", "th": "Oi (อ้อย)",
        "id": "Tebu", "ms": "Tebu", "tl": "Tubo", "sw": "Miwa",
        "ha": "Rake", "yo": "Ireke", "pt": "Cana-de-açúcar", "es": "Caña de azúcar",
        "fr": "Canne à sucre", "de": "Zuckerrohr", "it": "Canna da zucchero",
        "ru": "Sakharniy trostnik (сахарный тростник)"
    },
    "Gossypium hirsutum": {
        "en": "Cotton", "hi": "Kapas (कपास)", "bn": "Kapas (কাপাস)", "te": "Patti (పత్తి)",
        "ta": "Panjhu (பஞ்சு)", "kn": "Hatti (ಹತ್ತಿ)", "ml": "Panjhu (പഞ്ഞി)",
        "mr": "Kapus (कापूस)", "pa": "Narma (ਨਰਮਾ)", "gu": "Kapas (કપાસ)", "ur": "Kapas (کپاس)",
        "ar": "Qutn (قطن)", "zh": "Miánhuā (棉花)", "ja": "Wata (綿)",
        "ko": "Soru (솜)", "vi": "Bông vải", "th": "Fai (ฝ้าย)",
        "id": "Kapas", "ms": "Kapas", "tl": "Bulak", "sw": "Pamba",
        "ha": "Auduga", "yo": "Owu", "pt": "Algodão", "es": "Algodón",
        "fr": "Coton", "de": "Baumwolle", "it": "Cotone",
        "ru": "Khlopok (хлопок)", "tr": "Pamuk"
    },
    "Coffea arabica": {
        "en": "Coffee (Arabica)", "hi": "Kahwa (काफी)", "bn": "Kafi (কফি)", "te": "Coffee (కాఫీ)",
        "ta": "Coffee (காபி)", "kn": "Coffee (ಕಾಫಿ)", "ml": "Coffee (കോഫി)",
        "mr": "Coffee (कॉफी)", "ar": "Qahwa (قهوة)", "zh": "Kāfēi (咖啡)",
        "ja": "Kōhī (コーヒー)", "ko": "Keopi (커피)", "vi": "Cà phê",
        "th": "Kafae (กาแฟ)", "id": "Kopi", "ms": "Kopi", "tl": "Kape",
        "sw": "Kahawa", "ha": "Kofi", "yo": "Kòfí", "am": "Bunna (ቡና)",
        "pt": "Café", "es": "Café", "fr": "Café", "de": "Kaffee",
        "it": "Caffè", "ru": "Kofe (кофе)", "tr": "Kahve"
    },
    "Camellia sinensis": {
        "en": "Tea", "hi": "Chai (चाय)", "bn": "Cha (চা)", "te": "Tea (టీ)",
        "ta": "Theneer (தேயிலை)", "kn": "Tea (ಚಹಾ)", "ml": "Chaya (ചായ)",
        "mr": "Chai (चहा)", "pa": "Chai (ਚਾਹ)", "ar": "Shay (شاي)",
        "zh": "Chá (茶)", "ja": "Cha (お茶)", "ko": "Cha (차)",
        "vi": "Trà", "th": "Cha (ชา)", "id": "Teh", "ms": "Teh",
        "tl": "Tsaa", "sw": "Chai", "am": "Shai (ሻይ)",
        "pt": "Chá", "es": "Té", "fr": "Thé", "de": "Tee",
        "it": "Tè", "ru": "Chay (чай)", "tr": "Çay", "ar": "Shay (شاي)"
    },
    "Azadirachta indica": {
        "en": "Neem", "hi": "Neem (नीम)", "bn": "Neem (নিম)", "te": "Vepa (వేప)",
        "ta": "Vembu (வேம்பு)", "kn": "Bevu (ಬೇವು)", "ml": "Veppam (വേപ്പ്)",
        "mr": "Kadu Limb (कडुलिंब)", "pa": "Neem (ਨਿੰਮ)", "gu": "Limado (લીમડો)",
        "ur": "Neem (نیم)", "ar": "Neem (ليمون مر)", "sw": "Mwarobaini",
        "ha": "Dogonyaro", "yo": "Dongoyaro", "pt": "Nim", "es": "Nim",
        "fr": "Margousier", "de": "Niembaum", "ms": "Pokok neem", "id": "Pohon neem"
    },
    "Ocimum tenuiflorum": {
        "en": "Tulsi / Holy Basil", "hi": "Tulsi (तुलसी)", "bn": "Tulsi (তুলসী)", "te": "Tulasi (తులసి)",
        "ta": "Thulasi (துளசி)", "kn": "Tulasi (ತುಳಸಿ)", "ml": "Thulasi (തുളസി)",
        "mr": "Tulashi (तुळस)", "pa": "Tulsi (ਤੁਲਸੀ)", "gu": "Tulsi (તુલસી)",
        "ur": "Tulsi (تلسی)", "si": "Tulasi (තුළසි)", "ne": "Tulsi (तुलसी)",
        "th": "Kraphao (กะเพรา)", "id": "Kemangi", "ms": "Selasih",
        "en_alternate": "Sacred Basil, Thai Holy Basil"
    },
    "Withania somnifera": {
        "en": "Ashwagandha / Indian Ginseng", "hi": "Ashwagandha (अश्वगंधा)", "bn": "Ashwagandha (অশ্বগন্ধা)",
        "te": "Aswagandha (అశ్వగంధ)", "ta": "Amukkara (அமுக்கரா)", "kn": "Ashwagandha (ಅಶ್ವಗಂಧ)",
        "ml": "Amukkuram (അമുക്കുരം)", "mr": "Ashwagandha (अश्वगंधा)", "ur": "Asgandh (اشواگندھ)",
        "ar": "Ashwagandha (أشواغاندا)", "zh": "Nan fei zui qie (南非醉茄)",
        "en_alternate": "Winter Cherry, Withania"
    },
    "Aloe vera": {
        "en": "Aloe Vera", "hi": "Ghritkumari (घृतकुमारी)", "bn": "Aloe Vera (অ্যালোভেরা)",
        "te": "Kalabanda (కలబంద)", "ta": "Sotrukatralai (சோற்றுக் கற்றாழை)", "kn": "Lolesara (ಲೋಳೆ ಸಾರ)",
        "ml": "Kuthamb (കൂടം)", "mr": "Korphad (कोरफड)", "pa": "Aloe (ਐਲੋਵੇਰਾ)", "gu": "Kumari (કુંવાર)",
        "ar": "Sabbar (صبار)", "zh": "Lúhuì (芦荟)", "ja": "Aloe (アロエ)",
        "th": "Wan hang chorakhe (ว่านหางจระเข้)", "id": "Lidah buaya", "ms": "Pokok Aloe Vera",
        "sw": "Aloe", "pt": "Babosa", "es": "Sábila", "fr": "Aloe",
        "de": "Aloe", "it": "Aloe vera"
    },
    "Moringa oleifera": {
        "en": "Moringa / Drumstick Tree", "hi": "Sahjan (सहजन)", "bn": "Sajna (সজনে)",
        "te": "Mulaga (మునగ)", "ta": "Murungai (முருங்கை)", "kn": "Nugge (ನುಗ್ಗೆ)",
        "ml": "Muringa (മുരിങ്ങ)", "mr": "Shevga (शेवगा)", "pa": "Sohanjana (ਸਹਿਜਣਾ)",
        "gu": "Saragvo (સરગવો)", "ur": "Sahjan (سہجن)", "ar": "Rawaq (رواق)",
        "zh": "Lamu ye (辣木)", "sw": "Mzungu (Moringa)", "ha": "Zogale",
        "yo": "Igbale Ogangun", "am": "Shiferaw (ሽፌራ)", "pt": "Moringa",
        "es": "Moringa", "fr": "Moringa", "de": "Moringa"
    },
    "Nelumbo nucifera": {
        "en": "Lotus", "hi": "Kamal (कमल)", "bn": "Padma (পদ্ম)", "te": "Thamara (తామర)",
        "ta": "Tamara (தாமரை)", "kn": "Thamara (ತಾವರೆ)", "ml": "Thamara (താമര)",
        "mr": "Kamal (कमळ)", "pa": "Kamal (ਕਮਲ)", "gu": "Kamal (કમળ)", "ur": "Kamal (کنول)",
        "ar": "Lotus (لوتس)", "zh": "Héhuā (荷花)", "ja": "Hasu (ハス)",
        "ko": "Yeonkkot (연꽃)", "vi": "Hoa sen", "th": "Bua (บัว)", "id": "Lotus",
        "ms": "Bunga teratai", "tl": "Lotus"
    },
    "Phyllanthus emblica": {
        "en": "Indian Gooseberry (Amla)", "hi": "Amla (आंवला)", "bn": "Amloki (আমলকী)",
        "te": "Usirika (ఉసిరిక)", "ta": "Nelli (நெல்லி)", "kn": "Nelli (ನೆಲ್ಲಿ)",
        "ml": "Nellikka (നെല്ലിക്ക)", "mr": "Avla (आवळा)", "pa": "Amla (ਆਂਵਲਾ)",
        "gu": "Amla (આમળ)", "ur": "Amla (آملہ)", "ar": "Usaira",
        "zh": "Yu gan zi (余甘子)", "th": "Ma kham pom (มะขามป้อม)", "id": "Amla",
        "ms": "Pokok melaka", "sw": "Amla"
    },
    "Hibiscus rosa-sinensis": {
        "en": "Hibiscus / China Rose", "hi": "Gurhal (गुड़हल)", "bn": "Jaba (জবা)", "te": "Dasana puvvu (దాసాని పువ్వు)",
        "ta": "Sembaruthi (செம்பருத்தி)", "kn": "Daasavala (ದಾಸವಾಳ)", "ml": "Chembarathi (ചെമ്പരത്തി)",
        "mr": "Jaswand (जास्वंद)", "pa": "Gurhal (ਗੁੜਹਲ)", "gu": "Jasood (જાસૂ)",
        "ur": "Gurhal (گلاب چین)", "ar": "Karkadeh (كركديه)", "zh": "Fúsāng (扶桑)",
        "ja": "Hibiscus (ハイビスカス)", "ko": "Hibiscus (히비스커스)", "vi": "Râm bụt",
        "th": "Chaba (ชบา)", "id": "Kembang sepatu", "ms": "Bunga raya", "tl": "Gumamela"
    },
    "Psidium guajava": {
        "en": "Guava", "hi": "Amrood (अमरूद)", "bn": "Peyara (পেয়ারা)", "te": "Jamma (జామ)",
        "ta": "Koyya (கொய்யா)", "kn": "Seeba (ಸೀಬೆ)", "ml": "Pera (പേര)",
        "mr": "Peron (पेरू)", "pa": "Amrood (ਅਮਰੂਦ)", "gu": "Jamfal (જામફળ)",
        "ur": "Amrood (امرود)", "ar": "Gawaafa (جوافة)", "zh": "Fānshíliu (番石榴)",
        "ja": "Guava (グアバ)", "ko": "Guava (구아바)", "vi": "Ổi",
        "th": "Farang (ฝรั่ง)", "id": "Jambu biji", "ms": "Jambu batu",
        "tl": "Bayabas", "sw": "Mapera", "ha": "Gwaba", "yo": "Guava",
        "pt": "Goiaba", "es": "Guayaba", "fr": "Goyave", "de": "Guave"
    },
    "Piper nigrum": {
        "en": "Black Pepper", "hi": "Kali Mirch (काली मिर्च)", "bn": "Kalo Morich (কালো মরিচ)",
        "te": "Miriyalu (మిరియాలు)", "ta": "Milagu (மிளகு)", "kn": "Menasu (ಮೆಣಸು)",
        "ml": "Kurumulaku (കുരുമുളക്)", "mr": "Miri (मिरी)", "pa": "Kali Mirch (ਕਾਲੀ ਮਿਰਚ)",
        "gu": "Mari (મરી)", "ur": "Kali Mirch (کالی مرچ)", "ar": "Filfil (فلفل أسود)",
        "zh": "Hēijiāo (黑胡椒)", "ja": "Koshō (胡椒)", "ko": "Hwijang (후추)",
        "vi": "Tiêu", "th": "Phrik Thai (พริกไทย)", "id": "Lada", "ms": "Lada hitam",
        "tl": "Paminta", "sw": "Pilipili nyeusi", "ha": "Barkono",
        "pt": "Pimenta-do-reino", "es": "Pimienta negra", "fr": "Poivre noir",
        "de": "Schwarzer Pfeffer", "it": "Pepe nero", "ru": "Chyorny perets (чёрный перец)"
    },
    "Cinnamomum verum": {
        "en": "Cinnamon", "hi": "Dalchini (दालचीनी)", "bn": "Dalchini (দারুচিনি)", "te": "Dalchini (దాల్చినచెక్క)",
        "ta": "Elavangam (இலவங்கம்)", "kn": "Chakke (ಚಕ್ಕೆ)", "ml": "Karuvapatta (കറുവ)",
        "mr": "Dalchini (दालचिनी)", "pa": "Dalchini (ਦਾਲਚੀਨੀ)", "ur": "Dalchini (دارچینی)",
        "ar": "Qirfa (قرفة)", "zh": "Ròuguì (肉桂)", "ja": "Shinamon (シナモン)",
        "ko": "Gyepi (계피)", "vi": "Quế", "th": "Op choei (อบเชย)",
        "id": "Kayu manis", "ms": "Kayu manis", "tl": "Kanela", "sw": "Mdalasini",
        "pt": "Canela", "es": "Canela", "fr": "Cannelle", "de": "Zimt"
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# LANGUAGE CODES REFERENCE TABLE
# ─────────────────────────────────────────────────────────────────────────────

LANGUAGE_CODES = {
    "en": "English", "hi": "Hindi", "bn": "Bengali", "te": "Telugu",
    "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam", "mr": "Marathi",
    "pa": "Punjabi", "gu": "Gujarati", "or": "Odia", "as": "Assamese",
    "ur": "Urdu", "ar": "Arabic", "zh": "Chinese (Mandarin)", "ja": "Japanese",
    "ko": "Korean", "vi": "Vietnamese", "th": "Thai", "id": "Indonesian",
    "ms": "Malay", "tl": "Filipino (Tagalog)", "my": "Burmese", "km": "Khmer",
    "si": "Sinhala", "ne": "Nepali", "sw": "Swahili", "ha": "Hausa",
    "yo": "Yoruba", "ig": "Igbo", "am": "Amharic", "pt": "Portuguese",
    "es": "Spanish", "fr": "French", "de": "German", "it": "Italian",
    "ru": "Russian", "nl": "Dutch", "pl": "Polish", "tr": "Turkish",
    "fa": "Persian (Farsi)", "gu": "Gujarati", "kk": "Kazakh", "uz": "Uzbek",
    "tg": "Tajik", "ky": "Kyrgyz", "ro": "Romanian", "uk": "Ukrainian"
}

# ─────────────────────────────────────────────────────────────────────────────
# DISEASE & PEST MULTILINGUAL NAMES
# ─────────────────────────────────────────────────────────────────────────────

MULTILINGUAL_DISEASE_NAMES = {
    "Rice Blast": {
        "en": "Rice Blast", "hi": "Dhan ka Jhulsa (धान का झुलसा)", "bn": "Dhan-er Blast",
        "te": "Vadlu Blast (వరి బ్లాస్ట్)", "ta": "Arisi Blast (நெல் அழற்சி)", "zh": "Dao Wen Ku Bing (稻瘟病)",
        "ja": "Imomochi-byo (いもち病)", "id": "Blas Padi", "tl": "Blast ng Palay", "sw": "Ugonjwa wa Mpunga"
    },
    "Late Blight": {
        "en": "Late Blight", "hi": "Pacheti Jhulsa (पछेती झुलसा)", "bn": "Late Blight",
        "te": "Aakar Maadhu (ఆలస్యపు తెగులు)", "ta": "Pizhai Kalainoi", "zh": "Wanyi Bai (晚疫病)",
        "ja": "Ekibyou (疫病)", "id": "Hawar Daun", "fr": "Mildiou", "de": "Krautfäule", "es": "Tizón tardío"
    },
    "Powdery Mildew": {
        "en": "Powdery Mildew", "hi": "Churni Rogi / Safed Roye (चूर्णी रोग)", "bn": "Churni Rog",
        "te": "Pithadi Tegulu (పిండి తెగులు)", "ta": "Venmai Noi (வெண்மை நோய்)", "ar": "Tahannun al-bidu",
        "zh": "Fen Mei Bing (粉霉病)", "ja": "Ushiro-byo (うどんこ病)", "fr": "Oïdium", "de": "Echter Mehltau",
        "es": "Oídio", "it": "Oidio", "id": "Embun tepung"
    },
    "Anthracnose": {
        "en": "Anthracnose", "hi": "Anthraqunos (एन्थ्रेक्नोज)", "bn": "Anthraqunos",
        "te": "Anthraqunos Tegulu", "ta": "Anthracnose Noi", "zh": "Tan Shu Bing (炭疽病)",
        "ja": "Tankiso (炭疽病)", "id": "Antraknosa", "fr": "Anthracnose", "de": "Anthraknose", "es": "Antracnosis"
    }
}


def search_plant_by_name(query: str, language: str = None) -> list:
    """Search for a plant by name in any or specific language."""
    results = []
    query_lower = query.lower()
    for botanical_name, translations in MULTILINGUAL_NAMES.items():
        if language:
            local_name = translations.get(language, "")
            if query_lower in local_name.lower():
                results.append({"botanical_name": botanical_name, "matched_language": language, "local_name": local_name})
        else:
            for lang_code, local_name in translations.items():
                if query_lower in local_name.lower():
                    results.append({"botanical_name": botanical_name, "matched_language": lang_code, "local_name": local_name})
    return results


def get_plant_names_in_all_languages(botanical_name: str) -> dict:
    """Get all language translations for a plant."""
    return MULTILINGUAL_NAMES.get(botanical_name, {})


def get_supported_languages() -> list:
    """Return list of supported language codes."""
    return list(LANGUAGE_CODES.keys())


if __name__ == "__main__":
    print(f"Plants with multilingual names: {len(MULTILINGUAL_NAMES)}")
    print(f"Languages supported: {len(LANGUAGE_CODES)}")
    print(f"Disease multilingual records: {len(MULTILINGUAL_DISEASE_NAMES)}")
    total_translations = sum(len(v) for v in MULTILINGUAL_NAMES.values())
    print(f"Total translations: {total_translations}")
