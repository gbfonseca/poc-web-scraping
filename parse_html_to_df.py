from bs4 import BeautifulSoup
import pandas as pd


def parse_html_to_df(html_content: str):
    '''Parsing de html para pandas DataFrame'''
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontrar a tabela na página HTML
    table = soup.find("table")

    # Extrair os dados da tabela e armazená-los em listas
    data = []
    header = []
    for row in table.find_all("tr"):
        row_data = []
        for cell in row.find_all(["th", "td"]):
            row_data.append(cell.text.strip())
            if len(header) < len(row_data):
                header.append(cell.text.strip())
        if row_data:
            data.append(row_data)

    # Criar o DataFrame usando as listas de dados e cabeçalho
    del data[0]
    return pd.DataFrame(data, columns=header)
