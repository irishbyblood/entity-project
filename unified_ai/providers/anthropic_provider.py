"""
Anthropic Provider
Supports Claude models including Claude 3.5 Sonnet.
"""

from typing import Optional, List, Dict, Any
from ..config import Config


class AnthropicProvider:
    """Provider for Anthropic Claude models."""
    
    def __init__(self):
        self.api_key = Config.ANTHROPIC_API_KEY
        self.client = None
        if self.api_key:
            try:
                from anthropic import Anthropic
                self.client = Anthropic(api_key=self.api_key)
            except ImportError:
                print("Anthropic library not installed. Run: pip install anthropic")
    
    def is_available(self) -> bool:
        """Check if Anthropic service is available."""
        return self.client is not None
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "claude-3-5-sonnet-20241022",
        max_tokens: int = 1024,
        temperature: float = 0.7
    ) -> Optional[str]:
        """Generate chat completion using Claude models."""
        if not self.is_available():
            return None
        
        try:
            # Convert messages format if needed
            system_message = ""
            user_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    user_messages.append(msg)
            
            kwargs = {
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "messages": user_messages
            }
            
            if system_message:
                kwargs["system"] = system_message
            
            response = self.client.messages.create(**kwargs)
            return response.content[0].text
        except Exception as e:
            print(f"Anthropic chat completion error: {e}")
            return None
    
    def list_models(self) -> List[str]:
        """List available Claude models."""
        return [
            "claude-3-5-sonnet-20241022",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307"
        ]
