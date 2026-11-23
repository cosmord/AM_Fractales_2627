# `Newton.py`

Programa base que dibuja el fractal del método de Newton para la función compleja que eligió el grupo. Está escrito en Python con comentarios en gallego. Lee el archivo completo antes de tocar nada: la mitad inferior está marcada como "NON MODIFICAR".

## Estructura

| Bloque | Qué hace |
|---|---|
| Importaciones | `numpy` para la malla, `sympy` para derivar, `matplotlib` para dibujar |
| Definición de `f` | `z = Symbol('z')` y `f = ...`. Función del grupo, lo único que cambia de un grupo a otro |
| Derivada | `derf = Derivative(f,z,1).doit()`. SymPy deriva `f` respecto de `z` |
| Función de iteración | `g = simplify(z - f/derf)`. Un paso de Newton: `z_{n+1} = z_n - f(z_n)/f'(z_n)` |
| Parámetros | `maxiter`, `a`, `b`, `c`, `d`, `npuntos`. Ventana, malla y coste |
| Bloque fijo | Bajo "NON MODIFICAR": convierte las expresiones a numpy, itera y rellena la matriz |
| Salida | Imprime las fórmulas, dibuja y guarda el PNG |

La función del grupo es:

```python
f = z**3-2*z+2
```

Tiene tres raíces simples: `-1,769292`, `0,884646 + 0,589743i` y `0,884646 - 0,589743i`. Su derivada se anula en `z = ±0,816497`, dentro de la ventana; ahí `g(z)` tiene polos en Newton y Chebyshev (en Halley el factor cancela) y la guarda del bucle corta la iteración. Eso explica los puntos aislados, no es un error del programa.

## Parámetros

| Parámetro | Valor actual | Efecto | Editable |
|---|---|---|---|
| `maxiter` | 30 | Máximo de pasos por punto. Más pasos, más detalle en las fronteras | Sí |
| `a`, `b` | -2, 2 | Borde horizontal de la ventana, eje real | Sí |
| `c`, `d` | -2, 2 | Borde vertical, eje imaginario | Sí |
| `npuntos` | 600 | Puntos por eje. La malla tiene `(npuntos+1)^2` puntos | Sí |
| `tol` | 1e-6 | Umbral de convergencia sobre `|f(z)|` | No, está en el bloque fijo |
| `cmap` | 3 colores + gris | Una color por raíz; gris si no converge | Sí, por estética |
| `dpi` | 300 | Resolución del PNG guardado | Sí |

Subir `npuntos` de 600 a 1200 cuadruplica el trabajo. Para probar, baja a 300 y sube solo la imagen final.

## Qué hace el bucle

Para cada par de índices `i, j` entre `0` y `npuntos` se toma `z0 = x[i] + 1j*y[j]`:

1. Pone `n = 0`.
2. Mientras `n < maxiter` y `|f(z)| > tol`, aplica `z = g(z)` y suma 1 a `n`.
3. Antes de aplicar `g`, comprueba `|g(z)| < 1/tol`, es decir, `< 1e6`. Si no se cumple, rompe el bucle. Así evita valores infinitos cuando la iterate se dispara.
4. Escribe `n` en `fractal[npuntos-j, i]`. El `npuntos-j` invierte el eje Y para que la imagen se lea como el plano complejo.

El color de cada píxel indica a qué raíz convergió. Las zonas de un mismo color son la cuenca de atracción de una raíz; el gris marca los puntos sin convergencia. Las fronteras entre cuencas son el fractal. El número de iteraciones se guarda aparte para las estadísticas.

`gg(z)` es la función `g` completa ya convertida a numpy, no la derivada. Una llamada a `gg(z)` equivale a un paso de Newton. `ff(z)` es `f(z)` en numpy.

## Cómo ejecutarlo

Necesitas `numpy`, `sympy` y `matplotlib`. El enunciado recomienda instalar Anaconda. Desde la carpeta del proyecto:

```bash
python Newton.py
```

Se guarda `imaxes/fractal_Newton.png` (la carpeta se crea si no existe) y la figura se cierra al terminar, sin abrir ventana.

## Qué se puede cambiar y qué no

Sí: `f`, los parámetros de la ventana, `maxiter`, `npuntos`, `cmap`, `dpi`, el texto de los `print` y el nombre del PNG.

No, salvo la excepción documentada: los rangos de `i` y `j` se ampliaron a `npuntos+1` porque con `npuntos` quedaban 601 celdas sin calcular. Si necesitas otro método, copia el archivo a `Halley.py` o `Chebyshev.py` y cambia solo `g`. Ver [docs/metodos-halley-chebyshev.md](metodos-halley-chebyshev.md). Para un recorrido desde cero, [docs/tutorial-primer-fractal.md](tutorial-primer-fractal.md).

Dentro del bucle, `z` deja de ser el símbolo de SymPy y pasa a ser un número complejo. No lo renombres.

## Fallos típicos

| Síntoma | Causa probable |
|---|---|
| `NameError: ff` o `gg` | Se borró o se movió el bloque "NON MODIFICAR" |
| Imagen toda de un color | Ventana mal elegida o convergencia demasiado rápida |
| Valores `inf` o avisos de desbordamiento | Se quitó la guarda `abs(gg(z)) < 1/tol` |
| `ModuleNotFoundError` | Falta alguna de las tres librerías |
| El PNG no aparece | Se buscó en otra carpeta o se cambió el nombre del archivo |
