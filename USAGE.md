# Usage Guide

## Getting Started

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/irishbyblood/entity-project.git
cd entity-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys. You only need keys for the services you want to use.

### 3. Verify Setup

```bash
python main.py status
```

This will show which services are available based on your configuration.

## Common Use Cases

### Chat with AI Models

#### Simple Chat

```python
from unified_ai.app import UnifiedAI

ai = UnifiedAI()

messages = [
    {"role": "user", "content": "What is machine learning?"}
]

# Use OpenAI GPT-4
response = ai.chat(messages, provider="openai", model="gpt-4")
print(response)
```

#### Chat with System Instructions

```python
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "How do I sort a list in Python?"}
]

response = ai.chat(messages, provider="anthropic")
print(response)
```

#### Multi-turn Conversation

```python
conversation = [
    {"role": "user", "content": "What is Python?"}
]

# First response
response1 = ai.chat(conversation, provider="google")
conversation.append({"role": "assistant", "content": response1})

# Follow-up question
conversation.append({"role": "user", "content": "What are its main features?"})
response2 = ai.chat(conversation, provider="google")
```

#### Compare Responses from Different Models

```python
messages = [{"role": "user", "content": "Explain quantum computing"}]

providers = ["openai", "anthropic", "google", "mistral"]
for provider in providers:
    print(f"\n{provider.upper()}:")
    response = ai.chat(messages, provider=provider)
    if response:
        print(response[:200] + "...")
```

### Image Generation

#### Generate with DALL-E

```python
prompt = "A serene Japanese garden with cherry blossoms"
image_urls = ai.generate_image(prompt, provider="openai", model="dall-e-3")

if image_urls:
    for i, url in enumerate(image_urls):
        print(f"Image {i+1}: {url}")
```

#### High-Quality Image Generation

```python
prompt = "Professional portrait photo of a business executive"
image_urls = ai.generate_image(
    prompt,
    provider="openai",
    model="dall-e-3",
    size="1024x1792",  # Portrait orientation
    quality="hd"
)
```

### Computer Vision

#### Object Detection with YOLO

```python
# Detect objects in an image
detections = ai.detect_objects("street_scene.jpg", confidence=0.5)

if detections:
    print(f"Found {len(detections)} objects:")
    for det in detections:
        print(f"  - {det['class']}: {det['confidence']:.1%}")
        print(f"    Location: {det['bbox']}")
```

#### Image Classification with CLIP

```python
# Classify an image
labels = ["cat", "dog", "bird", "horse", "cow"]
results = ai.classify_image("animal.jpg", labels)

if results:
    # Sort by probability
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    print("Classification results:")
    for label, prob in sorted_results:
        print(f"  {label}: {prob:.1%}")
```

#### Custom Object Detection

```python
# Use a larger YOLO model for better accuracy
from unified_ai.providers.vision_provider import ComputerVisionProvider

vision = ComputerVisionProvider()
vision.load_yolo("yolov8l.pt")  # Large model
detections = vision.detect_objects("complex_scene.jpg", confidence=0.3)
```

### Text Analysis

#### Sentiment Analysis

```python
text = """
The new product launch exceeded all expectations. 
Customers are extremely satisfied with the quality and features.
"""

analysis = ai.analyze_text(text, features=["sentiment"])
if analysis and "sentiment" in analysis:
    sentiment = analysis["sentiment"]["document"]
    print(f"Sentiment: {sentiment['label']}")
    print(f"Score: {sentiment['score']:.2f}")
```

#### Extract Entities and Keywords

```python
text = """
Apple Inc. announced a new iPhone model in California.
The CEO Tim Cook presented the innovative features.
"""

analysis = ai.analyze_text(text, features=["entities", "keywords"])

if analysis:
    if "entities" in analysis:
        print("\nEntities:")
        for entity in analysis["entities"]:
            print(f"  - {entity['text']} ({entity['type']})")
    
    if "keywords" in analysis:
        print("\nKeywords:")
        for kw in analysis["keywords"]:
            print(f"  - {kw['text']} (relevance: {kw['relevance']:.2f})")
```

## Command-Line Usage

### Basic Commands

```bash
# Check status
python main.py status

# List models
python main.py models

# Simple chat
python main.py chat --provider openai --message "Hello, AI!"

# Chat with specific model
python main.py chat --provider anthropic --model claude-3-opus-20240229 --message "Explain relativity"

# Chat with system message
python main.py chat --provider google --system "You are a poet" --message "Write a haiku"
```

### Image Commands

```bash
# Generate image
python main.py generate-image --provider openai --prompt "A sunset over mountains"

# Detect objects
python main.py detect --image photo.jpg --confidence 0.5

# Classify image
python main.py classify --image photo.jpg --labels cat dog bird horse
```

### Text Analysis

```bash
# Analyze sentiment
python main.py analyze --text "This is an amazing product!"
```

## Advanced Usage

### Custom Temperature and Tokens

```python
# More creative responses
response = ai.chat(
    messages,
    provider="openai",
    temperature=0.9,
    max_tokens=500
)

# More deterministic responses
response = ai.chat(
    messages,
    provider="openai",
    temperature=0.1,
    max_tokens=100
)
```

### Batch Processing

```python
# Process multiple images
import os

image_dir = "images/"
for filename in os.listdir(image_dir):
    if filename.endswith((".jpg", ".png")):
        image_path = os.path.join(image_dir, filename)
        detections = ai.detect_objects(image_path)
        print(f"{filename}: {len(detections)} objects detected")
```

### Error Handling

```python
from unified_ai.app import UnifiedAI

ai = UnifiedAI()

# Check if service is available
if not ai.openai.is_available():
    print("OpenAI is not configured")
else:
    response = ai.chat(messages, provider="openai")
    if response:
        print(response)
    else:
        print("Failed to get response")
```

### Using Individual Providers

```python
# Direct access to providers for more control
from unified_ai.providers.openai_provider import OpenAIProvider

openai = OpenAIProvider()

if openai.is_available():
    # List available models
    models = openai.list_models()
    
    # Use specific model
    response = openai.chat_completion(
        messages,
        model="gpt-4-turbo-preview",
        temperature=0.7,
        max_tokens=1000
    )
```

## Tips and Best Practices

### 1. API Key Security
- Never commit `.env` files to version control
- Use environment variables in production
- Rotate API keys regularly

### 2. Cost Management
- Use smaller models when possible (e.g., gpt-3.5-turbo instead of gpt-4)
- Set reasonable max_tokens limits
- Cache responses when appropriate

### 3. Error Handling
- Always check return values for None
- Implement retry logic for production use
- Log errors for debugging

### 4. Model Selection
- Use GPT-4 for complex reasoning tasks
- Use Claude for long-context tasks
- Use Gemini for multimodal tasks
- Use Mistral for European data compliance
- Use local models (YOLO, CLIP) when API costs are a concern

### 5. Performance
- YOLO and CLIP models download on first use (~100MB-500MB)
- Reuse the UnifiedAI instance to avoid reloading models
- Consider caching image classification results

## Troubleshooting

### "OpenAI library not installed"
```bash
pip install openai
```

### "Module not found: anthropic"
```bash
pip install anthropic
```

### YOLO model download fails
- Check internet connection
- Models are cached in `~/.cache/torch/hub/`
- Try manually downloading model files

### API errors
- Verify API keys in `.env`
- Check API rate limits
- Ensure API keys have proper permissions

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```
