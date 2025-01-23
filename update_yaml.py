# update_yaml.py
import os
from pathlib import Path
import yaml

# Obtener la ruta absoluta del proyecto
project_path = Path(os.getcwd())

# Rutas absolutas para los directorios de imágenes
train_path = str(project_path / 'data/processed/yolo_dataset/train/images')
val_path = str(project_path / 'data/processed/yolo_dataset/valid/images')
test_path = str(project_path / 'data/processed/yolo_dataset/test/images')

# Configuración del dataset
dataset_config = {
    'train': train_path,
    'val': val_path,
    'test': test_path,
    'nc': 54,  # Número de clases
    'names': ['adidas', 'adidas_1', 'adidas_2', 'apple', 'apple_1', 'bmw', 'bmw_1', 'bmw_2', 
              'citroen_1', 'citroen_2', 'coca_cola_1', 'dhl_1', 'fedex_1', 'ferrari_1', 
              'ferrari_2', 'ford_1', 'google_1', 'google_1c', 'hec', 'heineken_1', 'heineken_2', 
              'hp_1', 'intel_1', 'mc_donalds_1', 'mc_donalds_2', 'mcaffe', 'mini_bmw_1', 
              'nbc_1', 'nbc_2', 'nike_1', 'nike_2', 'pepsi_1', 'pepsi_2', 'porsche_1', 
              'porsche_2', 'puma_1', 'puma_2', 'red_bull_1', 'red_bull_2', 'redbull_1', 
              'redbull_2', 'sprite_1', 'sprite_2', 'starbucks_1', 'texaco_1', 'texaco_2', 
              'unicef', 'unicef_1', 'unicef_2', 'vodafone_1', 'vodafone_2', 'yahoo', 
              'yahoo_1', 'yahoo_2']
}

# Guardar la configuración en el archivo yaml
yaml_path = project_path / 'data/processed/yolo_dataset/data.yaml'
with open(yaml_path, 'w') as f:
    yaml.dump(dataset_config, f, default_flow_style=False)

print(f"Archivo YAML actualizado con rutas absolutas en: {yaml_path}")
