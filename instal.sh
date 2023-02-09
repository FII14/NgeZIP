#!/bin/bash
# File untuk menginstal ZIPI otomatis.

apt-get update -y
apt-get install python3-pip -y
apt-get install git -y
git clone https://github.com/FII14/ZIPI
cd ZIPI
pip3 install colorama
python3 zipi.py
