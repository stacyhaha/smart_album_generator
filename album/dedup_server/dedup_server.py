# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     dedup_server.py
   Author :        
   time：          
   last edit time: 
   Description :   去重服务
-------------------------------------------------
"""

class DedupServer:
    def __init__(self):
        return
    
    def predict(self, inputs, **kwargs):
        """
        * inputs: 输入所有图片的路径
        * outputs: 输出不重复的图片路径
        * description: 执行dedup服务

        example:
        * inputs: ["images/image1.png", "images/image2.png", "images/image3.png", "images/image4.png", "images/image5.png"]
        * outputs: ["images/image1.png", "images/image2.png", "images/image3.png", "images/image4.png"] 
        """
        mock_result = inputs[:-1]
        return mock_result