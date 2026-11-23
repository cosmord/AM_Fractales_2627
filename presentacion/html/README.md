# Presentación HTML para clase

`index.html` es una presentación autocontenida: 10 diapositivas, navegación por teclado,
fragmentos revelados paso a paso, barra de progreso, partículas en canvas y animaciones
CSS. Estética de editor de código (VS Code), tipografía Cascadia Code y colores de
resaltado de sintaxis.

## Investigación previa

- [reveal.js](https://revealjs.com/) es el marco HTML de referencia para presentaciones:
  navegación con teclado, fragmentos, notas del relator, overview con `Esc`,
  auto-animate, transiciones y exportación a PDF. Se descartó como dependencia porque
  exige CDN en clase; se implementaron las piezas necesarias en un único archivo.
- Cascadia Code está disponible como paquete CDN
  ([@fontsource/cascadia-code](https://www.jsdelivr.com/package/npm/@fontsource/cascadia-code),
  v5.3.0, licencia OFL-1.1) y tiene fallback local a Consolas.
- Las partículas usan `requestAnimationFrame` con un máximo de 70 puntos y se desactivan
  con `prefers-reduced-motion`, para no cargar un portátil durante la exposición.

## Decisiones de diseño

- Un solo archivo, sin build: se abre con doble clic y funciona sin conexión salvo la fuente.
- Las tres imágenes se leen desde `../../imaxes/`; no se han incrustado para mantener
  el HTML ligero y usar las mismas PNG entregadas en el ZIP.
- Un único elemento protagonista: la ventana de editor con código resaltado y las tres
  figuras. El resto de la interfaz (activity bar, status bar, pestañas) es discreto.
- Paleta: fondo `#1e1e1e`, panel `#252526`, acento `#4ec9b0`, palabras clave `#c586c0`,
  funciones `#dcdcaa`, números `#b5cea8`, cadenas `#ce9178`.

## Controis

| Tecla | Acción |
|---|---|
| `→`, Espazo, `AvPáx` | Seguinte fragmento ou diapositiva |
| `←`, `RePáx` | Paso anterior ou diapositiva anterior |
| `Inicio` / `Fin` | Primeira / última diapositiva |
| `F` | Pantalla completa |
| `P` | Activar/desactivar partículas |
| `H` | Axuda |

## Verificación real

Se abrió en un navegador real: 10 diapositivas, contador `01 / 10`, las tres imágenes
cargadas (`naturalWidth > 0`), fuente Cascadia Code resuelta y navegación por fragmentos
funcionando.
