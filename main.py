import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    if isinstance(result, dict):
        st.subheader("Summary")
        st.write(result.get("summary", "No summary available."))

        st.subheader("Extracted Text")
        st.text_area("Text", result.get("text", ""), height=200)

        st.subheader("Links")
        links = result.get("links", [])
        if links:
            for link in links:
                st.write(link)
        else:
            st.write("No links found.")

        st.subheader("Images")
        images = result.get("images", [])
        if images:
            for img in images:
                st.write(img)
        else:
            st.write("No images found.")
    else:
        # Fallback for old return type (just summary)
        st.text_area("Scraped Content", result, height=400)