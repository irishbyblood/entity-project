"""
Mistral Provider
Supports Mistral Large 2 and other Mistral models.
"""

from typing import Optional, List, Dict, Any
from ..config import Config


class MistralProvider:
    """Provider for Mistral AI models."""
    
    def __init__(self):
        self.api_key = Config.MISTRAL_API_KEY
        self.client = None
        if self.api_key:
            try:
                from mistralai.client import MistralClient
                self.client = MistralClient(api_key=self.api_key)
            except ImportError:
                print("Mistral AI library not installed. Run: pip install mistralai")
    
    def is_available(self) -> bool:
        """Check if Mistral service is available."""
        return self.client is not None
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "mistral-large-latest",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """Generate chat completion using Mistral models."""
        if not self.is_available():
            return None
        
        try:
            from mistralai.models.chat_completion import ChatMessage
            
            # Convert messages to Mistral format
            mistral_messages = [
                ChatMessage(role=msg["role"], content=msg["content"])
                for msg in messages
            ]
            
            response = self.client.chat(
                model=model,
                messages=mistral_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Mistral chat completion error: {e}")
            return None
    
    def list_models(self) -> List[str]:
        """List available Mistral models."""
        return [
            "mistral-large-latest",
            "mistral-medium-latest",
            "mistral-small-latest"
        ]
