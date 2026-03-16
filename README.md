# Unified AI Application

A comprehensive Python application that integrates multiple AI models and services into a single, easy-to-use interface.

## Supported AI Services

### 🤖 Large Language Models (LLMs)
- **OpenAI GPT Models** - GPT-3.5, GPT-4, and GPT-4 Turbo
- **Anthropic Claude** - Claude 3.5 Sonnet and other Claude variants
- **Google Gemini** - Gemini Pro, Gemini Ultra, and Gemini Vision
- **Mistral AI** - Mistral Large 2, Mistral Medium, and Mistral Small
- **xAI Grok** - Grok beta and Grok-1
- **Microsoft Copilot** - Enterprise integration (placeholder)

### 🎨 Image Generation
- **OpenAI DALL-E** - DALL-E 2 and DALL-E 3
- **Midjourney** - Via third-party API (placeholder)

### 🎥 Video Generation
- **OpenAI Sora** - Text-to-video (when available)
- **Google Veo** - Video generation (when available)

### 👁️ Computer Vision
- **YOLO** - Real-time object detection (YOLOv8)
- **CLIP** - Image classification and understanding

### 🧠 Specialized AI Systems
- **IBM Watson** - Natural language understanding and analysis
- **Tesla Autopilot** - API integration (placeholder)
- **Google DeepMind AlphaGo** - Research integration (placeholder)

## Features

✨ **Unified Interface** - Access all AI models through a single, consistent API
🔌 **Modular Architecture** - Easy to add new providers and models
🔑 **Secure Configuration** - API keys managed through environment variables
🚀 **Easy to Use** - Simple Python API and command-line interface
📦 **Minimal Dependencies** - Only installs what you need

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/irishbyblood/entity-project.git
   cd entity-project
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   
   **Option A - Install everything:**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Option B - Install as package with specific providers:**
   ```bash
   # Core only
   pip install -e .
   
   # With OpenAI support
   pip install -e ".[openai]"
   
   # With all providers
   pip install -e ".[all]"
   ```

4. **Configure API keys:**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## Quick Start

For a faster introduction, see [QUICKSTART.md](QUICKSTART.md) - get running in 5 minutes!

## Configuration

Create a `.env` file in the project root with your API keys:

```env
# OpenAI (GPT, DALL-E, Sora)
OPENAI_API_KEY=your_openai_api_key

# Anthropic Claude
ANTHROPIC_API_KEY=your_anthropic_api_key

# Google Gemini/Veo
GOOGLE_API_KEY=your_google_api_key

# Mistral
MISTRAL_API_KEY=your_mistral_api_key

# xAI Grok
XAI_API_KEY=your_xai_api_key

# Microsoft Copilot
MICROSOFT_API_KEY=your_microsoft_api_key

# IBM Watson
IBM_WATSON_API_KEY=your_ibm_watson_api_key
IBM_WATSON_URL=your_ibm_watson_url

# Other services
MIDJOURNEY_API_KEY=your_midjourney_api_key
TESLA_API_KEY=your_tesla_api_key
DEEPMIND_API_KEY=your_deepmind_api_key
```

**Note:** You only need to configure the services you want to use. The application will work with whatever services you have API keys for.

## Usage

### Command-Line Interface

Check the status of all AI services:
```bash
python main.py status
```

Chat with an AI model:
```bash
python main.py chat --provider openai --message "What is artificial intelligence?"
python main.py chat --provider anthropic --message "Explain quantum computing"
python main.py chat --provider google --message "Tell me about machine learning"
```

Generate an image:
```bash
python main.py generate-image --provider openai --prompt "A futuristic AI city"
```

Detect objects in an image:
```bash
python main.py detect --image path/to/image.jpg
```

Classify an image:
```bash
python main.py classify --image path/to/image.jpg --labels cat dog bird
```

Analyze text:
```bash
python main.py analyze --text "Your text here"
```

List available models:
```bash
python main.py models
```

### Python API

```python
from unified_ai.app import UnifiedAI

# Initialize the application
ai = UnifiedAI()

# Check service status
ai.print_status()

# Chat with different models
messages = [{"role": "user", "content": "Hello, AI!"}]

# OpenAI GPT-4
response = ai.chat(messages, provider="openai", model="gpt-4")

# Anthropic Claude
response = ai.chat(messages, provider="anthropic")

# Google Gemini
response = ai.chat(messages, provider="google")

# Mistral Large
response = ai.chat(messages, provider="mistral")

# Generate images
image_urls = ai.generate_image("A beautiful sunset", provider="openai")

# Detect objects
detections = ai.detect_objects("image.jpg")

# Classify images
results = ai.classify_image("image.jpg", ["cat", "dog", "bird"])

# Analyze text
analysis = ai.analyze_text("Your text here")
```

### Examples

Run the examples file to see more usage patterns:
```bash
python examples.py
```

## Architecture

```
unified_ai/
├── __init__.py          # Package initialization
├── config.py            # Configuration management
├── app.py               # Main UnifiedAI class
└── providers/           # AI service providers
    ├── __init__.py
    ├── openai_provider.py      # OpenAI (GPT, DALL-E, Sora)
    ├── anthropic_provider.py   # Anthropic Claude
    ├── google_provider.py      # Google Gemini/Veo
    ├── mistral_provider.py     # Mistral AI
    ├── xai_provider.py         # xAI Grok
    ├── microsoft_provider.py   # Microsoft Copilot
    ├── ibm_watson_provider.py  # IBM Watson
    ├── vision_provider.py      # YOLO & CLIP
    └── specialized_provider.py # Tesla, DeepMind, Midjourney
```

## API Keys

### How to Get API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/
- **Google AI**: https://makersuite.google.com/app/apikey
- **Mistral**: https://console.mistral.ai/
- **xAI**: https://x.ai/api
- **IBM Watson**: https://cloud.ibm.com/catalog/services/natural-language-understanding
- **Microsoft**: Enterprise access required
- **Midjourney**: Third-party API services
- **Tesla/DeepMind**: Research/Enterprise access

## Notes

### Service Availability
- Some services (Sora, Veo, Tesla Autopilot, DeepMind AlphaGo) have placeholder implementations as their APIs are not publicly available yet
- Microsoft Copilot requires enterprise access and may use Microsoft Graph API or Azure OpenAI endpoints
- Midjourney does not provide a direct public API - the implementation assumes use of third-party API services
- xAI Grok API endpoint is based on expected patterns - update the URL when official documentation is available

### API Endpoint Notes
- **xAI Grok**: The base URL in the code is a placeholder. Update `unified_ai/providers/xai_provider.py` with the actual endpoint
- **Microsoft Copilot**: Configure the endpoint based on your Microsoft service (Graph API or Azure OpenAI)
- **Midjourney**: Use a third-party service provider URL (e.g., mj.imagineapi.dev or similar)

### Local Models
- YOLO and CLIP run locally and don't require API keys
- First-time use will download model files automatically

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See LICENSE file for details.

## Acknowledgments

This project integrates multiple AI services:
- OpenAI for GPT, DALL-E, and Sora
- Anthropic for Claude
- Google for Gemini and Veo
- Mistral AI for Mistral models
- xAI for Grok
- Microsoft for Copilot
- IBM for Watson
- Ultralytics for YOLO
- OpenAI for CLIP
- And others

## Support

For issues and questions, please open an issue on GitHub.
