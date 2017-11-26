#!./venv/bin/python

import unittest
from json import load as jsonload
from pathlib import Path
from ocr import get_consumption

class Test(unittest.TestCase):
    def test_meter_01(self):
        img01 = str(Path("compteurs") / "01.jpg")
        self.assertEqual(img01, 23355)

    def test_meter_02(self):
        img01 = str(Path("compteurs") / "02.jpg")
        self.assertEqual(img01, 4998)

    def test_meter_03(self):
        img01 = str(Path("compteurs") / "03.jpg")
        self.assertEqual(img01, 1)

    def test_meter_04(self):
        img01 = str(Path("compteurs") / "04.jpg")
        self.assertEqual(img01, 18364)

    def test_meter_05(self):
        img01 = str(Path("compteurs") / "05.jpg")
        self.assertEqual(img01, 1820)

    def test_meter_06(self):
        img01 = str(Path("compteurs") / "06.jpg")
        self.assertEqual(img01, 27)

    def test_meter_07(self):
        img01 = str(Path("compteurs") / "07.jpg")
        self.assertEqual(img01, 72546)

    def test_meter_08(self):
        img01 = str(Path("compteurs") / "08.jpg")
        self.assertEqual(img01, 70843)

    def test_meter_09(self):
        img01 = str(Path("compteurs") / "09.jpg")
        self.assertEqual(img01, 70107.9)

    def test_meter_10(self):
        img01 = str(Path("compteurs") / "10.jpg")
        self.assertEqual(img01, 0.01)

    def test_meter_11(self):
        img01 = str(Path("compteurs") / "11.jpg")
        self.assertEqual(img01, 13131.3)

    def test_meter_12(self):
        img01 = str(Path("compteurs") / "12.jpg")
        self.assertEqual(img01, 85407)


if __name__ == "__main__":
    unittest.main()