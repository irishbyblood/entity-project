#!/usr/bin/env python3
"""
Command-line interface for the Unified AI Application.
"""

import argparse
import sys
from unified_ai.app import UnifiedAI
from unified_ai.config import Config


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Unified AI Application - Access multiple AI services from one interface"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Status command
    subparsers.add_parser("status", help="Show status of all AI services")
    
    # List models command
    subparsers.add_parser("models", help="List all available models")
    
    # Chat command
    chat_parser = subparsers.add_parser("chat", help="Chat with an AI model")
    chat_parser.add_argument("--provider", default="openai", 
                           help="AI provider (openai, anthropic, google, mistral, xai)")
    chat_parser.add_argument("--model", help="Specific model to use")
    chat_parser.add_argument("--message", "-m", required=True, help="Message to send")
    chat_parser.add_argument("--system", help="System message")
    
    # Image generation command
    image_parser = subparsers.add_parser("generate-image", help="Generate an image")
    image_parser.add_argument("--provider", default="openai", 
                             help="AI provider (openai, midjourney)")
    image_parser.add_argument("--prompt", "-p", required=True, help="Image generation prompt")
    
    # Video generation command
    video_parser = subparsers.add_parser("generate-video", help="Generate a video")
    video_parser.add_argument("--provider", default="openai", 
                             help="AI provider (openai, google)")
    video_parser.add_argument("--prompt", "-p", required=True, help="Video generation prompt")
    
    # Object detection command
    detect_parser = subparsers.add_parser("detect", help="Detect objects in an image")
    detect_parser.add_argument("--image", "-i", required=True, help="Path to image file")
    detect_parser.add_argument("--confidence", type=float, default=0.25, 
                              help="Confidence threshold")
    
    # Image classification command
    classify_parser = subparsers.add_parser("classify", help="Classify an image")
    classify_parser.add_argument("--image", "-i", required=True, help="Path to image file")
    classify_parser.add_argument("--labels", "-l", required=True, nargs="+", 
                                help="Possible labels")
    
    # Text analysis command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze text with IBM Watson")
    analyze_parser.add_argument("--text", "-t", required=True, help="Text to analyze")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Initialize Unified AI
    ai = UnifiedAI()
    
    if args.command == "status":
        ai.print_status()
        return 0
    
    elif args.command == "models":
        print("\nAvailable Models:")
        print("=" * 60)
        models = ai.list_all_models()
        for provider, model_list in models.items():
            print(f"\n{provider}:")
            if isinstance(model_list, list):
                for model in model_list[:10]:  # Show first 10
                    print(f"  - {model}")
                if len(model_list) > 10:
                    print(f"  ... and {len(model_list) - 10} more")
            elif isinstance(model_list, dict):
                for category, models in model_list.items():
                    print(f"  {category}:")
                    for model in models:
                        print(f"    - {model}")
        return 0
    
    elif args.command == "chat":
        messages = []
        if args.system:
            messages.append({"role": "system", "content": args.system})
        messages.append({"role": "user", "content": args.message})
        
        print(f"\nSending message to {args.provider}...")
        response = ai.chat(messages, provider=args.provider, model=args.model)
        
        if response:
            print(f"\nResponse:\n{response}\n")
            return 0
        else:
            print(f"\nError: Failed to get response from {args.provider}")
            return 1
    
    elif args.command == "generate-image":
        print(f"\nGenerating image with {args.provider}...")
        result = ai.generate_image(args.prompt, provider=args.provider)
        
        if result:
            print(f"\nGenerated image URLs:")
            if isinstance(result, list):
                for i, url in enumerate(result, 1):
                    print(f"  {i}. {url}")
            else:
                print(f"  {result}")
            return 0
        else:
            print(f"\nError: Failed to generate image with {args.provider}")
            return 1
    
    elif args.command == "generate-video":
        print(f"\nGenerating video with {args.provider}...")
        result = ai.generate_video(args.prompt, provider=args.provider)
        
        if result:
            print(f"\nGenerated video URL: {result}")
            return 0
        else:
            print(f"\nNote: Video generation may not be available yet")
            return 1
    
    elif args.command == "detect":
        print(f"\nDetecting objects in {args.image}...")
        detections = ai.detect_objects(args.image, confidence=args.confidence)
        
        if detections:
            print(f"\nDetected {len(detections)} objects:")
            for i, det in enumerate(detections, 1):
                print(f"  {i}. {det['class']} (confidence: {det['confidence']:.2f})")
            return 0
        else:
            print(f"\nError: Failed to detect objects")
            return 1
    
    elif args.command == "classify":
        print(f"\nClassifying {args.image}...")
        results = ai.classify_image(args.image, args.labels)
        
        if results:
            print(f"\nClassification results:")
            sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
            for label, prob in sorted_results:
                print(f"  {label}: {prob:.2%}")
            return 0
        else:
            print(f"\nError: Failed to classify image")
            return 1
    
    elif args.command == "analyze":
        print(f"\nAnalyzing text with IBM Watson...")
        results = ai.analyze_text(args.text)
        
        if results:
            print(f"\nAnalysis results:")
            import json
            print(json.dumps(results, indent=2))
            return 0
        else:
            print(f"\nError: Failed to analyze text")
            return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
