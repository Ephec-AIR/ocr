#!./venv/bin/python

import unittest
from json import load as jsonload
from pathlib import Path
from ocr import get_consumption
from os import environ
environ["TESSDATA_PREFIX"] = "C:\Program Files (x86)\Tesseract-OCR"

class Test(unittest.TestCase):
##    def test_meter_01(self):
##        imgpath = str(Path("meters") / "01.jpg")
##        self.assertEqual(get_consumption(imgpath), 23355)
##
##    def test_meter_02(self):
##        imgpath = str(Path("meters") / "02.jpg")
##        self.assertEqual(get_consumption(imgpath), 4998)
##
##    def test_meter_03(self):
##        imgpath = str(Path("meters") / "03.jpg")
##        self.assertEqual(get_consumption(imgpath), 1)
##
##    def test_meter_04(self):
##        imgpath = str(Path("meters") / "04.jpg")
##        self.assertEqual(get_consumption(imgpath), 18364)
##
##    def test_meter_05(self):
##        imgpath = str(Path("meters") / "05.jpg")
##        self.assertEqual(get_consumption(imgpath), 1820)
##
##    def test_meter_06(self):
##        imgpath = str(Path("meters") / "06.jpg")
##        self.assertEqual(get_consumption(imgpath), 27)
##
##    def test_meter_07(self):
##        imgpath = str(Path("meters") / "07.jpg")
##        self.assertEqual(get_consumption(imgpath), 72546)
##
##    def test_meter_08(self):
##        imgpath = str(Path("meters") / "08.jpg")
##        self.assertEqual(get_consumption(imgpath), 70843)
##
##    def test_meter_09(self):
##        imgpath = str(Path("meters") / "09.jpg")
##        self.assertEqual(get_consumption(imgpath), 70107.9)
##
##    def test_meter_10(self):
##        imgpath = str(Path("meters") / "10.jpg")
##        self.assertEqual(get_consumption(imgpath), 0.01)
##
##    def test_meter_11(self):
##        imgpath = str(Path("meters") / "11.jpg")
##        self.assertEqual(get_consumption(imgpath), 13131.3)
##
##    def test_meter_12(self):
##        imgpath = str(Path("meters") / "12.jpg")
##        self.assertEqual(get_consumption(imgpath), 85407)
##
##    def test_meter_13(self):
##        imgpath = str(Path("meters") / "13.jpg")
##        self.assertEqual(get_consumption(imgpath), 868531)
##
##    def test_meter_14(self):
##        imgpath = str(Path("meters") / "14.jpg")
##        self.assertEqual(get_consumption(imgpath), 2257)

    def test_meter_15(self):
        imgpath = str(Path("meters") / "15.jpg")
        self.assertEqual(get_consumption(imgpath), 21278)


if __name__ == "__main__":
    unittest.main()
