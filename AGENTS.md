# AGENTS.md

Reglas para trabajar en este repositorio. Se aplican a cualquier persona o agente que edite archivos aquí.

## Fuentes de verdad

| Archivo | Autoridad |
|---|---|
| [`docs/Traballo_AM.pdf`](docs/Traballo_AM.pdf) | Enunciado oficial. Define entregables, plazos y rúbrica. No se edita. |
| [`Newton.py`](Newton.py) | Código base de FAITIC. No se edita salvo en los campos permitidos. |
| [`README.md`](README.md) y [`docs/*.md`](docs/) | Documentación de apoyo. Si contradicen al PDF, manda el PDF. |

No inventar datos para la memoria: fechas, nombres del grupo, notas ni resultados que no salgan del enunciado o de una ejecución real del código.

## Archivos editables

| Editable | No editable |
|---|---|
| `README.md`, `AGENTS.md`, `docs/*.md` | `docs/Traballo_AM.pdf` |
| `Halley.py`, `Chebyshev.py` (crear desde copia) | Bloque "NON MODIFICAR" de `Newton.py` |
| `fractal_*.png`, memoria, presentación | Firma del bucle de `Newton.py` (los rangos `range(0,npuntos+1)` se ampliaron expresamente para cubrir toda la malla) |
| En `Newton.py`: `f`, `maxiter`, `a`, `b`, `c`, `d`, `npuntos`, `cmap`, `dpi` | `tol` y la guarda `abs(gg(z)) < 1/tol` |

## Flujo de trabajo

1. Leer [docs/analisis-trabajo.md](docs/analisis-trabajo.md) antes de empezar y [docs/tutorial-primer-fractal.md](docs/tutorial-primer-fractal.md) si es la primera vez.
2. Mantener `f(z)` distinta a la de los otros grupos. Si se cambia, revisar la ventana de dibujo.
3. Para un método nuevo, copiar `Newton.py`; nunca meter Halley o Chebyshev dentro del archivo base.
4. Cambiar siempre el texto impreso y el nombre del PNG para que cada archivo diga qué método contiene.
5. Ejecutar el script y mirar la imagen antes de darla por buena. No basta con que corra sin errores.
6. Actualizar `README.md` y los documentos de `docs/` si aparece un archivo nuevo.
7. No hacer commit ni push salvo petición explícita.

## Convenciones

- Comentarios heredados de `Newton.py`: en gallego, tal cual.
- Documentación nueva: en español, con los términos del enunciado en gallego cuando se citen.
- Fórmulas: sacarlas del enunciado o de una fuente verificable y mostrarlas en la memoria tal como se implementaron.
- Nombres de imagen: `fractal_Newton.png`, `fractal_Halley.png`, `fractal_Chebyshev.png`.

## Checklist antes de subir a MOOVI

- [ ] `f(z)` es propia del grupo y está documentada en la memoria.
- [ ] Los tres scripts imprimen el método correcto.
- [ ] Los tres PNG existen, se abrieron y muestran estructura fractal.
- [ ] La memoria incluye deducción de Newton, historia de Halley, fórmulas de los tres e interpretación geométrica.
- [ ] La bibliografía está en la memoria con las referencias del enunciado.
- [ ] La duración de la exposición está entre 5 y 8 minutos.
- [ ] Todo está dentro de un único ZIP.
