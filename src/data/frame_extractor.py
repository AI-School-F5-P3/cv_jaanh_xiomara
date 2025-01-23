import cv2
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FrameExtractor:
    """Extracts frames from video files for testing the logo detector."""
    
    def __init__(self, output_dir: str = "data/processed/frames"):
        """Initialize frame extractor with output directory."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def extract_frames(self, video_path: str, interval: int = 30) -> list:
        """
        Extract frames from a video file at specified intervals.
        
        Args:
            video_path: Path to input video
            interval: Extract one frame every 'interval' frames
            
        Returns:
            List of paths to extracted frames
        """
        try:
            video = cv2.VideoCapture(video_path)
            if not video.isOpened():
                raise ValueError(f"Could not open video: {video_path}")
            
            frame_paths = []
            frame_count = 0
            video_name = Path(video_path).stem
            
            while True:
                success, frame = video.read()
                if not success:
                    break
                    
                if frame_count % interval == 0:
                    frame_path = self.output_dir / f"{video_name}_frame_{frame_count}.jpg"
                    cv2.imwrite(str(frame_path), frame)
                    frame_paths.append(str(frame_path))
                    logger.info(f"Extracted frame {frame_count} to {frame_path}")
                
                frame_count += 1
            
            video.release()
            logger.info(f"Extracted {len(frame_paths)} frames from {video_path}")
            return frame_paths
            
        except Exception as e:
            logger.error(f"Frame extraction error: {e}")
            raise
