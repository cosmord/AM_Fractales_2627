# Propuesta: explorador interactivo de fractales para el trabajo de AM

Ideas investigadas y revisadas para convertir `Newton.py` en una herramienta tipo Maxima/GeoGebra: Python en el backend, frontend HTML con Tailwind CSS, glassmorphism, gráficas reales e iconos. Esto es una propuesta, no código implementado.

## Resumen

La herramienta ideal no es una galería de imágenes bonitas. Es un explorador donde cada píxel y cada número salen de ejecutar las mismas fórmulas que entrega el trabajo. El alumno escribe `f(z)`, elige Newton, Halley o Chebyshev, hace zoom en el plano complejo, pincha un punto y ve la órbita completa de iteraciones con sus valores. La memoria y los tres PNG obligatorios siguen siendo los entregables; esta interfaz sirve para entenderlos y defenderlos en la exposición.

**Recomendación:** backend Python con FastAPI (SymPy + NumPy) y frontend estático con Tailwind. WebGL solo para el lienzo del fractal si el Canvas 2D se queda corto. Pyodide queda como opción offline, no como arquitectura principal.

## Contexto y límite de alcance

El enunciado (`docs/Traballo_AM.pdf`) pide memoria (30 %), exposición de 5 a 8 minutos (40 %) y tres fractales con fórmulas correctas (30 %). La herramienta no está en la rúbrica. Su valor está en la exposición: permite mostrar la convergencia paso a paso en lugar de una imagen estática. Si aprieta el plazo del 30 de noviembre, primero cerrar memoria, presentación y los tres scripts.

## Qué significa "representación real"

Una representación es real cuando cumple estas cinco condiciones:

1. El color de cada píxel viene de ejecutar la iteración sobre ese punto, con la misma `g(z)` y la misma guarda `abs(g(z)) < 1/tol` que `Newton.py`.
2. Las raíces que se marcan se calculan desde `f`, no se colocan a ojo.
3. La órbita que se dibuja es la sucesión `z₀, z₁, …` obtenida con el método seleccionado.
4. Las fórmulas `f`, `f'`, `f''` y `g` que se muestran son las que SymPy derivó, no texto copiado.
5. Cualquier imagen exportada lleva asociados los parámetros que la generaron y se puede reproducir.

Si algo de esto falta, la interfaz está decorando, no representando.

## Opciones de arquitectura

| Opción | Cómo funciona | A favor | En contra |
|---|---|---|---|
| A. Todo en el navegador con Pyodide | SymPy y NumPy compilados a WebAssembly; sin servidor | Se reparte como archivos estáticos; Python de verdad en el cliente | Arranca con la carga del runtime; cálculo más lento que nativo |
| B. FastAPI + frontend Tailwind | Python calcula; el navegador dibuja y envía parámetros | Mismo stack que los scripts de la entrega; fácil de depurar y validar | Necesita servidor corriendo |
| C. Híbrida (recomendada) | FastAPI calcula y sirve; WebGL/Canvas dibuja; Pyodide solo para demo offline | Paridad con `Newton.py`, buen render, opción sin servidor | Más piezas que mantener |

Pyodide incluye `sympy` 1.14.0 en su lista de paquetes y anuncia paquetes científicos como NumPy en su página principal ([Pyodide, packages built in](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)); se cargan con `loadPackage` o `micropip` ([Pyodide, loading packages](https://pyodide.org/en/stable/usage/loading-packages.html)). Eso hace viable la opción A, pero no obliga a elegirla.

## Stack propuesto

| Capa | Herramienta | Uso concreto | Evidencia |
|---|---|---|---|
| Backend | FastAPI + uvicorn | Endpoints de cálculo y WebSocket de progreso | [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) |
| Simbólico | SymPy | Derivadas y `g(z)` idénticas a los scripts | Ya está en `Newton.py` |
| Numérico | NumPy | Malla compleja e iteración vectorizada | Ya está en `Newton.py` |
| Frontend | HTML + Tailwind CSS | Paneles glass, controles, diseño responsive | [Tailwind backdrop-blur](https://tailwindcss.com/docs/backdrop-filter-blur) |
| Lienzo fractal | Canvas 2D → WebGL (fragment shader) | Render y pan/zoom del plano complejo | [Newton fractals with WebGL](https://jasmcole.com/2021/10/18/newton-fractals-with-webgl/), [visualización WebGL](https://lukezapart.com/newtons-method) |
| Gráficas secundarias | Plotly.js | Histograma de iteraciones, superficie 3D, órbita | [Plotly heatmaps JS](https://plotly.com/javascript/heatmaps/) |
| Iconos | Lucide (CDN o paquete vanilla) | Controles de método, zoom, exportar, play | [Lucide getting started](https://lucide.dev/guide/lucide/getting-started) |
| Fórmulas | KaTeX con auto-render | Mostrar `f`, `f'`, `f''`, `g` en notación limpia | [KaTeX auto-render](https://katex.org/docs/autorender) |

Confianza alta en las capacidades de las librerías: vienen de sus documentaciones oficiales. Confianza media en las recomendaciones de rendimiento: salen de artículos y hilos de comunidad, no de benchmarks propios.

## Diseño visual

El elemento protagonista es el fractal, no una tarjeta de métricas. Los paneles de cristal flotan sobre el lienzo y solo se ven bien porque hay algo detrás que desenfocar. Esa es la diferencia entre glassmorphism y una caja gris semitransparente.

```html
<section class="rounded-2xl border border-white/15 bg-white/10
                backdrop-blur-2xl shadow-2xl shadow-black/30">
```

Receta basada en `bg-white/10` plus `backdrop-blur` plus borde claro; ver [este tutorial de glassmorphism con Tailwind](https://efeele.dev/en/blog/posts/glassmorphism-with-tailwind-css/) y la [documentación oficial de blur](https://tailwindcss.com/docs/backdrop-filter-blur).

**Tokens propuestos**

| Rol | Valor |
|---|---|
| Fondo | `#070B14`, azul noche casi negro |
| Cristal | `bg-white/10`, borde `white/15`, `backdrop-blur-2xl` |
| Acento | `#6EE7F9` cian, solo para el método activo y el foco de teclado |
| Texto | `#E6EDF7`; secundario `#93A4BC` |
| Tipografía | Space Grotesk para títulos, IBM Plex Mono para números y coordenadas |

Evitar el paquete de clichés: fondo crema con serif, acento verde ácido, tarjetas idénticas con el mismo radio y sombra, etiquetas en mayúsculas espaciadas sobre cada bloque. Aquí el color lo pone el fractal y la interfaz se queda callada.

**Esquema de pantalla**

```text
┌──────────────────────────────────────────────────────────────┐
│ f(z) [ z/(z²+z)^(1/2) ]   Newton │ Halley │ Chebyshev   ⚙    │
├──────────────┬────────────────────────────────┬──────────────┤
│ Fórmulas     │  plano complejo                │ Punto elegido│
│ f(z)         │  pan/zoom, raíces, órbita      │ z₀ … z_n     │
│ f'(z)        │                                │ |f(z_n)|     │
│ f''(z)       │                                │ ▶ pausa      │
│ g(z)         │                                │              │
├──────────────┴────────────────────────────────┴──────────────┤
│ Histograma n │ Tríptico de los 3 métodos      │ Exportar PNG │
└──────────────────────────────────────────────────────────────┘
```

Detalles de acabado que importan: `tabular-nums` en los contadores de iteración, `text-wrap: balance` en los títulos, áreas de pulsación de 40 a 44 px, transiciones explícitas (nunca `transition: all`), entrada con opacidad y leve desplazamiento, salida más corta, y respeto a `prefers-reduced-motion`.

## Funcionalidades, por prioridad

**P0. Imprescindibles**

- Selector de los tres métodos con la misma ventana de coordenadas.
- Lienzo del plano complejo con pan, zoom y coordenadas del cursor.
- Cálculo real en Python con los parámetros de `Newton.py`: `a, b, c, d, npuntos, maxiter, tol`.
- Clic en un punto y dibujo de su órbita con tabla `n`, `z_n`, `|f(z_n)|`.
- Panel KaTeX con las fórmulas derivadas por SymPy.
- Exportación del PNG con los parámetros usados.

**P1. Diferenciales para la exposición**

- Tríptico sincronizado Newton/Halley/Chebyshev. Compara cuencas y velocidad sin cambiar de pestaña.
- Modo presentación: secuencia guiada «función → derivada → fórmula → órbita → fractal → zoom → comparación» con flechas de teclado. Cuenta la historia en 5 a 8 minutos.
- Coloreado suave con conteo continuo de iteraciones para quitar las bandas de color. La técnica está descrita para fractales de escape ([smooth iteration count](https://iquilezles.org/articles/msetsmooth/), [introducción a Newton fractals](https://ryhl.io/blog/newton-intro/)); adaptarla a convergencia hacia raíces exige validarla contra el conteo entero de `Newton.py`.
- Histograma del número de iteraciones por método. Enlaza directamente con el artículo de Varona que pide la bibliografía.

**P2. Si sobra tiempo**

- Marsh de parámetros con animación, por ejemplo hacer variar el término de una función con el tiempo, como en [esta visualización WebGL](https://lukezapart.com/newtons-method).
- Demo offline con Pyodide como fallback cuando no hay servidor.
- Guardar y cargar configuraciones en JSON para repetir una imagen exacta.

## Contrato Python ↔ frontend

HTTP para cálculos discretos y WebSocket solo para trabajos largos. Un `hash` de parámetros permite cachear resultados idénticos.

```json
POST /api/compute
{
  "function": "z/(z**2+z)**(1/2)",
  "method": "newton",
  "viewport": {"a": -1.1, "b": 0.6, "c": -0.5, "d": 0.5},
  "npuntos": 600,
  "maxiter": 30,
  "tol": 1e-6
}
```

```json
{
  "method": "newton",
  "formulas": {"f": "...", "df": "...", "g": "..."},
  "roots": [{"re": 0, "im": 0}],
  "iterations": [[0, 1, 2]],
  "elapsed_ms": 0,
  "params_hash": "..."
}
```

`/api/orbit` recibe `z0` y devuelve la lista de puntos con `|f(z_n)|` y el motivo de parada: convergió, alcanzó `maxiter` o saltó la guarda. Ese motivo debe verse en la interfaz; es información matemática, no un detalle de implementación.

## Precisión y paridad: el punto delicado

La función del grupo, `f(z) = z³-2z+2`, es un polinomio sin cortes de rama. El punto delicado son los ceros de `f'`, en `z=±0,816497`, donde `g(z)` tiene polos y la guarda `abs(g(z)) < 1/tol` decide el color. Un shader y NumPy pueden tratar el desbordamiento de forma distinta: si eso pasa, la imagen del explorador no coincide con `fractal_Newton.png` y la herramienta miente.

Antes de mostrar cualquier gráfico:

1. Tomar una muestra de 20 a 50 puntos complejos y comparar `g(z)` calculada en Python con la del renderizador.
2. Comparar el conteo de iteraciones de esos puntos contra la matriz que produce `Newton.py`.
3. Repetir la comprobación para Halley y Chebyshev, que añaden `f''`.
4. Documentar la tolerancia aceptada. Si un solo píxel difiere cerca de un polo de `g`, se marca como diferencia conocida en la memoria.

Otra trampa: Halley y Chebyshev necesitan derivada segunda. Si se calcula en el shader, hay que generar esa expresión desde SymPy y revisarla. Más seguro: calcular en Python y enviar al navegador una textura con la matriz de iteraciones. Plotly sirve para el histograma y la superficie 3D, no para mover 2000×2000 píxeles; ya hay reportes de lentitud con matrices grandes ([hilo de Plotly](https://community.plotly.com/t/performance-issues-when-displaying-large-matrices-as-heatmaps/23845)).

## Hoja de ruta

| Fase | Entrega | Condición de salida |
|---|---|---|
| 0 | Paridad matemática | Los puntos de prueba coinciden entre Python y renderizador |
| 1 | Estructura visual | Tailwind, glass, KaTeX, Lucide, controles sin datos falsos |
| 2 | Backend | `/api/compute` y `/api/orbit` devuelven los mismos valores que los scripts |
| 3 | Lienzo | Pan, zoom, raíces y órbita dibujada sobre el fractal real |
| 4 | Comparación | Tríptico, histograma, modos de color, exportación reproducible |
| 5 | Exposición | Modo presentación y capturas para las diapositivas |

La fase 0 va primero. Un render precioso calculado con la fórmula equivocada empeora la nota en el apartado de corrección de fórmulas.

## Revisión crítica

- No sustituye la memoria ni los tres scripts. La rúbrica no premia esta interfaz.
- No generar imágenes de ejemplo con datos inventados para rellenar la demo.
- No tocar `Newton.py`; la herramienta debe consumir su lógica, no reescribirla.
- Empezar con Canvas 2D a 300×300. Pasar a WebGL solo si el zoom se nota lento.
- Pyodide es cómodo para compartir, pero WASM no iguala el rendimiento de NumPy; usarlo como fallback, no como motor principal.
- El coloreado suave es estético, no obligatorio. Si no se valida, dejar el conteo entero del programa original.
- Riesgo principal de alcance: construir un producto completo cuando solo se necesita una herramienta de clase. La versión útil cabe en un fin de semana; la versión perfecta no cabe antes del 30 de noviembre.

## Fuentes

1. [Pyodide: paquetes incluidos](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) (SymPy 1.14.0), [carga de paquetes](https://pyodide.org/en/stable/usage/loading-packages.html) y [página principal](https://pyodide.org/): Python científico en el navegador.
2. [Tailwind CSS: backdrop-filter blur](https://tailwindcss.com/docs/backdrop-filter-blur) y [glassmorphism con Tailwind](https://efeele.dev/en/blog/posts/glassmorphism-with-tailwind-css/): base de la técnica de cristal.
3. [FastAPI: WebSockets](https://fastapi.tiangolo.com/advanced/websockets/): patrón de canal para progreso de cálculos largos.
4. [Plotly.js: heatmaps](https://plotly.com/javascript/heatmaps/) y [hilo de rendimiento con matrices grandes](https://community.plotly.com/t/performance-issues-when-displaying-large-matrices-as-heatmaps/23845): gráficas secundarias y límite del render.
5. [Newton fractals with WebGL](https://jasmcole.com/2021/10/18/newton-fractals-with-webgl/) y [Visualizing Newton's method using WebGL](https://lukezapart.com/newtons-method): cuencas de atracción y coloreado en tiempo real.
6. [Introduction to Newton Fractals](https://ryhl.io/blog/newton-intro/) y [smooth iteration count](https://iquilezles.org/articles/msetsmooth/): coloreado continuo.
7. [Lucide para JavaScript vanilla](https://lucide.dev/guide/lucide/getting-started) y [KaTeX auto-render](https://katex.org/docs/autorender): iconos y fórmulas.
8. [Newton fractal (Wikipedia)](https://en.wikipedia.org/wiki/Newton_fractal) y enunciado del curso (`docs/Traballo_AM.pdf`), que cita a Varona como referencia principal.

## Metodología

Se revisaron nueve búsquedas y los fragmentos de sus páginas de origen, priorizando documentación oficial y artículos técnicos. Se separaron tres niveles: capacidades verificadas de librerías, recomendaciones de rendimiento con una sola fuente y decisiones de diseño propias. No se ejecutó ninguna de estas librerías en este repositorio, así que el documento propone arquitectura, no la valida en máquina.
