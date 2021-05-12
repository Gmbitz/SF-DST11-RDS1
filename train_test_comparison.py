import pandas as pd

def check_dfs(df_1, df_2):
    '''
    Данная функция сравнивает между собой два датасета 
    по типам данных признаков и количеству уникальных значений
    '''
    columns_1, columns_2 = list(df_1.columns), list(df_2.columns)
    train_dict, test_dict = {}, {}
    train_dict['train_feats'], test_dict['test_feats'] = columns_1, columns_2
    train_dict['train_types'], test_dict['test_types'] = df_1.dtypes, df_2.dtypes
    train_dict['train_sample'], test_dict['test_sample'] = df_1.loc[10].values, df_2.loc[10].values
    train_dict['nunique_train'], test_dict['nunique_test'] = df_1.nunique().values, df_2.nunique().values

    train_df, test_df = pd.DataFrame.from_dict(train_dict), pd.DataFrame.from_dict(test_dict)
    df_insert = pd.DataFrame(columns=['< - >'])
    check_df = pd.concat([train_df, df_insert, test_df], axis=1)
    check_df.reset_index(inplace=True)
    check_df['< - >'] = '| - |'
    del check_df['index']
    display(check_df)

    temp_dict = {}
    list_1, list_2, list_3, list_4, list_5 = [], [], [], [], []

    for i in range(len(check_df)):
        if str(check_df['train_types'][i]) != str(check_df['test_types'][i]):
            list_1.append(check_df['train_feats'][i])
            list_2.append(check_df['test_feats'][i])
            list_3.append(str(check_df['train_types'][i]) + ' != ' + str(check_df['test_types'][i]))
            list_4.append(i)
        if check_df['nunique_test'][i]>0 and check_df['nunique_train'][i] != check_df['nunique_test'][i]:
            list_5.append(i)
    temp_dict['index'] = list_4
    temp_dict['train_feats'] = list_1
    temp_dict['не совпадают типы'] = list_3
    temp_dict['test_feats'] = list_2
    temp_df = pd.DataFrame.from_dict(temp_dict)
    temp_df.set_index('index', inplace=True)
    print(f'Резюме:\n1. Не совпали типы в:= {len(temp_df)} столбцах\n')
    print(f'2. Уникальные значения различаются в:= {len(list_5)} столбцах {list_5}')
    display(temp_df)

