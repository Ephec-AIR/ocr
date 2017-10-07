Reads the video stream, process it and upload the value to our centralized server where it is saved.

# Install

## Docker

*Not yet available*

    docker pull Ephec-AIR/ocr:latest


## Standalone

You must have python version >= 3.5, pip and virtualenv installed. (dabian packages: `python3`, `python3-pip`, `python3-virtualenv`)

    git clone https://github.com/Ephec-AIR/ocr && \
    cd ocr && \
    virtualenv -p $(which python3) venv && \
    venv/bin/pip install -r requirements.txt && \
    echo Installation complete ! || \
    echo Installation failed !

# Run

Feeds stdout:

    ./capture.py  # standalone
    docker run Ephec-AIR/ocr:latest  # docker

Feeds the Web API:

    ./capture.py --serial=<ocr_serial> --token=<ocr_token>  # standalone
    docker run Ephec-AIR/ocr:latest --serial=<ocr_serial> --token=<ocr_token>  # docker

*See `--help` for all available options.*

