import requests
from bs4 import BeautifulSoup
import pyttsx3

def read_website(url):
    try:
        # Pretend to be a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/140.0.7339.208 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts/styles
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ", strip=True)

        # Init speech engine
        engine = pyttsx3.init()
        engine.setProperty("rate", 180)
        engine.setProperty("volume", 1.0)

        print("🔊 Reading website content...\n")
        print(text[:1000], "...")  # preview

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Error:", e)


# Example
read_website("https://www.stickyminds.com/article/testers-innovators-adapting-qa-role-ai-era")
