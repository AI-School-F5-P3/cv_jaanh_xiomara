<<<<<<< HEAD
# Plot detection results
=======
# src/visualization/results_plotter.py

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ResultsPlotter:
    """Handles plotting and visualization of detection results."""
    
    def __init__(self, save_dir: str = "data/processed/frames"):
        """Initialize plotter with save directory."""
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        
    def plot_confidence_distribution(self, 
                                   detections: List[Dict],
                                   save_name: str = "confidence_dist.png"):
        """Plot distribution of confidence scores."""
        confidences = [d['confidence'] for d in detections]
        
        plt.figure(figsize=(10, 6))
        plt.hist(confidences, bins=20, range=(0, 1))
        plt.title("Distribution of Detection Confidence Scores")
        plt.xlabel("Confidence Score")
        plt.ylabel("Number of Detections")
        
        save_path = self.save_dir / save_name
        plt.savefig(save_path)
        plt.close()
        logger.info(f"Saved confidence distribution plot to {save_path}")
        
    def plot_detections_per_class(self, 
                                detections: List[Dict],
                                save_name: str = "class_distribution.png"):
        """Plot number of detections per class."""
        # Count detections per class
        class_counts = {}
        for det in detections:
            class_name = det['class']
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
            
        # Create bar plot
        plt.figure(figsize=(10, 6))
        plt.bar(class_counts.keys(), class_counts.values())
        plt.title("Number of Detections per Class")
        plt.xlabel("Class")
        plt.ylabel("Number of Detections")
        plt.xticks(rotation=45)
        
        save_path = self.save_dir / save_name
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        logger.info(f"Saved class distribution plot to {save_path}")
        
    def plot_detection_summary(self, 
                             detections: List[Dict],
                             save_prefix: str = "detection_summary"):
        """Create a summary of detection results with multiple plots."""
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Plot confidence distribution
        confidences = [d['confidence'] for d in detections]
        ax1.hist(confidences, bins=20, range=(0, 1))
        ax1.set_title("Confidence Distribution")
        ax1.set_xlabel("Confidence Score")
        ax1.set_ylabel("Number of Detections")
        
        # Plot class distribution
        class_counts = {}
        for det in detections:
            class_name = det['class']
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
            
        ax2.bar(class_counts.keys(), class_counts.values())
        ax2.set_title("Detections per Class")
        ax2.set_xlabel("Class")
        ax2.set_ylabel("Count")
        plt.xticks(rotation=45)
        
        # Save plot
        save_path = self.save_dir / f"{save_prefix}.png"
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        logger.info(f"Saved detection summary plots to {save_path}")
>>>>>>> 777777e (essential level)
