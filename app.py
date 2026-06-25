import streamlit as st
import google.generativeai as genai

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="AppLI - Blocco 2", layout="wide")

# --- CSS PERSONALIZZATO (Per replicare l'HTML) ---
st.markdown("""
<style>
    /* Colori e font */
    :root { --void: #0A0F1E; --blue: #0EA5E9; --mint: #06D6A0; }
    .stApp { background-color: #0A0F1E; color: #F8FAFC; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: #F8FAFC !important; }
    
    /* Card design */
    div[data-testid="stMetricValue"] { color: var(--blue); }
    .stInfo { background-color: #131d30; border: 1px solid #1a2540; color: #CBD5E1; }
    
    /* Layout Chat Panel */
    .chat-box { background: #131d30; border: 1px solid rgba(255,255,255,0.07); border-radius: 16px; padding: 1rem; height: 400px; overflow-y: auto; }
</style>
""", unsafe_allow_html=True)

# --- CONFIGURAZIONE API ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Configura GEMINI_API_KEY nei Secrets di Streamlit!")
    st.stop()

# --- LOGICA ---
st.title("📖 Scrivere Prompt Efficaci")
st.write("Impara a tradurre il tuo pensiero in istruzioni strutturate.")

# Tabs come nell'HTML
tab1, tab2 = st.tabs(["📖 La Teoria", "🏋️ La Palestra"])

with tab1:
    st.markdown("### 1. Il Principio del 'Nuovo Assunto'")
    st.info("Immagina l'IA come un assistente brillantissimo assunto stamattina. Senza contesto, tira a indovinare.")
    
    st.markdown("### 2. Anatomia del Prompt (C-T-F)")
    cols = st.columns(5)
    labels = ["🎭 Ruolo", "🌍 Contesto", "🎯 Compito", "🛑 Vincoli", "📊 Output"]
    for i, col in enumerate(cols):
        col.markdown(f"**{labels[i]}**")
    
    st.markdown("### 3. Few-Shot Prompting")
    st.write("Usa gli esempi come binari logici per l'IA.")

with tab2:
    st.markdown("### Palestra Pratica")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("**Chat 1: Prompt Vago**")
        prompt1 = st.text_input("Input vago", key="p1")
        if st.button("Invia C1"):
            res1 = model.generate_content(f"Sei un'IA pigra. Rispondi: {prompt1}")
            st.session_state.res1 = res1.text
        st.markdown(f"<div class='chat-box'>{st.session_state.get('res1', '')}</div>", unsafe_allow_html=True)
    
    with c2:
        st.markdown("**Chat 2: Nuovo Assunto**")
        prompt2 = st.text_input("Input strutturato", key="p2")
        if st.button("Invia C2"):
            res2 = model.generate_content(f"Sei un assistente pro. Rispondi: {prompt2}")
            st.session_state.res2 = res2.text
        st.markdown(f"<div class='chat-box'>{st.session_state.get('res2', '')}</div>", unsafe_allow_html=True)
        
    with c3:
        st.markdown("**🔍 Valutatore**")
        if st.button("Analizza Logica"):
            st.warning("Analisi in corso...")
            val = model.generate_content("Confronta questi due prompt e dimmi quale è meglio: " + st.session_state.get('res1', '') + st.session_state.get('res2', ''))
            st.write(val.text)
