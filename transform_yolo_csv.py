#%%
import pandas as pd 
import json


class Via2coordinate():
    def __init__(self, csv_path):
        df = pd.read_csv(csv_path) 
        dfRegion = df[['filename', 'region_shape_attributes']]
        self.separateLoc(dfRegion)

    def separateLoc(self, dfRegion):
        for i in range(len(dfRegion)): 
            detectDict = json.loads(dfRegion.loc[i,"region_shape_attributes"])
            print(dfRegion.loc[i,"filename"], detectDict['x'], detectDict['y'], detectDict['width'], detectDict['height'])
            break


if __name__ == '__main__':
    csv_path = r'via_project_2Mar2022_12h48m_csv (2).csv'
    Via2coordinate(csv_path)



 

