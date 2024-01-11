import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
from pandas.plotting import table

def export_to_pdf_by_custom_age_groups(file_path, output_pdf_path):
    try:
        df = pd.read_csv(file_path)

        # Rename columns
        df = df.rename(columns={
            'Qual o nome da criança? ': 'Nome',
            "Qual a idade da criança? (apenas o número)": 'Idade',
            'A criança possui algum tipo de alergia?': 'Alergia',
            'Se sim, a que? ': 'Alergia a',
            'A criança possui alguma intolerância alimentar?': 'Intolerancia',
            'Se sim,  a que?': 'Intolerancia a'
        })

        df = df.fillna('-')

        cleaned_df = df[["Nome", "Idade", "Alergia", "Alergia a", "Intolerancia", "Intolerancia a"]]

        df['Nome'] = df['Nome'].str.strip()

        # Filter rows where 'Alergia' or 'Intolerancia' is 'Sim'
        filtered_df = cleaned_df[(cleaned_df['Alergia'] == 'Sim') | (cleaned_df['Intolerancia'] == 'Sim')]

        filtered_df = filtered_df.drop(['Alergia', 'Intolerancia'], axis=1)

        filtered_df = filtered_df[filtered_df['Nome'] != 'Rafael Mousinho']

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(8, 4))

        num_columns = len(filtered_df.columns)

        # Define the column widths
        # Set a smaller width for the 'Idade' column, which is the second column
        column_widths = [0.35] * num_columns
        column_widths[1] = 0.15 
        print(column_widths)
        
        # Create a table plot
        ax.axis('off')
        tbl = table(ax, filtered_df, loc='center', colWidths=column_widths)
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(8)

        # Add a title
        plt.title("Crianças com alergia/Intolerância", fontsize=12)

        # Save the plot as a PDF
        plt.savefig(output_pdf_path, bbox_inches='tight')

        # Show the plot if needed
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
export_to_pdf_by_custom_age_groups('./source/data.csv', './planilhas/criancas_com_alergia.pdf')


# import pandas as pd
# import numpy as np
# import matplotlib.backends.backend_pdf
# import matplotlib.pyplot as plt

# def export_to_pdf_quem_tem_alergia(file_path):
#         df = pd.read_csv(file_path)

#         # Rename columns
#         df = df.rename(columns={
#             'Qual o nome da criança? ': 'Nome',
#             'A criança possui algum tipo de alergia?': 'Alergia',
#             'Se sim, a que? ': 'Alergia a',
#             'A criança possui alguma intolerância alimentar?': 'Intolerancia',
#             'Se sim,  a que?': 'Intolerancia a',
#             "Qual a idade da criança? ": 'Idade'
#         }) 

#         cleaned_df = df[['Nome', 'Alergia', 'Alergia a', 'Intolerancia', 'Intolerancia a', 'Idade']]

#         filtered_df = cleaned_df[(cleaned_df['Alergia'] == 'Sim') | (cleaned_df['Intolerancia'] == 'Sim')]

#         print(filtered_df)

# export_to_pdf_quem_tem_alergia('./source/2.csv')
