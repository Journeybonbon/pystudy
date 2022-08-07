import pandas as pd

#파일 읽어오기
temp = pd.read_excel('경로/' + 'babyNamesUS.xlsx', index_col=0)

#성별을 기준으로 이름이 등록된 수를 합하여 나열하는 피벗테이블 생성
name_df = temp.pivot_table(index = 'Name', values = 'Number', columns = 'Sex', aggfunc='sum')

#이름을 사용하는 성비 계산 (RF = Ratio of Femail, RM = Ratio of Male))
name_df['RF'] = name_df['F'] / (name_df['F'] + name_df['M']) *100
name_df['RM'] = name_df['M'] / (name_df['F'] + name_df['M']) *100

#성비를 비교하여 두 값의 차이가 적을수록 성별 구분 없이 사용되는 이름이다. (R = Ratio)
name_df['R'] = abs(name_df['RM'] - name_df['RF'])
name_df = name_df.round(2)

print(name_df.sort_values(by = 'R').head(30))