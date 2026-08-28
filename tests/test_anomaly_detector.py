import pytest
import pandas as pd
from src.anomaly_detector import AnomalyDetector

def test_deteccion_anomalias():
    # Crear datos de prueba
    df = pd.DataFrame({
        'hora': [10, 11, 12, 3, 4],
        'dia_semana': [1, 2, 3, 6, 0],
        'frecuencia_usuario': [10, 12, 11, 50, 8],
        'hora_media_usuario': [10.5, 11.0, 10.8, 15.0, 9.5]
    })
    
    detector = AnomalyDetector()
    detector.entrenar(df)
    resultado = detector.detectar(df)
    
    assert 'es_anomalia' in resultado.columns
    assert len(resultado) == len(df)
