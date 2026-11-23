# Tutorial: generar el primer fractal de Newton

Vas a dejar `fractal_Newton.png` en la carpeta del proyecto a partir del código base. No hace falta entender SymPy para llegar al resultado, pero [docs/newton-py.md](newton-py.md) explica cada bloque.

## Qué necesitas

- Python 3 con `numpy`, `sympy` y `matplotlib`. El enunciado recomienda Anaconda; si no lo tienes, usa `python -m pip install numpy sympy matplotlib`.
- Estar en la carpeta del proyecto, la que contiene `Newton.py`.
- Haber leído [docs/analisis-trabajo.md](analisis-trabajo.md) para saber qué entrega cada archivo.

## Paso 1: instalar las librerías

```bash
python -m pip install numpy sympy matplotlib
```

Si usas Anaconda, puedes saltarte este paso. Comprueba que las tres importan:

```bash
python -c "import numpy, sympy, matplotlib; print('listo')"
```

Debe salir `listo`.

## Paso 2: ejecutar el programa

```bash
python Newton.py
```

Verás por pantalla el encabezado `MÉTODO DE NEWTON` y las expresiones de `f(z)`, `derf(z)` y `g(z)`. Al terminar aparece `fractal_Newton.png` dentro de la carpeta `imaxes/`. La imagen tarda unos segundos porque `npuntos=600` y se guarda a 300 dpi.

## Paso 3: mirar el resultado

Abre `fractal_Newton.png`. Deben verse regiones de color uniforme separadas por fronteras con detalle. Cada región es la cuenca de atracción de una raíz; la frontera es el fractal.

Si sale una imagen plana o toda de un color, cambia la ventana (`a`, `b`, `c`, `d`) o sube `maxiter`. La tabla de [docs/newton-py.md](newton-py.md) dice qué hace cada parámetro.

## Qué has conseguido

Tienes el primer entregable gráfico. El siguiente paso es copiar `Newton.py` y obtener los otros dos fractales con [docs/metodos-halley-chebyshev.md](metodos-halley-chebyshev.md). La memoria y la presentación se apoyan en [docs/analisis-trabajo.md](analisis-trabajo.md).
