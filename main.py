#!./venv/bin/python

from argparse import ArgumentParser
from functools import partial
from sys import argv
from capture import temp_capture
from ocr import get_consumption
from webapi import WebAPI

def main():
    # Define CLI arguments
    parser = ArgumentParser(description="Reads the video stream, process it and post the value to the webapi.")
    parser.add_argument("-f", "--file", action="store", help="File to read image from. If not given, use raspistill to capture a new one using the camera")
    parser.add_argument("-t", "--thresh", action="store", type=int, help="Threshold used in the binarization for the image cleanup")
    parser.add_argument("-c", "--consumption", action="store", type=int, help="Consumption to post to web api. If not given, read it using a ocr")
    parser.add_argument("-s", "--serial", action="store", help="Serial code used along the POST request. If not given, print on stdout.")
    parser.add_argument("-o", "--secret", action="store", help="OCR Secret code used along the POST request. If not given, print on stdout.")

    # Parse the args
    cli = parser.parse_args(argv[1:])

    # If a threshold is set, patch get_consumption 
    if cli.thresh:
        pass
        #get_consumption = partial(get_consumption, threshold=cli.thresh)

    # Get consumption from CLI or from OCR.
    if cli.consumption is not None:
        consumption = cli.consumption
    elif cli.file is not None:
        consumption = get_consumption(cli.file)
    else:
        print("Taking picture...")
        with temp_capture() as filepath:
            print("Analysing...")
            consumption = get_consumption(filepath)
            print("Got %d" % consumption)

    # Output consumtion to stdout or to WebAPI
    if cli.serial is None or cli.secret is None:
        print(consumption)
    else:
        print("Feeding Web API")
        api = WebAPI(cli.serial, cli.secret)
        api.post_consumption(consumption)
        print("Done !")

if __name__ == "__main__":
    main()
else:
    raise ImportError("This file is not intended to be imported")
