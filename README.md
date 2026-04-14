# Mj's AI Research Assistant

> An intelligent multi-agent research assistant powered by **CrewAI**, **OpenRouter**, and **Streamlit**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-orange?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?style=flat-square&logo=streamlit)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 🔍 **AI Researcher Agent** — Finds the latest and most relevant information on any topic
- ✍️ **AI Writer Agent** — Converts research into a clean, structured Markdown report
- ⚡ **Sequential Processing** — Agents collaborate in an intelligent pipeline
- 🌐 **Web UI** — Simple and clean Streamlit interface
- 🔌 **OpenRouter Integration** — Use 100+ LLMs (free & paid) with one API

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [CrewAI](https://crewai.com) | Multi-agent orchestration framework |
| [OpenRouter](https://openrouter.ai) | LLM API gateway (supports 100+ models) |
| [Streamlit](https://streamlit.io) | Web UI |
| [Python Dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mjowaleullah/crewai-assistant.git
cd crewai-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=openrouter/elephant-alpha
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> 🔑 Get your free API key at [openrouter.ai](https://openrouter.ai)

### 4. Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
crewai-assistant/
│
├── app.py              # Main Streamlit application
├── .env                # Environment variables (never commit this!)
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 🤖 How It Works

```
User Input (Topic)
      │
      ▼
┌─────────────────┐
│  Researcher     │  ──► Finds key information about the topic
│  Agent          │
└─────────────────┘
      │
      ▼
┌─────────────────┐
│  Writer         │  ──► Writes a structured Markdown report
│  Agent          │
└─────────────────┘
      │
      ▼
  Final Report (displayed in Streamlit UI)
```


---

## 📦 Requirements

```
crewai
streamlit
python-dotenv
```


---

## 👨‍💻 Author

**Mj Owaleullah**

- GitHub: [@mjowaleullah](https://github.com/mjowaleullah)

---

## 📄 License

This project is licensed under the MIT License.
