"""
Example usage of the Unified AI Application.
"""

from unified_ai.app import UnifiedAI


def example_chat():
    """Example: Chat with different AI models."""
    print("\n" + "="*60)
    print("Example: Chat with Multiple AI Models")
    print("="*60 + "\n")
    
    ai = UnifiedAI()
    
    messages = [
        {"role": "user", "content": "What is artificial intelligence?"}
    ]
    
    # Try OpenAI GPT
    print("1. OpenAI GPT-4:")
    response = ai.chat(messages, provider="openai", model="gpt-4")
    if response:
        print(f"   {response[:200]}...\n")
    
    # Try Anthropic Claude
    print("2. Anthropic Claude:")
    response = ai.chat(messages, provider="anthropic")
    if response:
        print(f"   {response[:200]}...\n")
    
    # Try Google Gemini
    print("3. Google Gemini:")
    response = ai.chat(messages, provider="google")
    if response:
        print(f"   {response[:200]}...\n")
    
    # Try Mistral
    print("4. Mistral Large:")
    response = ai.chat(messages, provider="mistral")
    if response:
        print(f"   {response[:200]}...\n")


def example_image_generation():
    """Example: Generate images with different providers."""
    print("\n" + "="*60)
    print("Example: Image Generation")
    print("="*60 + "\n")
    
    ai = UnifiedAI()
    
    prompt = "A futuristic AI-powered city with flying cars"
    
    # Try DALL-E
    print("1. OpenAI DALL-E:")
    urls = ai.generate_image(prompt, provider="openai")
    if urls:
        print(f"   Generated images: {urls}\n")
    
    # Try Midjourney
    print("2. Midjourney:")
    url = ai.generate_image(prompt, provider="midjourney")
    if url:
        print(f"   Generated image: {url}\n")


def example_computer_vision():
    """Example: Object detection and image classification."""
    print("\n" + "="*60)
    print("Example: Computer Vision (YOLO & CLIP)")
    print("="*60 + "\n")
    
    ai = UnifiedAI()
    
    # Note: You need an actual image file for this to work
    image_path = "test_image.jpg"
    
    # Object detection with YOLO
    print("1. Object Detection with YOLO:")
    print(f"   Detecting objects in {image_path}...")
    detections = ai.detect_objects(image_path)
    if detections:
        for det in detections[:5]:  # Show first 5
            print(f"   - {det['class']}: {det['confidence']:.2%}")
    else:
        print("   (No image file found or detection failed)")
    
    # Image classification with CLIP
    print("\n2. Image Classification with CLIP:")
    labels = ["cat", "dog", "car", "airplane", "building"]
    results = ai.classify_image(image_path, labels)
    if results:
        for label, prob in sorted(results.items(), key=lambda x: x[1], reverse=True):
            print(f"   - {label}: {prob:.2%}")
    else:
        print("   (No image file found or classification failed)")


def example_text_analysis():
    """Example: Text analysis with IBM Watson."""
    print("\n" + "="*60)
    print("Example: Text Analysis with IBM Watson")
    print("="*60 + "\n")
    
    ai = UnifiedAI()
    
    text = """
    Artificial intelligence is transforming the world. 
    Companies are investing heavily in AI research and development.
    The future of technology looks incredibly promising.
    """
    
    print("Analyzing text sentiment, entities, and keywords...")
    results = ai.analyze_text(text.strip())
    
    if results:
        if "sentiment" in results:
            sentiment = results["sentiment"]["document"]
            print(f"\nSentiment: {sentiment['label']} ({sentiment['score']:.2f})")
        
        if "keywords" in results:
            print("\nKeywords:")
            for kw in results["keywords"][:5]:
                print(f"  - {kw['text']} (relevance: {kw['relevance']:.2f})")
    else:
        print("(Text analysis not available)")


def main():
    """Run all examples."""
    ai = UnifiedAI()
    
    # Show status
    ai.print_status()
    
    # Run examples
    print("\nRunning Examples...")
    print("Note: Examples will only work if you have configured the relevant API keys.")
    
    # Uncomment to run specific examples:
    # example_chat()
    # example_image_generation()
    # example_computer_vision()
    # example_text_analysis()
    
    print("\nTo run examples, uncomment the function calls in examples.py")
    print("Make sure to configure your API keys in .env file first!\n")


if __name__ == "__main__":
    main()
