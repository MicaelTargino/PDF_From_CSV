import pandas as pd
import numpy as np
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt

def custom_age_groups(age):
    if len(age) > 2:
        age = age[:2]
    age = float(age)
    if 1 <= age <= 3:
        return "1-3 anos (berçário)"
    elif 4 <= age <= 5:
        return "4-5 anos"
    elif 6 <= age <= 7:
        return "6-7 anos"
    elif 8 <= age <= 9:
        return "8-9 anos"
    elif 10 <= age:
        return "10-12 anos"


def export_to_pdf_by_custom_age_groups(file_path):
    try:
        df = pd.read_csv(file_path)

        df['Custom Age Group'] = df['Qual a idade da criança? (apenas o número)'].apply(custom_age_groups)

        df = df.rename(columns={'Qual o nome da criança? ': 'Nome'})


        grouped_data = df.groupby('Custom Age Group')

        # Create a PDF file
        pdf_pages = matplotlib.backends.backend_pdf.PdfPages('./planilhas/nomes_por_faixa_etaria.pdf')

        # Iterate over each group and create a table with a title in the PDF
        for age_group, group_df in grouped_data:
            # Specify the columns you want to include in the table
            selected_columns = ['Nome']

            # Create a new DataFrame with the selected columns
            table_df = group_df[selected_columns]

            plt.figure(figsize=(8, 6))

            # Add a title to the table
            title = f'{age_group}'
            plt.text(0.5, 1.1, title, horizontalalignment='center', fontsize=12, transform=plt.gca().transAxes)

            # Create a table from the DataFrame
            table = plt.table(cellText=table_df.values,
                              colLabels=table_df.columns,
                              cellLoc='center',
                              loc='upper left')
            
            table.scale(1, 1.5)

            # Remove axis
            plt.axis('off')

            plt.tight_layout()

            # Save the table to the PDF
            pdf_pages.savefig(plt.gcf(), bbox_inches='tight')
            plt.clf()

        # Close the PDF file
        pdf_pages.close()

        print("PDF file 'nomes_criancas_output.pdf' exported successfully.")
            
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example: Replace './2.csv' with the path to your CSV file
export_to_pdf_by_custom_age_groups('./source/data.csv')
