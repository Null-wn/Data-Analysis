import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#统一格式后
#1一卡通
#1一卡通
df1 = pd.read_excel(r'D:\公开数据集\一卡通\一卡通.xlsx',sheet_name=0)
df1

#2云闪付
df2=pd.read_excel(r'D:\公开数据集\云闪付\云闪付.xlsx',sheet_name=0)
df2

df1[['交易额', '商户名称']] = df2[['商户名称', '交易额']]#调换，使得一卡通和云闪付格式相同

#批量处理表格
#相同日期的整合在一起
for i in range(0,16):
    f+=1
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    x= pd.read_excel(tpath,sheet_name=0)
    a=b
    t=(df2['交易时间'].str.startswith('2022-03-'+str(f)))
    for i in range(b,101838):
        if(t[i]==True):
            b+=1
    t=df2.iloc[a:b,:]
    tpath = os.path.join('D:\\公开数据集\\日期1\\',str(f)+'.xlsx')
    k=pd.concat([x, t])
    k.to_excel(tpath,sheet_name=str(f),index=False)

dfx = pd.read_excel(r'D:\公开数据集\日期\6.xlsx',sheet_name=0)
temp=dfx['商户名称'].value_counts()

for i in range(0,19):
    f+=1
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx = pd.read_excel(tpath,sheet_name=0)
    list=["翔安校区竟丰餐厅一楼","翔安校区丰庭餐厅一楼","竞丰餐厅一楼快餐","丰庭一楼快餐组"]
    t=dfx[dfx['商户名称'].isin(list)]
    tpath = os.path.join('D:\\公开数据集\\日期1\\',str(f)+'.xlsx')
    t.to_excel(tpath,sheet_name=str("一期"),index=False)

#本科生课表
df=pd.read_excel(r'D:\公开数据集\春季学期课程数据_u.xlsx',sheet_name=1)
t=df['排课时间地点1'].str.contains("第3节-第4节")|df['排课时间地点2'].str.contains("第3节-第4节")|df['排课时间地点3'].str.contains("第3节-第4节")

for i in range(0,1053):
    if t[i]==True:
        df.iloc[i:i+1,:].to_csv(r'D:\公开数据集\本科生课程34.csv',index=False,mode='a',header=False)

f=6
for i in range(0,20):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx = pd.read_excel(tpath,sheet_name=0)
    list=["翔安校区竟丰餐厅一楼","竞丰餐厅一楼快餐"]
    t=dfx[dfx['商户名称'].isin(list)]
    tpath = os.path.join('D:\\公开数据集\\地点1期\\',str(f)+'.xlsx')
    t.to_excel(tpath,sheet_name=str("一期"),index=False)

f=6
for i in range(0,20)
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx = pd.read_excel(tpath,sheet_name=0)
    list=["翔安校区丰庭餐厅一楼","丰庭一楼快餐组"]
    t=dfx[dfx['商户名称'].isin(list)]
    tpath = os.path.join('D:\\公开数据集\\地点2期\\',str(f)+'.xlsx')
    t.to_excel(tpath,sheet_name=str("二期"),index=False)

temp=df['院系'].value_counts()

# 统平时和周末吃饭平均人数
# 平时
a = 0
# 周末
b = 0

for f in range(6, 27):
    tpath = os.path.join('D:\\公开数据集\\日期\\', str(f) + '.xlsx')
    dfx = pd.read_excel(tpath, sheet_name=0)
    if (f + 1) % 7 == 0 or (f + 2) % 7 == 0:
        b += dfx.shape[0]
    else:
        a += dfx.shape[0]

#分析周末
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7==0 or (f+2)%7==0:
        total+=dfx.shape[0]
        print(dfx.shape[0])
aver=total/6
aver

#结合院系分析平时
list=["信息学院","医学院","航空航天学院","海洋与地球学院","电子科学与技术学院（国家示范性微电子学院）","环境与生态学院","公共卫生学院","生命科学学院","能源学院","药学院","化学化工学院"]
a,b=0,0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    t=dfx[dfx['单位院系'].isin(list)]
    a+=dfx.shape[0]
    b+=t.shape[0]

list=["信息学院","医学院","航空航天学院","海洋与地球学院","电子科学与技术学院（国家示范性微电子学院）","环境与生态学院","公共卫生学院","生命科学学院","能源学院","药学院","化学化工学院"]
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        t=dfx[dfx['单位院系'].isin(list)]
        total+=t.shape[0]
aver=total/15

list=["信息学院","医学院","航空航天学院","海洋与地球学院","电子科学与技术学院（国家示范性微电子学院）","环境与生态学院","公共卫生学院","生命科学学院","能源学院","药学院","化学化工学院"]
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        t=dfx[dfx['单位院系'].isin(list)]
        total+=t.shape[0]
aver=total/15

#顺路一期食堂
list=["航空航天学院","海洋与地球学院","电子科学与技术学院（国家示范性微电子学院）","环境与生态学院","公共卫生学院","生命科学学院","能源学院","药学院","化学化工学院"]
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        t=dfx[dfx['单位院系'].isin(list)]
        total+=t.shape[0]
aver=total/15
aver


#顺路一期食堂
list=["航空航天学院","海洋与地球学院","电子科学与技术学院（国家示范性微电子学院）","环境与生态学院","公共卫生学院","生命科学学院","能源学院","药学院","化学化工学院"]
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\地点1期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        t=dfx[dfx['单位院系'].isin(list)]
        total+=t.shape[0]
aver=total/15
aver


#顺路二期食堂
list=["信息学院","医学院","航空航天学院","电子科学与技术学院（国家示范性微电子学院）","公共卫生学院"]
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\日期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        t=dfx[dfx['单位院系'].isin(list)]
        total+=t.shape[0]
aver=total/15
aver

#顺路二期食堂
list=["信息学院","医学院","航空航天学院","电子科学与技术学院（国家示范性微电子学院）","公共卫生学院"]
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\地点2期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        t=dfx[dfx['单位院系'].isin(list)]
        total+=t.shape[0]
aver=total/15
aver


#一期平时
num=0
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\地点1期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        num+=dfx.shape[0]
        total+=dfx['交易金额'].sum()
aver=total/num
aver

#一期周末
num=0
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\地点1期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7==0 or (f+2)%7==0:
        num+=dfx.shape[0]
        total+=dfx['交易金额'].sum()
aver=total/num
aver

#二期平时
num=0
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\地点2期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7!=0 and (f+2)%7!=0:
        num+=dfx.shape[0]
        total+=dfx['交易金额'].sum()
aver=total/num
aver

#二期周末
num=0
total=0
for f in range(6,27):
    tpath = os.path.join('D:\\公开数据集\\地点2期\\',str(f)+'.xlsx')
    dfx=pd.read_excel(tpath,sheet_name=0)
    if (f+1)%7==0 or (f+2)%7==0:
        num+=dfx.shape[0]
        total+=dfx['交易金额'].sum()
aver=total/num
aver


#数据中的日期从6号到26号
workday,weekend=0,0
num1,num2=0,0
for f in range(6, 27):
    t_path = os.path.join('D:\数据集\日期', str(f) + '.xlsx')
    t_table = pd.read_excel(t_path, sheet_name=0)
    if (f + 1) % 7 == 0 or (f + 2) % 7 == 0:
        weekend += t_table.shape[0]
        num2+=1
    else:
        workday += t_table.shape[0]
        num1+=1
aver1=workday/num1
aver2=weekend/num2


