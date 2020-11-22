import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

df = pd.read_csv('../data/temporal.csv')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

format_dict = {'data science': '${0:,.2f}', 'Mes': '{:%m-%Y}', 'machine learning': '{:.2%}'}
df['Mes'] = pd.to_datetime(df['Mes'])
df.head().style.format(format_dict)
format_dict = {'Mes': '{:%m-%Y}'}
df.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color="#ff0000")

# prof = ProfileReport(df)
# prof.to_file(output_file='report.html')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(df['Mes'], df['data science'], label='data science')
plt.plot(df['Mes'], df['machine learning'], label='machine learning')
plt.plot(df['Mes'], df['deep learning'], label='deep learning')
plt.xlabel('Date')
plt.ylabel('Popularity')
# Popularity of AI terms by date
plt.title('Popularity of AI terms by date')
plt.grid(True)
plt.legend()
plt.show()
