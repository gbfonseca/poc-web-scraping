from selenium import webdriver
from selenium.webdriver.common.by import By
from parse_html_to_df import parse_html_to_df

URI = "https://fundamentus.com.br/index.php"


def automated_scenarium():
    '''Cenário automatizado'''
    driver = webdriver.Firefox()
    driver.get(URI)
    fii_a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/span/a[2]')
    fii_a.click()

    min_dividend_yield_in_decimal = 0.04
    max_dividend_yield_in_decimal = 0.08

    min_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/span/input[1]')
    min_input.send_keys(min_dividend_yield_in_decimal)

    max_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/span/input[2]')
    max_input.send_keys(max_dividend_yield_in_decimal)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/input').click()

    html_content = driver.find_element(By.XPATH, '/html').get_attribute('outerHTML')
    driver.close()
    result_df = parse_html_to_df(html_content=html_content)

    result_df['Endereço'] = result_df['Endereço'].replace('', 'Sem endereço cadastrado')

    # Transforma o DataFrame em um arquivo csv
    result_df.to_csv("complex.csv")
    return
