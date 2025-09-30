---

```markdown
# 🐍 Python Utils 2

A collection of Python utility scripts and experiments for automation, data processing, visualization, translation, and multimedia tasks.  
This repo is a **toolbox of independent scripts** — each utility solves a specific problem and can be used standalone or imported into your own projects.

---

## 📂 Repository Structure

```

pythonUtils2/
│
├── audio_tools/
│   ├── readaloud.py          # Read website text aloud (requests + TTS)
│   ├── readaloud2.py         # Playwright-based web read-aloud
│
├── web_tools/
│   ├── GoogleMapsSearch.py   # Automate Google Maps search & scrape
│   ├── GooglePlaces.py       # Extract business details via Google Places
│   ├── ClickAndExtractListings.py  # Click-through scraping utility
│
├── video_tools/
│   ├── movietext.py          # Add text overlay to video
│   ├── movietxt3.py
│
├── translate_tools/
│   ├── TranslateEngtoMar.py  # English → Marathi translation
│   ├── TranslateEngtoMar2.py
│   └── TranslateEngtoMar3.py
│
├── storyline_tools/
│   └── storyline.py          # Storyline visualization (character interactions)
│
└── README.md

````

---

## 🚀 Features

- **Audio Tools**
  - Read aloud any website content using TTS (`pyttsx3`) or Playwright-based rendering for JS-heavy sites.
  - Save narration to audio files.

- **Web Tools**
  - Automate Google Maps search and extract location/business details.
  - Google Places scraping utility.
  - Click-through navigation & listing extraction with Playwright.

- **Video Tools**
  - Overlay text or captions on `.mp4` files (using `moviepy` and `Pillow`).

- **Translation Tools**
  - Translate English → Marathi (multiple approaches using APIs / libraries).

- **Storyline Tools**
  - Visualize character interactions across a storyline over time.

---

## 🛠 Installation

1. Clone this repository:

```bash
git clone https://github.com/narayanamare/pythonUtils2.git
cd pythonUtils2
````

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> ⚠️ For Playwright-based scripts, you also need to install the browser binaries:

```bash
playwright install
```

---

## 📖 Usage

Each script can be run independently. Example:

### 1. Read Aloud (Requests-based)

```bash
python audio_tools/readaloud.py
```

Edit the script to provide a target URL or pass it as an argument.

### 2. Read Aloud (Playwright-based)

```bash
python audio_tools/readaloud2.py
```

### 3. Add Text to Video

```bash
python video_tools/movietext.py
```

Make sure you provide a valid input video path inside the script.

### 4. Translate English → Marathi

```bash
python translate_tools/TranslateEngtoMar.py
```

### 5. Storyline Visualization

```bash
python storyline_tools/storyline.py
```

---

## 📌 Notes

* Some scripts depend on third-party APIs (e.g., Google Places) — you may need API keys.
* Ensure fonts are installed (for video text rendering).
* Some utilities are experimental and may need tweaking for specific use cases.

---

## 🤝 Contributing

This repo is a personal utility collection, but contributions are welcome:

* Improve existing scripts
* Add new utilities
* Report issues and suggest enhancements

---

## 📜 License

MIT License © 2025 Narayan Amare

```

---

Would you like me to also generate a **`requirements.txt`** for your repo based on the dependencies your scripts use (Playwright, pyttsx3, moviepy, Pillow, matplotlib, etc.)?
```
