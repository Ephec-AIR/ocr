#!./venv/bin/python

import unittest
from json import load as jsonload
from pathlib import Path
from ocr import get_consumption

class Test(unittest.TestMethod):

    with Path("compteurs", "compteurs.json").open("r") as jsonfile:
        meters = jsonload(jsonfile)

    def test_meters(self):
        for img_name, value in meters:
            img_path = str(Path("compteurs", img_name))
            self.assertEqual(get_consumption(img_path), value)

if __name__ == "__main__":
    unittest.main()