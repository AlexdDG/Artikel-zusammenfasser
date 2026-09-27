import streamlit as st
import trafilatura
import ollama

st.set_page_config(page_title="Link-Zusammenfasser", page_icon="📝", layout="centered")

st.title("Artikel zusammenfassen")

url = st.text_area("Link eingeben:")


if st.button("Zusammenfassen"):
    if url.strip() == "":
        st.warning("Bitte gebe einen Link ein.")
    else:
        with st.spinner("Lese Website..."):
            downloaded = trafilatura.fetch_url(url)
            text = trafilatura.extract(downloaded)

        if not text:
            st.error("Konnte keinen Text von dieser Seite extrahieren.")
        else:
            with st.spinner("KI fasst zusammen..."):
                 prompt = f"Fasse die wichtigsten Punkte aus folgendem Text als Bulletpoints zusammen:\n\n{text}"
                 antwort = ollama.chat (
                                 model="gemma4",
                                 messages = [{"role": "user", "content": prompt}]
                             )
                 
            st.subheader("Zusammenfassung:")
            st.write(antwort["message"]["content"])