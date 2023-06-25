import requests
from parse_html_to_df import parse_html_to_df


def simple_scenarium():
    '''Cenário Simples'''
    url = "https://fundamentus.com.br/fii_resultado.php"

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    response = requests.get(url, headers=headers, timeout=5)
    html_content = response.text
    result_df = parse_html_to_df(html_content=html_content)
    # Manipulando para substituir todos endereços vazios para uma inforamção propícia
    result_df['Endereço'] = result_df['Endereço'].replace('', 'Sem endereço cadastrado')
    # Transforma o DataFrame em um arquivo csv
    result_df.to_csv("simple.csv")
    # Imprimir o DataFrame
    # print(result_df)
    return
