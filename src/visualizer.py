"""
Módulo para visualización de datos y resultados.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

class Visualizer:
    """Genera visualizaciones para el análisis de accesos."""
    
    def __init__(self, output_dir="outputs"):
        """Inicializa el visualizador."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        plt.style.use('seaborn-v0_8-whitegrid')
    
    def graficar_accesos_por_hora(self, df, guardar=True):
        """Grafica la distribución de accesos por hora."""
        plt.figure(figsize=(12, 6))
        df['hora'].value_counts().sort_index().plot(kind='bar', color='skyblue')
        plt.title('Accesos por Hora del Día')
        plt.xlabel('Hora')
        plt.ylabel('Número de Accesos')
        plt.xticks(rotation=0)
        plt.tight_layout()
        
        if guardar:
            plt.savefig(self.output_dir / 'accesos_por_hora.png')
        plt.show()
    
    def graficar_accesos_por_modulo(self, df, guardar=True):
        """Grafica la distribución de accesos por módulo."""
        plt.figure(figsize=(10, 6))
        df['modulo_origen'].value_counts().plot(kind='bar', color='lightgreen')
        plt.title('Accesos por Módulo de Origen')
        plt.xlabel('Módulo')
        plt.ylabel('Número de Accesos')
        plt.xticks(rotation=0)
        plt.tight_layout()
        
        if guardar:
            plt.savefig(self.output_dir / 'accesos_por_modulo.png')
        plt.show()
    
    def graficar_anomalias(self, df_resultado, guardar=True):
        """Grafica los resultados de detección de anomalías."""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Distribución de anomalías por hora
        anomalies = df_resultado[df_resultado['es_anomalia'] == 1]
        if not anomalies.empty:
            anomalies['hora'].value_counts().sort_index().plot(
                kind='bar', ax=axes[0], color='red'
            )
            axes[0].set_title('Anomalías por Hora')
            axes[0].set_xlabel('Hora')
            axes[0].set_ylabel('Número de Anomalías')
        
        # Proporción de anomalías
        props = df_resultado['es_anomalia'].value_counts()
        labels = ['Normal', 'Anomalía']
        axes[1].pie(props, labels=labels, autopct='%1.1f%%', 
                    colors=['lightblue', 'red'], startangle=90)
        axes[1].set_title('Proporción de Anomalías')
        
        plt.tight_layout()
        if guardar:
            plt.savefig(self.output_dir / 'resultados_anomalias.png')
        plt.show()
