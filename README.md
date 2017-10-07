Reads the video stream, process it and upload the value to our centralized server where it is saved.

# Installation

## 1. Using Docker

*Not yet available*

    docker run -e "SERIAL=<the_orc_serial>" -e "TOKEN=<the_ocr_token>" Ephec-AIR/orc:latest

## 2. From source

### 1. Download the app and install its dependancies

You must have python version >= 3.5, pip and virtualenv installed. (dabian packages: `python3`, `python3-pip`, `python3-virtualenv`)

    git clone https://github.com/Ephec-AIR/ocr && \
    cd ocr && \
    virtualenv -p $(which python3) venv && \
    venv/bin/pip install -r requirements.txt && \
    echo Installation complete ! || \
    echo Installation failed !

### 2. Configure the app

By setting values along the CLI (see `./start.py --help` for all available settings)

    ./start.py serial=<the_ocr_serial> token=<the_ocr_token>

By exporting values in the environment variables (the variable is the same as in the config file)

    export SERIAL=<the_ocr_serial>
    export TOKEN=<the_ocr_token>

By editing the config file

    nano config.yml

If the same variable is set at differents place, the CLI is used first then the environ then the config file: `CLI > environ > config file`


### 3. Start the app

    cd ocr && ./start.py

