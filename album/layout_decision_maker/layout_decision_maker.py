# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     layout_decision_maker.py
   Author :  XIANGYI
   time：          
   last edit time: 
   Description :   
-------------------------------------------------
"""

import json 
import logging 
from GA import GA
from template_manager import TemplateManager
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class LayoutDecisionMaker:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.template_manager = TemplateManager(template_dir=template_dir)
    
    def predict(self, recognition_result, **kwargs):
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
        ga = GA(self.template_dir, recognition_result, n_generation=30, pop_size=5)
        align_result = ga.generate()

    
        



if __name__ == "__main__":
    template_dir= "/Users/stacy/iss/smart_album_generator/templates"
    recognition_result="/Users/stacy/iss/smart_album_generator/tests/recognition_result.json"
    layout_decision_maker = LayoutDecisionMaker(template_dir)
    layout_decision_maker.predict(recognition_result)



    