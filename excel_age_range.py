import pandas as pd
import numpy as np 

def custom_age_groups(age):
    if len(age) > 2:
        age = age[:2]
    age = int(age)
    if 4 <= age <= 6:
        return "4-6 anos"
    elif 7 <= age <= 9:
        return "7-9 anos"
    elif 10 <= age <= 12:
        return "10-12 anos"
    else:
        return "Outro"

def add_day_of_week_columns(df):
    # Add columns for 'Sexta', 'Sabado', and 'Domingo'
    df['Sexta'] = np.nan
    df['Sabado'] = np.nan
    df['Domingo'] = np.nan

    return df


def group_by_custom_age_groups(file_path):
    try:
        df = pd.read_csv(file_path)

        df['Custom Age Group'] = df['Qual a idade da criança? (apenas o número)'].apply(custom_age_groups)

        df = df.rename(columns={'Qual o nome da criança? ': 'Nome'})

        df = add_day_of_week_columns(df)

        grouped_data = df.groupby('Custom Age Group')

        for age_group, group_df in grouped_data:
            file_name = f'./planilhas/criancas_{age_group.replace(" ", "")}.xlsx'

            columns = ["Nome", "Sexta", "Sabado", "Domingo"]

            selected_df = group_df[columns]

            selected_df.to_excel(file_name, index=False)
            # print(f"\n {group_df.shape[0]} crianças na faixa etária de {age_group}:\n")

            # kids = ''
            
            # for index, row in group_df.iterrows():
            #     child_name = row["Qual o nome da criança? "]
            #     if len(kids) > 0:
            #         kids += f', {child_name}'
            #     else:
            #         kids += f'{child_name}'

            # print(kids)
            
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

group_by_custom_age_groups('./source/data.csv')



# import pandas as pd

# def read_csv_with_pandas(file_path):
#     try:
#         df = pd.read_csv(file_path)

#         grouped_data = df.groupby('Qual a idade da criança? ')
#         for age_group, group_df in grouped_data:
#             print(f"\n {group_df.shape[0]} criança(s) de {age_group} anos:\n")

#             for index, row in group_df.iterrows():
#                 kids = ''

#                 child_name = row["Qual o nome da criança? "]
#                 if len(kids) > 0:
#                     kids += child_name
#                 else:
#                     kids += f', {child_name}'
#                 print(child_name)
        
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# read_csv_with_pandas('./inscricoes_1.csv')

