# Ficha del dataset — SpamShield

## 1. Identificación

- **Proyecto:** SpamShield.
- **Asignatura:** INF-8239 Ciencia de Datos II.
- **Modalidad:** Proyecto aplicado de ciencia de datos.
- **Problema:** clasificación binaria de correos electrónicos como legítimos o no deseados.
- **Dataset:** SpamAssassin Public Corpus.
- **Variable de entrada:** `message`.
- **Variable objetivo:** `label`.
- **Clases:** `ham` (correo legítimo) y `spam` (correo no deseado).
- **Archivo procesado:** `data/processed/emails_clean.csv`.

## 2. Procedencia y cobertura

El conjunto de datos utilizado procede del **SpamAssassin Public Corpus**, una colección histórica de mensajes de correo electrónico publicada para estudiar y evaluar técnicas de filtrado de spam.

**Fuente oficial:**  
https://spamassassin.apache.org/old/publiccorpus/readme.html

Los cinco archivos utilizados en el experimento son:

- `20030228_easy_ham.tar.bz2`
- `20030228_easy_ham_2.tar.bz2`
- `20030228_hard_ham.tar.bz2`
- `20030228_spam.tar.bz2`
- `20050311_spam_2.tar.bz2`

El corpus contiene mensajes históricos, principalmente de 2003 y 2005. Por tanto, no representa necesariamente las características del correo no deseado actual y sus resultados no garantizan el mismo desempeño ante campañas contemporáneas.

### 2.1 Trazabilidad y condiciones de uso

- **Fuente consultada:** SpamAssassin Public Corpus.
- **URL de referencia:** https://spamassassin.apache.org/old/publiccorpus/readme.html
- **Fecha de consulta:** 20/10/2026.
- **Fecha de descarga:** 22/10/2026.
- **Archivos originales:** los cinco archivos enumerados en esta ficha.
- **Licencia y redistribución:** deben documentarse según las condiciones aplicables a la versión y distribución utilizadas. No se atribuye automáticamente una licencia única a todos los mensajes, cuyo contenido puede estar sujeto a derechos de terceros.

La disponibilidad pública de un corpus no debe interpretarse, por sí sola, como autorización irrestricta para redistribuir todos sus mensajes. Antes de publicar los mensajes originales o extractos, deben revisarse las condiciones aplicables.

## 3. Composición del conjunto de datos

### 3.1 Datos antes de la limpieza

El proceso inicial identificó **6,048 mensajes**:

| Indicador | Cantidad |
|---|---:|
| Mensajes legítimos (`ham`) | 4,153 |
| Mensajes no deseados (`spam`) | 1,895 |
| Valores faltantes detectados | 0 |
| Mensajes vacíos detectados | 0 |
| Filas duplicadas completas | 147 |
| Mensajes repetidos al comparar el texto | 151 |
| Textos con etiquetas contradictorias | 0 |

Las cantidades de filas duplicadas completas y mensajes repetidos por texto corresponden a criterios de comparación diferentes; no deben sumarse como si representaran grupos independientes de registros.

### 3.2 Datos después de la limpieza

Después de eliminar las repeticiones de texto, el conjunto quedó compuesto por **5,897 mensajes**.

| Clase | Mensajes | Porcentaje |
|---|---:|---:|
| `ham` | 4,111 | 69.71 % |
| `spam` | 1,786 | 30.29 % |
| **Total** | **5,897** | **100 %** |

La distribución presenta un desequilibrio moderado a favor de los mensajes legítimos. Por ello, la evaluación no se limita a la exactitud: también considera el F1 Macro y las métricas específicas de la clase `spam`.

## 4. Limpieza y preparación

El procesamiento contempla las siguientes operaciones:

1. Identificar los registros que contienen mensajes y etiquetas válidos.
2. Excluir los mensajes vacíos y los registros que no cumplen el contrato de datos.
3. Eliminar las repeticiones de texto para evitar que un mismo mensaje aparezca varias veces en el conjunto final.
4. Conservar el archivo original sin sobrescribirlo.
5. Guardar el conjunto limpio en `data/processed/emails_clean.csv`.
6. Mantener `source_archive` para trazabilidad, sin utilizarlo como predictor.

La variable `source_archive` se excluye de las características predictivas porque la procedencia del archivo puede estar asociada con la clase. Su utilización podría permitir que el modelo aprendiera señales relacionadas con la distribución de los datos en lugar de patrones generalizables del mensaje.

### 4.1 Representación del texto

Los modelos utilizan TF-IDF para transformar el texto en características numéricas. La configuración contempla:

- Conversión a minúsculas.
- Normalización de acentos.
- Unigramas y bigramas.
- Límite de 50,000 características.
- `sublinear_tf=True`.

La transformación se incorpora al pipeline de cada modelo para que el vocabulario y los pesos de TF-IDF se ajusten con los datos de entrenamiento, evitando utilizar información del conjunto de prueba durante el ajuste.

## 5. Contrato de datos

El conjunto procesado debe cumplir las siguientes condiciones:

| Elemento | Condición esperada |
|---|---|
| Archivo | `data/processed/emails_clean.csv` |
| Columnas principales | `message`, `label` |
| Columna de trazabilidad | `source_archive` |
| Mensaje | No nulo ni vacío |
| Etiqueta | `ham` o `spam` |
| Repeticiones de texto | Ninguna, según la normalización utilizada por el proceso de limpieza |
| Clases | Dos clases presentes |
| Registros esperados | 5,897 |

La comprobación automatizada de estas condiciones forma parte de las pruebas del proyecto.

## 6. Partición experimental

Para comparar los modelos bajo las mismas condiciones se utilizó una partición estratificada de entrenamiento y prueba.

| Indicador | Valor |
|---|---:|
| Registros limpios | 5,897 |
| Entrenamiento | 4,717 |
| Prueba | 1,180 |
| Proporción | 80/20 |
| Semilla aleatoria | `random_state=42` |
| Estratificación | Sí |
| Clase positiva para las métricas de spam | `spam` |

El conjunto de prueba se mantiene separado durante el ajuste de los modelos. La estratificación procura conservar la proporción de ambas clases en los dos subconjuntos.

## 7. Limitaciones y riesgos

- **Antigüedad:** los mensajes proceden principalmente de 2003 y 2005, por lo que pueden no representar las técnicas actuales de spam.
- **Representatividad:** el corpus no garantiza cubrir todos los idiomas, sectores, proveedores de correo ni tipos de mensajes legítimos.
- **Cabeceras y firmas:** los mensajes pueden contener cabeceras, citas, firmas y otros elementos que faciliten la clasificación por motivos distintos del significado del contenido.
- **Duplicados aproximados:** la eliminación de textos repetidos no garantiza que se hayan eliminado todos los mensajes casi idénticos o relacionados con una misma campaña.
- **Partición aleatoria:** mensajes relacionados pueden distribuirse entre entrenamiento y prueba. Esto puede producir una estimación optimista del desempeño ante mensajes verdaderamente nuevos.
- **Desbalance de clases:** una proporción mayor de mensajes legítimos puede afectar la interpretación de métricas agregadas.
- **Errores de clasificación:** un mensaje legítimo clasificado como spam puede ocasionar la pérdida de una comunicación importante. Un mensaje spam clasificado como legítimo puede llegar a la bandeja de entrada.
- **Generalización:** el desempeño medido en esta partición no garantiza resultados equivalentes en producción.
- **Privacidad y derechos:** los mensajes pueden contener información de terceros; su publicación y redistribución requieren revisar las condiciones correspondientes.

## 8. Reproducibilidad

Los componentes relacionados con la preparación y evaluación de los datos son:

- `src/clean_data.py`: limpieza y generación del archivo procesado.
- `src/audit_data.py`: auditoría de calidad y duplicados.
- `src/train_models.py`: carga de datos, validaciones, partición experimental, entrenamiento y evaluación.
- `reports/results/split_config.json`: registro de la configuración de la partición.
- `tests/test_train_models.py`: pruebas automatizadas de los datos, el protocolo experimental y el comportamiento de la demostración.

Para reproducir el flujo completo desde la raíz del proyecto, con el entorno virtual activado:

```powershell
python src/clean_data.py
python src/audit_data.py
python src/train_models.py
python src/generate_reports.py
python -m pytest -v
```

La ejecución de `train_models.py` vuelve a entrenar los modelos y puede reemplazar los artefactos existentes. Si únicamente se desea revisar los resultados ya generados, no es necesario ejecutar nuevamente todo el flujo.

## 9. Referencia

Apache SpamAssassin Project. *SpamAssassin Public Corpus*.  
https://spamassassin.apache.org/old/publiccorpus/readme.html

Consulta complementaria sobre las prácticas de selección y limpieza de corpus:

Apache SpamAssassin Project. *Corpus Cleaning*.  
https://cwiki.apache.org/confluence/spaces/SPAMASSASSIN/pages/119542142/CorpusCleaning

