import streamlit as st
from pydantic_agent.agent import ScriptAgent, AgentOutput

st.set_page_config(page_title="Mood Script", page_icon="🎙️", layout="wide")

st.title("🎙️ Mood Script")

# Session-state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", 
         "content":{
             "agent_response": "Olá, como posso te ajudar hoje?",
             "audio_path": None,
             "script_file_path": None
             }}
    ]

def get_agent_reply(user_input: str) -> AgentOutput:
    """Instantiate the ScriptAgent and return a string reply.
    Handles plain strings and simple dict returns."""
    try:
        agent = ScriptAgent(user_id=1, user_input=user_input, user_first_name="Jean")
        result = agent.run_agent()

        return result
    except Exception as e:
        # Surface the error to the user so you can debug quickly
        return f"Error running agent: {e}"

# Input area
user_input = st.chat_input("Qual o script para hoje?")

if user_input:
    # save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

if user_input:
    # quit shortcut
    if user_input.lower() in {"quit", "exit", "q"}:
        st.session_state.messages.append({"role": "assistant", "content": {
            "agent_response": "Goodbye!",
            "audio_path": None,
            "script_file_path": None
        }})
    else:
        with st.spinner("Analisando..."):
            reply = get_agent_reply(user_input)
        st.session_state.messages.append({"role": "assistant", "content": {
            "agent_response": reply.agent_response,
            "audio_path": reply.audio_path,
            "script_file_path": reply.script_file_path,
        }})

# Render chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            if text := msg["content"]["agent_response"]:
                st.write(text)

            if script_file_path := msg["content"]["script_file_path"]:
                with open(script_file_path, "r") as f:
                    st.code(f.read(), language=None, wrap_lines=True, height="content", width="content")

            if audio_path := msg["content"]["audio_path"]:
                st.audio(audio_path)
