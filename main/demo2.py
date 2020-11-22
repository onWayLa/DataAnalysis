import matplotlib.pyplot as plt
import pandas as pd
import os


def get_analysis_image():
    files = os.listdir(".")
    plt.rcParams['font.family'] = ['Arial Unicode MS']
    plt1 = plt.figure(figsize=(12, 7)).add_subplot(111)
    plt1.set_title("HDP MER @5dBmV")
    plt1.set_xlabel('频率(MHz)')
    plt1.set_ylabel('MER(dB)')

    plt2 = plt.figure(figsize=(12, 7)).add_subplot(111)
    plt2.set_title("HDP Power @5dBmV")
    plt2.set_xlabel('频率(MHz)')
    plt2.set_ylabel('Power(dBmV)')
    df_sum = pd.DataFrame()
    column_names = ["频率"]
    index = 0
    for i in range(len(files)):
        if files[i].endswith('xlsx'):
            power = "信号强度_%d" % (index + 1)
            mer = "误码率_%d" % (index + 1)
            column_names.extend((power, mer))
            df = pd.read_excel(files[i])
            plt1.plot(df['频率'], df['误码率'], label='No.%d' % (index + 1))
            plt2.plot(df['频率'], df['信号强度'], label='No.%d' % (index + 1))

            if df_sum.empty:
                df_sum = df.iloc[:, 3:6]
            else:
                df_sum = df_sum.merge((df.iloc[:, 3:6]), on='频率')
            index += 1
    # print(df_sum.head(5))

    df_sum.columns = column_names
    plt1.legend(loc='lower right')
    plt2.legend(loc='lower right')

    df_sum.to_excel('MER Power@5dBmV.xlsx', 'sheet1')
    plt1.figure.savefig("MER@5dBmV.png")
    plt2.figure.savefig("Power@5dBmV.png")


if __name__ == '__main__':
    get_analysis_image()
