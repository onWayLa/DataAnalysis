import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


def get_analysis_image(files_path, current_power):
    files = os.listdir(files_path)
    print(files)
    # 根据当前运行的平台来决定中文显示
    if sys.platform == "win32":
        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.sans-serif'] = ['SimHei']
    else:
        plt.rcParams['font.family'] = ['Arial Unicode MS']
    plt1 = plt.figure(figsize=(12, 7)).add_subplot(111)
    plt1.set_title("HDP MER @%sdBmV" % current_power)
    plt1.set_xlabel('频率(MHz)')
    plt1.set_ylabel('MER(dB)')

    plt2 = plt.figure(figsize=(12, 7)).add_subplot(111)
    plt2.set_title("HDP Power @%sdBmV" % current_power)
    plt2.set_xlabel('频率(MHz)')
    plt2.set_ylabel('Power(dBmV)')
    df_sum = pd.DataFrame()
    column_names = ["频率"]
    index = 0
    for i in range(len(files)):
        if files[i].endswith('xlsx'):
            file_name = files[i].split(".")[0]
            power = "信号强度_%s" % file_name
            mer = "误码率_%s" % file_name
            column_names.extend((power, mer))
            df = pd.read_excel(files_path + "\\" + files[i])
            plt1.plot(df['频率'], df['误码率'], label=file_name)
            plt2.plot(df['频率'], df['信号强度'], label=file_name)
            if df_sum.empty:
                df_sum = df.iloc[:, 3:6]
            else:
                df_sum = df_sum.merge((df.iloc[:, 3:6]), on='频率')
            index += 1

    df_sum.columns = column_names
    plt1.legend(loc='lower right')
    plt2.legend(loc='lower right')
    df_sum.to_excel(files_path + "//汇总数据@%sdBmV.xlsx" % current_power, 'sheet1')
    plt1.figure.savefig(files_path + "//MER@%sdBmV.png" % current_power)
    plt2.figure.savefig(files_path + "//Power@%sdBmV.png" % current_power)


if __name__ == '__main__':
    flag = 1
    while flag:
        path = input("请输入待处理数据存储路径：")
        power = input("请输入当前处理的Power：")
        print("数据处理中...")
        get_analysis_image(path, power)
        print("数据处理完成^_^， 请在%s中查看。" % (path if(path != ".") else "当前目录"))
        go_on = input("是否继续？(Y/N)：")
        if go_on.lower() == "n":
            flag = 0
