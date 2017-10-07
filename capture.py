#!./venv/bin/python

def get_consumption():
    """Read the video stream and process it to return the consumption"""
    raise NotImplementedError()

if __name__ == "__main__":
    from argparse import ArgumentParser
    from collections import namedtuple
    from functools import partial
    from json import dumps as json_dumps
    from sys import argv, stdout, version_info
    from requests import post as httppost

    # Patch print function to output to stdout (default is stderr)
    print = partial(print, file=stdout)

    # Define CLI options
    parser = ArgumentParser(description="Reads the video stream, process it and upload the value to our centralized server where it is saved.")
    parser.add_argument("-s", "--serial", action="store", help="OCR serial code. Needed to feed the web api")
    parser.add_argument("-t", "--token", action="store", help="OCR secret token. Needed to feed the web api")
    parser.add_argument("-c", "--consumption", action="store", type=int, help="Use this value instead for the one given by the OCR.")

    # Parse the args
    cli = parser.parse_args(argv[1:])

    if cli.serial and cli.token:
        # Feeds web api
        httppost("https://air.ephec-ti.org/api/v1/",
            headers={
                "content-type": "application/json"
            },
            data=json_dumps({
            "serial": cli.serial,
            "token": cli.token,
            "consumption": cli.consumption if cli.consumption else get_consumption()
        }))

    else:
        # Feeds stdout
        print(get_consumption())
