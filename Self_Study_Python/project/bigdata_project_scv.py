# -*- coding: utf-8 -*-
"""bigdata_project_scv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fyy8slLyUvF3wBo0lhNycZH9wCMmb1cD

# Bigdata_Project Team SCV
## 파이썬 빅데이터 분석 프로젝트
### 주제: 서울시 공공자전거 이용 분석

## 모듈 임포트, csv파일 읽기
"""

# Commented out IPython magic to ensure Python compatibility.
# 그래프 한글 폰트

# %matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

!apt-get update -qq
!apt-get install fonts-nanum* -qq

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=path, size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

fm._rebuild()
mpl.rcParams['axes.unicode_minus'] = False

# drive mount

from google.colab import drive
drive.mount('/content/drive')

# colab to pdf install

# !apt-get install texlive texlive-xetex texlive-latex-extra pandoc
# !pip install pypandoc

# colab to pdf code

# !jupyter nbconvert --to PDF '/content/drive/MyDrive/Colab Notebooks/bigdata_project_scv.ipynb'

import plotly as py
import cufflinks as cf
cf.go_offline(connected=True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# resize matplotlib graph
plt.rc('figure', figsize=(20, 6))

# read_csv dep, rent total 2019~2020
dep_total_2019 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/dep_total_year/dep_total_2019.csv')
dep_total_2020 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/dep_total_year/dep_total_2020.csv')
rent_total_2019 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/rent_total_year/rent_total_2019.csv')
rent_total_2020 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/rent_total_year/rent_total_2020.csv')

"""## 그래프 라벨 저장
- gu_list: 자치구 시리즈(한국어)
- months: 월 리스트(영어)
- months_num: 월 리스트(숫자)
"""

# 라벨 자치구를 시리즈로 저장
gu_list = dep_total_2019['자치구']
# 라벨 월 리스트로 저장
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months_num = [x for x in range(1, 13)]
# color[0] - 2019, color[1] - 2020
color = ['#51c4d3', '#e84545']

"""# 2019 전체 자치구 월별(plot)

## 2019년 전체 자치구 배차, 대여, 이용률 합계 저장
"""

# 2019년 월별 전체 자치구 배차 합계 시리즈
dep_mon_list_19 = dep_total_2019.iloc[:, 1:-1].sum()
# dep_mon_list_19

# 2019년 월별 전체 자치구 대여 합계 시리즈
rent_mon_list_19 = rent_total_2019.iloc[:, 1:-1].sum()
# rent_mon_list_19

# 2019년 월별 전체 자치구 이용률 합계 시리즈
# 총 이용률 = 총 대여수 / 총 배차수
avg_mon_list_19 = round(rent_mon_list_19 / dep_mon_list_19, 2)
# avg_mon_list_19

"""## 2019년 그래프
- 2019년 전체 구 월별 공공자전거 총 배차수
- 2019년 전체 구 월별 공공자전거 총 대여수
- 2019년 전체 구 월별 공공자전거 총 이용률

### 2019년 전체 구 월별 공공자전거 총 배차수
"""

plt.plot(months_num, dep_mon_list_19, label='총 배차수', color=color[0])
plt.xticks(months_num)
plt.legend()
plt.title('2019년 전체 구 월별 공공자전거 총 배차수')
plt.xlabel('월')
plt.ylabel('배차수')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""### 2019년 전체 구 월별 공공자전거 총 대여수"""

plt.plot(months_num, rent_mon_list_19, label='총 대여수', color=color[0])
plt.xticks(months_num)
plt.legend()
plt.title('2019년 전체 구 월별 공공자전거 총 대여수')
plt.xlabel('월')
plt.ylabel('대여수')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""### 2019년 전체 구 월별 공공자전거 총 이용률"""

plt.plot(months_num, avg_mon_list_19, label='총 이용률', color=color[0])
plt.xticks(months_num)
plt.legend()
plt.title('2019년 전체 구 월별 공공자전거 총 이용률')
plt.xlabel('월')
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""# 2020 전체 자치구 월별(plot)

## 2020년 전체 자치구 배차, 대여, 이용률 합계  저장
"""

# 2020년 월별 전체 자치구 배차 합계 시리즈
dep_mon_list_20 = dep_total_2020.iloc[:, 1:-1].sum()
# dep_mon_list_20

# 2020년 월별 전체 자치구 대여 합계 시리즈
rent_mon_list_20 = rent_total_2020.iloc[:, 1:-1].sum()
# rent_mon_list_20

# 2020년 월별 전체 자치구 이용률 합계 시리즈
# 총 이용률 = 총 대여수 / 총 배차수
avg_mon_list_20 = round(rent_mon_list_20 / dep_mon_list_20, 2)
# avg_mon_list_20

"""## 2020년 그래프
- 2020년 전체 구 월별 공공자전거 총 배차수
- 2020년 전체 구 월별 공공자전거 총 대여수
- 2020년 전체 구 월별 공공자전거 총 이용률

### 2020년 전체 구 월별 공공자전거 총 배차수
"""

plt.plot(months_num, dep_mon_list_20, label='총 배차수', color=color[1])
plt.xticks(months_num)
plt.legend()
plt.title('2020년 전체 구 월별 공공자전거 총 배차수')
plt.xlabel('월')
plt.ylabel('배차수')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""### 2020년 전체 구 월별 공공자전거 총 대여수"""

plt.plot(months_num, rent_mon_list_20, label='총 대여수', color=color[1])
plt.xticks(months_num)
plt.legend()
plt.title('2020년 전체 구 월별 공공자전거 총 대여수')
plt.xlabel('월')
plt.ylabel('대여수')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""### 2020년 전체 구 월별 공공자전거 총 이용률"""

plt.plot(months_num, avg_mon_list_20, label='총 이용률', color=color[1])
plt.xticks(months_num)
plt.legend()
plt.title('2020년 전체 구 월별 공공자전거 총 이용률')
plt.xlabel('월')
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""# 2019, 2020 전체 자치구 월별(plot)

## 2019, 2020년도 전체 자치구 월별 비교 그래프
"""

plt.plot(months_num, dep_mon_list_19, marker='o', label='2019', color=color[0])
plt.plot(months_num, dep_mon_list_20, marker='o', label='2020', color=color[1])
# x축 ticks
plt.xticks(months_num)
# 범주
plt.legend()
# 두 영역 사이 채우기
plt.fill_between(months_num[:], dep_mon_list_19, dep_mon_list_20, color='lightgray', alpha=0.5)
# 타이틀
plt.title('2019년 2020년 전체 구 월별 공공자전거 배차수')
# x축 라벨
plt.xlabel('월')
# y축 라벨
plt.ylabel('배차수')
plt.rc('figure', figsize=(20, 6))
plt.show()

plt.plot(months_num, rent_mon_list_19, marker='o', label='2019', color=color[0])
plt.plot(months_num, rent_mon_list_20, marker='o', label='2020', color=color[1])
# x축 ticks
plt.xticks(months_num)
# 범주
plt.legend()
# 두 영역 사이 채우기
plt.fill_between(months_num[:], rent_mon_list_19, rent_mon_list_20, color='lightgray', alpha=0.5)
# 타이틀
plt.title('2019년 2020년 전체 구 월별 공공자전거 대여수')
# x축 라벨
plt.xlabel('월')
# y축 라벨
plt.ylabel('대여수')
plt.rc('figure', figsize=(20, 6))
plt.show()

plt.plot(months_num, avg_mon_list_19, marker='o', label='2019', color=color[0])
plt.plot(months_num, avg_mon_list_20, marker='o', label='2020', color=color[1])
# x축 ticks
plt.xticks(months_num)
# 범주
plt.legend()
# 두 영역 사이 채우기
plt.fill_between(months_num[:], avg_mon_list_19, avg_mon_list_20, color='lightgray', alpha=0.5)
# 타이틀
plt.title('2019년 2020년 전체 구 월별 공공자전거 이용률')
# x축 라벨
plt.xlabel('월')
# y축 라벨
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""# 2019, 2020년도 구별 월평균 이용률(bar)

## 2019년 각 구  연평균 이용률
- 각 구  연평균 이용률 = 각 구 월별 대여수 / 각 구 월별 배차수
"""

# 2019 각 구 월별 이용률 평균
gu_use_mon_19 = pd.concat([gu_list, round(rent_total_2019.iloc[:, 1:-1] / dep_total_2019.iloc[:, 1:-1],2)], axis=1)
# gu_use_mon_19

gu_use_19 = round(gu_use_mon_19.iloc[:].sum(axis=1) / 12, 2)
# gu_use_19

plt.bar(gu_use_mon_19.loc[:]['자치구'], gu_use_19.sort_values(), color=color[0])
plt.xticks(rotation=45)
plt.title('2019년 각 구의 연평균 이용률')
plt.xlabel('자치구')
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""## 2020년 각 구  연평균 이용률"""

# 2020년 각 구 월별 이용률 평균
gu_use_mon_20 = pd.concat([gu_list, round(rent_total_2020.iloc[:, 1:-1] / dep_total_2020.iloc[:, 1:-1],2)], axis=1)
# gu_use_mon_20

gu_use_20 = round(gu_use_mon_20.iloc[:].sum(axis=1) / 12, 2)
# gu_use_20

plt.bar(gu_use_mon_20.loc[:]['자치구'], gu_use_20.sort_values(), color=color[1])
plt.xticks(rotation=45)
plt.title('2020년 각 구의 연평균 이용률')
plt.xlabel('자치구')
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))
plt.show()

"""## 2019, 2020 각 구  연평균 이용률 비교"""

plt.subplot(121)
plt.bar(gu_use_mon_19.loc[:]['자치구'], gu_use_19.sort_values(), color=color[0])
plt.xticks(rotation=45)
plt.title('2019년 각 구의 연평균 이용률')
plt.xlabel('자치구')
plt.ylabel('이용률')

plt.subplot(122)
plt.bar(gu_use_mon_20.loc[:]['자치구'], gu_use_20.sort_values(), color=color[1])
plt.xticks(rotation=45)
plt.title('2020년 각 구의 연평균 이용률')
plt.xlabel('자치구')
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))

plt.show()

"""## 2019, 2020 각 구의 연평균 이용률 스택바, 표준편차"""

gu_std_20 = round(gu_use_mon_20.iloc[:, 1:].std(axis=1) / 12, 2)
 gu_std_19 = round(gu_use_mon_19.iloc[:, 1:].std(axis=1) / 12, 2)

fig, ax = plt.subplots()
plt.bar(gu_use_mon_19.loc[:]['자치구'], gu_use_19, yerr=gu_std_19, label='2019', color=color[0])
# plt.xticks(rotation=45)
# plt.title('2019년 각 구의 연평균 이용률')

plt.bar(gu_use_mon_20.loc[:]['자치구'], gu_use_20, yerr= gu_std_20, bottom=gu_use_19, label='2020', color=color[1])
plt.xticks(rotation=45)
plt.title('2019년 2020년 각 구의 연평균 이용률')
plt.xlabel('자치구')
plt.ylabel('이용률')
plt.rc('figure', figsize=(20, 6))
plt.legend()

plt.show()

"""## 2019대비 2020 연평균 이용률 차이"""

plt.barh(gu_use_mon_20.loc[:]['자치구'], gu_use_20 - gu_use_19, color='#93329e')
plt.title('2019대비 2020 연평균 이용률 차이')
plt.ylabel('자치구')
plt.axvline( color='grey', linewidth=0.4)
plt.xlabel('이용률 차이')
plt.rc('figure', figsize=(4, 8))
fig.tight_layout()
plt.show()

"""# 2019, 2020년도 공공자전거 지도(map)
- 2019 배차수, 대여수
- 2020 배차수, 대여수
"""

import folium
import pandas as pd
import json
import re

geo_json='https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'

# dep_total_2019 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/dep_total_year/dep_total_2019.csv', encoding='cp949', thousands=',')
# dep_total_2020 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/dep_total_year/dep_total_2020.csv', encoding='cp949', thousands=',')
# rent_total_2019 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/rent_total_year/rent_total_2019.csv', encoding='cp949', thousands=',')
# rent_total_2020 = pd.read_csv('/content/drive/MyDrive/bigdata_team3/Source/rent_total_year/rent_total_2020.csv', encoding='cp949', thousands=',')

rent_19=rent_total_2019[['자치구', '총합계']]
rent_19.columns=['name', 'values']
rent_19=rent_19.sort_values(by='name')
rent_19['name'] = rent_19['name'].apply(lambda x: re.compile('[가-힣]+').findall(x)[0])

rent_20=rent_total_2020[['자치구', '총합계']]
rent_20.columns=['name', 'values']
rent_20=rent_20.sort_values(by='name')
rent_20['name'] = rent_20['name'].apply(lambda x: re.compile('[가-힣]+').findall(x)[0])

dep_19=dep_total_2019[['자치구', '총합계']]
dep_19.columns=['name', 'values']
dep_19=dep_19.sort_values(by='name')
dep_19['name'] = dep_19['name'].apply(lambda x: re.compile('[가-힣]+').findall(x)[0])

dep_20=dep_total_2020[['자치구', '총합계']]
dep_20.columns=['name', 'values']
dep_20=dep_20.sort_values(by='name')
dep_20['name'] = dep_20['name'].apply(lambda x: re.compile('[가-힣]+').findall(x)[0])

dif=pd.DataFrame(gu_use_20 - gu_use_19, columns=['차이'])
dif=dif.assign(자치구=list(np.array(gu_use_mon_20.loc[:]['자치구'])))
# dif

from folium.features import DivIcon
from folium import plugins

m3 = folium.Map(
    location=[37.566345, 126.977893],
    tiles='cartodbpositron',
    zoom_start=10
)
dep_m=folium.plugins.DualMap(
    location=[37.566345, 126.977893],
    tiles='cartodbpositron',
    zoom_start=10
)

rent_m=folium.plugins.DualMap(
    location=[37.566345, 126.977893],
    tiles='cartodbpositron',
    zoom_start=10
)

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=dep_19,
    columns=['name','values'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='2019 배차수(좌)'
).add_to(dep_m.m1)

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=dep_20,
    columns=['name','values'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='2020 배차수(우)'
).add_to(dep_m.m2)

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=rent_19,
    columns=['name','values'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='2019 대여수(좌)'
).add_to(rent_m.m1)

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=rent_20,
    columns=['name','values'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='2020 대여수(우)'
).add_to(rent_m.m2)

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=dif,
    columns=['자치구','차이'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='2019대비 2020 연평균 이용률 차이',
    tiles='cartodbpositron'
).add_to(m3)

"""## 2019, 2020 자치구별 연 배차수 총 합계"""

dep_m

"""## 2019, 2020 자치구별 연 대여수 총 합계"""

rent_m

"""## 2019대비 2020 연평균 이용률 차이"""

m3

# !jupyter nbconvert --to PDF '/content/drive/MyDrive/Colab Notebooks/bigdata_project_scv.ipynb'