# Smartboard notebook Exporter
<!-- MikeCat made this :3 --->
Exporta tus archivos Smartboard `.notebook` de manera local y a lo que quieras (siempre y cuando lo tengamos).

> **notebook-format.es.md**  
> Lee este documento en: [ENGLISH](notebook-format.md) [ESPAÑOL](notebook-format.es.md)

---

Toda la información obtenida sobre el archivo `.notebook` que se muestra en este documento, ha sido producto de la ingeniería inversa realizada a los archivos generados con una "SMART Board MX065 iQ", los cuáles están disponibles dento del directorio [`/tests`](../tests/) de este repositorio. Esta información es otorgada "tal y como es", sin ningún tipo de garantía.

Si hay poca o nada de información sobre cualquier elemento del archivo `.notebook`, es porque no es relevante para el exportador o porque no ha sido estudiado todavía.

## Estructura del Archivo
### El Contenedor
El archivo `.notebook` es un archivo ZIP ofuscado el cuál contiene todos los contenidos que componen a la pizarra digital. Para desempaquetar sus contenidos, no hay ningúna direrencia que con un archivo `.zip` común. Gracias a la naturaleza de los archivos ZIP, las feschas de modificación se preservan, permitiendo estimar el origen de cada uno de los archivos contenidos. 
<!-- thx KDE Dolphin for telling me this <3 -->

La regla de nomenclatura del archivo `.notebook` sigue el patrón `MM`-`DD`-`YYYY` `hh`-`mm`-`ss` `AM/PM`.notebook", lo que se corresponde con la fecha exacta de la creación del archivo. Este nombre no se modifica tras su creación.

### Estructura Mínima
All `.notebook` files always fulfill a minimal structure of 6 files at the root of the archive. This can be seen inside the test file ["Blank" (04-13-26 11-34-53 AM.notebook)](../tests/04-13-26%2011-34-53%20AM.notebook).
Todos los archivos `.notebook` siempre cumplen una estructura mínima compuesta de 6 archivos en la raiz del contenedor. Esto se puede apreciar dentro del archivo de test ["Blank" (04-13-26 11-34-53 AM.notebook)](../tests/04-13-26%2011-34-53%20AM.notebook) ("Vacío").

- **`acetate_ids_repaired`**: Un archivo vacío. Creado en el mismo instante que el propio archivo `.notebook`. Archivo de soporte, su propósito no se ha identificado todavía.

- **`imsmanifest.xml`**: Un archivo XML. Contiene la etiqueta `<resource identifier="group0_pages">`, la cual enumera cada página y, más imporante, define el orden lógico de las páginas. Se copia desde una plantilla interna de la Smartboard dado que a veces tiene una fecha de "útima modificación" del "2021-02-03 18:05", independientemente del instante de la creación del `.notebook`. Este archivo es modificado siempre que se añade una nueva página o si se reorganiza el orden lógico.

- **`metadata.xml`**: Un archivo XML. Se copia desde una plantilla interna de la Smartboard dado que a veces tiene una fecha de "útima modificación" del "2021-02-03 18:05", independientemente del instante de la creación del `.notebook`. Archivo de soporte, su propósito no se ha identificado todavía dado que es idéntico para todos los archivos de test.

- **`page0.svg`**: Un archivo SVG. Creado en el mismo instante que el archivo `.notebook`. La página inicial de la pizarra blanca.

- **`preview.png`**: Un archivo PNG. Se copia desde una plantilla interna de la Smartboard dado que a veces tiene una fecha de "útima modificación" del "2021-02-03 18:05", independientemente del instante de la creación del `.notebook`. Su propósito es ser una previsualizción para el explorador de archivos propietario de Smartboard. Por defecto esta imágen es un plano completamente blanco de 250x150 px. Si `page0.svg` no está vacío, `preview.png` será sobreescrito con una rasterización de este archivo SVG a un tamaño de 200x113 px si se ha creado con la aplicación de pizarra blanca, y 620x360 px si proviene de una captura de pantalla.

- **`settings.xml`**: Un archivo XML. Se copia desde una plantilla interna de la Smartboard dado que a veces tiene una fecha de "útima modificación" del "2021-02-03 18:05", independientemente del instante de la creación del `.notebook`. Archivo de soporte, su propósito no se ha identificado todavía dado que es idéntico para todos los archivos de test. Este archivo parece ser modificado cuando ha sido creado mediante una captura de pantalla en vez de la apliación de pizarra blanca.

Ejemplo de la estructura mínima tomada del archivo de test ["Blank"](../tests/04-13-26%2011-34-53%20AM.notebook) ("Vacío").
```
[zip] 04-13-26 11-34-53 AM.notebook
├─ [?] acetate_ids_repaired
├─ [xml] imsmanifest.xml
├─ [xml] metadata.xml
├─ [svg] page0.svg
├─ [png] preview.png
└─ [xml] settings.xml
```

### Recursos (Carpetas y Archivos Opcionales)
Una vez satisfecha la estructura mínima, la Smartboard añadirá todos los recursos requeridos al archivo `.notebook` en función de las necesidades de la pizarra blanca que representa.

#### Páginas SVG
Cuando el usuario pulsa el botón "Añadir una Nueva Página", se crea un nuevo archivo SVG en la raiz del archivo `.notebook`. Toda página adicional sigue la misma norma de nomenclatura: "page`X`.svg", donde la "`X`" representa el índice de la página, creado al sumar 1 al último índice más alto (empezando por 0).

```
├─ [svg] page0.svg
├─ [svg] page1.svg
├─ [svg] page2.svg
...
├─ [svg] page9.svg
├─ [svg] page10.svg
├─ [svg] page11.svg
...
```

#### Imágenes
Si la pizarra blanca contiene una imágen, sin importar de que sea una captura de pantalla, una foto insertada, una miniatura de un vídeo, un patrón para un fondo embaldosado o la imágen de un widget; se crea una carpeta llamada `images` conteniendo las imágenes requeridas en la raiz del archivo `.notebook`.

Todas las imágenes dentro del directorio `images` son nombradas utilizando un UUID (Identificador Universalmente Único, del inglés Universally Unique Identifier) a excepción de las capturas de pantalla, cuya única imágen tiene el nombre de `background.jpeg`. Todas las imágenes son archivos PNG a excepción de los patrones para los fondos embaldosados, los cuáles son archivos JPEG. Aparentemente, todas las imágenes tienen su extensión de archivo, a excepción de las imágenes insertadas desde la web.

Ejemplo del directorio `images` tomado del archivo de test ["Main" (01-30-26 11-14-16 AM.notebook)](../tests/01-30-26%2011-14-16%20AM.notebook) ("Principal").
```
[zip] 01-30-26 11-14-16 AM.notebook
├─ ...
└─ [dir] images
   ├─ ...
   ├─ [png] e01ca24a-ddf7-4798-b80b-40665213c932	# Image from web
   ├─ [png] a54826e3-fc98-4701-9c91-7a7936a3a9de.png	# Video miniature
   ├─ [jpeg] c4859910-ebe8-479f-a45d-22789240b923.jpg	# Tile for a tiling pattern
   └─ [png] bf7802d9-8317-478b-8c14-b957608a410a.png	# Clock Widget
```

## Análisis de las Páginas SVG
The contents of each page of the `.notebook` file, are stored inside individual SVG files.
Los contenidos de cada página del archivo `.notebook` son almacenados dentro de archivos SVG individuales.

El Estándar SVG que siguen estos archivos SVG es completamente compatible con cualquier otro software diseñado para trabajar con este tipo de archivos.

### Lienzo y Ventana Gráfica
Toda la información sobre el lienzo y la ventana gráfica del SVG están dentro de la etiqueta raíz (`<svg>`) de cada archivo SVG. Esta etiqueta siempre aparece en cada uno de los archivos SVG del archivo `.notebook` como la etiqueta raíz, dado que esta es la etiqueta que define que ese árbol XML es un SVG.

La información dentro de la etiqueta `<svg>`, cuando se extrae directamente del archivo `.notebook`, puede ser engañosa. Todos los archivos SVG siempre tendrán los atributos `width="800"` y `height="600"` sin importar su anchura y/o altura verdadera.

La anchura y altura verdadera del lienzo se puede calcular a partir del atributo `canvas_bounds`, el cuál dibuja un rectángulo desde la Esquina Superior Izquierda hasta la Esquina Inferior Derecha del verdadero lienzo. Y al calcular la diferencia en la altura y anchura entre ambas esquinas, se obtiene el ancho y la altura verdaderos. Este atributo toma 4 parámetros para las coordenadas de ambas esquinas: "`Superior X`,`Superior Y`,`Inferior X`,`Inferior Y`". Las coordenadas para la Esquina Superior siempre son negativas.

- **Anchura Verdadera** (AnchoV): `Inferior X` - `Superior X`
- **Altura Verdadera** (AltoV): `Inferior Y` - `Superior Y`
- **Etiqueta`<svg>` arreglada**: `<svg width="AnchoV" height="AltoV" canvas_bounds="[...]" [...] >`

### Alineación del Contenido
Todo el contenido creado por el usuario, como trazos o imágenes insertadas, están agrupados bajo una única etiqueta de grupo (`<g>`), la cuál es la única etiqueta `<g>` que se encuentra directamente bajo la etiqueta raíz `<svg>`. Esta etiqueta aparece en todos los archivos SVG del archivo `.notebook` con un atributo y un valor de `class="foreground"`.

Cuando se ajusta el tamaño del lienzo a su tamaño verdadero, todos los contenidos se encuentran desplazados. Para arreglar la alineación, el artibuto `transform` con un valor de "translate(`X`,`Y`)" se debe de añadir a esta etiqueta `<g>`. Los valores para `X` e `Y` son los mismos valores que `Superior X` y `Superior Y` (del atributo `canvas_bounds` de la etiqueta raíz `<svg>`) pero multiplicado por -1 para hacer que estos valores sean positivos.

- **Desplazamiento Horizontal** (DespH): `Superior X` * -1
- **Desplazamiento Vertical** (DespV): `Superior Y` * -1
- **Etiqueta `<g>` arreglada**: `<g [...] transform="translate(DespH,DespV)">`

### Lógica de la Ordenación de las Páginas
Todos los archivos SVG se encuentran en la raíz del archivo `.notebook` y siguen la misma norma de nomenclatura: "page`X`.svg", donde la "`X`" representa el índice de la página, creado al sumar 1 al último índice más alto (empezando por 0).

El órden de las páginas definido por el usuario no se corresponde con el órden lógico de los índices de cada página SVG. Este órden está definido en el archivo `imsmanifest.xml` dentro de su etiqueta `<resource identifier="group0_pages">`.

### Trazos de Subrayador
Cuando el usuario dibuja con la herramienta subrayador, los trazos creados tienen un atributo personalizado `hilighter="1"`. Estos trazos se muestran por debajo de cualquier otro trazo para simular el efecto de un subrayador.
