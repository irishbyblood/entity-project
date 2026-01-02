"""
Unified AI Application
Main interface that integrates all AI providers.
"""

from typing import Optional, List, Dict, Any
from .config import Config
from .providers.openai_provider import OpenAIProvider
from .providers.anthropic_provider import AnthropicProvider
from .providers.google_provider import GoogleProvider
from .providers.mistral_provider import MistralProvider
from .providers.xai_provider import XAIProvider
from .providers.microsoft_provider import MicrosoftProvider
from .providers.ibm_watson_provider import IBMWatsonProvider
from .providers.vision_provider import ComputerVisionProvider
from .providers.specialized_provider import TeslaProvider, DeepMindProvider, MidjourneyProvider


class UnifiedAI:
    """
    Unified AI Application that provides a single interface to multiple AI services.
    
    Supported Services:
    - OpenAI GPT models (GPT-3.5, GPT-4)
    - OpenAI DALL-E (image generation)
    - OpenAI Sora (video generation - when available)
    - Anthropic Claude (Claude 3.5 Sonnet)
    - Google Gemini (Ultra and other variants)
    - Google Veo (video generation - when available)
    - Mistral Large 2
    - xAI Grok
    - Microsoft Copilot
    - IBM Watson
    - YOLO (object detection)
    - CLIP (image classification)
    - Midjourney (image generation)
    - Tesla Autopilot (API placeholder)
    - Google DeepMind AlphaGo (API placeholder)
    """
    
    def __init__(self):
        """Initialize all AI providers."""
        self.openai = OpenAIProvider()
        self.anthropic = AnthropicProvider()
        self.google = GoogleProvider()
        self.mistral = MistralProvider()
        self.xai = XAIProvider()
        self.microsoft = MicrosoftProvider()
        self.ibm_watson = IBMWatsonProvider()
        self.vision = ComputerVisionProvider()
        self.tesla = TeslaProvider()
        self.deepmind = DeepMindProvider()
        self.midjourney = MidjourneyProvider()
    
    def get_available_services(self) -> Dict[str, bool]:
        """Get status of all available services."""
        return {
            "OpenAI (GPT, DALL-E, Sora)": self.openai.is_available(),
            "Anthropic Claude": self.anthropic.is_available(),
            "Google Gemini/Veo": self.google.is_available(),
            "Mistral": self.mistral.is_available(),
            "xAI Grok": self.xai.is_available(),
            "Microsoft Copilot": self.microsoft.is_available(),
            "IBM Watson": self.ibm_watson.is_available(),
            "YOLO": self.vision.is_yolo_available(),
            "CLIP": self.vision.is_clip_available(),
            "Midjourney": self.midjourney.is_available(),
            "Tesla Autopilot": self.tesla.is_available(),
            "DeepMind": self.deepmind.is_available(),
        }
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        provider: str = "openai",
        model: Optional[str] = None,
        **kwargs
    ) -> Optional[str]:
        """
        Universal chat completion interface.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            provider: AI provider to use ('openai', 'anthropic', 'google', 'mistral', 'xai')
            model: Specific model to use (optional, uses default if not specified)
            **kwargs: Additional parameters like temperature, max_tokens
        
        Returns:
            Generated response text or None if error
        """
        provider = provider.lower()
        
        if provider == "openai":
            model = model or "gpt-4"
            return self.openai.chat_completion(messages, model=model, **kwargs)
        elif provider == "anthropic" or provider == "claude":
            model = model or "claude-3-5-sonnet-20241022"
            return self.anthropic.chat_completion(messages, model=model, **kwargs)
        elif provider == "google" or provider == "gemini":
            model = model or "gemini-pro"
            return self.google.chat_completion(messages, model=model, **kwargs)
        elif provider == "mistral":
            model = model or "mistral-large-latest"
            return self.mistral.chat_completion(messages, model=model, **kwargs)
        elif provider == "xai" or provider == "grok":
            model = model or "grok-beta"
            return self.xai.chat_completion(messages, model=model, **kwargs)
        elif provider == "microsoft" or provider == "copilot":
            return self.microsoft.chat_completion(messages, **kwargs)
        else:
            print(f"Unknown provider: {provider}")
            return None
    
    def generate_image(
        self,
        prompt: str,
        provider: str = "openai",
        **kwargs
    ) -> Optional[Any]:
        """
        Universal image generation interface.
        
        Args:
            prompt: Text prompt for image generation
            provider: AI provider to use ('openai', 'midjourney')
            **kwargs: Additional parameters
        
        Returns:
            Generated image URL(s) or None if error
        """
        provider = provider.lower()
        
        if provider == "openai" or provider == "dalle":
            return self.openai.generate_image(prompt, **kwargs)
        elif provider == "midjourney":
            return self.midjourney.generate_image(prompt, **kwargs)
        else:
            print(f"Unknown image provider: {provider}")
            return None
    
    def generate_video(
        self,
        prompt: str,
        provider: str = "openai",
        **kwargs
    ) -> Optional[str]:
        """
        Universal video generation interface.
        
        Args:
            prompt: Text prompt for video generation
            provider: AI provider to use ('openai', 'google')
            **kwargs: Additional parameters
        
        Returns:
            Generated video URL or None if error
        """
        provider = provider.lower()
        
        if provider == "openai" or provider == "sora":
            return self.openai.generate_video(prompt, **kwargs)
        elif provider == "google" or provider == "veo":
            return self.google.generate_video(prompt, **kwargs)
        else:
            print(f"Unknown video provider: {provider}")
            return None
    
    def detect_objects(
        self,
        image_path: str,
        **kwargs
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Detect objects in an image using YOLO.
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional parameters like confidence threshold
        
        Returns:
            List of detected objects with bounding boxes and confidence
        """
        return self.vision.detect_objects(image_path, **kwargs)
    
    def classify_image(
        self,
        image_path: str,
        labels: List[str],
        **kwargs
    ) -> Optional[Dict[str, float]]:
        """
        Classify image using CLIP.
        
        Args:
            image_path: Path to the image file
            labels: List of possible labels
            **kwargs: Additional parameters
        
        Returns:
            Dictionary mapping labels to probabilities
        """
        return self.vision.classify_image(image_path, labels, **kwargs)
    
    def analyze_text(
        self,
        text: str,
        **kwargs
    ) -> Optional[Dict[str, Any]]:
        """
        Analyze text using IBM Watson.
        
        Args:
            text: Text to analyze
            **kwargs: Additional parameters like features
        
        Returns:
            Analysis results including sentiment, entities, keywords, etc.
        """
        return self.ibm_watson.analyze_text(text, **kwargs)
    
    def list_all_models(self) -> Dict[str, Any]:
        """List all available models from all providers."""
        models = {}
        
        if self.openai.is_available():
            models["OpenAI"] = self.openai.list_models()
        
        if self.anthropic.is_available():
            models["Anthropic"] = self.anthropic.list_models()
        
        if self.google.is_available():
            models["Google"] = self.google.list_models()
        
        if self.mistral.is_available():
            models["Mistral"] = self.mistral.list_models()
        
        if self.xai.is_available():
            models["xAI"] = self.xai.list_models()
        
        models["ComputerVision"] = self.vision.list_models()
        
        return models
    
    def print_status(self):
        """Print status of all AI services."""
        print("\n" + "="*60)
        print("Unified AI Application Status")
        print("="*60)
        
        services = self.get_available_services()
        configured = Config.get_configured_services()
        
        print(f"\nConfigured Services ({len(configured)}):")
        for service in configured:
            print(f"  ✓ {service}")
        
        print(f"\nService Status:")
        for service, available in services.items():
            status = "✓ Available" if available else "✗ Not Available"
            print(f"  {status}: {service}")
        
        print("\n" + "="*60 + "\n")
