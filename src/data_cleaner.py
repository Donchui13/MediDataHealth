"""
Módulo para limpieza y estandarización de datos.
"""
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class DataCleaner:
    """Limpia y estandariza datos de accesos."""
    
    def __init__(self):
        self.acciones_estandar = {
            'ver': 'VISUALIZACION',
            'view': 'VISUALIZACION',
            'visualizar': 'VISUALIZACION',
            'editar': 'EDICION',
            'modificar': 'EDICION',
            'edit': 'EDICION',
            'descargar': 'DESCARGA',
            'download': 'DESCARGA'
        }
    
    def estandarizar_acciones(self, df):
        """Estandariza los nombres de acciones."""
        df['accion_realizada'] = df['accion_realizada'].str.lower()
        df['accion_realizada'] = df['accion_realizada'].map(
            self.acciones_estandar
        ).fillna(df['accion_realizada']).str.upper()
        return df
    
    def limpiar_fechas(self, df):
        """Convierte fechas a formato datetime."""
        df['fecha_acceso'] = pd.to_datetime(df['fecha_acceso'], errors='coerce')
        # Eliminar filas con fechas nulas
        df = df.dropna(subset=['fecha_acceso'])
        return df
    
    def eliminar_duplicados(self, df):
        """Elimina registros duplicados."""
        antes = len(df)
        df = df.drop_duplicates()
        logger.info(f"Eliminados {antes - len(df)} registros duplicados")
        return df
