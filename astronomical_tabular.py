# -*- coding: utf-8 -*-
"""Astronomical tabular.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ue60Pb3L9TAbJThF3NG-3gJAxVnHWbMJ
"""

# importing the libraries
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# peek into the data by creating pandas dataframe
star_df=pd.read_csv('https://drive.usercontent.google.com/download?id=1BQVc6MHjQFtDC9iP1isT_K4ojVe_Oil-&authuser=0')
star_df.sample(5)

star_df.info()

# create a directory

folder_name="testnm"
os.makedirs(folder_name,exist_ok=True)
base_dir=f'/content/{folder_name}/'

# bar chart to visualise the count of star type
star_df['Star type'].value_counts().plot(kind="bar")
plt.show()

plt.figure(figsize=(5,5))
plt.style.use("dark_background")
ax = star_df['Star type'].value_counts().plot(kind="bar", color=['red','brown','green','blue','yellow','orange'])
ax.bar_label(ax.containers[0], color='red')
plt.title('Visualise chart by Star type',color="royalblue", weight="bold")
plt.ylabel('# of Stars', color='white' , fontsize=11)
plt.yticks(color='tab:pink')
plt.xticks(ticks=[0,1,2,3,4,5],labels=["Brown","Red","White","Main","Super\nGiants","Hyper\nGiants"],
           rotation=45)
plt.savefig(base_dir+'star_count_using_metaplot.png')
plt.show()

# visualise barchart using Matplot + seaborn
sns.barplot(x=star_df["Star color"].value_counts().index,
            y=star_df["Star color"].value_counts(),
            palette='viridis')
plt.xticks(rotation=10, fontsize=10)
plt.ylabel('Star color', color='orange')
plt.savefig(base_dir+'seaborn-barchart.png')
plt.show()

# Visualise outliers in the data
plt.figure(figsize=(30,8))
plt.style.use('default')
plt.suptitle('Visualizing the outliers in the numeric feature of the Star type',
             color='black', weight='bold', fontsize=20)
for i in range(4):
  plt.subplot(1,4,i+1)
  sns.boxplot(x=star_df['Star type'],y=star_df.iloc[:,i])
  plt.title(star_df.columns[i], color='red')

plt.show()

plt.savefig(base_dir+'boxplot_star_type.png')

# Line plots
colors=['royalblue','lime','pink','grey','orange','yellow']

plt.figure(figsize=(30,8))
plt.suptitle('Visualizing the distribution of numeric feature of the Star type',
             color='black', weight='bold', fontsize=20)
for i in range(4):
  plt.subplot(4,1,i+1)
  plt.plot(star_df.iloc[:,i], color=colors[i])
  plt.title(star_df.columns[i], color='red')

plt.tight_layout()
plt.show()
plt.savefig(base_dir+'line_subplot_star_type.png')

from google.colab import drive
drive.mount('/content/drive')