# Generative AI Chat Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Latest-green.svg)](https://ollama.ai/)

A full-stack web application featuring a conversational AI assistant built with Flask, LangChain, and Ollama. This project demonstrates practical implementation of generative AI in a production-ready web application, showcasing skills in AI integration, backend development, and modern web technologies.

## 🚀 Features

- **Conversational AI Interface**: Interactive chat with AI responses powered by Ollama LLMs
- **Structured Response Parsing**: JSON-based output parsing with Pydantic models for consistent responses
- **Real-time Response Timing**: Performance metrics for each AI interaction
- **Responsive Web UI**: Modern, clean interface built with HTML5, CSS3, and vanilla JavaScript
- **Error Handling**: Robust error management with user-friendly messages
- **Modular Architecture**: Clean separation of concerns between frontend, backend, and AI components

## 🛠️ Tech Stack

### Backend
- **Flask**: Lightweight web framework for Python
- **LangChain**: Framework for building LLM-powered applications
- **Ollama**: Local LLM inference server
- **Pydantic**: Data validation and serialization

### Frontend
- **HTML5/CSS3**: Semantic markup and modern styling
- **Vanilla JavaScript**: DOM manipulation and API interactions
- **IBM Plex Sans**: Professional typography

### AI/ML
- **Llama 3 8B**: Base language model via Ollama
- **Prompt Engineering**: Structured prompts for consistent outputs
- **JSON Parsing**: Structured response extraction

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Llama 3 8B model pulled in Ollama (`ollama pull llama3:8b`)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cyborg92/generative-ai-chat-assistant.git
   cd generative-ai-chat-assistant
   ```

2. **Set up Python virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama server** (in a separate terminal)
   ```bash
   ollama serve
   ```

5. **Pull the required model**
   ```bash
   ollama pull llama3:8b
   ```

## 🚀 Usage

1. **Start the Flask application**
   ```bash
   python flask-app-server/app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Start chatting**
   - Type your message in the input field
   - Press Enter or click Send
   - View AI responses with timing information

## 📡 API Endpoints

### GET `/`
Serves the main chat interface.

### POST `/generate`
Generates AI responses.

**Request Body:**
```json
{
  "message": "Your question here"
}
```

**Response:**
```json
{
  "response": "AI-generated response text",
  "duration": 2.345
}
```

## 📁 Project Structure

```
generative-ai-chat-assistant/
├── flask-app-server/
│   ├── app.py              # Flask application & routes
│   ├── model.py            # LangChain chains & AI logic
│   ├── config.py           # Ollama configuration
│   ├── llm_test.py         # Model testing utilities
│   ├── templates/
│   │   └── index.html      # Chat interface
│   └── static/
│       ├── script.js       # Frontend logic
│       └── style.css       # UI styling
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔍 Key Components

### AI Response Structure
The application uses structured JSON responses with the following schema:
- **summary**: Concise input summary
- **sentiment**: Score from 0 (negative) to 1 (positive)
- **response**: AI-generated reply

### Configuration
Model parameters are configurable in `config.py`:
- Model: llama3:8b
- Temperature: 0.0 (deterministic)
- Max tokens: 256
- Base URL: http://localhost:11434
- local ollama downloaded model

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 Author

**Rachit Handa**
- LinkedIn: https://www.linkedin.com/in/rachit-handa-026ba366/
- Email: rachithanda93@gmail.com

## 🙏 Acknowledgments

- IBM for the Generative AI Applications course inspiration
- LangChain community for excellent documentation
- Ollama team for making local LLM inference accessible

## 🔮 Future Enhancements

- [ ] Add conversation memory for multi-turn dialogues
- [ ] Implement response caching for performance
- [ ] Add support for multiple LLM models
- [ ] Integrate user authentication
- [ ] Add conversation export functionality

---

*Built with ❤️ by a seasoned developer transitioning into Applied AI & Solutions Engineering*
