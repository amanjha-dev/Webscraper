# AI Web Scraper

This project is an **AI-powered web scraper** built with Python, Streamlit, Selenium, BeautifulSoup, and [LangChain](https://python.langchain.com/) + [Ollama](https://ollama.com/) for local LLM summarization.  
It extracts readable text, links, and images from any website and provides a concise summary using a local language model (no OpenAI API required).

---

## Features

- **Easy-to-use Streamlit web interface**
- **Extracts:**  
  - Main text content  
  - All links  
  - All images  
- **Summarizes** the content using a local LLM (e.g., `gemma:2b`, `phi3`) via Ollama and LangChain
- **No cloud API costs** – runs entirely on your machine

---

## Requirements

- Python 3.9+
- [Google Chrome](https://www.google.com/chrome/) installed
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (matching your Chrome version, placed as `chromedriver.exe` in the project folder)
- [Ollama](https://ollama.com/download) installed and running
- Python packages:  
  - `selenium`
  - `beautifulsoup4`
  - `streamlit`
  - `langchain`
  - `langchain-community`
  - `ollama`

---

## Setup

1. **Clone this repository**  
   Or download the project files.

2. **Install Python dependencies:**
   ```bash
   pip install selenium beautifulsoup4 streamlit langchain langchain-community ollama
   ```

3. **Install and start Ollama:**  
   - Download from [https://ollama.com/download](https://ollama.com/download)
   - Open a terminal and run:
     ```bash
     ollama serve
     ```
   - Pull a small model (recommended: `gemma:2b` or `phi3`):
     ```bash
     ollama pull gemma:2b
     ```

4. **Download ChromeDriver:**  
   - [Find your Chrome version](chrome://settings/help)
   - Download the matching [ChromeDriver](https://chromedriver.chromium.org/downloads)
   - Place `chromedriver.exe` in the project folder.

5. **Run the app:**
   ```bash
   streamlit run main.py
   ```

---

## Usage

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`)
2. Enter a website URL and click **Scrape Site**
3. View the extracted summary, text, links, and images

---

## Configuration

- **Change the LLM model:**  
  Edit `scrape.py` and set the model in `Ollama(model="gemma:2b")` to any supported model you have installed (e.g., `"phi3"`).

---

## Troubleshooting

- **Ollama not found:**  
  Make sure `ollama serve` is running before you use the app.
- **Model memory errors:**  
  Use a smaller model like `gemma:2b` or `phi3`.
- **ChromeDriver errors:**  
  Ensure your ChromeDriver version matches your Chrome browser.

---

## Credits

- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)

---

## License

MIT License

---
