# Avaliación do Traballo de Análise Matemática 2026/2027

*(Evaluación redactada para o expediente: profesor titular de Análise Matemática, Universidade de Vigo, ESEI Ourense)*

## 1. Perfil del evaluador y tono

Profesor titular de **Análise Matemática**, gallego, 58 años. Imparto esta materia en Enxeñaría Informática desde hace veinte años y he corregido suficientes traballos como para desconfiar de todo lo que brilla. Tono: seco, preciso, ligeramente irónico, exigente pero justo. No penalizo la forma por ser forma —pero tampoco la confundo con el fondo—. Valoro especialmente que la deducción esté bien hecha y que el alumno sepa defender lo que entrega: aquí es donde este trabajo flaquea. Detesto la decoración sin sustancia y los datos que se repiten sin haberse vuelto a mirar. Escribo en español, conservando los términos gallegos del enunciado cuando cito la plantilla.

**Advertencia previa:** el ZIP (`entrega_AM.zip`) y la portada de la memoria dejan en blanco los campos «GRUPO:» y «Alumno que realiza a presentación:», y la diapositiva 1 tampoco identifica al grupo. Es un defecto formal de entrega: antes de levantar acta hay que subsanarlo. No altera la nota de la plantilla, pero sí la condiciona administrativamente.

---

## 2. Plantilla de valoración (rubrica oficial, plantilla de la Figura 2)

Cada bloque pondera 40 / 30 / 30 % y reparte 10 puntos por criterio, de modo que **cada criterio equivale exactamente al 10 % de la nota final**.

| Bloque | Criterio | Evidencia encontrada (real, verificada) | Puntos | Ponderación |
|---|---|---|---|---|
| **EXPOSICIÓN 40 %** | **Duración** (5–8 min = 1; 4–5 u 8–9 = 0,5; <4 o >9 = 0) | No es observable en el material entregado. Las notas del relator suman **≈9,5 min** (1 + 2 + 1,5 + 1 + 2 + 1 = 8,5 min de las diapositivas 2–7, más apertura y cierre ≈0,5 + 0,5), aunque la diapositiva 1 dice «Duración total obxectivo: de 5 a 8 minutos». Contradicción interna: si se siguen las notas al pie de la letra se supera el umbral de 9 min. Se concede 0,5 por no poder comprobar la ejecución real. | 0,5 | 5,0 % |
| | **Estrutura** | 8 diapositivas: título → obxectivos → Newton → Halley → Chebyshev → tres fractais → resultados → conclusións. Todos los temas exigidos aparecen y en orden lógico; notas de relator enlazadas diapositiva a diapositiva. | 1 | 10,0 % |
| | **Estilo** (habla alta, mira a audiencia, notas resumidas sin leer, animada y amena) | Solo es verificable un carácter: las notas son efectivamente resumidas («Debuxar a tanxente no aire», «Pechar cunha pregunta») y no guiones literales. Los demás (voz, mirada, animación) no constan en el expediente. | 0,5 | 5,0 % |
| | **Material** | Transparencias sobrias, fórmulas en recuadros, diapositiva 6 con las tres imágenes **rotuladas mediante tabla** (Newton / Halley / Chebyshev con su `g(z)`), vínculo estrecho con las notas. Pega: imágenes de 3,7″ de ancho, algo pequeñas, y portada sin identificación. | 1 | 10,0 % |
| **MEMORIA 30 %** | **Presentación** (organizada, coherente, sin faltas de ortografía) | 6 páginas, 9 secciones, dos tablas y tres figuras, orden impecable. Pero hay errores de forma: «se anula **nese** puntos» (debe ser «neses puntos», pág. 3) y «A distribución de cores **reflexo** dunha convergencia…» (calco de «reflejo», pág. 4). La plantilla exige «non presenta faltas de ortografía». | 0,5 | 5,0 % |
| | **Corrección** | Fallos conceptuales de calado (ver §4): «raíz simple» en z=0 cuando `lim f′(z) = +∞`; «polo» en z=−1 cuando el comportamiento es `(z+1)^(−1/2)`; «expresión ambigua»: al escribir «cando f″ é case nula, a corrección é case nula e Halley case coincide con Newton» se identifica mal qué término se anula (es el **término adicional** en `f″`, no el salto `f/f′`; el salto sigue siendo el de Newton). Frase a reescribir con precisión. Y la columna «Orde 2/3/3» se presenta como si fuera la de esta función. El resto —fórmulas, derivadas, metodología— es correcto y reproducible. | 0,5 | 5,0 % |
| | **Completitude** | Cubre todo lo pedido: deducción de Newton, historia y fórmula de Halley, fórmula de Chebyshev, interpretación geométrica de los tres, función propia, metodología, tres fractales, resultados numéricos, conclusiones y las cuatro referencias de la bibliografía. Las interpretaciones de Halley y Chebyshev son más algebraicas que geométricas, pero están presentes. | 1 | 10,0 % |
| **FRACTALES 30 %** | **Corrección** | Verificado ejecutando el código con SymPy 1.14: `g_Newton = z(−2z−1)`, `g_Halley = −z/(4z+3)`, `g_Chebyshev = z²(4z+3)`. Las tres son correctas y coinciden con lo escrito en memoria, scripts y diapositiva 6. | 1 | 10,0 % |
| | **Estética** | La imagen de Halley (inspeccionada) muestra anillos concéntricos y una costura vertical marcada en x≈−0,43, con la paleta turbo casi toda en rojo/naranja (≈788 colores discretos): estructura fractal **débil**, poco atractivo. Newton y Chebyshev presentan mejor contraste (15.819 y 797 colores distintos, dominio azul/rojo). No se cumple «en todas as imaxes… son orixinais e atractivas». | 0,5 | 5,0 % |
| | **Calidade** | PNG de 1713×1210, 2241×1488 y 2241×1472 px a 300 dpi: formalmente alta resolución de guardado, pero la malla de iteración es de solo 300×300, así que los contornos están escalonados y sin antialiasing (la inspección visual confirma pixelado, no desenfoque). «Gran nitidez» sería generoso; corresponde a «nitidez e calidade media». | 0,5 | 5,0 % |
| | | **TOTAL** | **7,0 / 10** | **70,0 %** |

**Desglose:** EXPOSICIÓN 30,0/40 · MEMORIA 20,0/30 · FRACTALES 20,0/30 → **70,0 % = 7,0 sobre 10**.

---

## 3. Preguntas de defensa oral (8) y respuesta que espero

1. **«Escribe que en z=0 está “a raíz simple”. Calcula `f′(0)` para `f(z)=z/√(z²+z)`. ¿Es simple esa raíz?»**
   *Esperado:* No. `f(z)=√(z/(z+1))∼√z`, luego `f′(z)→+∞` cuando `z→0⁺` (verificado con SymPy). z=0 es un **punto de ramificación**, no una raíz simple. Quien diga «simple» está aplicando el teorema de convergencia cuadrática sin comprobar su hipótesis.

2. **«Tu `g_N(z)=−z(2z+1)`. ¿Cuánto vale `g′_N(0)`? ¿Es un punto fijo superatrayente? ¿Qué orden tiene realmente Newton aquí?»**
   *Esperado:* `g′_N(0)=−1`: multiplicador de módulo 1, punto fijo **neutro**, no superatrayente. `g_N²(z)=z−8z³+O(z⁴)`: convergencia sublineal/muy lenta. La tabla no debería poner «Orde 2» como si se aplicase a esta f.

3. **«Halley tarda 25,22 iteraciones de media con orde 3. Calcula `g′_H(0)` y explica la contradicción sin echarle la culpa solo al polo.»**
   *Esperado:* `g_H(z)=−z/(4z+3)` → `g′_H(0)=−1/3`: convergencia **lineal** con factor 1/3. La orde 3 exige raíz simple; aquí no la hay. Además sólo un 0,04 % de puntos agota `maxiter`, así que la explicación de la memoria («moitos puntos se achegan ao polo, onde |f(z)| non baixa da tolerancia») es incompatible con sus propios datos. El freno real es el multiplicador 1/3, agravado por el polo de `g_H` en z=−3/4.

4. **«En la página 2 dices que si f″ es casi nula “a corrección é case nula e Halley case coincide con Newton”. ¿Esto es correcto?»**
   *Esperado:* No. Si `f″≈0`, la corrección de Halley es `f·f′/(f′²) = f/f′`, exactamente la de Newton. Lo que se anula es el **término correctivo adicional** de orden superior, no la corrección entera. Frase a corregir.

5. **«El enunciado pide para Chebyshev la interpretación xeométrica. ¿Qué construcción geométrica da `x_{n+1}`?»**
   *Esperado:* La intersección del eje OX con la **parábola osculatriz** (parábola tangente) en `(x_n, f(x_n))`; Halley corresponde a la hipsérbola/racional osculatriz (o al aproximante de Padé (1,1) de la inversa). «Usa un polinomio en vez de una expresión racional» es una descripción algebraica, no una interpretación xeométrica.

6. **«Comprueba `g(−1)` en los tres métodos. Todos dan −1. ¿Qué significa y qué ocurre si el punto inicial es exactamente −1?»**
   *Esperado:* z=−1 es punto fijo **espurio** de los tres mapas (en un punto donde f no está definida: `f(−1)=−∞+i·NaN`). La iteración se queda quieta y se contabiliza como 30 iteraciones sin convergencia. Y no es un polo en sentido estricto: `f(z)∼i(z+1)^(−1/2)`, singularidad algebraica de ramificación. La diapositiva 6 lo dice mejor que la memoria: «puntos de ramificación en 0 e −1». Contradicción interna a resolver.

7. **«Tus porcentajes son exactamente 30,82 / 0,04 / 94,68 %. Lo he reproducido: sale de usar la matriz completa de 301×301. ¿Tiene algún problema esa matriz?»**
   *Esperado:* Sí. El bucle `for i in range(0,npuntos)`, `for j in range(0,npuntos)` con `fractal[npuntos-j,i]` **nunca escribe** la fila 0 ni la columna 300: quedan 601 celdas inicializadas a 0 y se cuentan como «convergidas en 0 iteraciones». Sobre la malla realmente iterada (300×300) los valores son **13,64 / 25,30 / 4,91** y el «<10» de Halley baja de 0,66 % a **0,33 %**. El alumno debe saberlo y explicar por qué su tabla usa el array completo.

8. **«Si ampliásemos la ventana a [−2,1]×[−1,1] o cambiaramos la rama de la raíz cuadrada, ¿qué pasaría con las imágenes y con la comparación?»**
   *Esperado:* Aparición de más estructura alrededor de −1, subida del % de `maxiter` sobre todo en Newton, y dependencia de la rama: al cambiar de rama se cruza el corte y se reordenan las concas/coloración. Es una limitación real que la memoria ya menciona de pasada («uso da rama principal»), pero no cuantifica.

---

## 4. Errores y lagunas concretos detectados

| # | Hallazgo | Evidencia |
|---|---|---|
| E1 | **«Raíz simple» en z=0**: falso. `f(z)∼√z`, `f′(0)=+∞`. | Memoria §5, pág. 3; límite calculado con SymPy. |
| E2 | **«Polo» en z=−1**: impreciso/falso; es `(z+1)^(−1/2)`, punto de ramificación. | Memoria §5 frente a nota de la diapositiva 6. |
| E3 | **«A corrección é case nula»** si `f″≈0`: expresión ambigua. Lo que se anula es el término adicional en `f″`; el salto sigue siendo `f/f′`, como en Newton. Hay que escribirlo con precisión. | Memoria §3, pág. 2. |
| E4 | **Orde 2/3/3 presentada como propiedad de estos fractales**: es la orde genérica para raíz simple. Multiplicadores reales en z=0: `−1` (neutro), `−1/3` (lineal), `0` con `g_C≈3z²` (cuadrática). | Memoria §7 y tabla de la diapositiva 6. |
| E5 | **Explicación de Halley incoherente con sus datos**: achaca la lentitud al polo, pero sólo 0,04 % agota iteraciones; la causa principal es el multiplicador 1/3. | Memoria §7. |
| E6 | **601 celdas fantasma** (fila 0 y columna 300) contadas como n=0 en las estadísticas. | Reproducido ejecutando la lógica exacta de los tres scripts. |
| E7 | **Identificación en blanco** (grupo y relator) en memoria, README_entrega.md, portada y ZIP. | Portada pág. 1, README líneas 3–4. |
| E8 | **Interpretación xeométrica insuficiente** de Halley y Chebyshev: se describen diferencias algebraicas, sin parábola/hipérbola osculatriz, que es lo que pide el enunciado. | Memoria §§3–4. |
| E9 | **Duración planeada ≈9,5 min**, por encima del máximo de 8 (y del umbral de 9 si se leen las notas literales). | Notas de las 8 diapositivas. |
| E10 | **Calidad visual desigual**: imagen de Halley con costura vertical y dominio rojo/naranja, detalle fractal débil; pixelado en los tres por malla 300×300. | Inspección visual de `fractal_Halley.png` y estadística de color de los tres PNG. |
| E11 | **Faltas de forma**: «nese puntos», «reflexo» (calco), fórmulas escritas en notación plana `x_{n+1}` en una memoria en Galego. | Memoria págs. 3–4. |

**Lo que sí está bien, y conviene decirlo:** las tres fórmulas de iteración son correctas y están verificadas; la deducción de Newton es correcta; el dato histórico de Halley (1656–1742, 1694, familia de Householder, Padé (1,1)) es exacto; la bibliografía es la del enunciado; los scripts son reproducibles y los números de la tabla se pueden recomputar; el análisis cualitativo final («a orde teórica non determina por si soa o aspecto do fractal») es una observación inteligente, aunque la explicación concreta sea mejorable.

---

## 5. Nota final y justificación

**Nota: 7,0 / 10 (70 %).**

Se aprueba con nota alta pero no con matrícula. La parte **FRACTALES** es sólida en corrección fórmulas (10/10) pero floja en estética y nitidez (5+5): hay estructura fractal, sí, pero la de Halley cuesta encontrarla. La **MEMORIA** está muy bien presentada y es completa (10+10 en presentación de conjunto y completitude… salvo las faltas de forma, que bajan Presentación a 5), y sólidamente documentada, pero comete tres errores conceptuales que en Análise non se poden pasar por alto: confundir un punto de ramificación con unha raíz simple, dar por buena una orde de convergencia cuyas hipótesis no se cumplen, y una afirmación planamente falsa sobre la corrección de Halley cuando f″ se anula. La **EXPOSICIÓN** no puede calificarse del todo sin ver al alumno: estructura y material merecen 10, estilo y duración quedan en 5 por falta de evidencia y por un plan de tiempos que se pasa de largo.

No le quito puntos por «decoración» —la hay poca y es funcional—, se los quito por no haber vuelto a mirar lo que ya estaba escrito. Un 7,0 honrado.

---

## 6. Tres recomendaciones concretas de mejora

1. **Rehacer el análisis de la función antes de hablar de órdenes.** Escribir explícitamente que `z=0` es punto de ramificación de `√z` y `z=−1` una singularidad de tipo `(z+1)^(−1/2)`, calcular `g′(0)` de los tres mapas `(−1, −1/3, 0)` y distinguir entre «orde genérica de Newton/Halley/Chebyshev para raíz simple» y «comportamiento real de estos `g` en esta f». Corregir la frase de `f″≈0` y sustituir «polo» por «singularidade de ramificación». Añadir la construcción de la parábola osculatriz para Chebyshev.

2. **Arreglar las estadísticas y su interpretación.** Calcular sobre la malla realmente iterada (o rellenar correctamente la fila/columna frontera) y reportar 13,64 / 25,30 / 4,91 con Halley <10 % = 0,33 %; explicar la lentitud de Halley por el multiplicador 1/3 y el polo de `g_H` en −3/4, no sólo por el polo de `f`. Medir la convergencia con `|z_n−c|` además de `|f(z)|`, y registrar a qué raíz/corte se converge.

3. **Mejorar el paquete y la defensa.** Subir la malla a 600×600 con antialiasing, normalizar la coloración por `log(n)` o colorear por conca para rescatar detalle en Halley, eliminar la costura tratando explícitamente el corte de rama, rotular ejes como Re/Im, cubrir grupo y relator en memoria, portada y README, y recortar las notas a ~7 min (p. ej. 0,5 / 1 / 1,5 / 1 / 1 / 1,5 / 0,5 / 0,5) ensayando en voz alta.

---

## 7. Veredicto (en carácter)

> Vaia, pois. O traballo está feito con oficio: as fórmulas son correctas, os scripts corren, e ata me fixeron caso das catro referencias. Pero confundir un punto de ramificación cunha raíz simple e seguir escribindo «orde 3» como se a hipótese de raíz simple fose un detalle de estilo… iso é precisamente o que eu non podo deixar pasar nunha materia chamada **Análise Matemática**. A táboa de resultados é tan exacta que ata reproduce unha fila e unha columna que o bucle nunca calculou; bonito detalle, aínda que non fose intencionado. O fractal de Halley, esa mazá de cor laranxa cunha costura no medio, é o retrato perfecto da aplicación cega dunha fórmula sen mirar o multiplicador. Non obstante, hai fondo, hai dedución e hai unha idea final honesta sobre a orde teórica que non basta por si soa. Por iso non suspendo: **sete sobre dez**, e que o relator, cando encha o seu nome en blanco, vaia preparado a defender por que `g′(0)=−1/3`. Esa é a pregunta que lle vou facer primeiro.

---

## 8. Anexo: imaxe examinada e transcrición da rúbrica

A imaxe adxunta (`348F3E6C-6331-4D1E-975C-F742DBD3EAD8_113eea.png`, 1582 × 880 px, RGBA) é un **escaneo en branco e negro da plantilla de valoración**, en galego, co título centrado «Traballo de Análise Matemática». Non é un fractal nin unha captura de código. Está lixeiramente desenfocada e as etiquetas da columna esquerda aparecen recortadas no borde. Coincide coa Figura 2 do enunciado (`docs/Traballo_AM.pdf`).

Campos superiores, todos en branco: `GRUPO:`, cinco liñas numeradas 1.–5. para os membros, `Alumno que realiza a presentación:` e `NOTA FINAL:`. Non hai nomes escritos nin cualificación.

### Transcrición da grella

Columnas: **1 punto / 0,5 puntos / 0 puntos** (coma decimal galega). Os tres bloques suman 4 + 3 + 3 = 10 puntos.

**EXPOSICIÓN (40 %)**

| Criterio | 1 punto | 0,5 puntos | 0 puntos |
|---|---|---|---|
| Duración | Entre 5 e 8 minutos. | Entre 4-5 ou 8-9 minutos. | Menos de 4 minutos ou máis de 9 minutos. |
| Estrutura | Presentación ben estruturada: trátanse todos os temas requiridos con claridade. | Presentación pouco estruturada: falta algún dos temas requiridos ou non se explican con claridade. | Presentación mal estruturada. |
| Estilo | Fala alto, mira a audiencia, desenvolve as ideas a partir de notas resumidas (non le nin recita de memoria), a presentación é animada e amena. | A presentación ten polo menos dúas características mencionadas anteriormente. | A presentación ten menos de dúas características mencionadas anteriormente. |
| Material | Utiliza o material de maneira pedagóxica: tamaño de letra adecuado, transparencias con pouca letra, vínculo estreito entre transparencias e explicacións orais. | Utiliza o material de maneira pouco pedagóxica. | Non utiliza material de apoio. |

**MEMORIA ESCRITA (30 %)**

| Criterio | 1 punto | 0,5 puntos | 0 puntos |
|---|---|---|---|
| Presentación | A memoria está ben organizada, é coherente e non presenta faltas de ortografía. | Falla algunha das características mencionadas anteriormente. | Fallan polo menos dúas características mencionadas anteriormente. |
| Corrección | Os temas tratados son correctos e a información incluída é relevante. | A memoria contén algún erro ou información pouco relevante. | A maioría da memoria é errónea ou irrelevante. |
| Completitude | A memoria inclúe toda a información requirida. | A memoria non inclúe algunha da información requirida. | A memoria non inclúe a maioría da información requirida. |

**FRACTAIS (30 %)**

| Criterio | 1 punto | 0,5 puntos | 0 puntos |
|---|---|---|---|
| Corrección | As fórmulas usadas nos 3 métodos son correctas. | Hai polo menos 1 fórmula correcta distinta da do exemplo (Método de Newton). | Ningunha fórmula distinta da do exemplo (Método de Newton) é correcta. |
| Estética | En todas as imaxes obtidas apréciase a estrutura fractal, son orixinais e atractivas esteticamente. | Nas imaxes apréciase a estrutura fractal pero non presentan orixinalidade ou atractivo estético. | Nas imaxes non se aprecia estrutura fractal. |
| Calidade | As imaxes presentan gran nitidez e calidade. | As imaxes presentan nitidez e calidade media. | As imaxes están pixeladas ou son de baixa calidade. |

### Notas de lectura

- Polo desenfoque, nalgunha celda a lectura dubida entre «Faltan…» e «Falla…/Fallan…», e entre «desenvólve» e a forma normativa «desenvolve». Non se inventou contido nas celas ambiguas; escolléronse as formas que coinciden co PDF.
- A plantilla emprega «tódolos temas» e «Completitude»; en galego normativo serían «todos os temas» e «completude». A coma decimal é correcta.
- Non aparece ningunha fórmula escrita. A única referencia matemática explícita é «Método de Newton», é dicir, a iteración `z_{n+1} = z_n − f(z_n)/f′(z_n)` no plano complexo e as concas de atracción que producen a fronteira fractal.
- A visión directa desde a sesión principal devolveu un erro 429 (límite de taxa). A transcrición obtivo o subaxente de imaxe con dúas lecturas exitosas da imaxe orixinal; os equivalentes ampliados tamén foron bloqueados polo mesmo límite, e por iso se marcan as dúbidas.
- Esta grella é a que se aplica literalmente na sección 2: nove criterios dun punto cada un, logo **cada fila vale exactamente o 10 % da nota final**.
