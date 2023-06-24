import requests
from parse_html_to_df import parse_html_to_df


def simple_scenarium():
    url = "https://fundamentus.com.br/fii_resultado.php"

    headers = {
        'User-Agent': 'My User Agent 1.0'  # This is another valid field
    }
    response = requests.get(url, headers=headers)
    html_content = response.text
    
    df = parse_html_to_df(html_content=html_content)
    
    # Transforma o DataFrame em um arquivo csv
    df.to_csv("simple.csv")
    
    # Imprimir o DataFrame
