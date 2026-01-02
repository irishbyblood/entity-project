# API Reference

## UnifiedAI Class

The main class that provides a unified interface to all AI services.

### Initialization

```python
from unified_ai.app import UnifiedAI

ai = UnifiedAI()
```

### Methods

#### `get_available_services() -> Dict[str, bool]`

Returns a dictionary of all services and their availability status.

```python
services = ai.get_available_services()
# Returns: {"OpenAI": True, "Anthropic": False, ...}
```

#### `chat(messages, provider, model=None, **kwargs) -> Optional[str]`

Universal chat completion interface.

**Parameters:**
- `messages` (List[Dict]): List of message dictionaries with 'role' and 'content'
- `provider` (str): AI provider ('openai', 'anthropic', 'google', 'mistral', 'xai', 'microsoft')
- `model` (str, optional): Specific model name
- `**kwargs`: Additional parameters (temperature, max_tokens, etc.)

**Returns:** Generated response text or None

**Example:**
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is AI?"}
]
response = ai.chat(messages, provider="openai", model="gpt-4", temperature=0.7)
```

#### `generate_image(prompt, provider='openai', **kwargs) -> Optional[Any]`

Universal image generation interface.

**Parameters:**
- `prompt` (str): Text description of the image to generate
- `provider` (str): AI provider ('openai', 'midjourney')
- `**kwargs`: Additional parameters (size, quality, etc.)

**Returns:** Image URL(s) or None

**Example:**
```python
urls = ai.generate_image(
    "A futuristic cityscape at sunset",
    provider="openai",
    size="1024x1024",
    quality="hd"
)
```

#### `generate_video(prompt, provider='openai', **kwargs) -> Optional[str]`

Universal video generation interface.

**Parameters:**
- `prompt` (str): Text description of the video to generate
- `provider` (str): AI provider ('openai', 'google')
- `**kwargs`: Additional parameters

**Returns:** Video URL or None

**Note:** Sora and Veo APIs are not yet publicly available.

#### `detect_objects(image_path, **kwargs) -> Optional[List[Dict]]`

Detect objects in an image using YOLO.

**Parameters:**
- `image_path` (str): Path to the image file
- `**kwargs`: Additional parameters (confidence threshold, etc.)

**Returns:** List of detected objects with class, confidence, and bounding boxes

**Example:**
```python
detections = ai.detect_objects("image.jpg", confidence=0.5)
for det in detections:
    print(f"{det['class']}: {det['confidence']:.2%}")
```

#### `classify_image(image_path, labels, **kwargs) -> Optional[Dict[str, float]]`

Classify an image using CLIP.

**Parameters:**
- `image_path` (str): Path to the image file
- `labels` (List[str]): List of possible labels
- `**kwargs`: Additional parameters

**Returns:** Dictionary mapping labels to probabilities

**Example:**
```python
results = ai.classify_image(
    "image.jpg",
    labels=["cat", "dog", "bird", "car"]
)
```

#### `analyze_text(text, **kwargs) -> Optional[Dict[str, Any]]`

Analyze text using IBM Watson.

**Parameters:**
- `text` (str): Text to analyze
- `**kwargs`: Additional parameters (features list, etc.)

**Returns:** Analysis results including sentiment, entities, keywords

**Example:**
```python
analysis = ai.analyze_text(
    "AI is transforming the world.",
    features=["sentiment", "entities", "keywords"]
)
```

#### `list_all_models() -> Dict[str, Any]`

List all available models from all configured providers.

**Example:**
```python
models = ai.list_all_models()
for provider, model_list in models.items():
    print(f"{provider}: {model_list}")
```

#### `print_status()`

Print the status of all AI services to console.

**Example:**
```python
ai.print_status()
```

## Individual Providers

### OpenAIProvider

```python
from unified_ai.providers.openai_provider import OpenAIProvider

provider = OpenAIProvider()
response = provider.chat_completion(messages, model="gpt-4")
image_urls = provider.generate_image("A sunset", model="dall-e-3")
```

### AnthropicProvider

```python
from unified_ai.providers.anthropic_provider import AnthropicProvider

provider = AnthropicProvider()
response = provider.chat_completion(messages, model="claude-3-5-sonnet-20241022")
```

### GoogleProvider

```python
from unified_ai.providers.google_provider import GoogleProvider

provider = GoogleProvider()
response = provider.chat_completion(messages, model="gemini-pro")
```

### MistralProvider

```python
from unified_ai.providers.mistral_provider import MistralProvider

provider = MistralProvider()
response = provider.chat_completion(messages, model="mistral-large-latest")
```

### XAIProvider

```python
from unified_ai.providers.xai_provider import XAIProvider

provider = XAIProvider()
response = provider.chat_completion(messages, model="grok-beta")
```

### ComputerVisionProvider

```python
from unified_ai.providers.vision_provider import ComputerVisionProvider

provider = ComputerVisionProvider()
detections = provider.detect_objects("image.jpg")
classifications = provider.classify_image("image.jpg", ["cat", "dog"])
```

### IBMWatsonProvider

```python
from unified_ai.providers.ibm_watson_provider import IBMWatsonProvider

provider = IBMWatsonProvider()
analysis = provider.analyze_text("Sample text")
```

## Configuration

### Config Class

```python
from unified_ai.config import Config

# Check if a key is configured
is_configured = Config.validate_key("OPENAI_API_KEY")

# Get list of configured services
services = Config.get_configured_services()
```

## Error Handling

All methods return `None` on error and print error messages to console. Always check return values:

```python
response = ai.chat(messages, provider="openai")
if response:
    print(response)
else:
    print("Failed to get response")
```
