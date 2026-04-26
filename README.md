🤖 Agentic AI Chatbot

A stateful AI chatbot built using LangGraph and LangChain, supporting persistent memory, multi-threaded conversations, and real-time streaming responses.

🚀 Features
🧠 Stateful Conversations – Maintains chat history using persistent memory
🔄 Multi-Threaded Chat – Supports multiple chat sessions using unique thread IDs
⚡ Real-Time Streaming – Token-level streaming responses for better user experience
🗂️ Checkpointing – SQLite-based persistence for conversation recovery
🧩 Agent Workflow – Modular architecture using LangGraph
💻 Interactive UI – Built with Streamlit for seamless interaction
🛠️ Tech Stack
Backend: Python, LangGraph, LangChain
LLM: Groq (LLaMA 3.3)
Database: SQLite (for checkpointing & memory)
Frontend: Streamlit
🏗️ Architecture Overview
Uses LangGraph to define a graph-based workflow (START → chat_node → END)
Maintains conversation state using TypedDict (ChatState)
Stores chat history via SQLite checkpointing
Streams responses using LLM streaming APIs
Handles session management using thread_id
⚙️ Installation
# Clone the repository
git clone https://github.com/ayu-maker/agentic_chatbot.git

# Navigate to project
cd agentic-ai-chatbot

# Install dependencies
pip install -r requirements.txt
🔑 Environment Setup

Create a .env file and add your Groq API key:

GROQ_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app.py
📂 Project Structure
├── backend.py        # LangGraph workflow + chatbot logic
├── app.py            # Streamlit UI
├── chatbot.db        # SQLite database (auto-created)
├── requirements.txt
└── README.md
📸 Screenshots

Add screenshots of your UI here (recommended)

🔮 Future Improvements
Add tool-calling agents (web search, calculator, APIs)
Implement RAG (Retrieval-Augmented Generation)
Add vector database (FAISS / ChromaDB)
Improve observability (logging & metrics)
🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

📜 License

This project is open-source and available under the MIT License.

🙌 Acknowledgements
LangChain & LangGraph
Groq LLM API
Streamlit
