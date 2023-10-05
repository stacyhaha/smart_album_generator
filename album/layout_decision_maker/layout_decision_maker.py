# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     layout_decision_maker.py
   Author :        
   time：          
   last edit time: 
   Description :   遗传算法进行决策
-------------------------------------------------
"""
class LayoutDecisionMaker:
    def __init__(self):
        return
    
    def predict(self, Input, **kwargs):
        """
        * Input: 图片属性信息路径，例如tests/recognition_result.json
        * output: 输出图片所处模版信息
        * description: 遗传算法

        example:
        * input: "tests/recognition_result.json"
        * output: [
           {
              "image": "images/image1.png",
              "template_info": {
                  "template_idx": "A4_1", 
                  "location_idx": 0,
                  "location_left_upper": (0.2, 0.6),
                  "location_right_bottom": (0.2, 0.8)
              }
           }
	]
        """
        mock_results = [
           {
              "image": "images/image1.png",
              "template_info": {
                  "template_idx": "A4_1", 
                  "location_idx": 0,
                  "location_left_upper": (0.2, 0.6),
                  "location_right_bottom": (0.2, 0.8)
              }
           },
           {
              "image": "images/image2.png",
              "template_info": {
                  "template_idx": "A4_1", 
                  "location_idx": 1,
                  "location_left_upper": (0.2, 0.6),
                  "location_right_bottom": (0.2, 0.8)
              }
           },
           {
              "image": "images/image3.png",
              "template_info": {
                  "template_idx": "A4_2", 
                  "location_idx": 0,
                  "location_left_upper": (0.2, 0.6),
                  "location_right_bottom": (0.2, 0.8)
              }
           }
	]
        
        return mock_results