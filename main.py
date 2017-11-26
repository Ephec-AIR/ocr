#!./venv/bin/python

from argparse import ArgumentParser
from sys import argv
from capture import temp_capture
from ocr import get_consumption
from webapi import WebAPI

def main():
    # Define CLI arguments
    parser = ArgumentParser(description="Reads the video stream, process it and post the value to the webapi.")
    parser.add_argument("-f", "--file", action="store", help="File to read image from. If not given, use raspistill to capture a new one using the camera")
    parser.add_argument("-c", "--consumption", action="store", type=int, help="Consumption to post to web api. If not given, read it using a ocr")
    parser.add_argument("-s", "--serial", action="store", help="Serial code used along the POST request. If not given, print on stdout.")
    parser.add_argument("-t", "--token", action="store", help="OCR Secret code used along the POST request. If not given, print on stdout.")

    # Parse the args
    cli = parser.parse_args(argv[1:])

    # Get consumption from CLI or from OCR.
    if cli.consumption is not None:
        consumption = cli.consumption
    elif cli.file is not None:
        consumption = get_consumption(cli.file)
    else:
        with temp_capture() as filepath:
            consumption = get_consumption(filepath)

    # Output consumtion to stdout or to WebAPI
    if cli.serial is None or cli.token is None:
        print(consumption)
    else:
        api = WebAPI(cli.serial, cli.token)
        api.post_consumption(consumption)

if __name__ == "__main__":
    main()
else:
    raise ImportError("This file is not intended to be imported")
