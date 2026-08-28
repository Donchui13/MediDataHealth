# Plan de Pruebas - MediData Health

## Tipos de Pruebas

### 1. Pruebas Unitarias
- **Herramienta:** Pytest
- **Cobertura objetivo:** 85%
- **Ejecución:** `pytest tests/`

### 2. Pruebas de Integración
- **Pipeline de datos:** Carga → Limpieza → Features
- **Pipeline de detección:** Features → Modelo → Alertas

### 3. Pruebas de Rendimiento
| Métrica | Objetivo |
|:---|:---:|
| Procesamiento 1M registros | < 10 min |
| Inferencia por acceso | < 100 ms |
| Memoria | < 2 GB |

### 4. Pruebas de Seguridad
- Verificar seudonimización
- Validar control de acceso
- Comprobar cifrado de datos

### 5. Pruebas del Modelo
| Métrica | Objetivo |
|:---|:---:|
| Precisión | > 85% |
| Recall | > 90% |
| Falsos Positivos | < 5% |
| Falsos Negativos | < 1% |
