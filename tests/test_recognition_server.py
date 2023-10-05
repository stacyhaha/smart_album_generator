# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_recognition_server.py
   Author :        
   time：          
   last edit time: 
   Description :   测试图片识别模型
-------------------------------------------------
"""
import os
import json
import unittest
from album.recognition_server.recognition_server import RecognitionServer

class TestRecognitionServer(unittest.TestCase):
    def test_recognition_server(self):
        """
        测试方式：
        终端：
        python3.6 -m unittest tests/test_recognition_server.py
        """
        server = RecognitionServer()
        inputs = {
            "Input": "images/image1.png"
        }
        result = server.predict(**inputs)
        import pprint
        pprint.pprint(result)
        

