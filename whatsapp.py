from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pyperclip  # You might need to install this: pip install pyperclip

# Initialize Chrome
driver = webdriver.Chrome()
baseurl = "https://web.whatsapp.com"
driver.get(baseurl)

# Fixed message template - using a single string
MESSAGE_TEMPLATE = """Bonjour,

Je suis Nabil, développeur web spécialisé dans la création de sites pour les sociétés de location de voitures.

Je propose des sites web professionnels et responsifs avec :
• Intégration WhatsApp pour une communication instantanée avec vos clients
• Formulaire de contact pour capturer des leads
• Personnalisation complète (logo, couleurs, services) adaptée à votre identité
• Design adapté à tous les appareils mobiles

De plus, je vous offre une stratégie efficace pour augmenter vos avis positifs sur Google Maps.

Vous pouvez consulter l'exemple de website ici : https://car-rental-rho-sandy.vercel.app/

Seriez-vous intéressé(e) par un échange sur la façon dont un site web personnalisé pourrait développer votre activité de location de voitures ?

Cordialement,
Nabil"""

# Wait for QR scan
print("Veuillez scanner le code QR dans les 40 secondes...")
time.sleep(40)

with open("contact.csv", newline='') as csvfile:
    readContacts = csv.reader(csvfile)
    for row in readContacts:
        if len(row) < 1:  # Check for at least phone number
            continue
            
        phone = row[0].strip()
        print(f"Envoi à: {phone}")

        try:
            # Open chat
            chat_url = f"{baseurl}/send?phone={phone}"
            driver.get(chat_url)
            
            # Wait for chat to load
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            
            # Find message box
            message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            
            # Use clipboard to paste the entire message at once (this preserves formatting better)
            pyperclip.copy(MESSAGE_TEMPLATE)
            message_box.send_keys(Keys.CONTROL + 'v')  # Paste from clipboard
            
            # Small delay to ensure the paste operation completes
            time.sleep(1)
            
            # Send message
            message_box.send_keys(Keys.RETURN)
            print(f"Message envoyé à {phone}")
            time.sleep(8)  # Wait between messages
            
        except Exception as e:
            print(f"Échec d'envoi à {phone}: {str(e)}")
            time.sleep(10)
            continue

driver.quit()
print("Tous les messages ont été traités")