# Smartboard notebook Exporter
<!-- MikeCat made this :3 --->
Export your Smartboard `.notebook` files locally and however you want (and we support).

> **testing.md**  
> Read this document in: [ENGLISH](testing.md) [ESPAÑOL](testing.es.md)

---

These test files have been created to fullfill two main purposes, check that the exporter works properly and see how the `.notebook` file behaves under different circumstances to be able to understand its internal structure and how it stores data (see [notebook-format.md](notebook-format.md) for more information).

All `.notebook` test files, located inside the [`/tests`](../tests/) directory of this repository, have been created with a "SMART Board MX065 iQ" and exported to and external media with the "Share .notebook" integrated function. The naming scheme is the original one established by the Smartboard.

Each test file has its own `.pdf` respective with the same name, created and exported with the integrated funcion "Share as .pdf". The naming scheme is the original one established by the Smartboard. These files serve as a reference for the page order, and as an exact reference for the `pdf-png-merged` output type of this exporter.

## Main Test File
Includes the majority of the tests inside one file. This file has been used as a reference for the full `.notebook` file tree structure. Not every page has been created after each other, this can lead for some unexpected behaviour.
<!-- i didn't expect to add page 9 and its tests lol -->
- `.notebook`: [01-30-26 11-14-16 AM.notebook](../tests/01-30-26%2011-14-16%20AM.notebook)
<!-- Link with original path cannot be used bc it uses spaces in the link part...: [01-30-26 11-14-16 AM.notebook](../tests/01-30-26 11-14-16 AM.notebook). Spaces inside the path must be replaced with a "%20" -->
- Smartboard's `pdf-png-merged`: [01-30-26 11-14-16 AM.pdf](../tests/01-30-26%2011-14-16%20AM.pdf)
### What it tests
- Canvas size.
- Background with custom colors.
- Background with custom patterns.
- Pen and Highlighter width.
- Pen and Hightlighter defaults colors.
- Pen and Hightlighter layering.
- Formated text Pen behaviour.
- Grouping elements.
- "Send to background" feature.
- "Infinite Cloner" feature.
- Inserting, duplicating and rotating Images.
- Inserting Video-links.
- Whiteboard Widgets.
- Blank page.
- Full `.notebook` internal structure.

## Screenshot Test File
A simple test to see how the Smartboard stores the screenshots with some writting on it.
- `.notebook`: [01-22-26 11-32-29 AM.notebook](../tests/01-22-26%2011-32-29%20AM.notebook)
- Smartboard's `pdf-png-merged`: [01-22-26 11-32-29 AM.pdf](../tests/01-22-26%2011-32-29%20AM.pdf)
### What it tests
- Smartboard screenshoot management.
- Images.
- Locked elements (screenshot image).

## Blank Test File
The most basic whiteboard that can be done. Created by simply opening the whiteboard app.
- `.notebook`: [04-13-26 11-34-53 AM.notebook](../tests/04-13-26%2011-34-53%20AM.notebook)
- Smartboard's `pdf-png-merged`: [04-13-26 11-34-53 AM.pdf](../tests/04-13-26%2011-34-53%20AM.pdf)
### What it tests
- Minimal `.notebook` internal structure.
- Blank page.

## Page Order Test File
Test how the `.svg` files inside the `.notebook` file are named and what metadata is involved for the final output order seen in "Smartboard's `pdf-png-merged`". This test was created after some unexpected behaviour while exporting the main test.
- `.notebook`: [04-13-26 11-19-30 AM.notebook](../tests/04-13-26%2011-19-30%20AM.notebook)
- Smartboard's `pdf-png-merged`: [04-13-26 11-19-30 AM.pdf](../tests/04-13-26%2011-19-30%20AM.pdf)
### What it tests
- Internal page naming (following creation order).
- Metadata for page order.
