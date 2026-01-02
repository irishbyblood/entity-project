"""
Configuration management for the Unified AI Application.
Loads API keys and settings from environment variables.
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()


class Config:
    """Configuration class for managing API keys and settings."""
    
    # OpenAI (GPT, DALL-E, Sora)
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # Anthropic (Claude)
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    # Google (Gemini, Veo)
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    
    # Mistral
    MISTRAL_API_KEY: Optional[str] = os.getenv("MISTRAL_API_KEY")
    
    # xAI (Grok)
    XAI_API_KEY: Optional[str] = os.getenv("XAI_API_KEY")
    
    # Microsoft (Copilot)
    MICROSOFT_API_KEY: Optional[str] = os.getenv("MICROSOFT_API_KEY")
    
    # Midjourney
    MIDJOURNEY_API_KEY: Optional[str] = os.getenv("MIDJOURNEY_API_KEY")
    
    # IBM Watson
    IBM_WATSON_API_KEY: Optional[str] = os.getenv("IBM_WATSON_API_KEY")
    IBM_WATSON_URL: Optional[str] = os.getenv("IBM_WATSON_URL")
    
    # Tesla
    TESLA_API_KEY: Optional[str] = os.getenv("TESLA_API_KEY")
    
    # DeepMind
    DEEPMIND_API_KEY: Optional[str] = os.getenv("DEEPMIND_API_KEY")
    
    @classmethod
    def validate_key(cls, key_name: str) -> bool:
        """Check if an API key is configured."""
        key = getattr(cls, key_name, None)
        return key is not None and key != ""
    
    @classmethod
    def get_configured_services(cls) -> list:
        """Get list of configured services."""
        services = []
        key_mappings = {
            "OPENAI_API_KEY": "OpenAI (GPT, DALL-E, Sora)",
            "ANTHROPIC_API_KEY": "Anthropic Claude",
            "GOOGLE_API_KEY": "Google Gemini/Veo",
            "MISTRAL_API_KEY": "Mistral",
            "XAI_API_KEY": "xAI Grok",
            "MICROSOFT_API_KEY": "Microsoft Copilot",
            "MIDJOURNEY_API_KEY": "Midjourney",
            "IBM_WATSON_API_KEY": "IBM Watson",
            "TESLA_API_KEY": "Tesla Autopilot",
            "DEEPMIND_API_KEY": "Google DeepMind",
        }
        
        for key, service in key_mappings.items():
            if cls.validate_key(key):
                services.append(service)
        
        return services
