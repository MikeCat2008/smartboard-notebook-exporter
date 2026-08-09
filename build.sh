#!/bin/bash
pyinstaller --onefile --windowed --collect-all cairosvg --name "sbne-v1.1.0-linux" src/gui.py
