import pytest
import pandas as pd
from src.data_loader import DataLoader

def test_cargar_datos():
    # Crear datos de prueba
    df_test = pd.DataFrame({
        'fecha_acceso': ['2023-01-01', '2023-01-02'],
        'id_usuario': ['usr1', 'usr2'],
        'id_paciente': ['pac1', 'pac2'],
        'modulo_origen': ['CONSULTA', 'HOSPITALIZACION'],
        'accion_realizada': ['VER', 'EDITAR']
    })
    df_test.to_csv('test_data.csv', index=False)
    
    loader = DataLoader()
    df = loader.cargar_desde_csv('test_data.csv')
    
    assert len(df) == 2
    assert all(col in df.columns for col in loader.columnas_requeridas)
