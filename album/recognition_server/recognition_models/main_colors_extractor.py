# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     main_colors_extractor.py
   Author :        
   time：          
   last edit time: 
   Description :   识别图片的主要颜色
-------------------------------------------------
"""

class MainColorsExtractor:
    def __init__(self):
        return
    
    def predict(self, Input, **kwargs):
        """
        * input: 输入单张图片的路径
        * output: 输出图片的主要颜色
        
        example:
        * input: "images/image1.png"
        * output: [
            [(233,3,4), 0.8],
            [(12, 45, 2), 0.1],
            [(87,22, 222), 0.1]
        ]  # list[0]指颜色，list[1]指颜色在图片中的比例
        """
        mock_result = [
            [(233,3,4), 0.8],
            [(12, 45, 2), 0.1],
            [(87,22, 222), 0.1]
        ]
        return mock_result