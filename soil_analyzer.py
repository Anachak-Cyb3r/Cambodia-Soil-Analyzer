"""
Soil Analysis Module for Cambodia Soil Analyzer Bot

Uses Google Gemini AI to analyze soil images and provide
agricultural recommendations for Cambodian farmers
"""
import io
import time
from PIL import Image
import google.generativeai as genai
import config

# Configure Gemini AI
genai.configure(api_key=config.GEMINI_API_KEY)

CAMBODIA_SOIL_PROMPT_EN = """You are an expert soil scientist specializing in Cambodian agriculture.

FIRST: Check if this soil looks like it's from Cambodia (tropical climate, matching Cambodian soil colors/textures).

Cambodia has ONLY 5 soil types:
1. Sandy Shale - rocky/gravelly, mountains/coastal
2. Red/Basaltic - reddish/brown, Kampong Cham, Kratie, Pailin (very fertile)
3. Sandy - light colored, Pursat, Kampong Chhnang, Siem Reap
4. Clay/Alluvial - dark brown/black, Prey Veng, Svay Rieng, Kandal, Takeo (best for rice)
5. Alluvial Mixed - brown, riverbanks, Phnom Penh area (vegetables/fruits)

Format your response EXACTLY like this (ENGLISH ONLY):

[ONLY IF soil is NOT from Cambodia, start with: "⚠️ WARNING: This soil does NOT appear to be from Cambodia. It looks like [describe]. For accurate advice, please send a photo of Cambodian soil." Then STOP.]

[IF soil IS from Cambodia, skip warning and start directly with:]

🔍 SOIL TYPE
Type: [Which of the 5 Cambodian types]
Color: [Exact color]
Texture: [Describe texture]
Moisture: [Dry/moist/wet]
Found in: [Cambodian provinces]

⭐ QUALITY: [Excellent ⭐⭐⭐⭐⭐ / Good ⭐⭐⭐⭐ / Fair ⭐⭐⭐ / Poor ⭐⭐]
Why: [2 sentences explaining the quality and what affects it]

🌱 RECOMMENDED CROPS (4 crops)
1. [Crop name] - [Season] - [Why it works well]
2. [Crop name] - [Season] - [Why it works well]
3. [Crop name] - [Season] - [Why it works well]
4. [Crop name] - [Season] - [Why it works well]

💊 FERTILIZERS
Chemical: NPK [ratio] - Apply [when and how] - $[cost]/hectare
Organic: [Type] - Apply [amount] - $[cost]/hectare
Where: Agricultural shops in [specific towns]
Note: [Any special fertilizer advice]

🔧 SOIL IMPROVEMENT
1. [First improvement] - [How to do it] - $[cost]
2. [Second improvement] - [How to do it] - $[cost]
3. [Third improvement] - [How to do it] - $[cost]
Total: $[total cost]/hectare

⚠️ IMPORTANT TIPS
Don't plant: [Crops to avoid and why]
Main problem: [Biggest issue with this soil]
Water: [Water management advice]
Best season: [When to plant - specific months]

Be detailed and practical. ENGLISH ONLY."""

CAMBODIA_SOIL_PROMPT_KM = """អ្នកគឺជាទីប្រឹក្សាកសិកម្មសម្រាប់កសិករកម្ពុជា។ និយាយភាសាខ្មែរសាមញ្ញ ងាយយល់។

សំខាន់: ពិនិត្យមើលថាតើដីនេះមកពីកម្ពុជាឬអត់។

កម្ពុជាមានដី ៥ ប្រភេទ:
១. ដីខ្សាច់ - ស្រាល, ពោធិ៍សាត់ កំពង់ឆ្នាំង សៀមរាប
២. ដីក្រហម - ក្រហម, កំពង់ចាម ក្រចេះ ប៉ៃលិន (ល្អណាស់)
៣. ដីឥដ្ឋ/ដីល្បាប់ - ខ្មៅ, ព្រៃវែង ស្វាយរៀង កណ្តាល តាកែវ (ល្អដាំស្រូវ)
៤. ដីលាយ - ត្នោត, មាត់ទន្លេ ភ្នំពេញ (ល្អដាំបន្លែ)
៥. ដីភ្នំ - មានថ្ម, តំបន់ភ្នំ

សូមឆ្លើយតាមទម្រង់នេះ (ប្រើភាសាខ្មែរសាមញ្ញ):

[បើដីមិនមែនកម្ពុជា: "⚠️ ដីនេះមើលទៅមិនដូចដីកម្ពុជាទេ។ សូមផ្ញើរូបដីកម្ពុជា។" រួចបញ្ចប់។]

[បើជាដីកម្ពុជា:]

🔍 ប្រភេទដី
ប្រភេទ: [ដីខ្សាច់/ដីក្រហម/ដីឥដ្ឋ/ដីលាយ/ដីភ្នំ]
ពណ៌: [ពណ៌អ្វី]
លក្ខណៈ: [ពិពណ៌នាសាមញ្ញ]
ស្ងួតឬសើម: [ស្ងួត/សើម/លិច]
ខេត្ត: [ខេត្តណាខ្លះមានដីបែបនេះ]

⭐ គុណភាពដី
ពិន្ទុ: [ល្អបំផុត ⭐⭐⭐⭐⭐ / ល្អ ⭐⭐⭐⭐ / មធ្យម ⭐⭐⭐ / ខ្សោយ ⭐⭐]
មូលហេតុ: [ពន្យល់ងាយៗ ២ប្រយោគ]

🌱 ដំណាំល្អបំផុត (៤ ដំណាំ)
១. [ដំណាំ] - [រដូវវស្សា/ប្រាំង] - [ហេតុអ្វីល្អ]
២. [ដំណាំ] - [រដូវវស្សា/ប្រាំង] - [ហេតុអ្វីល្អ]
៣. [ដំណាំ] - [រដូវវស្សា/ប្រាំង] - [ហេតុអ្វីល្អ]
៤. [ដំណាំ] - [រដូវវស្សា/ប្រាំង] - [ហេតុអ្វីល្អ]

💊 ជីត្រូវប្រើ
ជីគីមី: NPK [លេខ] - ដាក់ពេល[ណា] - តម្លៃ $[ចំនួន]/ហិកតា
ជីធម្មជាតិ: [ប្រភេទ] - ដាក់[បរិមាណ] - តម្លៃ $[ចំនួន]/ហិកតា
ទិញបាននៅ: ហាងកសិកម្មក្នុង[ក្រុង]
ចំណាំ: [ដំបូន្មានពិសេស]

🔧 របៀបកែលម្អដី
១. [វិធីទី១] - [ធ្វើយ៉ាងណា] - ចំណាយ $[ចំនួន]
២. [វិធីទី២] - [ធ្វើយ៉ាងណា] - ចំណាយ $[ចំនួន]
៣. [វិធីទី៣] - [ធ្វើយ៉ាងណា] - ចំណាយ $[ចំនួន]
សរុប: $[ចំនួន]/ហិកតា

⚠️ ចំណុចសំខាន់
កុំដាំ: [ដំណាំអ្វីមិនល្អ - ហេតុផល]
បញ្ហា: [បញ្ហាធំបំផុត]
ទឹក: [គ្រប់គ្រងទឹកយ៉ាងណា]
ពេលដាំល្អ: [ខែណា]

ប្រើពាក្យសាមញ្ញ ងាយយល់ សម្រាប់កសិករ។ ភាសាខ្មែរតែប៉ុណ្ណោះ។"""


def analyze_soil_image(image_bytes, language='en'):
    """
    Analyze soil image using Google Gemini (FREE)
    
    Args:
        image_bytes: Image file bytes
        language: 'en' or 'km' for response language
    
    Returns:
        str: Analysis result
    """
    try:
        # Open and process image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Resize if too large (max 2048px)
        max_size = 2048
        if max(image.size) > max_size:
            ratio = max_size / max(image.size)
            new_size = tuple(int(dim * ratio) for dim in image.size)
            image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        # Select prompt based on language
        if language == 'km':
            prompt = CAMBODIA_SOIL_PROMPT_KM
        else:
            prompt = CAMBODIA_SOIL_PROMPT_EN
        
        # Use Gemini Flash (FREE and supports images)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Retry logic for rate limits
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = model.generate_content([prompt, image])
                return response.text
            except Exception as e:
                if "429" in str(e) and attempt < max_retries - 1:
                    # Rate limit hit, wait and retry
                    wait_time = (attempt + 1) * 10  # 10, 20, 30 seconds
                    print(f"Rate limit hit, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    raise
        
    except Exception as e:
        print(f"Error analyzing soil: {e}")
        raise
