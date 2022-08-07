import pandas as pd

temp = pd.read_excel('경로/' + 'exam.xlsx', index_col=0)
extra = pd.read_excel('경로/' + 'exam_extra.xlsx', index_col=0)

total = pd.merge(temp, extra, how = 'outer', left_index= True, right_index=True)

print(total)

# s = sum , n = numbers of grades
s = 0
n = 0

for i in total['국어']:
    if not pd.isna(i):
        s += i
        n += 1

avg = s/n
new2 = total.fillna({'국어':avg})
print(new2)