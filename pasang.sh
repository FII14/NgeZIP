#!/bin/bash
# File untuk mendeskripsi file ngezip

base64 -d src/ngezip > src/ngezip.py
rm src/ngezip
chmod +x src/ngezip.py
