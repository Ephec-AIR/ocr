#!./venv/bin/python

from argparse import ArgumentParser
from json import dumps as json_dumps
from requests import post as httppost
from sys import argv


def get_consumption():
    """Read the video stream and process it to return the consumption."""
    raise NotImplementedError()


def send_consumption(serial, token, consumption):
    """
    Feed the web api.
    
    Args:
        serial: OCR public serial
        token: OCR private token
        consumption: Measured consumption
    """
    httppost("https://air.ephec-ti.org/api/v1/",
             headers={
                 "content-type": "application/json"
             },
             data=json_dumps({
                 "serial": serial,
                 "token": token,
                 "consumption": consumption
             }))


if __name__ == "__main__":
    # Define CLI options
    parser = ArgumentParser(description="Reads the video stream, process it and upload the value to our centralized server where it is saved.")
    parser.add_argument("-s", "--serial", action="store", help="OCR serial code. Needed to feed the web api")
    parser.add_argument("-t", "--token", action="store", help="OCR secret token. Needed to feed the web api")
    parser.add_argument("-c", "--consumption", action="store", type=int, help="Use this value instead for the one given by the OCR.")

    # Parse the args
    cli = parser.parse_args(argv[1:])

    if cli.serial and cli.token:
        # Feeds web api
        send_consumption(cli.serial, cli.token, cli.consumption or get_consumption())

    else:
        # Feeds stdout
        print(cli.consumption or get_consumption())
