<<<<<<< HEAD
# Test YOLO detector
=======

import unittest
import sys
from pathlib import Path
from src.models.yolo_detector import LogoDetector
import logging
import argparse

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestLogoDetector(unittest.TestCase):
    """Pruebas unitarias para el detector de logos."""
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.detector = LogoDetector()
        self.test_images_dir = Path("data/processed/yolo_dataset/test/images")
    
    def test_model_loading(self):
        """Verifica que el modelo se carga correctamente."""
        self.assertIsNotNone(self.detector.model)
    
    def test_detection_on_single_image(self):
        """Prueba la detección en una sola imagen."""
        # Obtener primera imagen de prueba
        test_images = list(self.test_images_dir.glob("*.jpg"))
        if not test_images:
            self.skipTest("No se encontraron imágenes de prueba")
        
        test_image = str(test_images[0])
        image, detections = self.detector.detect(test_image)
        
        # Verificar que las detecciones tienen el formato correcto
        if detections:
            detection = detections[0]
            self.assertIn('class', detection)
            self.assertIn('confidence', detection)
            self.assertIn('bbox', detection)
            # Verificar que solo detecta las clases que nos interesan
            self.assertIn(detection['class'], ['adidas_1', 'adidas_2', 'nike_1', 'nike_2'])

def main():
    """Función principal para ejecutar pruebas desde línea de comandos."""
    parser = argparse.ArgumentParser(description='Prueba del Detector de Logos')
    parser.add_argument(
        '--image',
        help='Ruta a una imagen específica para prueba'
    )
    parser.add_argument(
        '--output',
        default='data/processed/frames/result.jpg',
        help='Ruta donde guardar el resultado'
    )
    
    args = parser.parse_args()
    
    if args.image:
        # Modo de prueba en una imagen específica
        try:
            detector = LogoDetector()
            logger.info(f"Probando detección en: {args.image}")
            
            image, detections = detector.detect(args.image)
            detector.save_result(image, args.output)
            
            print("\nResultados de la Detección:")
            print("-" * 50)
            for det in detections:
                print(f"Logo: {det['class']}")
                print(f"Confianza: {det['confidence']:.2f}")
                print(f"Ubicación: {det['bbox']}")
                print("-" * 50)
                
        except Exception as e:
            logger.error(f"Error en la detección: {e}")
            sys.exit(1)
    else:
        # Ejecutar todas las pruebas unitarias
        unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == "__main__":
    main()
>>>>>>> 777777e (essential level)
