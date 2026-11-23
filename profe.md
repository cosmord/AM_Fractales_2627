# Avaliación do Traballo de Análise Matemática 2026/2027 — rama `vibedv2`

**Función do grupo:** `f(z) = z³ − 2z + 2`  ·  **Expediente evaluado:** `memoria/memoria.pdf` (7 páx.), `presentacion/presentacion.pptx` (8 diap.), `presentacion/html/index.html` (10 diap.), `Newton.py`, `Halley.py`, `Chebyshev.py`, `imaxes/fractal_*.png`, `entrega_AM.zip` (9 entradas).

> Esta é unha avaliación **nova**, non unha copia da de `docs/archived_sessions/2026-11-23_v1/profe_v1.md`. Aquela correspondía a outra función (`f(z)=z/√(z²+z)`) e só se usa aquí como comparación histórica, nunca como fonte de conclusions sobre este traballo.

---

## 1. Perfil del evaluador y tono

Profesor titular de **Análise Matemática**, gallego, 58 años. Imparto esta materia en Enxeñaría Informática desde hace veinte años y he corregido suficientes traballos como para desconfiar de todo lo que brilla. Tono: seco, preciso, ligeramente irónico, exigente pero justo. No penalizo la forma por ser forma —pero tampoco la confundo con el fondo—. Valoro que la deducción esté bien hecha y que el alumno sepa defender lo que entrega; desconfío de los datos que se repiten sin haberse vuelto a mirar. Escribo en español y conservo los términos gallegos del enunciado cuando cito la plantilla.

**Método de verificación seguido (nada de suposiciones):** extracción de texto de los dos PDF con `pypdf`; lectura del PPTX y sus notas con `python-pptx`; lectura del HTML; reimplementación independiente —vectorizada y escalar— del bucle de los tres scripts sobre la malla `601×601`, con la guarda `abs(g(z)) < 1/tol` y `maxiter=30`; álgebra simbólica con SymPy para `g`, raíces y polos; inspección de los PNG con Pillow y de sus imágenes; `zipfile.testzip()` sobre el ZIP. Los números que doy por buenos salen de ahí, no de la memoria.

**Advertencia administrativa previa:** la portada de la memoria (pág. 1), la diapositiva 1, `README_entrega.md` (líneas 3–4) y el ZIP siguen con `GRUPO:` y `Alumno que realiza a presentación:` en blanco. Es un defecto formal de entrega: antes de levantar acta hay que subsanarlo. **No altera la nota de la plantilla, pero sí la condiciona.** No invento nombres.

---

## 2. Plantilla oficial (Figura 2) con evidencia y puntuación

Cada bloque pondera 40 / 30 / 30 % y reparte 10 puntos por criterio: **cada criterio equivale exactamente al 10 % de la nota final**.

| Bloque | Criterio | Evidencia encontrada (real, verificada) | Puntos | Peso |
|---|---|---|---|---|
| **EXPOSICIÓN 40 %** | **Duración** (5–8 = 1; 4–5 u 8–9 = 0,5; <4 o >9 = 0) | Las notas del relator suman **7,0 min** en las diapositivas 2–8 (0,5+1,5+1+1+1,5+1+0,5) y la apertura añade ~0,3–0,5: plan ≈**7,3–7,5 min**, dentro del intervalo. Ya no hay la contradicción de la v1. Pero la ejecución real no es observable en el expediente; mantengo el criterio que apliqué entonces: **0,5 por prudencia, no por defecto del plan**. | 0,5 | 5 % |
| | **Estrutura** | 8 diapositivas: título → obxectivos → Newton → Halley → Chebyshev → tres fractais → resultados → conclusións. Todos los temas exigidos, en orden lógico, con notas enlazadas una a una y bibliografía en la última. | 1 | 10 % |
| | **Estilo** (voz alta, mirada, notas resumidas sin leer, animada y amena) | Solo verificable un carácter: las notas son realmente resumidas («Debuxar a tanxente no aire», «Pechar cunha pregunta»), no guiones literales. Voz, mirada y animación no constan en el expediente. El HTML tiene fragmentos animados, pero eso es material, no estilo del relator. | 0,5 | 5 % |
| | **Material** | Transparencias sobrias, fórmulas en recuadros, diapositiva 6 con las tres imágenes **y tabla rotulada** (Newton/Halley/Chebyshev con orden y media), vínculo estrecho con las notas. Pegas: imágenes a 3,7″ de ancho (algo pequeñas) y portada sin identificar. | 1 | 10 % |
| **MEMORIA 30 %** | **Presentación** (organizada, coherente, sin faltas de ortografía) | 7 páginas, 9 secciones, 2 tablas y 3 figuras, orden impecable. **No encuentro las faltas de la v1**: ahora dice «Nos dous puntos…» y «reflexa». Mácula tipográfica real: en pág. 3 el PDF muestra `z■ − 1` —el carácter `zⁿ` del spec no existe en Helvetica y se sustituye por un cuadro—, y las fórmulas siguen en notación plana `x_{n+1}`. Esto no es una falta de ortografía, pero conviene corregirlo. | 1 | 10 % |
| | **Corrección** | Casi todo verificado correcto (ver §3). Pero una afirmación **falsa y repetida en §5, §7 y §8**: «Nas tres, os polos están nos ceros de 3z²−2» y «Nos dous puntos onde f′ se anula, g non está definida». SymPy da `g_H(√(2/3)) = √6/3`, finito: el denominador `2f′²−ff″` no se anula donde `f′=0`. Halley **no tiene** esos polos; Newton y Chebyshev sí. Es «algún erro», no «a maioría errónea». | 0,5 | 5 % |
| | **Completitude** | Cubre todo lo pedido: deducción de Newton, historia y fórmula de Halley, fórmula de Chebyshev, interpretación xeométrica de los tres —ahora con parábola osculatriz y cónica/hipérbola osculatriz—, función propia, metodología, tres fractales, resultados numéricos, conclusiones y las cuatro referencias. | 1 | 10 % |
| **FRACTAIS 30 %** | **Corrección** | Verificado con SymPy: `g_N = 2(z³−1)/(3z²−2)`, `g_H = (3z⁵+2z³−12z²+4)/(2(3z⁴−3z²−3z+2))`, `g_C` racional de grado 7. Coinciden con memoria, scripts y diapositiva 6. Raíces `-1,7692924` y `0,88464618 ± 0,5897428i`; `gcd(f,f′)=1`, así que las tres son simples. | 1 | 10 % |
| | **Estética** | Las tres imágenes muestran estructura fractal clara (inspección visual de los tres PNG), son originales —función propia— y usan bien la paleta turbo. Frente a la v1, la de Halley ya no es una manzana roja con costura. Limitación pedagógica: el color codifica **nº de iteraciones**, no la conca; no se ve a qué raíz converge cada punto. La plantilla no exige lo contrario. | 1 | 10 % |
| | **Calidade** | PNG de 1632×1314, 1953×1591 y 1953×1591 px a 300 dpi, sobre malla 601×601 (el doble que en v1). Sin pixelado grave; aliasing leve en los filamentos más finos. «Gran nitidez e calidade» es aquí una afirmación defendible. Detalle menor: la imagen de Newton es más pequeña porque su script no fija `figsize`. | 1 | 10 % |
| | | **TOTAL** | **8,5 / 10** | **85 %** |

**Desglose:** EXPOSICIÓN 30,0/40 · MEMORIA 25,0/30 · FRACTALES 30,0/30 → **85,0 % = 8,5 sobre 10**.

---

## 3. Comparación con la sesión archivada v1 (función distinta)

La v1 se evaluó con `7,0/10`. No traslado sus conclusiones matemáticas, pero sí su lista E1–E11 como checking de honestidad intelectual:

| Id (v1) | Estado en `vibedv2` | Evidencia concreta |
|---|---|---|
| E1 — «raíz simple» en `z=0`, punto de ramificación | **Resuelto por cambio de función y de razonamiento.** | Ahora es polinomio; memoria pág. 2: «as tres raíces son simples, porque f′ non se anula ningunha delas». Verificado: `gcd(f,f′)=1` y `f′(c)≠0` en las tres raíces. |
| E2 — «polo» en `z=−1` | **No aplicable / resuelto.** | Memoria pág. 3: «Ao ser un polinomio, a función non ten cortes de rama». No hay singularidades algebraicas. |
| E3 — frase ambigua sobre `f″≈0` en Halley | **Resuelto textualmente.** | Pág. 2: «Non se anula o salto, senón a corrección debida a f″». Ahora es correcto. |
| E4 — órdenes 2/3/3 sin comprobar hipótesis | **Resuelto.** | Columna «Orde xenérica» en la tabla y «preto de cada raíz… os multiplicadores g′(c) son 0». La hipótesis de raíz simple sí se cumple aquí. |
| E5 — lentitud de Halley mal explicada | **Resuelto.** | Explicación cuantitativa: 99,69 % en <10 pasos, media 3,98, frente a Newton 7,02. Reproducido por mí cifra a cifra. |
| E6 — 601 celdas fantasma (fila 0 y columna 300) | **Resuelto.** | Los tres bucles van `range(0, npuntos+1)` y escriben `fractal[npuntos−j, i]`; quedan cubiertas las 601×601 celdas. Recomputado: 7,0229 / 3,9803 / 5,2751 de media. |
| E7 — grupo y relator en blanco | **Sigue abierto.** | Portada pág. 1, diapositiva 1, `README_entrega.md` y ZIP. Sin datos reales; no se inventan. |
| E8 — interpretación xeométrica insuficiente | **Resuelto.** | Memoria pág. 3: «intersección do eixo OX coa parábola osculatriz… mentres Halley usa a cónica osculatriz»; también en el slide 5 del HTML. |
| E9 — duración planeada ≈9,5 min | **Resuelto.** | Notas ahora ≈7,0 min + apertura; dentro de 5–8. Queda la prudencia de no haber visto la ejecución. |
| E10 — imagen de Halley débil y contornos escalonados | **Mejorado.** | Malla 300×300 → 600×600; las tres imágenes tienen estructura fractal visible (7.616 / 22.542 / 35.636 colores distintos). Sigue sin colorearse por conca. |
| E11 — «nese puntos», «reflexo», notación plana | **Resuelto en lo esencial.** | Ya no aparecen esas dos formas. Queda el cuadro `z■` y el estilo `x_{n+1}` sin tipografiar. |

**Hallazgos nuevos de esta revisión (no estaban en v1):**

| Id | Hallazgo | Consecuencia |
|---|---|---|
| N1 | «Nas tres, os polos están nos ceros de 3z²−2» es falso para Halley: `g_H(√(2/3)) = √6/3`, finito. Repetido en §5, §7 y §8. | baja **Corrección** a 0,5. |
| N2 | `zⁿ` se renderiza como `z■` en la memoria PDF (fuente Helvetica, sin glifo U+207F). | mácula tipográfica; no baja la nota. |
| N3 | La guarda no se cuantifica: en Chebyshev corta en **11 celdas** (dos de ellas con `n=0`, junto a `z≈−0,8165`); en Newton y Halley, en 0. La memoria habla de «os dous puntos» como si fuesen celdas muestreadas. | laguna, no penalizada por la plantilla. |
| N4 | La convergencia se mide solo con `|f(z)|<1e-6`, nunca con `|z_n−c|`, y no se registra a qué raíz se converge. | laguna metodológica. |
| N5 | El HTML de 10 diapositivas no está dentro del ZIP (9 entradas: memoria, pptx, 3 scripts, 3 PNG, README). | laguna menor de paquete. |

**Lo que sí está bien y conviene decirlo:** las tres fórmulas son correctas y verificadas; la deducción de Newton es impecable; el dato histórico de Halley (1656–1742, Householder, Padé (1,1)) es exacto; la bibliografía es la del enunciado; los scripts son reproducibles y los números de la tabla se recomputan; y la idea final —«a orde teórica non determina por si soa o aspecto do fractal»— es una observación inteligente, ahora mejor documentada.

---

## 4. Preguntas de defensa oral (8) y respuesta que espero

1. **«En la página 3 escribís: “Nas tres, os polos están nos ceros de 3z²−2”. Calculad `g_H(√(2/3))`.»**
   *Esperado:* da `√6/3 ≈ 0,8165`, es decir, el propio punto: **no hay polo**. El denominador de Halley es `2f′² − f·f″`, que en `f′=0` vale `−f·f″ ≠ 0`. Quien dice «nas tres» está aplicando a Halley la forma de Newton. Solo `g_N` y `g_C` tienen polos ahí (de orden 1 y 3). Corregir las tres frases de §5, §7 y §8.

2. **«¿Cómo sabéis que las tres raíces son simples sin mirarlas una a una?»**
   *Esperado:* `gcd(f,f′)=1`, o equivalentemente los ceros de `f′=3z²−2` (`±0,816497`) no anulan `f` (`f(0,8165)≈0,911`; `f(−0,8165)≈3,089`). Entonces `g′(c)=0` en las tres raíces y las órdenes 2, 3, 3 son legítimas **cerca de cada raíz**. Es la hipótesis que la v1 no comprobaba; aquí sí.

3. **«Medís la convergencia con `|f(z)|<1e-6`, no con `|z_n−c|`. ¿Puede un punto darse por convergido estando lejos de una raíz?»**
   *Esperado:* cerca de una raíz simple `|f(z)|≈|f′(c)||z−c|`, así que sirve como proxy; pero cerca de un crítico `f′≈0` el criterio es engañoso, y la guarda `|g|<1/tol` también corta la iteración y se contabiliza como `n`. Lo correcto es registrar además `|z_n−c|` y la raíz de destino.

4. **«Halley tiene orden 3 y media 3,98. ¿Es por eso “más barato” que Newton?»**
   *Esperado:* más barato **en número de iteraciones**, no necesariamente en tiempo: cada paso exige `f″` y una expresión racional de grado 5. La tabla compara iteraciones, no flops. Una respuesta honesta debe separar ambas cosas en lugar de decir «Halley é o máis rápido» sin calificativo.

5. **«¿Por qué el color es el número de iteraciones y no la conca de atracción, como en la Figura 1 del enunciado?»**
   *Esperado:* es la opción heredada del `Newton.py` de FAITIC; es legítima y la memoria la explica («Cada cor representa cantos pasos tarda en converxer»), pero impide responder a la pregunta central del tema —qué raíz atrae cada punto inicial—. Una codificación por conca con sombreado por `n` sería más informativa. Debe saber defender la elección y reconocer la pérdida.

6. **«¿Cuántas celdas dispara la guarda `abs(g(z))<1/tol` y en qué método? ¿Por qué?»**
   *Esperado:* 0 en Newton, 0 en Halley y **11 en Chebyshev** (dos con `n=0`, pegadas a `z≈−0,8165`): `f′=0` no está exactamente en la malla, y la singularidad de Chebyshev es de orden 3, mucho más agresiva que la de Newton. Es la consecuencia directa de la pregunta 1 y la respuesta a la frase «nos dous puntos onde f′ se anula, g non está definida».

7. **«¿Qué cambia si subís `maxiter` de 30 a 60 o ampliáis la ventana a [−3,3]×[−3,3]?»**
   *Esperado:* cambian la media y el 1,11 % de `maxiter` de Newton (subiría el tiempo y bajaría ese porcentaje); la ventana actual contiene justo las tres raíces y los dos ceros de `f′`. Al ampliar aparece más frontera, **no nuevas raíces** —el polinomio solo tiene tres— y se mantiene la simetría conjugada respecto al eje real, pero no hay simetría rotacional. Debe distinguir «más detalle» de «más raíces».

8. **«Decís “Chebyshev é polinómico; Halley é racional”. ¿Eso es la interpretación xeométrica que pide el enunciado?»**
   *Esperado:* no: es una descripción algebraica. La interpretación es la **intersección con el eje OX de la parábola osculatriz** en `(x_n, f(x_n))` para Chebyshev y de la **cónica/hipérbola osculatriz** (o Padé (1,1) de la inversa) para Halley. La memoria ya lo dice en pág. 3; el alumno debe poder repetirlo sin leer y explicar por qué ambas dan orden 3.

---

## 5. Lagunas restantes

- **E7 abierta:** identificación de grupo y relator en blanco en memoria, portada, diapositiva 1, `README_entrega.md` y ZIP. Bloqueo administrativo antes del acta.
- **N1:** concepto erróneo sobre los polos de `g_H`, repetido en tres secciones de la memoria.
- **N3/N4:** guarda no cuantificada; convergencia medida solo con `|f(z)|`, sin seguimiento de la raíz de destino ni de `|z_n−c|`.
- **Estilo y duración:** no verificables sin ver al relator; el plan encaja, pero la ejecución queda sin calificar en dos criterios.
- **N2 y detalle de imagen:** glifo `z■` en memoria pág. 3; `Newton.py` no fija `figsize`, por lo que su PNG es más pequeño que los otros dos.
- **N5:** el HTML de 10 diapositivas queda fuera del ZIP; si se usa en clase, conviene incluirlo o indicarlo explícitamente en `README_entrega.md`.
- Las tres imágenes se colorean por iteración, no por conca: estructura fractal sí, lectura de cuencas no.

---

## 6. Nota final y justificación

**Nota: 8,5 / 10 (85 %).**

Se aprueba con nota alta, sin matrícula. La parte **FRACTALES** está ahora redonda: corrección 10, estética 10, calidad 10; la malla se duplicó respecto a la v1 y la imagen de Halley dejó de ser el punto débil. La **MEMORIA** es completa, ordenada y ya no comete los tres errores conceptuales de la v1, pero sí incurre en uno nuevo y repetido —los polos de Halley—, que baja Corrección a 5. La **EXPOSICIÓN** no puede calificarse del todo sin ver al alumno: estructura y material merecen 10; estilo y duración quedan en 5 por falta de evidencia y por prudencia, aunque esta vez el plan de tiempos sí está bien ajustado.

No le quito puntos por la forma —la forma aquí es buena y incluso mejora clara respecto a la entrega archivada—. Se los quito por una frase que se copió en tres sitios sin volver a calcularla. **8,5 honrados**, condicionados a que se rellene la portada antes de levantar acta.

---

## 7. Tres mejoras concretas

1. **Corregir el análisis de los polos antes de hablar de convergencia.** Sustituir «nas tres, os polos están nos ceros de 3z²−2» y «g non está definida» por: `g_N` y `g_C` tienen polos en `±√(2/3)` (órdenes 1 y 3), mientras `g_H` es analítica ahí con `g_H(±√(2/3))=±√(2/3)` porque `2f′²−ff″ = −ff″ ≠ 0`. Añadir una línea explicando que esa es precisamente la ventaja algebraica de Halley, y cuantificar la guarda: 11 celdas en Chebyshev, 0 en los otros dos.
2. **Hacer la estadística auditable y las imágenes más informativas.** Registrar `|z_n−c|` y la raíz de destino además de `|f(z)|`; colorear por conca con sombreado por `n` (así se ve lo que el enunciado pregunta) o, si se mantiene turbo, decir explícitamente que el color no identifica la raíz. Unificar `figsize=(9,6)` en los tres scripts y sustituir `zⁿ` por `z^n`/`z³` en el spec para eliminar el cuadro de la pág. 3.
3. **Cerrar el paquete y ensayar la defensa.** Rellenar grupo y relator en `memoria_spec.json` → reconstruir PDF → `README_entrega.md` → ZIP; incluir el HTML de 10 diapositivas en el ZIP o referenciarlo. Ensayar en voz alta los ~7,5 min previstos y, sobre todo, preparar la pregunta 1: `g_H(√(2/3)) = √6/3`. Esa es la primera que haré.

---

## 8. Veredicto (en carácter)

> Vaia, pois. La primera vez me entregaron una fórmula preciosa que no había sido mirada por dentro; esta vez me encuentro con un polinomio honesto, tres scripts que se pueden ejecutar, unas cuentas que he reproducido una por una y una memoria que ha corregido casi todo lo que le señalé. Incluso el plan de tiempos, que antes se pasaba de largo, ahora encaja. Eso se nota y se agradece.
>
> Pero sigo sin poder dar el diez. Hay una frase —«nas tres, os polos están nos ceros de 3z²−2»— que aparece en la página 3, en la 4 y otra vez en las conclusiones, y que es falsa para Halley. Halley no divide por `f′` a secas: por eso su mapa es finito justo donde Newton y Chebyshev se disparan. Es exactamente el tipo de detalle que separa «aplicar un método» de «entender Análise Matemática». Y me siguen sin decir quién presenta el trabajo, así que esta acta queda en el cajón hasta que rellenen la portada.
>
> Dicho esto: hay fondo, hay deducción, hay números verificables y una idea final sensata sobre la orden teórica. Por eso **oito sobre dez e medio**, non sete. Y en cuanto escriban su nombre en el sitio que está en blanco, la primera pregunta será `g_H(√(2/3))`. Si la contestan sin mirar las notas, todavía me atrevo a subirles la nota.

---

## 9. Anexo: identificación y transcripción de la imagen de la rúbrica

**Identificación.** En la sesión archivada se evaluó una imagen (`348F3E6C-6331-4D1E-975C-F742DBD3EAD8_113eea.png`, 1582×880 px, RGBA) que era un escaneo en blanco y negro de la **plantilla de valoración**, en galego, con el título centrado «Traballo de Análise Matemática»: ni un fractal ni una captura de código. **Ese fichero ya no está en el árbol de `vibedv2`** (verificado: no aparece ninguna imagen de rúbrica fuera de `imaxes/`). Por tanto no finjo haberla re-inspeccionado: la transcripción de abajo procede de las dos fuentes que sí están y he verificado:

- **`docs/rubrica.md`** — transcripción canónica en texto (27 líneas), a la que remito para cualquier cotejo.
- **`docs/Traballo_AM.pdf`, pág. 4, Figura 2** — la plantilla original tal como se entrega con el enunciado; extraída y comparada, coincide con el markdown.

Los campos superiores están en blanco: `GRUPO:`, cinco líneas numeradas 1.–5., `Alumno que realiza a presentación:` y `NOTA FINAL:`. No hay nombres ni calificación escrita. No aparece ninguna fórmula en la grella; la única referencia matemática explícita es «Método de Newton». Columnas: **1 punto / 0,5 puntos / 0 puntos** (coma decimal galega). Los tres bloques suman 4+3+3 = 10 puntos.

### Transcripción de la grella (según `docs/rubrica.md`)

**EXPOSICIÓN (40 %)**

| Criterio | 1 punto | 0,5 puntos | 0 puntos |
|---|---|---|---|
| Duración | Entre 5 e 8 minutos. | Entre 4-5 ou 8-9 minutos. | Menos de 4 minutos ou máis de 9 minutos. |
| Estrutura | Presentación ben estruturada: trátanse tódolos temas requiridos con claridade. | Presentación pouco estruturada: falta algún dos temas requiridos ou non se explican con claridade. | Presentación mal estruturada. |
| Estilo | Fala alto, mira a audiencia, desenvolve as ideas a partir de notas resumidas (non lee nin recita de memoria), a presentación é animada e amena. | A presentación ten polo menos dúas características mencionadas anteriormente. | A presentación ten menos de dúas características mencionadas anteriormente. |
| Material | Utiliza o material de maneira pedagóxica: tamaño de letra adecuado, transparencias con pouca letra, vínculo estreito entre transparencias e explicacións orais. | Utiliza o material de maneira pouco pedagóxica. | Non utiliza material de apoio. |

**MEMORIA ESCRITA (30 %)**

| Criterio | 1 punto | 0,5 puntos | 0 puntos |
|---|---|---|---|
| Presentación | A memoria está ben organizada, é coherente e non presenta faltas de ortografía. | Falla algunha das características mencionadas anteriormente. | Fallan polo menos dúas características mencionadas anteriormente. |
| Corrección | Os temas tratados son correctos e a información incluída é relevante. | A memoria contén algún erro ou información pouco relevante. | A maioria da memoria é errónea ou irrelevante. |
| Completitude | A memoria inclúe toda a información requirida. | A memoria non inclúe algunha da información requirida. | A memoria non inclúe a maioría da información requirida. |

**FRACTAIS (30 %)**

| Criterio | 1 punto | 0,5 puntos | 0 puntos |
|---|---|---|---|
| Corrección | As fórmulas usadas nos 3 métodos son correctas. | Hai polo menos 1 fórmula correcta distinta da do exemplo (Método de Newton). | Ningunha fórmula distinta da do exemplo (Método de Newton) é correcta. |
| Estética | En todas as imaxes obtidas apréciase a estrutura fractal, son orixinais e atractivas estéticamente. | Nas imaxes obtidas apréciase a estrutura fractal pero non presentan orixinalidade ou atractivo estético. | Nas imaxes obtidas non se aprecia estrutura fractal. |
| Calidade | As imaxes obtidas presentan gran nitidez e calidade. | As imaxes obtidas presentan nitidez e calidade media. | As imaxes obtidas están pixeladas ou son de baixa calidade. |

**Notas de lectura:** la plantilla usa «tódolos temas» y «Completitude» (en galego normativo, «todos os temas» y «completude»); la coma decimal es correcta. Onde el escaneo antiguo dejaba dudas entre «Falla»/«Fallan» y «desenvólve»/«desenvolve», `docs/rubrica.md` fija la forma que coincide con el PDF. Esta es la grella que se aplica literalmente en el §2: **nueve criterios de un punto, luego cada fila vale exactamente el 10 % de la nota final**.

---

## 10. Actualización posterior al informe

Después de cerrar esta evaluación se corrigieron tres detalles señalados aquí:

- **N1:** la memoria ya no atribuye polos de `g_H` a `z = ±√(2/3)`; se indica que el factor cancela en Halley y que solo Newton y Chebyshev tienen polos ahí.
- **N2:** `zⁿ` se sustituyó por `z^n` en el spec de la memoria, de modo que el PDF ya no muestra el glifo ausente.
- **Figura:** `Newton.py` fija ahora `figsize=(9, 6)`, igual que los otros dos scripts.

La nota de **8,5 / 10** corresponde al estado evaluado, anterior a estos ajustes. Queda pendiente, como se indicó, la identificación del grupo y del relator.
