# Cómo ejecutar todo

Todo se hace desde la raíz del repositorio, en la rama `vibedv2`.

## 1. Entorno (una sola vez)

```bash
python -m venv .venv
source .venv/Scripts/activate        # Windows (Git Bash)
pip install numpy sympy matplotlib reportlab python-pptx pypdf Pillow
```

## 2. Generar los tres fractales

```bash
python Newton.py
python Halley.py
python Chebyshev.py
```

Cada script imprime `f`, `f'`, `f''` y `g(z)`, y escribe su imagen en `imaxes/`.
Parámetros reales: `f(z)=z³-2z+2`, ventana `[-2,2]×[-2,2]`, 600 puntos por eje,
30 iteraciones y tolerancia `1e-6`. La guarda `abs(g(z)) < 1/tol` corta los polos en
`z = ±0,816497`.

## 3. Reconstruir memoria, presentación y ZIP

```bash
python scripts/rebuild_artifacts.py
```

Ese script ejecuta los tres programas, reconstruye `memoria/memoria.pdf` desde
`memoria/memoria_spec.json`, `presentacion/presentacion.pptx` desde
`presentacion/deck_spec.json` y `entrega_AM.zip`, y comprueba el ZIP con `testzip`.

Resultados esperados (verificados con una implementación vectorizada independiente):

| Método | Media | Mediana | % ≥ 30 iter. | % < 10 iter. |
|---|---|---|---|---|
| Newton | 7,02 | 6 | 1,11 % | 86,45 % |
| Halley | 3,98 | 4 | 0,02 % | 99,69 % |
| Chebyshev | 5,28 | 4 | 0,03 % | 93,04 % |

## 4. Presentación HTML para clase

Abrir `presentacion/html/index.html` con doble clic, o servir la carpeta:

```bash
cd presentacion/html
python -m http.server 8000
```

Luego visitar `http://localhost:8000`. No requiere instalación: es un único HTML con
CSS y JavaScript embebidos. Solo la fuente Cascadia Code se descarga de un CDN; sin
conexión se usa Consolas u otra monoespaciada.

Controles: `→`/Espazo avanza (paso a paso por fragmentos), `←` retrocede, `F` pantalla
completa, `P` partículas, `H` axuda.

## 5. Antes de entregar en MOOVI

Rellenar grupo e relator en `memoria/memoria.pdf` (editando `memoria/memoria_spec.json`
y reconstruyendo) y en `README_entrega.md`, volver a generar el ZIP y subir solo
`entrega_AM.zip`.
