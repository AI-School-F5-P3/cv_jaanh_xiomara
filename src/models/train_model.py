from ultralytics import YOLO
import logging
from pathlib import Path
import yaml
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train_logo_detector():
    """
    Entrena el modelo YOLOv8 usando nuestro dataset de logos.
    """
    try:
        # Obtener la ruta absoluta del proyecto
        project_root = Path(os.getcwd())
        
        # Ruta al archivo de configuración
        data_yaml = project_root / 'data/processed/yolo_dataset/data.yaml'
        
        # Verificar que existe el archivo yaml
        if not data_yaml.exists():
            raise FileNotFoundError(f"No se encontró el archivo {data_yaml}")
        
        # Cargar y verificar la configuración
        with open(data_yaml, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Configuración cargada correctamente: {len(config['names'])} clases")
            
            # Verificar que existen los directorios
            for path_key in ['train', 'val', 'test']:
                if not Path(config[path_key]).exists():
                    raise FileNotFoundError(f"No se encontró el directorio: {config[path_key]}")
        
        # Inicializar y entrenar el modelo
        model = YOLO('yolov8n.pt')
        
        results = model.train(
            data=str(data_yaml),
            epochs=50,
            imgsz=640,
            batch=16,
            patience=10,
            save=True,
            project=str(project_root / 'data/models'),
            name='logo_detector',
            pretrained=True,
            optimizer='Adam'
        )
        
        logger.info("¡Entrenamiento completado!")
        logger.info(f"Modelo guardado en: {project_root}/data/models/logo_detector/weights/best.pt")
        
    except Exception as e:
        logger.error(f"Error durante el entrenamiento: {e}")
        raise

if __name__ == "__main__":
    train_logo_detector()