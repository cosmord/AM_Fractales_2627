# Halley.py y Chebyshev.py

Los otros dos gráficos salen de copiar [`Newton.py`](../Newton.py) y sustituir únicamente la función de iteración `g(z)`. El bucle, la malla y la guarda contra desbordamientos se quedan igual; los tres recorren ahora la malla completa de 601 x 601 puntos. Si aún no has generado el primer fractal, empieza por [el tutorial](tutorial-primer-fractal.md) y consulta [docs/newton-py.md](newton-py.md) para los parámetros.

## Fórmulas

Con `f' = derf` y `f'' = derf2`, escribiendo `g(z)` como el nuevo valor que sustituye a `z`:

| Método | `g(z)` | Orden de convergencia |
|---|---|---|
| Newton | `z - f/f'` | 2 |
| Halley | `z - (f·f') / ((f')² - f·f''/2)` | 3 |
| Chebyshev | `z - f/f' - (f²·f'')/(2·(f')³)` | 3 |

Halley sustituye el paso de Newton dentro de la serie de Taylor de segundo orden por un aproximante racional (1,1) de la función inversa. Chebyshev sustituye ese mismo salto por la expansión polinómica de orden 2 de la inversa. Los dos son cúbicos y se diferencian en la corrección que añaden al paso de Newton. Esa distinción conviene explicarla en la memoria.

## Pasos

1. Copia `Newton.py` a `Halley.py` y a `Chebyshev.py`.
2. Añade la derivada segunda justo debajo de `derf`:

```python
derf2 = Derivative(f, z, 2).doit()
```

3. Sustituye la definición de `g` por la del método.

En `Halley.py`:

```python
g = simplify(z - (f * derf) / (derf**2 - f * derf2 / 2))
```

En `Chebyshev.py`:

```python
g = simplify(z - f/derf - (f**2 * derf2) / (2 * derf**3))
```

4. Cambia el cartel que se imprime y el nombre del archivo:

```python
print('MÉTODO DE HALLEY')
plt.savefig('fractal_Halley.png', dpi=2000)
```

Y lo mismo con `MÉTODO DE CHEBYSHEV` y `fractal_Chebyshev.png`.

5. Ajusta la ventana y los colores si el fractal sale pequeño o plano. Cada método converge a distinta velocidad y los mismos parámetros no sirven igual para los tres.

## Verificación

- El `print` de `g(z)` debe mostrar la fórmula nueva, no la de Newton.
- Deben salir tres PNG con nombres distintos y estructura fractal visible.
- Compara las tres imágenes: los colores pueden cambiar porque `n` cuenta pasos distintos, pero las raíces y las cuencas deben coincidir.

## Fallos típicos

| Síntoma | Causa probable |
|---|---|
| `g(z)` sigue siendo `z - f/derf` | Se editó `Newton.py` en vez de la copia |
| `NameError: derf2` | Falta la línea de la derivada segunda |
| Imagen en blanco o toda de un color | `g` mal parcheada: revisa paréntesis y signos |
| Valores `inf` o avisos de desbordamiento | Se perdió la guarda `abs(gg(z)) < 1/tol` |
| Las tres imágenes son idénticas | No se cambió `g` o se guardó siempre `fractal_Newton.png` |

## Para la memoria

Halley necesita además un párrafo histórico: Edmond Halley, astrónomo inglés, publicó el método a finales del siglo XVII. Chebyshev lleva el nombre de Pafnuty Chebyshev, matemático ruso del siglo XIX. La plantilla baja de nota si no hay al menos una fórmula correcta distinta de la de Newton, así que conviene revisar las dos antes de entregar.
