# Brand Detection System

A computer vision system for detecting and tracking brand logos in videos.

## Features
- Brand logo detection using YOLOv8
- Video processing and frame extraction
- Brand appearance time tracking
- Detection storage in database
- Web interface for uploading and analyzing videos

## Installation
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
1. Configure model settings in `configs/model_config.yaml`
2. Run the web interface:
   ```bash
   streamlit run src/webapp/app.py
   ```

## Project Structure
[Project structure will be automatically inserted here]

## Development Levels

### Essential Level
- Single image brand detection
- Bounding box visualization
- Basic brand recognition

### Medium Level
- Video file processing
- Brand name display
- Detection confidence display

### Advanced Level
- Detection database
- Cropped detection storage
- Multi-brand detection
- Time analysis reports

### Expert Level
- Web interface
- Cloud deployment
- API service
