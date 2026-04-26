# Smartboard notebook Exporter
<!-- MikeCat made this :3 --->
Export your Smartboard `.notebook` files locally and however you want (and we support).

> **notebook-format.md**  
> Read this document in: [ENGLISH](notebook-format.md)

---

All the information obtained about the `.notebook` file featured in this document, has been reversed engineered from the files created with a "SMART Board MX065 iQ", which are provided inside the [`/tests`](../tests/) directory of this repository. This information is provided "as is", without warranty of any kind.

If there is poor or no information about any element of the `.notebook` file, it is because it has not been found relevant for the exporter or because it has not been studied yet.

## File Structure
### The Container
The `.notebook` file is a disguised ZIP Archive containing all the contents that make up the whiteboard. In order to unpack its contents there is no difference with a regular `.zip` file. Thanks to the nature of the ZIP files, modification dates are preserved, allowing us to estimate the origin of every file inside.
<!-- thx KDE Dolphin for telling me this <3 -->

The naming scheme of the `.notebook` file follows the pattern "`MM`-`DD`-`YYYY` `hh`-`mm`-`ss` `AM/PM`.notebook", which corresponds with the exact time of creation of the file. This name always remains the same after its creation.

### Minimal Structure
All `.notebook` files always fulfill a minimal structure of 6 files at the root of the archive. This can be seen inside the test file ["Blank" (04-13-26 11-34-53 AM.notebook)](../tests/04-13-26%2011-34-53%20AM.notebook).

- **`acetate_ids_repaired`**: An empty file. Created at the same time the `.notebook` file is created. Support file, its purpose has not been identified yet.

- **`imsmanifest.xml`**: An XML file. It contains the tag `<resource identifier="group0_pages">`, which lists every page and, most importantly, defines the logical order of the pages. It is copied from an internal template of the Smartboard as it sometimes has a "last modification" date from "2021-02-03 18:05", independent of the `.notebook` creation. This file is modified whenever a new page is added or rearranged.

- **`metadata.xml`**: An XML file. It is copied from an internal template of the Smartboard as it sometimes has a "last modification" date from "2021-02-03 18:05", independent of the `.notebook` creation. Support file, its purpose has not been identified yet as it is the same for all test files.

- **`page0.svg`**: An SVG file. Created at the same time the `.notebook` file is created. The initial whiteboard page.


- **`preview.png`**: A PNG file. It is copied from an internal template of the Smartboard as it sometimes has a "last modification" date from "2021-02-03 18:05", independent of the `.notebook` creation. Its purpose is to be an image preview for Smartboard's own filebrowser. This image defaults with plain white 200x150 px. If `page0.svg` is not blank, `preview.png` will be overwritten with a rasterization of this SVG file of 200x113px if it has been created with the witeboard app, and 620x360 px if it cames from a screenshot.

- **`settings.xml`**: An XML file. It is copied from an internal template of the Smartboard as it sometimes has a "last modification" date from "2021-02-03 18:05", independent of the `.notebook` creation. Support file, its purpose has not been identified yet as it is the same for all test files. This file appears to be modified when it has been created through a screenshot instead of the whiteboard app.

Example of the minimal structure taken from the ["Blank"](../tests/04-13-26%2011-34-53%20AM.notebook) test file.
```
[zip] 04-13-26 11-34-53 AM.notebook
├─ [?] acetate_ids_repaired
├─ [xml] imsmanifest.xml
├─ [xml] metadata.xml
├─ [svg] page0.svg
├─ [png] preview.png
└─ [xml] settings.xml
```

### Assets (Optional Folders and Files)
Once fulfilled the minimal structure, the Smartboard will add all the required assets to the `.notebook` file according to the needs of the whiteboard it represents.

#### SVG Pages
Whenever the user presses the button of "Add a New Page", a new SVG file is created at the root level of the `.notebook` file. Every new page follows the same naming scheme: "page`X`.svg", where the "`X`" stands for the page index, created by adding 1 to the last highest index (starting from 0).

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

#### Images
If the whiteboard contains an image, regardless of it being a screenshot, an inserted photo, a video miniature, a pattern for a tiling background or a picture of a widget, a folder named `images` containing the required pictures, is created at the root level of the `.notebook` file.

The images inside the directory `images` are named with a UUID (Universally Unique Identifier) except in the case of a screenshot, then the only image . All the pictures are PNG files except the tiles for the tiled backgrounds, which are JPEG files. Apparently, all the pictures have their file extension, except the images inserted from the web.

Example of the `images` directory taken from the ["Main" (01-30-26 11-14-16 AM.notebook)](../tests/01-30-26%2011-14-16%20AM.notebook) test file.
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

## Page SVG Analysis
The contents of each page of the `.notebook` file, are stored inside individual SVG files.

The SVG Standar followed by these SVG files is fully compatible with any other software designed to work with these type of files.

### Canvas and Viewport
All information about the SVG canvas and viewport are inside the root tag (`<svg>`) of each SVG file. This tag always appears on every SVG file of the `.notebook` as the root tag, as it is the tag that defines that this XML tree is an SVG.

The information inside the `<svg>` tag, when directly extracted from the `.notebook` file, can be misleading. All SVG files will always have the attributes and values of `width="800"` and `height="600"` regardless of their real width and height. 

The real width and height of the canvas can be calculated from the attribute `canvas_bounds`, which draws a rectangle from the Top Left Corner to the Bottom Right Corner of the real canvas size. And by calculating the difference in width and height of both corners from each other, the real width and the real height can be obtained. This attribute receives 4 parameters for the coordinates of both corners: "`Top X`,`Top Y`,`Bottom X`,`Bottom Y`". The coordinates for the Top corner are always negative.

- **True Width** (TWidth): `Bottom X` - `Top X`
- **True Height** (THeight): `Bottom Y` - `Top Y`
- **Fixed `<svg>` tag**: `<svg width="TWidth" height="THeight" canvas_bounds="[...]" [...] >`

### Content Alignment
All the contents created by the user, such as strokes or inserted images, are grouped under one single group tag (`<g>`), which is the only `<g>` tag that is directly under the root `<svg>` tag. This tag always appears on every SVG file of the `.notebook` with an attribute and value of `class="foreground"`.

When the canvas size is fixed with its real size, all contents are shifted. To fix the aligment, a `transform` attribute with a value of "translate(`X`,`Y`)" must be added to this `<g>` tag. The values for `X` and `Y` are the same values as `Top X` and `Top Y` (from the `canvas_bounds` attribute of the `<svg>` root tag) but multiplied by -1 in order to make these values positive.

- **Horizontal Shift** (HShift): `Top X` * -1
- **Vertical Shift** (VShift): `Top Y` * -1
- **Fixed `<g>` tag**: `<g [...] transform="translate(HShift,VShift)">`

### Page Ordering Logic
All SVG files are located at the root level of the `.notebook`, and follow the same naming scheme: “page`X`.svg”, where the “`X`” stands for the page index, created by adding 1 to the last highest index (starting from 0).

The page order defined by the user does not correspond with the logical order of the indexes of each SVG page. This page order is defined in the file `imsmanifest.xml` inside its tag `<resource identifier="group0_pages">`.