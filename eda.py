import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv("data/한국가스공사_시간별 공급량_20181231.csv", encoding='euc-kr')

#"연월일","시간","구분","공급량"
a_df = df.loc[df.구분 == 'A']
print(a_df.head())

fig = plt.figure()
ax = plt.axes()

ax.plot(a_df.시간, a_df.공급량)