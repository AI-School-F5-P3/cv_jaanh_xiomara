<<<<<<< HEAD
# Bounding box visualization
=======
# src/visualization/bbox_visualizer.py

import cv2
import numpy as np
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BBoxVisualizer:
    """Handles visualization of detection results with bounding boxes."""
    
    def __init__(self):
        """Initialize visualizer with default styling."""
        self.colors = {
            'box': (0, 255, 0),  # Green
            'text': (0, 0, 0),   # Black
            'background': (0, 255, 0)  # Green
        }
        self.text_scale = 0.5
        self.text_thickness = 2
        self.box_thickness = 2
        
    def draw_detections(self, image: np.ndarray, detections: List[Dict]) -> np.ndarray:
        """
        Draw all detections on an image.
        
        Args:
            image: Input image
            detections: List of detection dictionaries with class, confidence, and bbox
            
        Returns:
            Image with drawn detections
        """
        annotated_image = image.copy()
        
        for detection in detections:
            self.draw_single_detection(annotated_image, detection)
            
        return annotated_image
        
    def draw_single_detection(self, image: np.ndarray, detection: Dict) -> None:
        """Draw a single detection on the image."""
        # Extract detection info
        bbox = detection['bbox']
        label = f"{detection['class']}: {detection['confidence']:.2f}"
        
        # Draw box
        cv2.rectangle(
            image,
            (bbox[0], bbox[1]),
            (bbox[2], bbox[3]),
            self.colors['box'],
            self.box_thickness
        )
        
        # Get label size for background
        (label_w, label_h), baseline = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            self.text_scale,
            self.text_thickness
        )
        
        # Draw label background
        cv2.rectangle(
            image,
            (bbox[0], bbox[1] - label_h - 10),
            (bbox[0] + label_w, bbox[1]),
            self.colors['background'],
            -1
        )
        
        # Draw label text
        cv2.putText(
            image,
            label,
            (bbox[0], bbox[1] - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            self.text_scale,
            self.colors['text'],
            self.text_thickness
        )

    @staticmethod
    def create_summary_image(images: List[np.ndarray], 
                           max_images: int = 16,
                           cols: int = 4) -> np.ndarray:
        """
        Create a summary image showing multiple detections.
        
        Args:
            images: List of images with detections
            max_images: Maximum number of images to show
            cols: Number of columns in the grid
            
        Returns:
            Grid image combining multiple detection results
        """
        # Limit number of images
        images = images[:max_images]
        if not images:
            return None
            
        # Calculate grid dimensions
        n_images = len(images)
        rows = (n_images + cols - 1) // cols
        
        # Get target size
        cell_height = 300
        cell_width = 400
        
        # Create output image
        output = np.zeros((rows * cell_height, cols * cell_width, 3), dtype=np.uint8)
        
        for idx, img in enumerate(images):
            i = idx // cols
            j = idx % cols
            
            # Resize image to fit cell
            resized = cv2.resize(img, (cell_width, cell_height))
            
            # Place in grid
            output[i*cell_height:(i+1)*cell_height,
                  j*cell_width:(j+1)*cell_width] = resized
            
        return output
>>>>>>> 777777e (essential level)
