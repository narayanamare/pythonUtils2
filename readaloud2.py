import asyncio
from playwright.async_api import async_playwright
import pyttsx3
from bs4 import BeautifulSoup

async def fetch_page_content(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                                "Chrome/118.0.0.0 Safari/537.36")

        # More reliable wait
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)

        html = await page.content()
        await browser.close()
        return html


def read_aloud(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)   # adjust speed
    engine.setProperty("volume", 1.0) # max volume
    print("🔊 Reading website content...\n")
    print(text[:1000], "...")  # preview
    engine.say(text)
    engine.runAndWait()


async def main():
    url = "https://www.stickyminds.com/article/testers-innovators-adapting-qa-role-ai-era"

    # Get page HTML
    html = await fetch_page_content(url)

    # Extract text
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text(separator=" ", strip=True)

    # Read aloud
    read_aloud(text)


if __name__ == "__main__":
    asyncio.run(main())
