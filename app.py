import streamlit as st
import google.generativeai as genai
import os

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="AppLI - Blocco 2", layout="wide")

# Caricamento chiave API da Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Errore: Chiave API non trovata. Configura 'GEMINI_API_KEY' nei Secrets di Streamlit.")
    st.stop()

model = genai.GenerativeModel('gemini-1.5-flash')

# --- LOGICA DI STATO ---
if "chat1" not in st.session_state: st.session_state.chat1 = []
if "chat2" not in st.session_state: st.session_state.chat2 = []

# --- INTERFACCIA ---
st.title("📖 Blocco 2: Scrivere Prompt Efficaci")
st.markdown("Impara a tradurre il tuo pensiero in istruzioni strutturate per la macchina.")

tab1, tab2 = st.tabs(["📖 1. La Teoria", "🏋️ 2. La Palestra"])

with tab1:
    st.subheader("Tappa 1: Il Principio del 'Nuovo Assunto'")
    st.write("Immagina l'IA come un assistente umano brillantissimo, ma appena assunto. Se non elimini la nebbia con le giuste istruzioni, tirerà a indovinare.")
    
    st.subheader("Tappa 2: Il Modello C-T-F")
    cols = st.columns(5)
    labels = ["🎭 Ruolo", "🌍 Contesto", "🎯 Compito", "🛑 Vincoli", "📊 Output"]
    for i, col in enumerate(cols):
        col.info(labels[i])
        
    st.subheader("Tappa 3: Few-Shot Prompting")
    st.write("Il trucco avanzato: mostra all'IA un esempio di ciò che vuoi. Copierà la tua struttura logica.")

with tab2:
    st.subheader("Palestra dei Prompt")
    
    # Selettore Esercizio
    ex_type = st.selectbox("Scegli il motore di allenamento:", 
                           ["Esercizio 1: Test della Scimmia Letterale", 
                            "Esercizio 2: Scassinatore di Strutture (C-T-F)"])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("Chat 1: Prompt Vago")
        user_input1 = st.text_input("Scrivi qui...", key="inp1")
        if st.button("Invia Chat 1"):
            sys_prompt = "Sei un assistente pigro. Rispondi in modo minimalista e robotico."
            response = model.generate_content(f"{sys_prompt}\n\nDomanda: {user_input1}")
            st.session_state.chat1.append(response.text)
        st.write(st.session_state.chat1[-1] if st.session_state.chat1 else "")

    with col2:
        st.success("Chat 2: Nuovo Assunto")
        user_input2 = st.text_input("Scrivi applicando la teoria...", key="inp2")
        if st.button("Invia Chat 2"):
            sys_prompt = "Sei un assistente professionale. Rispondi con massima precisione."
            response = model.generate_content(f"{sys_prompt}\n\nDomanda: {user_input2}")
            st.session_state.chat2.append(response.text)
        st.write(st.session_state.chat2[-1] if st.session_state.chat2 else "")

    with col3:
        st.warning("🔍 Valutatore")
        if st.button("Analizza Processo"):
            prompt_log = f"Valuta la differenza tra le due risposte. C1: {st.session_state.chat1[-1]}, C2: {st.session_state.chat2[-1]}"
            val_response = model.generate_content(prompt_log)
            st.write(val_response.text)
