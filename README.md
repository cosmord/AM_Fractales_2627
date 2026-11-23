# Fractales con métodos iterativos (AM 2026/2027)

Trabajo de Análise Matemática de la UVigo (ESEI Ourense, Grado en Enxeñaría Informática). Cada grupo entrega una memoria, una presentación, tres scripts Python y tres imágenes fractales en un único ZIP en MOOVI.

## Mapa del repositorio

| Archivo | Para qué sirve |
|---|---|
| [`docs/Traballo_AM.pdf`](docs/Traballo_AM.pdf) | Enunciado oficial. Fuente de verdad. No editar. |
| [`Newton.py`](Newton.py) | Programa base de FAITIC con la función del grupo ya puesta. |
| [`docs/analisis-trabajo.md`](docs/analisis-trabajo.md) | Qué hay que hacer, en qué orden y cómo se evalúa. |
| [`docs/tutorial-primer-fractal.md`](docs/tutorial-primer-fractal.md) | De cero a `fractal_Newton.png` en tres pasos. |
| [`docs/newton-py.md`](docs/newton-py.md) | Cómo está montado `Newton.py` y qué se puede cambiar. |
| [`docs/metodos-halley-chebyshev.md`](docs/metodos-halley-chebyshev.md) | Cómo derivar `Halley.py` y `Chebyshev.py`. |
| [`improvement.md`](improvement.md) | Propuesta investigada de una interfaz glassmorphism tipo GeoGebra para el trabajo. |
| [`profe.md`](profe.md) | Evaluación del profesor sobre `vibedv2`: nota 8,5/10, preguntas y correcciones. |
| [`Newton.py`](Newton.py), [`Halley.py`](Halley.py), [`Chebyshev.py`](Chebyshev.py) | Código fuente de los tres fractales. |
| [`memoria/memoria.pdf`](memoria/memoria.pdf) | Memoria escrita en gallego, con resultados reales. |
| [`presentacion/presentacion.pptx`](presentacion/presentacion.pptx) | Presentación de 8 diapositivas con notas. |
| [`presentacion/html/index.html`](presentacion/html/index.html) | Presentación HTML para clase: VS Code, Cascadia Code, partículas y animaciones. |
| [`docs/ejecucion.md`](docs/ejecucion.md) | Comandos para ejecutar y reconstruir toda la entrega. |
| [`scripts/rebuild_artifacts.py`](scripts/rebuild_artifacts.py) | Reconstruye memoria, PPTX y ZIP desde los specs. |
| [`imaxes/`](imaxes/) | Tres imágenes PNG generadas por los scripts. |
| [`entrega_AM.zip`](entrega_AM.zip) | ZIP final para subir a MOOVI. |
| [`AGENTS.md`](AGENTS.md) | Reglas de trabajo y checklist antes de subir el ZIP. |

## Entrega final

El ZIP `entrega_AM.zip` contiene memoria, presentación, los tres scripts y las tres imágenes. Los resultados numéricos de la memoria y las diapositivas salieron de ejecutar los tres scripts sobre una malla de 601 x 601 puntos.

## Secuencia mínima

1. Confirmar la función `f(z)` del grupo en `Newton.py`. Tiene que ser distinta a la de los otros grupos.
2. Ejecutar `Newton.py` y guardar `fractal_Newton.png`.
3. Copiar `Newton.py` a `Halley.py`; cambiar `g(z)` y añadir la derivada segunda.
4. Copiar `Newton.py` a `Chebyshev.py`; cambiar `g(z)` y añadir la derivada segunda.
5. Escribir la memoria: deducción de Newton, fórmula e historia de Halley, fórmula de Chebyshev, interpretación geométrica de los tres y bibliografía.
6. Preparar la exposición de 5 a 8 minutos.
7. Subir memoria, presentación, tres `.py` y tres `.png` en un ZIP a MOOVI.

## Requisitos para ejecutar

Python con `numpy`, `sympy` y `matplotlib`. El enunciado recomienda Anaconda. No hay archivo de dependencias en el repositorio.

## Antes de entregar

Seguir la checklist de `AGENTS.md`. No se hace commit sin pedirlo explícitamente.
