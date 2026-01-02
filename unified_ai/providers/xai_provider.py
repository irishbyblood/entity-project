"""
xAI Provider
Supports Grok models.
"""

from typing import Optional, List, Dict, Any
import httpx
from ..config import Config


class XAIProvider:
    """Provider for xAI Grok models."""
    
    def __init__(self):
        self.api_key = Config.XAI_API_KEY
        self.base_url = "https://api.x.ai/v1"
    
    def is_available(self) -> bool:
        """Check if xAI service is available."""
        return self.api_key is not None
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "grok-beta",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """Generate chat completion using Grok models."""
        if not self.is_available():
            return None
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
            }
            
            if max_tokens:
                data["max_tokens"] = max_tokens
            
            with httpx.Client() as client:
                response = client.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=60.0
                )
                response.raise_for_status()
                result = response.json()
                return result["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"xAI Grok chat completion error: {e}")
            return None
    
    def list_models(self) -> List[str]:
        """List available Grok models."""
        return ["grok-beta", "grok-1"]
