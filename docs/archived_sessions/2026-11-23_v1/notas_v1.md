# Sesión v1 (archivada)

Evaluación del profesor y entrega que la originó. Se conserva para comparar con la iteración v2.

## Errores detectados por el profesor (E1–E11)

| Id | Error |
|---|---|
| E1 | `z=0` descrito como «raíz simple»; es punto de ramificación (`f∼√z`, `f′→∞`). |
| E2 | `z=−1` descrito como «polo»; es singularidad de ramificación `(z+1)^(−1/2)` y punto fijo espurio. |
| E3 | Frase ambigua sobre `f″≈0` en Halley: se anula el término adicional, no el salto `f/f′`. |
| E4 | Órdenes 2/3/3 presentadas como propiedades de esta `f` sin verificar la hipótesis de raíz simple. |
| E5 | Lentitud de Halley atribuida al polo de `f`; la causa principal es el multiplicador `g′_H(0)=−1/3`. |
| E6 | 601 celdas fantasma: el bucle no escribía fila 0 ni columna `npuntos`. |
| E7 | Grupo y relator en blanco en memoria, portada, README y ZIP. |
| E8 | Interpretación geométrica de Halley y Chebyshev insuficiente (falta cónica osculatriz). |
| E9 | Notas de la presentación sumaban ~9,5 min, por encima del máximo de 8. |
| E10 | Imagen de Halley débil y contornos escalonados por malla de 300×300. |
| E11 | «nese puntos», «reflexo» y notación plana en la memoria. |

## Nota de la v1

7,0 / 10 (exposición 30/40, memoria 20/30, fractales 20/30).

## Estado

E1–E6, E8–E11 se corrigen en la rama `vibed` durante la iteración v2. E7 queda pendiente de datos reales del grupo; no se inventan nombres.
