import streamlit as st
import os
from google import genai
import time

# ============================================================================
# PAGE CONFIGURATION & STYLING
# ============================================================================

st.set_page_config(
    page_title="Personal AI Chat",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for premium styling with improved interactivity
st.markdown("""
    <style>
        /* Main background */
        body {
            background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 100%);
        }
        
        .main {
            background: transparent;
        }
        
        /* Title styling */
        h1 {
            text-align: center;
            background: linear-gradient(90deg, #00d4ff, #0099ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 3em;
            font-weight: 700;
            margin-bottom: 0.3em;
            letter-spacing: 2px;
        }
        
        /* Subtitle */
        .subtitle {
            text-align: center;
            color: #a0aec0;
            font-size: 1em;
            margin-bottom: 1.5em;
            font-weight: 300;
        }
        
        /* Chat container centered */
        .chat-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Chat input styling */
        .stChatInputContainer {
            padding: 20px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(0, 212, 255, 0.3);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .stChatInputContainer:focus-within {
            border-color: rgba(0, 212, 255, 0.8);
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
        }
        
        /* Chat messages with better styling */
        .stChatMessage {
            border-radius: 15px;
            padding: 15px 20px;
            margin: 12px 0;
            background: rgba(255, 255, 255, 0.03);
            border-left: 4px solid #00d4ff;
            transition: all 0.3s ease;
        }
        
        .stChatMessage:hover {
            background: rgba(255, 255, 255, 0.06);
            transform: translateX(5px);
        }
        
        /* User message styling */
        [data-testid="chatAvatarIcon-user"] {
            background: linear-gradient(135deg, #00d4ff, #0099ff) !important;
        }
        
        /* Assistant message styling with accent color */
        [data-testid="chatAvatarIcon-assistant"] {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
        }
        
        /* Suggested buttons styling */
        .suggested-prompt {
            display: inline-block;
            margin: 5px;
        }
        
        .suggested-prompt button {
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid rgba(0, 212, 255, 0.5);
            color: #00d4ff;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.85em;
        }
        
        .suggested-prompt button:hover {
            background: rgba(0, 212, 255, 0.3);
            border-color: #00d4ff;
            transform: scale(1.05);
        }
        
        /* Character counter */
        .char-count {
            text-align: right;
            color: #a0aec0;
            font-size: 0.8em;
            margin-top: 5px;
        }
        
        /* Sidebar styling with better clarity */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a2e 0%, #0f0f1e 100%);
            border-right: 2px solid rgba(0, 212, 255, 0.3);
        }
        
        /* Sidebar header */
        .sidebar-header {
            background: linear-gradient(90deg, #00d4ff, #0099ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 1.3em;
            font-weight: 700;
            margin-bottom: 1.5em;
            padding: 15px 0;
            border-bottom: 2px solid rgba(0, 212, 255, 0.2);
        }
        
        /* Sidebar section titles */
        .sidebar-title {
            font-size: 1em;
            font-weight: 600;
            color: #00d4ff;
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            padding: 10px 0;
            border-left: 3px solid #00d4ff;
            padding-left: 10px;
        }
        
        /* Radio button styling */
        [data-testid="stRadio"] {
            background: rgba(0, 212, 255, 0.05);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 10px;
            padding: 12px;
            margin: 8px 0;
        }
        
        /* Toggle switch styling */
        [data-testid="stCheckbox"] {
            background: rgba(0, 212, 255, 0.05);
            border-radius: 8px;
            padding: 10px;
            margin: 8px 0;
        }
        
        /* Button styling in sidebar */
        .stButton button {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 212, 255, 0.3);
            background: rgba(0, 212, 255, 0.1);
            color: #00d4ff;
        }
        
        .stButton button:hover {
            background: rgba(0, 212, 255, 0.25);
            border-color: #00d4ff;
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
        }
        
        /* Info box styling */
        .info-box {
            background: rgba(102, 126, 234, 0.1);
            border: 1px solid rgba(102, 126, 234, 0.3);
            border-radius: 10px;
            padding: 15px;
            margin-top: 1.5em;
        }
        
        /* Expander styling */
        [data-testid="stExpander"] {
            background: rgba(0, 212, 255, 0.05);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 10px;
        }
        
        /* Caption text */
        .stCaption {
            color: #a0aec0 !important;
            font-size: 0.9em;
            margin-top: 5px;
            margin-bottom: 10px;
        }
        
        /* Divider styling */
        .sidebar-divider {
            border-bottom: 2px solid rgba(0, 212, 255, 0.15);
            margin: 1.5em 0;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

def initialize_session_state():
    """Initialize all session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = "gemini-pro"
    if 'remember_context' not in st.session_state:
        st.session_state.remember_context = True
    if 'is_loading' not in st.session_state:
        st.session_state.is_loading = False
    if 'scroll_to_bottom' not in st.session_state:
        st.session_state.scroll_to_bottom = True

initialize_session_state()

# ============================================================================
# API CONFIGURATION & QUERY FUNCTION
# ============================================================================

def get_api_key() -> str:
    """
    Retrieve API key from Streamlit secrets or environment variables.
    DO NOT hardcode API keys in code.
    """
    # Try Streamlit secrets first
    if "google_api_key" in st.secrets:
        api_key = st.secrets["google_api_key"]
        if api_key and api_key != "AIzaSyAcFv8rTH4DzUHY5mD9WQRvsRkX8gySVJQ":
            return api_key
    
    # Try environment variable
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        return api_key
    
    # Show helpful error message with setup instructions
    st.error("❌ **API Key Not Found!**")
    st.markdown("""
    ### 📝 How to Set Up Your Google API Key:
    
    1. **Get your API key:**
       - Go to: https://makersuite.google.com/app/apikey
       - Click "Create API Key"
       - Copy the key
    
    2. **Add to secrets.toml (Recommended):**
       - Open: `D:\\Personal AI Chat\\.streamlit\\secrets.toml`
       - Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual API key
       - Save the file
       - Refresh this page
    
    3. **Alternative - Use Environment Variable:**
       - Open PowerShell and run:
       ```
       $env:GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
       ```
       - Then restart Streamlit
    
    4. **Verify it works:**
       - After adding the key, refresh this page
       - You should see the chat interface
    """)
    st.stop()

def initialize_client() -> genai.Client:
    """Initialize and return Google Gemini API client."""
    return genai.Client(api_key=get_api_key())

def get_available_models() -> list:
    """Fetch list of available models from Google Gemini API."""
    try:
        client = initialize_client()
        # Use the correct API endpoint to list models
        models = client.models.list()
        available_models = []
        
        for model in models:
            model_name = model.name
            if isinstance(model_name, str):
                model_name = model_name.replace('models/', '')
            available_models.append(model_name)
        
        return available_models if available_models else None
    except Exception as e:
        st.warning(f"⚠️ Could not fetch models: {str(e)}")
        return None

def query_gemini(user_query: str, model: str) -> str:
    """
    Generate AI response using Google Gemini API.
    
    Args:
        user_query: User's input message
        model: Model name
    
    Returns:
        AI-generated response text
    """
    try:
        client = initialize_client()
        
        # Ensure model name has correct format
        if not model.startswith("models/"):
            model = f"models/{model}"
        
        response = client.models.generate_content(
            model=model,
            contents=user_query
        )
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ============================================================================
# SIDEBAR: CONFIGURATION & CONTROLS
# ============================================================================

with st.sidebar:
    # Sidebar header
    st.markdown("<div class='sidebar-header'>⚙️ CHAT SETTINGS</div>", unsafe_allow_html=True)
    
    # ─────────────────────────────────────────────────────────────────────
    # SECTION 1: MODEL SELECTION
    # ─────────────────────────────────────────────────────────────────────
    st.markdown("<div class='sidebar-title'>📊 AI Model</div>", unsafe_allow_html=True)
    
    # Available model options to try
    model_options = [
        "gemini-3-flash",
        "gemini-1.5-pro",
        "gemini-1.0-pro",
        "gemini-pro",
        "gemini-pro-vision"
    ]
    
    # Try to fetch available models, if fails use defaults
    available_models = get_available_models()
    if available_models:
        model_list = available_models
        st.success(f"✅ Found {len(available_models)} model(s)")
    else:
        model_list = model_options
        st.warning("⚠️ Using default models (auto-detect failed)")
    
    selected_model = st.selectbox(
        "Choose your model:",
        model_list,
        key="model_selector"
    )
    st.session_state.selected_model = selected_model
    
    # Display model info
    st.info(f"📌 Using: **{selected_model}**")
    if available_models:
        st.caption(f"Available: {', '.join(available_models)}")
    else:
        st.caption("Tip: If error occurs, check your API key at makersuite.google.com")
    
    # ─────────────────────────────────────────────────────────────────────
    # SECTION 2: CHAT MEMORY
    # ─────────────────────────────────────────────────────────────────────
    st.markdown("<hr style='margin: 2em 0; border: 1px solid rgba(0, 212, 255, 0.2);'>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-title'>💾 Chat Memory</div>", unsafe_allow_html=True)
    
    remember_context = st.toggle(
        "Remember conversation context",
        value=st.session_state.remember_context,
        help="ON: AI considers entire chat history | OFF: AI only sees latest message"
    )
    st.session_state.remember_context = remember_context
    
    if remember_context:
        st.success("✅ Context memory is ON")
    else:
        st.warning("⚠️ Context memory is OFF")
    
    # ─────────────────────────────────────────────────────────────────────
    # SECTION 3: CHAT MANAGEMENT
    # ─────────────────────────────────────────────────────────────────────
    st.markdown("<hr style='margin: 2em 0; border: 1px solid rgba(0, 212, 255, 0.2);'>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-title'>🗑️ Chat Management</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        messages_count = len(st.session_state.messages)
        st.metric("Messages", messages_count)
    
    with col2:
        st.metric("Model", selected_model.replace("models/", "")[:15])
    
    if st.button("🔄 Clear History", use_container_width=True):
        st.session_state.messages = []
        st.success("✅ Chat cleared successfully!")
        st.rerun()
    
    # ─────────────────────────────────────────────────────────────────────
    # SECTION 4: APP INFORMATION
    # ─────────────────────────────────────────────────────────────────────
    st.markdown("<hr style='margin: 2em 0; border: 1px solid rgba(0, 212, 255, 0.2);'>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ About This App"):
        st.markdown("""
        ### Personal AI Chat v1.0
        
        A premium Streamlit chat application powered by **Google's Gemini AI**.
        
        #### ✨ Features:
        - 💬 Real-time AI responses
        - 🔄 Persistent chat memory
        - 🚀 Multiple model selection
        - ⌨️ Smooth typing effects
        - 🎯 Smart prompt suggestions
        
        #### 📖 How to Use:
        1. **Select Model** - Choose from available Gemini models
        2. **Toggle Memory** - Enable/disable context awareness
        3. **Type Message** - Enter your query in the input field
        4. **View Response** - Watch AI respond with typing effect
        
        #### 💡 Pro Tips:
        - Use the selected model for all queries
        - Enable **Memory** for longer conversations
        - Click suggested prompts for quick start
        - Clear history when starting new topics
        
        #### 🔐 Privacy:
        - Chats are stored locally in session
        - API key is secure (not hardcoded)
        - Clear history anytime
        
        **Made with ❤️ using Streamlit**
        """)

# ============================================================================
# MAIN CHAT INTERFACE
# ============================================================================

st.markdown("<h1>✨ Personal AI Chat</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Powered by Google's Gemini AI • Select a model in the sidebar</p>", unsafe_allow_html=True)

# Suggested prompts section
st.markdown("### 💡 Suggested Prompts")
col1, col2, col3 = st.columns(3)

suggested_prompts = [
    "Explain quantum computing",
    "Write a Python function",
    "Summarize machine learning"
]

with col1:
    if st.button("Explain quantum computing", key="prompt_1"):
        st.session_state.suggested_input = suggested_prompts[0]
        st.rerun()

with col2:
    if st.button("Write a Python function", key="prompt_2"):
        st.session_state.suggested_input = suggested_prompts[1]
        st.rerun()

with col3:
    if st.button("Summarize machine learning", key="prompt_3"):
        st.session_state.suggested_input = suggested_prompts[2]
        st.rerun()

st.divider()

# Chat container (centered)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input with character count
col1, col2 = st.columns([1, 0.15])

with col1:
    user_input = st.chat_input(
        "Type your message here...",
        disabled=st.session_state.is_loading
    )
    
    # Check if suggested input should be used instead
    if st.session_state.get('suggested_input'):
        user_input = st.session_state.suggested_input
        del st.session_state.suggested_input

# Character count display
with col2:
    if user_input:
        st.markdown(f"<p class='char-count'>{len(user_input)}/2000</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# MESSAGE PROCESSING & RESPONSE GENERATION
# ============================================================================

if user_input:
    # Validate input
    if len(user_input.strip()) == 0:
        st.warning("⚠️ Please enter a message!")
    elif len(user_input) > 2000:
        st.error("❌ Message is too long! Maximum 2000 characters.")
    else:
        # Set loading state to disable input
        st.session_state.is_loading = True
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Prepare context for AI
        if st.session_state.remember_context:
            # Send entire conversation history for context
            context = "\n".join(
                [f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.messages[:-1]]
            ) + f"\nUSER: {user_input}"
        else:
            # Only send current message
            context = user_input
        
        # Generate and display response with streaming effect
        with st.chat_message("assistant"):
            with st.spinner("✨ Thinking..."):
                # Call API
                response = query_gemini(context, st.session_state.selected_model)
                
                # Display response with typing effect
                message_placeholder = st.empty()
                full_response = ""
                
                # Simulate streaming effect by displaying text progressively
                for char in response:
                    full_response += char
                    message_placeholder.markdown(full_response + "▌")
                    time.sleep(0.01)  # Adjust speed (0.01 = fast, 0.05 = slower)
                
                # Display final response
                message_placeholder.markdown(full_response)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Reset loading state
        st.session_state.is_loading = False
        
        # Auto-scroll to bottom
        st.rerun()        