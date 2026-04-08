# Wilk-z-Sokatesa
import os
import time
import urllib.request
import xml.etree.ElementTree as ET
from google import genai

# ==========================================
# 1. KONFIGURACJA Z BEZPIECZNYM KLUCZEM
# ==========================================
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Brak klucza API! Dodaj GEMINI_API_KEY do GitHub Secrets.")

client = genai.Client(api_key=API_KEY)

# ==========================================
# 2. POBIERANIE DANYCH (Skaner RSS)
# ==========================================
def pobierz_newsy(ticker):
    print(f"[*] Omijamy blokady... Zasysam nagłówki RSS dla: {ticker}...")
    url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"
    
    tekst_newsow = ""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        
        count = 0
        for item in root.findall('.//item'):
            if count >= 5: break
            title = item.find('title').text
            tekst_newsow += f"- {title}\n"
            count += 1
            
    except Exception as e:
        print(f"Błąd RSS: {e}")
        return ""
        
    return tekst_newsow

# ==========================================
# 3. ANALIZA AI
# ==========================================
def analizuj_z_gemini(ticker, newsy):
    print("[*] Gemini mieli dane. Czekaj...")
    
    prompt = f"""
    Jesteś bezlitosnym analitykiem giełdowym. 
    Masz przed sobą najświeższe nagłówki dotyczące spółki {ticker}:
    
    {newsy}
    
    Twoje zadanie:
    1. Sentyment (Byczy / Niedźwiedzi / Neutralny).
    2. Ocena od 1 do 10 (1 - uciekaj, 10 - kupuj).
    3. Jedno zdanie brutalnie szczerego komentarza dla inwestora, który ma tylko 1000 PLN kapitału.
    """
    
    for proba in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            if '503' in str(e) or 'UNAVAILABLE' in str(e):
                print(f"[!] Serwery przeciążone (próba {proba+1}/3). Czekam 10 sekund...")
                time.sleep(10)
            else:
                return f"Krytyczny błąd: {e}"
                
    return "Serwery padły pod natłokiem zapytań."

# ==========================================
# 4. START MASZYNY
# ==========================================
cel = "MSFT" 
dane = pobierz_newsy(cel)

if dane:
    raport = analizuj_z_gemini(cel, dane)
    print("\n" + "="*30)
    print("📈 RAPORT WILKA Z WALL STREET 📉")
    print("="*30)
    print(raport)
else:
    print("Brak świeżych wiadomości do analizy. Rynek śpi.")
