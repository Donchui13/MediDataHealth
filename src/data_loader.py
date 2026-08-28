"""
Módulo para carga y validación de datos de acceso.
"""
import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """Carga y valida datos de logs de acceso."""
    
    def __init__(self):
        self.columnas_requeridas = [
            'fecha_acceso', 'id_usuario', 'id_paciente',
            'modulo_origen', 'accion_realizada'
        ]
    
    def cargar_desde_csv(self, ruta):
        """Carga datos desde archivo CSV."""
        path = Path(ruta)
        if not path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {ruta}")
        
        logger.info(f"Cargando datos desde: {ruta}")
        df = pd.read_csv(ruta)
        
        # Validar columnas
        faltantes = set(self.columnas_requeridas) - set(df.columns)
        if faltantes:
            raise ValueError(f"Columnas faltantes: {faltantes}")
        
        # Convertir fecha
        df['fecha_acceso'] = pd.to_datetime(df['fecha_acceso'])
        
        logger.info(f"Datos cargados: {len(df)} registros")
        return df
    
    def obtener_resumen(self, df):
        """Obtiene estadísticas básicas del dataset."""
        return {
            'total_registros': len(df),
            'periodo': f"{df['fecha_acceso'].min()} - {df['fecha_acceso'].max()}",
            'usuarios_unicos': df['id_usuario'].nunique(),
            'pacientes_unicos': df['id_paciente'].nunique()
        }
