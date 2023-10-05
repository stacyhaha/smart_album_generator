# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     background_extractor.py
   Author :        
   time：          
   last edit time: 
   Description :   照片背景识别模型
-------------------------------------------------
"""

class BackgroundExtractor:
    def __init__(self):
        return
    
    def predict(self, Input, **kwargs):
        """
        * input: 输入单张图片的路径
        * output: 输出图片的主要颜色
        
        example:
        * input: "images/image1.png"
        * output: "canteen"  # 具体输出形式以模型为准
        https://github.com/CSAILVision/places365
        """
        mock_result = "canteen"
        return mock_result