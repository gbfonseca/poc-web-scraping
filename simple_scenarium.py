import requests
from parse_html_to_df import parse_html_to_df


def simple_scenarium():
    url = "https://fundamentus.com.br/fii_resultado.php"

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
   
    response = requests.get(url, headers=headers)
    
    html_content = response.text
    
    df = parse_html_to_df(html_content=html_content)
   
    # Manipulando para substituir todos endereços vazios para uma inforamção propícia
    df['Endereço'] = df['Endereço'].replace('', 'Sem endereço cadastrado')
    
    # Transforma o DataFrame em um arquivo csv
    df.to_csv("simple.csv")
    
    # Imprimir o DataFrame
    # print(df)
