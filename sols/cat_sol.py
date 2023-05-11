import pandas as pd
import matplotlib.pyplot as plt 
import typing as tp
from matplotlib.axes import Axes
class CatExam:
    def __init__(self, path_to_df: str="cat_exam_data.csv"): # task0
        self.df = pd.read_csv(path_to_df)
        
    def task1(self) -> pd.DataFrame:
        return self.df.head()
    
    def task2(self) -> tp.List[str]:
        data = self.df.isna().sum()
        mask = data != 0
        return list(data[mask].keys())

    def task3(self) -> pd.DataFrame:
        self.df = self.df.dropna()
        return self.df
    
    def task4(self) -> pd.DataFrame:
        return self.df.describe()
    
    def task5(self) -> int:
        return self.df.test_score[self.df.test_score == 100].size
    
    def task6(self) -> pd.DataFrame:
        num_info= self.df[['school', 'number_of_students']].drop_duplicates()

        cnt = self.df[self.df.test_score==100].groupby(by = 'school', as_index = False).count()[['school', 'number_of_students']].rename(columns = {'number_of_students':'cnt_100'})
        return pd.merge(num_info, cnt, on = 'school').sort_values(by = ['cnt_100', 'school'], ascending=False)
        
        
    def task7(self) -> pd.DataFrame:
        data = self.df.groupby(by = 'school', as_index=False).mean().sort_values(['test_score', 'school'], ascending=False)
        return data[0:10]

    def task8(self) -> pd.DataFrame:
        data = self.df.groupby(by = 'school', as_index=False).mean().sort_values(['test_score', 'school'], ascending=True)
        return data[0:10]


    def task9(self) -> Axes:
        self.df[self.df.number_of_students>1000]["test_score"].hist( bins = 10, alpha = 0.5)
        self.df[self.df.number_of_students<=1000]["test_score"].hist( bins = 10, alpha = 0.5)
        plt.ylabel("number_of_students")
        plt.xlabel("test_score")
        plt.title("Big and small schools scores")
        plt.legend(['big', 'small'])
        return plt.gca()
