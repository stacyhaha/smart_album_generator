# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     time_extractor.py
   Author :        
   time：          
   last edit time: 
   Description :   时间识别模型，识别图片的拍摄时间
-------------------------------------------------
"""
import datetime

class TimeExtractor:
    def __init__(self):
        return
    
    def predict(self, Input, **kwargs):
        """
        * input: 输入单张图片的路径
        * output: 输出图片的拍摄时间

        example:
        * input: "images/image1.png"
        * output: "2023-09-07 00:23:00"
        """
        mock_result = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return mock_result