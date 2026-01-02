"""
Google Provider
Supports Gemini models and Veo video generation.
"""

from typing import Optional, List, Dict, Any
from ..config import Config


class GoogleProvider:
    """Provider for Google AI services (Gemini, Veo)."""
    
    def __init__(self):
        self.api_key = Config.GOOGLE_API_KEY
        self.model = None
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.genai = genai
                self.model = genai.GenerativeModel('gemini-pro')
            except ImportError:
                print("Google Generative AI library not installed. Run: pip install google-generativeai")
    
    def is_available(self) -> bool:
        """Check if Google AI service is available."""
        return self.model is not None
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gemini-pro",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """Generate chat completion using Gemini models."""
        if not self.is_available():
            return None
        
        try:
            # Use the specified model
            current_model = self.genai.GenerativeModel(model)
            
            # Convert messages to Gemini format
            prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
            
            generation_config = {
                "temperature": temperature,
            }
            if max_tokens:
                generation_config["max_output_tokens"] = max_tokens
            
            response = current_model.generate_content(
                prompt,
                generation_config=generation_config
            )
            return response.text
        except Exception as e:
            print(f"Google Gemini chat completion error: {e}")
            return None
    
    def generate_image(
        self,
        prompt: str,
        model: str = "gemini-pro-vision"
    ) -> Optional[str]:
        """Generate or analyze images using Gemini Vision."""
        if not self.is_available():
            return None
        
        try:
            vision_model = self.genai.GenerativeModel(model)
            response = vision_model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Google Gemini Vision error: {e}")
            return None
    
    def generate_video(
        self,
        prompt: str,
        duration: int = 5
    ) -> Optional[str]:
        """Generate video using Google Veo (placeholder for future API)."""
        if not self.is_available():
            return None
        
        print("Note: Google Veo API is not yet publicly available.")
        print(f"Video generation requested: {prompt}")
        return None
    
    def list_models(self) -> List[str]:
        """List available Google AI models."""
        if not self.is_available():
            return []
        
        try:
            models = self.genai.list_models()
            return [model.name for model in models]
        except Exception as e:
            print(f"Error listing models: {e}")
            return ["gemini-pro", "gemini-pro-vision", "gemini-ultra"]
