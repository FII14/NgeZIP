#!/bin/bash
# File untuk mendeskripsi file ngezip

apt-get update
apt-get install python3-pip
pip3 install colorama
base64 -d src/ngezip > src/ngezip.py
rm src/ngezip
chmod +x src/ngezip.py
