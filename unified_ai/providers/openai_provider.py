"""
OpenAI Provider
Supports GPT models, DALL-E, and Sora (when available).
"""

from typing import Optional, Dict, Any, List
from ..config import Config


class OpenAIProvider:
    """Provider for OpenAI services (GPT, DALL-E, Sora)."""
    
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.client = None
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except ImportError:
                print("OpenAI library not installed. Run: pip install openai")
    
    def is_available(self) -> bool:
        """Check if OpenAI service is available."""
        return self.client is not None
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """Generate chat completion using GPT models."""
        if not self.is_available():
            return None
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI chat completion error: {e}")
            return None
    
    def generate_image(
        self,
        prompt: str,
        model: str = "dall-e-3",
        size: str = "1024x1024",
        quality: str = "standard",
        n: int = 1
    ) -> Optional[List[str]]:
        """Generate images using DALL-E."""
        if not self.is_available():
            return None
        
        try:
            response = self.client.images.generate(
                model=model,
                prompt=prompt,
                size=size,
                quality=quality,
                n=n
            )
            return [img.url for img in response.data]
        except Exception as e:
            print(f"DALL-E image generation error: {e}")
            return None
    
    def generate_video(
        self,
        prompt: str,
        duration: int = 5
    ) -> Optional[str]:
        """Generate video using Sora (placeholder for future API)."""
        if not self.is_available():
            return None
        
        print("Note: Sora API is not yet publicly available.")
        print(f"Video generation requested: {prompt}")
        return None
    
    def list_models(self) -> Optional[List[str]]:
        """List available OpenAI models."""
        if not self.is_available():
            return None
        
        try:
            models = self.client.models.list()
            return [model.id for model in models.data]
        except Exception as e:
            print(f"Error listing models: {e}")
            return None
