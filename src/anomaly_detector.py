"""
Módulo para detección de anomalías con Isolation Forest.
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import logging

logger = logging.getLogger(__name__)

class AnomalyDetector:
    """Detector de anomalías usando Isolation Forest."""
    
    def __init__(self, contamination=0.01, random_state=42):
        """
        Inicializa el detector.
        
        Args:
            contamination: Proporción esperada de anomalías.
            random_state: Semilla para reproducibilidad.
        """
        self.modelo = IsolationForest(
            contamination=contamination,
            random_state=random_state,
            n_estimators=100
        )
        self.scaler = StandardScaler()
        self.entrenado = False
    
    def preparar_datos(self, df):
        """Prepara los datos para el modelo."""
        features = ['hora', 'dia_semana', 'frecuencia_usuario', 'hora_media_usuario']
        
        # Seleccionar solo columnas numéricas
        X = df[features].copy()
        
        # Manejar valores nulos
        X = X.fillna(X.mean())
        
        # Escalar datos
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, X.columns
    
    def entrenar(self, df):
        """Entrena el modelo con datos de acceso."""
        logger.info("Entrenando modelo de detección de anomalías...")
        X, _ = self.preparar_datos(df)
        self.modelo.fit(X)
        self.entrenado = True
        logger.info("Modelo entrenado correctamente")
    
    def detectar(self, df):
        """
        Detecta anomalías en los datos.
        
        Returns:
            DataFrame con columna 'es_anomalia' (1=anomalía, 0=normal)
        """
        if not self.entrenado:
            raise ValueError("El modelo debe ser entrenado primero")
        
        X, _ = self.preparar_datos(df)
        
        # Predicción: -1 = anomalía, 1 = normal
        predicciones = self.modelo.predict(X)
        
        df_resultado = df.copy()
        df_resultado['es_anomalia'] = (predicciones == -1).astype(int)
        
        n_anomalias = df_resultado['es_anomalia'].sum()
        logger.info(f"Detectadas {n_anomalias} anomalías ({n_anomalias/len(df)*100:.2f}%)")
        
        return df_resultado
