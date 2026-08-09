# Smartboard notebook Exporter
<!-- MikeCat made this :3 --->
Exporta tus archivos Smartboard `.notebook` de manera local y a lo que quieras (siempre y cuando lo tengamos)..

> **testing.es.md**  
> Lee este documento en: [ENGLISH](testing.md) [ESPAÑOL](testing.es.md)

---

Estos archivos de test se han creado para cumplir con 2 propósitos principales, comprobar que el exportador funciona correctamente y ver como el archivo `.notebook` se comporta bajo distintas circunstancias para poder enteder su estructura interna y ver cómo almacena la información (ver [notebook-format.es.md](notebook-format.es.md) para más detalles).

Todos los archivos de test `.notebook`, disponibles en el directorio [`/tests`](../tests/) de este repositorio, han sido generados con una "SMART Board MX065 iQ" y exportados a un almacenamiento externo con la función integrada "Compartir .notebook". La norma de nomenclatura de los archivos es la original establecida por la Smartboard.

Cada uno de los archivos de test tiene su respectivo `.pdf` con el mismo nombre, generado y exportado con la función integrada "Compartir como .pdf". La norma de nomenclatura de los archivos es la original establecida por la Smartboard. Estos archivos sirven como una referencia para el órden lógico de las páginas, además de ser una referencia exacta para el formato de salida `pdf-png-merged` de este exportador.

## Archivo de Test Main (Principal)
Incluye la mayoría de las pruebas dentro de un solo archivo. Este archivo se ha empleado como referencia del árbol completo de la estructura interna del `.notebook`. No todas las páginas se han creado después de la anterior, esto puede resultar en comportamientos inesperados.
<!-- i didn't expect to add page 9 and its tests lol -->
- `.notebook`: [01-30-26 11-14-16 AM.notebook](../tests/01-30-26%2011-14-16%20AM.notebook)
<!-- Link with original path cannot be used bc it uses spaces in the link part...: [01-30-26 11-14-16 AM.notebook](../tests/01-30-26 11-14-16 AM.notebook). Spaces inside the path must be replaced with a "%20" -->
- Versión de Smartboard de `pdf-png-merged`: [01-30-26 11-14-16 AM.pdf](../tests/01-30-26%2011-14-16%20AM.pdf)
### ¿Qué comprueba?
- Tamaño del lienzo.
- Fondo con colores personalizados.
- Fondo embaldosado personalizado.
- Ancho de trazo de las herramientas Bolígrafo y Subrayador.
- Colores por defecto de las herramientas Bolígrafo y Subrayador.
- Pen and Hightlighter layering.
- Comportamiento de la herramienta de Bolígrafo de texto formateado.
- Agrupación de elementos.
- Característica "Mover al fondo".
- Característica "Duplicador Infinito".
- Insertar, duplicar y rotar imágenes.
- Insertar enlaces de Vídeo.
- Widgets de Pizarra Blanca.
- Página vacía.
- Estructura interna completa del `.notebook`

## Archivo de Test Screenshot (Captura de Pantalla)
Una prueba simple para ver cómo la Smartboard almacena las capturas de pantalla que tienen trazos en ellas.
- `.notebook`: [01-22-26 11-32-29 AM.notebook](../tests/01-22-26%2011-32-29%20AM.notebook)
- Versión de Smartboard de `pdf-png-merged`: [01-22-26 11-32-29 AM.pdf](../tests/01-22-26%2011-32-29%20AM.pdf)
### ¿Qué comprueba?
- Gestión de las capturas de pantalla de Smartboard.
- Imágenes.
- Elementos bloqueados (la imágen de la captura de pantalla)

## Archivo de Test Blank (Vacío)
La pizarra blanca más simple que se puede hacer. Creada tras simplemente abrir la aplicación de pizarra blanca.
- `.notebook`: [04-13-26 11-34-53 AM.notebook](../tests/04-13-26%2011-34-53%20AM.notebook)
- Versión de Smartboard de `pdf-png-merged`: [04-13-26 11-34-53 AM.pdf](../tests/04-13-26%2011-34-53%20AM.pdf)
### ¿Qué comprueba?
- Estructura interna mínima del `.notebook`.
- Página vacía.

## Archivo de Test Page Order (Órden de las Páginas)
Comprueba cómo los archivos `.svg` del archivo `.notebook` son nombrados y qué metadatos están involucrados en el órden lógico que se ve en el archivo de salida de la "Versión de la Smartboard de `pdf-png-merged`". Este archivo se creó tras descubrir comportamientos extraños al exportar el archivo de test principal. 
- `.notebook`: [04-13-26 11-19-30 AM.notebook](../tests/04-13-26%2011-19-30%20AM.notebook)
- Versión de Smartboard de `pdf-png-merged`: [04-13-26 11-19-30 AM.pdf](../tests/04-13-26%2011-19-30%20AM.pdf)
### ¿Qué comprueba?
- Nomenclatura interna de las páginas (siguiendo el órden de creación).
- Metadatos para el órden lógico de las páginas.
