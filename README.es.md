# Smartboard notebook Exporter
<!-- MikeCat made this :3 --->
Exporta tus archivos Smartboard `.notebook` de manera local y a lo que quieras (siempre y cuando lo tengamos).

> **README.md**  
> Lee este documento en: [ENGLISH](README.md) [ESPAÑOL](README.es.md)

---

"Smartboard notebook Exporter" (`sbne`) es un proyecto libre y de código abierto escrito en Python, diseñado para exportar tus pizarras digitales desde el formato Smartboard `.notebook` a otros tipos de formatos (aparte del `pdf-png-merged`) de manera completamente local.

Este programa te permite tomar el archivo `.notebook` (el cual le puedes extraer desde tu pizarra a un almacenamiento externo con la función de compartir) y convertirlo a otros formatos en tu ordenador. Esto rompe la limitación de Smarttech de solo poder exportar las pizarras como un archivo PDF con imágenes rasterizadas de cada página (`pdf-png-merged`), otorgandote una mayor flexibilidad.

> **AVISO**  
> Este proyecto no está afiliado con Smarttech o con ninguna otra marca.  
Este proyecto es otorgado "tal y como es", sin ningún tipo de garantía.

### Funcionamiento
Cuando se le da un archivo `.notebook` a `sbne`, la aplicación lo descomprime para conseguir acceder a cada página, almacenadas como archivos `.svg` por cada página. Después, se arreglan cada uno de los archivos `.svg` para ajustar su tamaño de lienzo y ajustar los contenidos al nuevo lienzo. Finalmente, se exportan todos los archivos `.svg` ya arreglados al formato elegido.

### Formatos de Salida Disponibles
- `svg-fixed-pages`: Un archivo zip con todas las páginas `.svg` ya arregladas.
- `png-pages`: Un archivo zip con todas las páginas como imágenes rasterizadas `.png`.
- `pdf-svg-pages`: Un archivo zip con cada una de las páginas como archivos `.pdf` individuales (contenido vectorial).
- `pdf-svg-merged`: Un único archivo PDF con todas las páginas como archivos `.svg` arreglados (contenido vectorial).  
- `pdf-png-pages`: Un archivo zip con cada una de las páginas como imágenes rasterizadas `.png` (contenido rasterizado).
- `pdf-png-merged`: Un único archivo PDF con todas las páginas como imágenes rasterizadas `.png` (contenido rasterizado).

### Documentación
- [Format Deep Dive](docs/notebook-format.es.md): Información sobre el archivo `.notebook`, su estructura interna y cómo almacena la información.
- [Testing Guide](docs/testing.es.md): Detalles sobre los archivos de test y cómo comprobar que el exportador funciona adecuadamente.

## Requisitos

### Binario
- [***Tha binary***](https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest) :3  
No hay ningún requisito como tal, tan solo descarga el ejecutable compatible con tu ordenador, ¡y eso es todo! :D

### Código fuente
- **Python**: 3.10 o superior (3.12 o 3.13 recomendado).
- **Python Pip**: Si no viene incluido en el paquete de Python, la misma versión que Python.
- **Python venv**: Si no viene incluido en el paquete de Python, la misma versión que Python.
- **Python Tkinter**: Si no viene incluido en el paquete de Python, la misma versión que Python.
- **System Dependencies**: Cairo.
- **Dependencies**: Listado en [`requirements.txt`](requirements.txt).

## Instalación

### Mediante Binario
Descarga y ejecuta este programa desde su binaro completamente portable. No se necesita permiso de superusuario/administrador. Solo está disponible la GUI (Interfáz Gráfica de Usuario, del inglés Graphics User Interface).

Tan solo necesitas descargar el binario específico a tu SO (Windows, Linux) y Arquitectura de tu ordenador (AMD64, ARM64...) desde la [Releases Tab](https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest) (Página de Lanzamientos) de este repositorio y ejecuta el programa. Si tu SO/Arquitectura no aparece en la Página de Lanzamientos, necesitaras instalar este programa mediante el código fuente y ejecutarlo o compilar un binario específico para tu dispositivo.

**Binarios Disponibles**

<table>
    <thead>
        <tr>
            <th>Sistema Operativo</th>
            <th>Versión</th>
            <th>Arquitectura</th>
            <th>Binario</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Debian</td>
            <td>Debian 13 Trixie</td>
            <td>AMD64</td>
            <td>sbne-vX.X.X-debian-trixie-amd64</td>
        </tr>
        <tr>
            <td rowspan="2">Windows</td>
            <td>Windows 10</td>
            <td>AMD64</td>
            <td rowspan="2">sbne-vX.X.X-windows-amd64.exe</td>
        </tr>
        <tr>
            <td>Windows 11</td>
            <td>AMD64</td>
        </tr>
    </tbody>
</table>

> **AVISO**  
> La única fuente de confianza de binarios compilados de este programa es este [Repositorio de GitHub](https://github.com/MikeCat2008/smartboard-notebook-exporter).  
> Otras páginas o fuentes de descargas pueden ser un potencial riesgo de virus u otro tipo de malware. Esto se debe a que los binarios son solo el código máquina (un puñado de ceros y unos) compilado a partir de un código fuente, el cuál no se puede trazar de vuelta desde los binarios. Por tanto, dos binarios pueden parecer idénticos pero comportarse de manera totalmente distinta. Comprobar el SHA256 de los binarios es sumamente recomendable.

### Mediante Código Fuente
Instala y ejecuta este programa desde su código fuente.

<details>
<summary><b>Linux (Debian/Ubuntu)</b></summary>

**Instalación y primera ejecución**

1. **Instalación de las dependencias del sistema**: `python`, `pip`, `venv`, `tkinter`, `git` y librerías de CairoSVG (`libcairo2`, `libffi-dev` y `python3-dev`) . Se requiere acceso a `sudo` (a menos que las dependencias ya estén satisfechas, en ese caso avanza al siguiente paso).

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk git libcairo2 libffi-dev python3-dev
```

2. **Clonar código fuente**: Clona este repositorio y mueve el directorio de trabajo al nuevo directorio de la instalación.

```bash
git clone https://github.com/MikeCat2008/smartboard-notebook-exporter.git
cd smartboard-notebook-exporter
```

3. **Configuración del entorno de Python**: Crea y activa el entorno virtual de python y nómbralo `.venv`. Instala todas las librerías requeridas que están listadas en `requirements.txt` usando `pip`.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
```

4. **Ejecuta**: Ejecuta la Interfáz de Línea de Comandos (del inglés CLI, Command Line Interface) con `src/main.py` o la Interfáz Gráfica de Usuario (del inglés GUI, Graphical User Interface) con `src/gui.py`.

```bash
python3 src/main.py # CLI
python3 src/gui.py  # GUI
```

**Ejecuciones posteriores:**

Para volver a lanzar el programa después de la instalación, asegúrate de estar en la misma carpeta donde has clonado el código fuente. Después activa el mismo entorno virtual (`.venv`) y ejecuta la Interfáz de Usuario que desees.

```bash
source .venv/bin/activate
python3 src/main.py # CLI
python3 src/gui.py  # GUI
```

</details>

<details>
<summary><b>Windows</b></summary>

**Instalación y primera ejecución:**

1. **System dependencies installation**: `python`, `git` and [GTK Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer) (for CairoSVG). Access to Administrator mode is required (unless dependencies are already fulfilled, in that case go to the next step).

```powershell
# Run this in a terminal as Administrator
winget install python Git.Git tschoonj.GTKForWindows
exit
```

> **NOTA**  
> After installing all system dependencies, closing the terminal with `exit` and opening a new one is required for the system PATH to update.

2. **Clonar código fuente**: Clona este repositorio y mueve el directorio de trabajo al nuevo directorio de la instalación.

```powershell
git clone https://github.com/MikeCat2008/smartboard-notebook-exporter.git
cd smartboard-notebook-exporter
```

3. **Configuración del entorno de Python**: Crea y activa el entorno virtual de python y nómbralo `.venv`. Instala todas las librerías requeridas que están listadas en `requirements.txt` usando `pip`.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. **Ejecuta**: Ejecuta la Interfáz de Línea de Comandos (del inglés CLI, Command Line Interface) con `src/main.py` o la Interfáz Gráfica de Usuario (del inglés GUI, Graphical User Interface) con `src/gui.py`.

```powershell
python src\main.py # CLI
python src\gui.py  # GUI
```

**Ejecuciones posteriores:**

Para volver a lanzar el programa después de la instalación, asegúrate de estar en la misma carpeta donde has clonado el código fuente. Después activa el mismo entorno virtual (`.venv`) y ejecuta la Interfáz de Usuario que desees.

```powershell	
.venv\Scripts\activate
python src\main.py # CLI
python src\gui.py  # GUI
```

</details>

## Compilación
Para compilar un binario de este programa, es necesario haber hecho previamente la instalación mediante mediante código fuente y haber ejecutado el programa al menos una vez para cerciorarse de que todo funcione adecuadamente tras la instalación.

Para compilar este programa, activa el entorno virtual (`.venv`) de la instalación y ejecuta el comando `build` correspondiente al SO donde se ha realizado la instalación: `.sh` para los basados en Linux y `.bat` para Windows. Cuando el programa termine de empaquetar y compilar el programa, el binario resultante se encontrará en la carpeta `dist/` dentro del directorio principal de la instalación de este proyecto. Este binario es completamente portable y no requiere permiso de superusuario/administrador para ejecutarse.

El programa de compilación utiliza PyInstaller para empaquetar el código fuente junto al intérprete de Python, todas las librerías requeridas y cualquier librería del sistema que requieran las propias librerías de python, dentro de un único ejecutable y portable. Es importante destacar que los binarios producidos por PyInstaller no son compatibles entre distintas plataformas, lo que supone que, por ejemplo, un binario compilado para Windows no podrá ejecutarse en Debian o viceversa.

## Uso
Para poder exportar tu archivo `.notebook` al formato de salida deseado es necesario configurar los siguientes parámetros: 
- **`.notebook` file path**: Ruta a tu archivo `.notebook` (absoluta o relativa a la ruta desde la que se ha lanzado el programa).
- **Export Type**: Elige uno de los 6 formatos de salida disponibles.
- **Export Path** (opcional): Cambia el directorio de salida para tu archivo exportado. Si se deja vacío, el directorio de salida será el mismo desde donde se ha tomado el archivo `.notebook`.
- **Export Name** (opcional): Cambia el nombre del archivo de salida. Si se deja vacío, el nombre de salida mantendrá el mismo nombre que el archivo `.notebook` de entrada.
- **Output Name Extension**: Bandera booleana para añadir al nombre del archivo de salida "_`Tipo de Conversión`". Si se deja vacío o se da una entrada errónea, se asumirá la opción por defecto (y, sí).

Cualquier archivo exportado terminará con su respectiva ".`Extensión de Tipo de Conversión`

Tras la instalación, ejecuta el programa acorde al método de instalación seguido.

### GUI
Interfáz Gráfica de Usuario (del inglés GUI, Graphical User Interface). La GUI está disponible en los lanzamientos de los binarios y en las instalaciónes mediante código fuente. Esta es la opción recomendada para la mayoría de los usuarios.

**Uso**

Cuando la GUI del programa se abre, el usuario poddrá ver, descrito de arriba a abajo, el nombre de la aplicación, la sección para el manejo de la versión, la configuración del idioma de la GUI, todos los parámetros requeridos para exportar los archivos notebook, el botón de exportar y enlaces útiles.

En la sección para el manejo de la versión, el usuario puede ver la versión de compilación actual del binario de su app y comprobar actualizaciones. El botón `Comprobar Actualizaciones` es un enlace a la página de GitHub de la [Latest Release](https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest) (Último Lanzamiento), donde el usuario puede descargarse los binarios compilados más recientes de la app. Se recomienda encarecidamente revisar de vez en cuando esta página para estar al día con las actualizaciones y arreglo de bugs. 

La sección de la configuración del idioma muestra al usuario el idioma que se está utilizando en la GUI y los botones para elegir las traducciones disponibles. Inglés es el idioma por defecto.

El primer grupo de campos es `Archivo Notebook`, el cuál deja al usuario elegir qué archivo `.notebook` exportar al especificar la ruta a dicho archivo. El archivo puede ser indicado escribiendo la ruta relativa a la ruta desde donde se ha lanzado la aplicación o con la ruta absoluta, o también utilizando el botón de `BUSCAR`. Solo se permiten archivos `.notebook`. Si la ruta al archivo se deja en blanco, no existe o no es un archivo válido, cuando se intente exportar, aparecerá una ventana con un aviso/error.

El segundo grupo de campos es `Exportar Archivo`, el cuál deja al usuario configurar el archivo de salida. El campo `Carpeta de Salida` se comporta igual que el campo Archivo Notebook, con la diferencia de que tan solo admite rutas relativas o absolutas a carpetas en vez de a archivos. Si se deja vacío, el archivo de salida será exportado al mismo directorio desde donde se ha tomado el archivo que se está exportando. El campo `Nombre` permite al usuario poner un nombre personalizado al archivo de salida. Si se deja en blanco, el archivo de salida utilizará el mismo nombre que el archivo que se está exportando. La pestaña de seleción `Tipo de Conversión` permite al usuario elegir a qué formato disponible exportar. La casilla de marcado `Añadir Etiqueta de Conversión` añade al final del nombre un identificador del tipo de conversión empleado para el archivo de salida. Abajo hay una previsualización activa del nombre del archivo de salida, incluyendo el nombre personalizado (o el mismo que el archivo notebook), la etiqueta de conversión (si se ha marcado que sí) y la extensión correspondiente al formato de salida elegido.

Cuando se pulsa el botón de exportar, el proceso de exportar dará comienzo y se lo indicará al usuario al desactivarse y cambiar su apariencia. Este proceso normalmente terminará exportando el archivo de salida y mostrando una ventana emergente de información. El proceso de exportación puede interumpirse si hay parámetros no válidos, hay riesgo de sobreescritura de archivos o en el caso de que suceda un error durante la exportación, lo cuál resultará en una interrupción del proceso anunciada por una ventana emergente de aviso/error. Después de que el proceso de exportación haya finalizado (sin importar de que haya sido exitoso o no), el botón de exportación se reactivará.

Los enlaces útiles se abrirán en el navegador por defecto cuando sean pulsados. Estos enlaces son este [Repositorio de GitHub](https://github.com/MikeCat2008/smartboard-notebook-exporter) y la [Licencia GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)

### CLI
Interfáz de Línea de Comandos (del inglés CLI, Command Line Interface). Únicamente disponible mediante la ejecución del código fuente.

**Uso**
```text
(.venv) $ python src/main.py
'.notebook' file path: ./tests/01-30-26 11-14-16 AM.notebook
Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.
Export Type: pdf-svg-merged
Export Path (opt): ./
Export Name (opt): 
Output Name Extension. y/n (y): Y

(.venv) $ 
```

```text
[dir] . # Current Directory
├─[dir] tests
| └─ [notebook] 01-30-26 11-14-16 AM.notebook
└─ [pdf] 01-30-26 11-14-16 AM_pdf-svg-merged.pdf
```

## Licencia
Este proyecto está licenciado bajo la GNU General Public License v3.0. Revisa el archivo [LICENSE](LICENSE) para más detalles.
