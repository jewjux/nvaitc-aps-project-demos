# IntelliExo AI Advisor Panel: Your Panel of Personal AI Advisors 

IntelliExo AI Advisor Panel is an innovative AI platform that provides personalized advice and insights by simulating conversations with various historical figures, thought leaders, and experts. Using Knowledge Graph RAG technology, each AI advisor maintains the authentic voice, knowledge, and perspective of their real-world counterpart.

## Features 🌟

- **Multiple AI Personas**: Interact with various personalities including Lee Kuan Yew, Albert Einstein, Confucius, Daniel Kahneman, and more
- **Customizable AI Advisors**: Add new personas by adding persona prompt and uploading documents like interview transcripts, biographies, and articles
- **Voice Synthesis**: Listen to responses in persona-specific voices using ElevenLabs technology
- **Knowledge-Based Responses**: Utilizes LightRAG for accurate information retrieval from persona-specific documents
- **Interactive UI**: Built with Streamlit for a seamless user experience
- **Response Summaries**: Get concise summaries of multiple advisor responses
- **Personalization**: Adapts responses based on user context and profile

## Technical Stack 🛠️

- **Framework**: Streamlit
- **Language Models**: Llama 3.1 70B Instruct (via NVIDIA NIMs)
- **Voice Synthesis**: ElevenLabs API
- **Document Processing**: textract
- **Vector Storage**: FAISS
- **Knowledge Base**: LightRAG (Knowledge Graph RAG) implementation
- **Pre-requisites**: Python 3.11.8 and above, Streamlit 1.41.1 and above.

## Project Structure 📁

```
intelliexo-ai-advisor-panel/
├── data/                    # Persona-specific knowledge bases
│   ├── Albert Einstein/
│   ├── Lee Kuan Yew/
│   ├── Confucius/
│   └── ...
├── lightrag/               # Custom RAG implementation
├── src/
│   └── pages/             # Streamlit pages
└── voices/                # Voice samples for synthesis
```

## Hardware Requirements 💻

- **GPU**: NVIDIA GPU with 8GB+ VRAM (recommended for local inference)
- **RAM**: 16GB minimum, 32GB recommended
- **Storage**: 10GB for base installation + space for persona documents
- **Network**: Stable internet connection for NVIDIA NIM API calls

## Setup 🚀

### Quick Start (Docker)
```bash
export NVIDIA_API_KEY=your_nvidia_api_key
export ELEVENLABS_API_KEY=your_elevenlabs_api_key  # Optional
./quickstart.sh
```

### Manual Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```
NVIDIA_API_KEY=your_nvidia_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

4. Run the application:
```bash
streamlit run main.py
```

## Expected Results 📊

- **Response Time**: 2-5 seconds per query (using NVIDIA NIM API)
- **Accuracy**: 90%+ relevance based on persona knowledge base
- **Voice Synthesis**: ~1 second additional latency with ElevenLabs
- **Concurrent Users**: Supports 10+ simultaneous users
- **Knowledge Graph**: Builds in <30 seconds for typical persona documents

## Usage 💡

1. Select one or more AI advisors from the available personas
2. Ask your question in the chat interface
3. Receive personalized responses from each selected advisor
4. Optionally:
   - Listen to responses in the advisor's voice
   - View source documents for responses
   - Get a summary of all advisors' perspectives

## Contributing 🤝
Project By:
Ethan Wei (NVIDIA Student Ambassador), Darren Tan (NVIDIA), Aik Beng Ng (NVIDIA), Simon See (NVIDIA)
An NVAITC APS project (NVIDIA).

## 📄 License

This project is licensed under the MIT License - see the repository's [LICENSE](../../LICENSE) file for details.