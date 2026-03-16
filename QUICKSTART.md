# Quick Start Guide

Get up and running with the Unified AI Application in 5 minutes!

## Step 1: Install

```bash
# Clone and navigate
git clone https://github.com/irishbyblood/entity-project.git
cd entity-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (install only what you need)
pip install python-dotenv httpx certifi

# For OpenAI
pip install openai

# For Anthropic Claude
pip install anthropic

# For Google Gemini
pip install google-generativeai

# For Mistral
pip install mistralai

# For IBM Watson
pip install ibm-watson ibm-cloud-sdk-core

# For Computer Vision (YOLO & CLIP)
pip install ultralytics transformers torch torchvision pillow opencv-python numpy
```

## Step 2: Configure

```bash
# Copy example config
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

Minimal `.env` example:
```env
OPENAI_API_KEY=sk-...your-key...
```

## Step 3: Test

```bash
# Check what's available
python main.py status

# Try a simple chat
python main.py chat --provider openai --message "Hello, AI!"
```

## Step 4: Use in Your Code

```python
from unified_ai.app import UnifiedAI

# Initialize
ai = UnifiedAI()

# Chat with any model
messages = [{"role": "user", "content": "What is AI?"}]

# OpenAI
response = ai.chat(messages, provider="openai")
print(response)

# Claude
response = ai.chat(messages, provider="anthropic")
print(response)

# Gemini
response = ai.chat(messages, provider="google")
print(response)
```

## Common Tasks

### Generate an Image
```python
urls = ai.generate_image("A futuristic city", provider="openai")
print(urls[0])  # Image URL
```

### Detect Objects (YOLO)
```python
detections = ai.detect_objects("image.jpg")
for obj in detections:
    print(f"{obj['class']}: {obj['confidence']:.2%}")
```

### Classify Image (CLIP)
```python
results = ai.classify_image("image.jpg", ["cat", "dog", "bird"])
for label, prob in results.items():
    print(f"{label}: {prob:.2%}")
```

### Analyze Text (Watson)
```python
analysis = ai.analyze_text("This is amazing!")
print(analysis["sentiment"])
```

## Tips

💡 **Start Simple**: Get one provider working first (recommend OpenAI)
💡 **Check Status**: Use `python main.py status` to see what's configured
💡 **Read Errors**: Error messages tell you exactly what's missing
💡 **Use Examples**: Run `python examples.py` for more patterns

## Need Help?

- 📖 Full docs: `README.md`
- 🔧 API reference: `API.md`
- 📚 Usage guide: `USAGE.md`
- 💬 Examples: `examples.py`

## Model Recommendations

| Task | Best Provider | Model |
|------|--------------|-------|
| General chat | OpenAI | gpt-4 |
| Long context | Anthropic | claude-3-5-sonnet |
| Multimodal | Google | gemini-pro-vision |
| Fast/cheap | OpenAI | gpt-3.5-turbo |
| Image gen | OpenAI | dall-e-3 |
| Object detection | Local | YOLO (yolov8n.pt) |
| Image classify | Local | CLIP |

That's it! You're ready to use all the AI models through one simple interface! 🚀
