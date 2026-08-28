"""
Módulo para creación de características (features).
"""
import pandas as pd
import numpy as np

class FeatureEngineer:
    """Crea features para el modelo de detección de anomalías."""
    
    def crear_features_temporales(self, df):
        """Crea características basadas en tiempo."""
        df['hora'] = df['fecha_acceso'].dt.hour
        df['dia_semana'] = df['fecha_acceso'].dt.dayofweek
        df['mes'] = df['fecha_acceso'].dt.month
        df['es_fin_semana'] = df['dia_semana'].isin([5, 6]).astype(int)
        df['hora_laboral'] = ((df['hora'] >= 8) & (df['hora'] <= 18)).astype(int)
        return df
    
    def crear_features_usuario(self, df):
        """Crea características por usuario."""
        # Frecuencia de accesos por usuario
        freq_usuario = df.groupby('id_usuario').size().reset_index(name='frecuencia_usuario')
        df = df.merge(freq_usuario, on='id_usuario', how='left')
        
        # Horas promedio de acceso por usuario
        hora_media = df.groupby('id_usuario')['hora'].mean().reset_index(name='hora_media_usuario')
        df = df.merge(hora_media, on='id_usuario', how='left')
        
        return df
    
    def preparar_features(self, df):
        """Ejecuta todas las transformaciones."""
        df = self.crear_features_temporales(df)
        df = self.crear_features_usuario(df)
        return df
