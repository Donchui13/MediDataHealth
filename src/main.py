"""
Script principal para ejecutar el flujo completo de detección de anomalías.
"""
import logging
from pathlib import Path
from data_loader import DataLoader
from data_cleaner import DataCleaner
from feature_engineering import FeatureEngineer
from anomaly_detector import AnomalyDetector
from visualizer import Visualizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Ejecuta el flujo principal del proyecto."""
    logger.info("=== INICIANDO SISTEMA DE DETECCIÓN DE ANOMALÍAS ===")
    
    # 1. Cargar datos
    loader = DataLoader()
    df = loader.cargar_desde_csv('data/raw/accesos.csv')
    logger.info(f"Resumen: {loader.obtener_resumen(df)}")
    
    # 2. Limpiar datos
    cleaner = DataCleaner()
    df = cleaner.estandarizar_acciones(df)
    df = cleaner.limpiar_fechas(df)
    df = cleaner.eliminar_duplicados(df)
    
    # 3. Crear features
    engineer = FeatureEngineer()
    df = engineer.preparar_features(df)
    
    # 4. Visualizar distribución
    visualizer = Visualizer()
    visualizer.graficar_accesos_por_hora(df)
    visualizer.graficar_accesos_por_modulo(df)
    
    # 5. Entrenar y detectar anomalías
    detector = AnomalyDetector(contamination=0.02)
    detector.entrenar(df)
    df_resultado = detector.detectar(df)
    
    # 6. Mostrar resultados
    visualizer.graficar_anomalias(df_resultado)
    
    # 7. Guardar resultados
    output_path = Path('outputs/resultados_deteccion.csv')
    df_resultado.to_csv(output_path, index=False)
    logger.info(f"Resultados guardados en: {output_path}")
    
    logger.info("=== PROCESO COMPLETADO ===")

if __name__ == "__main__":
    main()
