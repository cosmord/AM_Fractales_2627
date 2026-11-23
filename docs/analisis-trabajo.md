# Análisis del trabajo

Todo lo que sigue sale del enunciado ([`docs/Traballo_AM.pdf`](Traballo_AM.pdf), apartados 1 a 1.3 y plantilla de valoración). Si este documento contradice al PDF, manda el PDF. Antes de empezar, [el tutorial](tutorial-primer-fractal.md) lleva de cero a la primera imagen.

## Qué se pide

Traballo de Análise Matemática, curso 2026/2027. Título: "Métodos iterativos de resolución de ecuaciones: obtención de gráficos fractais co ordeador". La memoria describe tres métodos iterativos para aproximar raíces de funciones complejas y muestra el fractal que produce cada uno.

El punto de partida es `Newton.py`, descargado de FAITIC. El programa deriva con SymPy, itera sobre una malla de números complejos y pinta el resultado.

## Entregables

| Entregable | Formato | Peso en la nota |
|---|---|---|
| Memoria | Documento escrito | 30 % |
| Presentación | Diapositivas, 5 a 8 minutos | 40 % |
| `Newton.py`, `Halley.py`, `Chebyshev.py` | Código fuente | Dentro del bloque de fractales |
| `fractal_Newton.png`, `fractal_Halley.png`, `fractal_Chebyshev.png` | Imágenes | 30 % |
| Bibliografía | Dentro de la memoria | Parte de la memoria |

Todo va junto en un único ZIP en MOOVI. No se entregan los archivos sueltos.

## Plazos

| Momento | Qué pasa |
|---|---|
| 30 de noviembre a 4 de diciembre | Exposición en clase de grupos reducidos. Habla un miembro elegido por sorteo. |
| Día del examen final | Los alumnos declarados NON ASISTENTES exponen ese mismo día, aula y hora por indicar. |

## Tareas, en orden

| # | Tarea | Listo cuando |
|---|---|---|
| 1 | Elegir `f(z)` propia del grupo; no hace falta que sea polinomio | `f` está en `Newton.py` y no coincide con la de otro grupo |
| 2 | Ajustar ventana, `maxiter` y `npuntos` en `Newton.py` | `fractal_Newton.png` muestra cuencas de atracción con nitidez |
| 3 | Crear `Halley.py` desde `Newton.py` | `g` usa la fórmula de Halley y sale `fractal_Halley.png` |
| 4 | Crear `Chebyshev.py` desde `Newton.py` | `g` usa la fórmula de Chebyshev y sale `fractal_Chebyshev.png` |
| 5 | Redactar la memoria | Newton con deducción y dibujo, Halley con contexto histórico, los tres con interpretación geométrica y fórmula, bibliografía incluida |
| 6 | Preparar la exposición | Guion de 5 a 8 minutos con las diapositivas de los tres fractales |
| 7 | Montar el ZIP y subirlo a MOOVI | Un solo archivo con todos los entregables |

La memoria y la presentación se pueden escribir en paralelo a las tareas 2 a 4. El código tiene que estar cerrado antes de pegar las imágenes en las diapositivas.

## Cómo se evalúa

| Bloque | Peso | Lo que más cuenta |
|---|---|---|
| Exposición | 40 % | Duración de 5 a 8 minutos, estructura clara, mirar a la audiencia sin leer notas, material legible |
| Memoria | 30 % | Orden y corrección ortográfica, temas correctos, toda la información pedida |
| Fractales | 30 % | Fórmulas correctas, sobre todo al menos una distinta de Newton; imágenes con estructura fractal, originales y atractivas |

La plantilla baja de nota la exposición de menos de 4 o más de 9 minutos, y los fractales en los que no se aprecia estructura fractal.

## Bibliografía que pide el enunciado

- Varona, J. L., "Graphic and numerical comparison between iterative methods", *Math. Intelligencer* 24 (2002), 37-46. Referencia principal para comparar los tres métodos.
- Varona, J. L., "Representación gráfica de fractales mediante un programa de cálculo simbólico", *Gac. R. Soc. Mat. Esp.* 6 (2003), 213-230.
- 3B1B, "Newton's Fractal (which Newton knew nothing about)". Vídeo.
- Gleick, J., *Caos: la creación de una ciencia*, Crítica, 2012.

## Fuera de alcance

No hace falta cambiar el bucle de iteración de `Newton.py`, añadir interfaces ni usar otra biblioteca distinta de las tres que ya importa el programa base.
