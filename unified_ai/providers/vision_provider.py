"""
Computer Vision Provider
Supports YOLO and CLIP models.
"""

from typing import Optional, List, Any, Dict
import os


class ComputerVisionProvider:
    """Provider for computer vision models (YOLO, CLIP)."""
    
    def __init__(self):
        self.yolo_model = None
        self.clip_model = None
        self.clip_processor = None
        
        # Try to load YOLO
        try:
            from ultralytics import YOLO
            self.YOLO = YOLO
        except ImportError:
            print("Ultralytics not installed. Run: pip install ultralytics")
        
        # Try to load CLIP
        try:
            from transformers import CLIPProcessor, CLIPModel
            self.CLIPProcessor = CLIPProcessor
            self.CLIPModel = CLIPModel
        except ImportError:
            print("Transformers not installed. Run: pip install transformers")
    
    def is_yolo_available(self) -> bool:
        """Check if YOLO is available."""
        return hasattr(self, 'YOLO')
    
    def is_clip_available(self) -> bool:
        """Check if CLIP is available."""
        return hasattr(self, 'CLIPModel')
    
    def load_yolo(self, model_name: str = "yolov8n.pt") -> bool:
        """Load YOLO model."""
        if not self.is_yolo_available():
            return False
        
        try:
            self.yolo_model = self.YOLO(model_name)
            return True
        except Exception as e:
            print(f"Error loading YOLO model: {e}")
            return False
    
    def detect_objects(
        self,
        image_path: str,
        confidence: float = 0.25
    ) -> Optional[List[Dict[str, Any]]]:
        """Detect objects in an image using YOLO."""
        if not self.yolo_model:
            if not self.load_yolo():
                return None
        
        try:
            results = self.yolo_model(image_path, conf=confidence)
            detections = []
            
            for result in results:
                for box in result.boxes:
                    detection = {
                        "class": result.names[int(box.cls)],
                        "confidence": float(box.conf),
                        "bbox": box.xyxy[0].tolist()
                    }
                    detections.append(detection)
            
            return detections
        except Exception as e:
            print(f"YOLO object detection error: {e}")
            return None
    
    def load_clip(self, model_name: str = "openai/clip-vit-base-patch32") -> bool:
        """Load CLIP model."""
        if not self.is_clip_available():
            return False
        
        try:
            self.clip_model = self.CLIPModel.from_pretrained(model_name)
            self.clip_processor = self.CLIPProcessor.from_pretrained(model_name)
            return True
        except Exception as e:
            print(f"Error loading CLIP model: {e}")
            return False
    
    def classify_image(
        self,
        image_path: str,
        labels: List[str]
    ) -> Optional[Dict[str, float]]:
        """Classify image using CLIP."""
        if not self.clip_model:
            if not self.load_clip():
                return None
        
        try:
            from PIL import Image
            
            image = Image.open(image_path)
            inputs = self.clip_processor(
                text=labels,
                images=image,
                return_tensors="pt",
                padding=True
            )
            
            outputs = self.clip_model(**inputs)
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1)
            
            results = {}
            for label, prob in zip(labels, probs[0].tolist()):
                results[label] = prob
            
            return results
        except Exception as e:
            print(f"CLIP image classification error: {e}")
            return None
    
    def list_models(self) -> Dict[str, List[str]]:
        """List available computer vision models."""
        return {
            "yolo": ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt", "yolov8l.pt", "yolov8x.pt"],
            "clip": ["openai/clip-vit-base-patch32", "openai/clip-vit-large-patch14"]
        }
