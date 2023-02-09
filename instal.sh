#!/bin/bash
# File untuk menginstal ZIPI otomatis.

apt-get install python3-pip -y
pip3 install colorama
python3 zipi.py
