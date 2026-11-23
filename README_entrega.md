# Entrega MOOVI - Traballo de Análise Matemática 2026/2027

GRUPO: _______________________________________
Alumno que realiza a presentación: _______________________________________

## Contido do arquivo comprimido

| Ficheiro | Descrición |
|---|---|
| `memoria/memoria.pdf` | Memoria escrita: Newton, Halley e Chebyshev con dedución, interpretación xeométrica, resultados e bibliografía |
| `presentacion/presentacion.pptx` | Presentación de 8 diapositivas con notas do relator |
| `Newton.py` | Código fuente do fractal de Newton |
| `Halley.py` | Código fuente do fractal de Halley |
| `Chebyshev.py` | Código fuente do fractal de Chebyshev |
| `imaxes/fractal_Newton.png` | Fractal do método de Newton |
| `imaxes/fractal_Halley.png` | Fractal do método de Halley |
| `imaxes/fractal_Chebyshev.png` | Fractal do método de Chebyshev |
| `README_entrega.md` | Este ficheiro |

## Función escollida

f(z) = z³ - 2z + 2. Cada grupo usa unha función distinta. Esta non pertence á familia z^n - 1 e as súas tres raíces dan concas de tamaños distintos. As derivadas son f'(z) = 3z² - 2 e f''(z) = 6z.

## Reprodución dos resultados

Necesítanse `numpy`, `sympy` e `matplotlib`. Desde a raíz do proxecto:

```bash
python Newton.py
python Halley.py
python Chebyshev.py
```

Cada script escribe a súa imaxe en `imaxes/` e non abre ventá. Parámetros comúns: ventá [-2, 2] x [-2, 2], 600 puntos por eixo, 30 iteracións máximas e tolerancia 1e-6.

## Nota

Os tres programas comparten o bloque de iteración orixinal de `Newton.py`. Para Halley e Chebyshev só se engadiu a segunda derivada e se cambiou a función `g(z)`.
