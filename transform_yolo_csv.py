#%%
import pandas as pd 
import json
import os
import flirimageextractor
import matplotlib.pyplot as plt
from matplotlib import cm
import cv2


class Via2coordinate():
    def __init__(self, csv_path, img_input, img_output):
        self.img_input = img_input

        df = pd.read_csv(csv_path) 
        dfRegion = df[['filename', 'region_shape_attributes']]
        self.separateLoc(dfRegion)

    def separateNP(self, imgPath):     
        """                           
        自訂函數 : 分離原始圖像與溫度影像
        """
        palettes = [cm.gnuplot2]                        # 影像調色板
        flir = flirimageextractor.FlirImageExtractor(palettes=palettes)                        # 熱影像轉換套件
        flir.process_image(imgPath)       
        flirRGB = flir.extract_embedded_image()                                                     # 輸出 RGB
        flirHot = flir.get_thermal_np()                                                             # 輸出熱影像資訊
        
        return flirRGB, flirHot

    def separateLoc(self, dfRegion):
        for i in range(len(dfRegion)): 
            detectDict = json.loads(dfRegion.loc[i,"region_shape_attributes"])
            print(dfRegion.loc[i,"filename"], detectDict['x'], detectDict['y'], detectDict['width'], detectDict['height'])
            
            imgPath = self.img_input + '\\' + dfRegion.loc[i,"filename"]
            flirRGB, flirHot = self.separateNP(imgPath)

            x1 = detectDict['x']
            y1 = detectDict['y'] 

            x2 = x1 + int(detectDict['width'])
            y2 = y1 + int(detectDict['height'])

            print(flirRGB.shape, (x1, y1), (x2, y2))
            
            cv2.rectangle(flirRGB, (x1, y1), (x2, y2), (255, 0, 0), 3, cv2.LINE_AA)
            plt.imshow(flirRGB)
            plt.show()

            # break


if __name__ == '__main__':
    csv_path = r'via_project_2Mar2022_12h48m_csv (2).csv'
    img_input = r'溫度影像_全部'
    img_output = r''
    Via2coordinate(csv_path, img_input, img_output)




 

