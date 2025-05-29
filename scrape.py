import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def scrape_website(website):
    """
    Scrapes the given website, extracts text, links, images, and summarizes the content using LangChain + Ollama.
    """
    print('Launching chrome browser.... ')

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(5)

        # Extract readable text and resources using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n", strip=True)

        # Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # Extract all image sources
        images = [img['src'] for img in soup.find_all('img', src=True)]

        # Summarize text with LangChain + Ollama
        try:
            summary = summarize_with_ollama_langchain(text)
        except Exception as e:
            summary = f"Summarization failed: {e}"

        # Return all extracted data
        return {
            "summary": summary,
            "text": text[:2000],  # Limit to first 2000 chars for readability
            "links": links,
            "images": images
        }
    finally:
        driver.quit()

def summarize_with_ollama_langchain(text):
    """
    Summarizes the given text using LangChain and Ollama.
    """
    llm = Ollama(model="gemma:2b")  # Use 'phi3' or another small model if needed
    prompt = PromptTemplate(
        input_variables=["content"],
        template="Summarize the following webpage content in a concise, readable way:\n\n{content}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke({"content": text[:4000]})
    return result["text"]