import streamlit as st
from backend import chatbot,retrievel_all_threads
from langchain_core.messages import HumanMessage
import uuid;
import time

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agent")
st.write(" Interact with the AI Agent!")

#****** Utility function to generate unique thread ***********
def generate_thread():
    thread_id=uuid.uuid4();
    return thread_id;

def reset_chat():
    thread_id=generate_thread();
    st.session_state['thread_id']=thread_id;
    # add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]
    
def add_thread(thread_id,title):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)
        st.session_state['chat_threads_meta'][thread_id]=title

def load_history(thread_id):
    state=chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('messages',[])

def title_generator(user_input:str):
    words=user_input.strip().split()
    title=" ".join(words[:6])
    return title.capitalize()
    
#session dictionary which not erase every time unless we refresh it manually
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]
if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread();
if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread']=retrievel_all_threads()
# add_thread(st.session_state['thread_id'])

if 'chat_threads_meta' not in st.session_state:
    st.session_state['chat_threads_meta']={}


#*************** Sidebar UI ****************************
st.sidebar.title('Langgraph Chatbot')
if st.sidebar.button('New Chat'):
    reset_chat();
st.sidebar.header('My Conversation')
for thread_id in st.session_state['chat_thread']:
    # title=st.session_state['chat_threads_meta'].get(thread_id,"New Chat")
    if thread_id not in st.session_state['chat_threads_meta']:
        messages=load_history(thread_id)
        if messages:
            first_user_msg=next(
                (m.content for m in messages if isinstance(m,HumanMessage)),
                "New Chat"
            )
            st.session_state['chat_threads_meta'][thread_id]=title_generator(first_user_msg)
        else:
            st.session_state['chat_threads_meta'][thread_id]="New Chat"
    title=st.session_state['chat_threads_meta'][thread_id]
    if st.sidebar.button(title, key=f"thread_{thread_id}"):
        st.session_state['thread_id']=thread_id;
        messages=load_history(thread_id)
        temp_mesages=[]
        for msg in messages:
            if isinstance(msg,HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_mesages.append({'role':role,'content':msg.content})
        st.session_state['message_history']=temp_mesages;


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


    
user_input=st.chat_input('Type here')

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    #response=chatbot.invoke({'messages':HumanMessage(content=user_input)},config=config)
    #ai_message=response['messages'][-1].content
    #st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    if st.session_state['thread_id'] not in st.session_state['chat_threads_meta']:
        title=title_generator(user_input)
        add_thread(st.session_state['thread_id'],title)
    # CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']},
              "metadata":{
                  "thread_id":st.session_state["thread_id"]
              }
              ,
              "run_name":"chat_turn"
              }
    ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
