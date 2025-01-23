from ultralytics import YOLO
import cv2
import logging
from pathlib import Path
import numpy as np
from typing import Dict, List, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class YOLODetector:
    """
    Brand logo detector using a trained YOLOv8 model.
    """
    
    def __init__(self):
        """Initialize the detector with our trained model."""
        self.model = None
        self.load_trained_model()
        
    def load_trained_model(self):
        """Load our trained model for logo detection."""
        model_path = Path("data/models/logo_detector/weights/best.pt")
        
        if not model_path.exists():
            raise FileNotFoundError(
                "Trained model not found! Please run train_model.py first."
            )
            
        try:
            self.model = YOLO(str(model_path))
            logger.info(f"Loaded trained model from {model_path}")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise

    def detect(self, image_path: str, conf_threshold: float = 0.25) -> Tuple[np.ndarray, List[Dict]]:
        """
        Perform logo detection on an image.
        
        Args:
            image_path: Path to the input image
            conf_threshold: Confidence threshold for detections
            
        Returns:
            Tuple containing:
            - Original image with detections
            - List of detections (class, confidence, bbox)
        """
        try:
            if self.model is None:
                raise ValueError("Model not loaded! Please check model initialization.")
                
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Could not read image: {image_path}")
                
            # Run inference
            results = self.model(image, conf=conf_threshold)[0]
            
            # Process results
            detections = []
            for box in results.boxes:
                # Get detection information
                coords = box.xyxy[0].cpu().numpy()
                confidence = float(box.conf[0].cpu().numpy())
                class_id = int(box.cls[0].cpu().numpy())
                class_name = results.names[class_id]
                
                detection = {
                    'class': class_name,
                    'confidence': confidence,
                    'bbox': coords.astype(int).tolist()
                }
                detections.append(detection)
            
            return image, detections
            
        except Exception as e:
            logger.error(f"Detection error: {e}")
            raise
            
    def save_result(self, image: np.ndarray, output_path: str) -> None:
        """Save the detection result image."""
        try:
            cv2.imwrite(output_path, image)
            logger.info(f"Saved result to {output_path}")
        except Exception as e:
            logger.error(f"Error saving result: {e}")
            raise
