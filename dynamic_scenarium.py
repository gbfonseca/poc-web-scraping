from selenium import webdriver
from selenium.webdriver.common.by import By
from parse_html_to_df import parse_html_to_df

uri = "https://fundamentus.com.br/index.php"


def dynamic_scenarium():
    driver = webdriver.Firefox()
    driver.get(uri)
    fii_a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/span/a[2]')
    fii_a.click()

    min_dividend_yield_in_decimal = 0.04
    max_dividend_yield_in_decimal = 0.08

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/span/input[1]').send_keys(min_dividend_yield_in_decimal)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/span/input[2]').send_keys(max_dividend_yield_in_decimal)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/input').click()

    html_content = driver.find_element(By.XPATH, '/html').get_attribute('outerHTML')
    driver.close()
    df = parse_html_to_df(html_content=html_content)
    
    df['Endereço'] = df['Endereço'].replace('', 'Sem endereço cadastrado')

    # Transforma o DataFrame em um arquivo csv
    df.to_csv("complex.csv")
