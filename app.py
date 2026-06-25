import streamlit as st
import google.generativeai as genai

# Configurazione Pagina
st.set_page_config(page_title="AppLI - Blocco 2", layout="wide")

# CSS per rendere l'interfaccia elegante e "Dark Mode" professionale
st.markdown("""
<style>
    .main { background-color: #0A0F1E; }
    .stMarkdown, .stText { color: #CBD5E1; line-height: 1.8; }
    .theory-box { background-color: #131d30; padding: 2rem; border-radius: 16px; border-left: 5px solid #0EA5E9; margin-bottom: 2rem; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #0EA5E9; color: white; border: none; }
    .chat-container { height: 300px; overflow-y: auto; background: #0D1526; padding: 1rem; border-radius: 12px; border: 1px solid #1a2540; }
</style>
""", unsafe_allow_html=True)

# API Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Sidebar di Navigazione
menu = st.sidebar.radio("Percorso Didattico", ["Introduzione", "Anatomia del Prompt", "Few-Shot & Consigli", "Palestra Pratica"])

# --- CONTENUTI TEORICI ---
if menu == "Introduzione":
    st.title("📖 1. Il Principio del 'Nuovo Assunto'")
    st.markdown("""
    <div class='theory-box'>
    Molte persone usano l'IA come se fosse Google. Il risultato? Un testo piatto e robotico. 
    L'errore è alla base: immagina l'IA come un assistente brillantissimo, ma appena assunto. 
    Se a un collega nuovo dici solo 'Scrivi un'email', lui non sa chi sei né cosa vendi.
    <b>Il prompt serve a eliminare questa nebbia.</b>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Anatomia del Prompt":
    st.title("🏗️ 2. La Struttura (C-T-F)")
    st.write("Un prompt professionale si compone di 5 mattoncini:")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("**1. Ruolo:** Chi è l'IA (es. 'Agisci come un esperto di marketing')")
        st.markdown("**2. Contesto:** La storia e i dettagli del problema.")
        st.markdown("**3. Compito:** Verbi chiari (Scrivi, Analizza, Riassumi).")
        st.markdown("**4. Vincoli:** Regole del gioco (lunghezza, tono).")
        st.markdown("**5. Output:** La forma visiva (Tabella, Lista, Email).")

elif menu == "Few-Shot & Consigli":
    st.title("🚀 3. Il Consiglio dello Specialista")
    st.markdown("""
    Il trucco definitivo è il **Few-Shot Prompting**: *mostrale un esempio di ciò che vuoi*.
    Se hai un vecchio testo che ha funzionato benissimo, incollalo dicendo: 
    'Ecco un esempio dello stile che voglio: [Incolla il tuo testo]. Ora scrivine uno nuovo simile.'
    """)
    st.warning("Ricorda: Più tempo spendi a strutturare l'input, meno tempo perderai a correggere l'output.")

# --- PALESTRA PRATICA ---
else:
    st.title("🏋️ Palestra dei Prompt")
    st.write("Metti alla prova la teoria. Confronta un prompt pigro con uno strutturato.")
    
    colA, colB = st.columns(2)
    with colA:
        st.subheader("Chat 1: Prompt Vago")
        p1 = st.text_area("Input:", key="p1")
        if st.button("Analizza Chat 1"):
            with st.spinner("L'IA sta tirando a indovinare..."):
                res1 = model.generate_content(f"Sei un assistente IA letterale e pigro. Rispondi: {p1}")
                st.session_state.r1 = res1.text
        st.markdown(f"<div class='chat-container'>{st.session_state.get('r1', 'Aspetto input...')}</div>", unsafe_allow_html=True)

    with colB:
        st.subheader("Chat 2: Nuovo Assunto (C-T-F)")
        p2 = st.text_area("Input:", key="p2")
        if st.button("Analizza Chat 2"):
            with st.spinner("L'IA sta applicando il metodo C-T-F..."):
                res2 = model.generate_content(f"Sei un assistente eccellente che segue le istruzioni C-T-F. Rispondi: {p2}")
                st.session_state.r2 = res2.text
        st.markdown(f"<div class='chat-container'>{st.session_state.get('r2', 'Aspetto input...')}</div>", unsafe_allow_html=True)
