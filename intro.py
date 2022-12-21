import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


df=pd.read_excel("Canada.xlsx",sheet_name="Canada by Citizenship",skiprows=range(20),skipfooter=2)
# print(df.head())
df["Total"]=df.loc[:,1980:2013].sum(axis=1)
# print(df.head())
# print(df.columns)
df.index=df["OdName"]
# print(df.index)



def doWork(df):
    years=list(map(int,range(1980,2013)))
    df.sort_values(["Total"],ascending=False,inplace=True,axis=0)
    print(df.head())
    df.drop(columns=["Total","Type","Coverage","AREA","AreaName","REG","RegName","DEV","DevName"],inplace=True)
    df_top5=df.head()
    
    # print(df_top5.columns)
    # print(years)
    df_top5=df_top5[years].transpose()
    
    # print(df_top5)
    # displayAreaPlot(df_top=df_top5)
    # displayHistPlot(df=df)
    # displayBarChart(df=df)
    displayPieChart(df=df)
def displayAreaPlot(df_top):
    print(df_top.columns)
    df_top.plot(kind="area")
    plt.title("Imigration trend in the top 5 countries")
    plt.xlabel("Years")
    plt.ylabel("Number of Imigrants")
    plt.show()
def displayHistPlot(df):
    count,bin_edges=np.histogram(df[2013])
    df[2013].plot(kind="hist",xticks=bin_edges)
    plt.title("Histogram immigration from 195 countries to Canada in 2013")
    plt.xlabel("Number of Immigrants")
    plt.ylabel("Number of COuntries")
    plt.show()
def displayBarChart(df):
    print(df.head())
    years=list(map(int, range(1980,2013)))
    df_iceland=df.loc['Iceland',years]
    print(df_iceland.head())
    df_iceland.plot(kind="bar")
    plt.title("Number of Immigrants from Iceland to Canada from 1980 to 2013")
    plt.xlabel("Year")
    plt.ylabel("Number of immigrants")
    plt.show()
def displayPieChart(df):
    # add autopct parameter to add percentages to your pie chart
    # to remove labels from the chart set the labels parameter to none and add plt.legend()
    # to give the pie chart some sort of wedge include the explode paramter
    if "AreaName" in df.columns:
        df.groupby("AreaName") 
    else:
        df.groupby("Areaname") 
    df.plot(kind="pie",figsize=(12,12))
    plt.title("Representation of immigrants to Canada from all continents from 1980 to 2013")
    plt.show()




doWork(df=df)