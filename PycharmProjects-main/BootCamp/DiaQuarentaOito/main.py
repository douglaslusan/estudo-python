from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_drive = r"C:\desenvolvimento\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_drive)

# driver.get('https://www.amazon.com.br/Teclado-para-Logitech-Prodigy-ABNT2/dp/B081P3Z565/ref=asc_df_B081P3Z565/?tag=googleshopp00-20&linkCode=df0&hvadid=379720486248&hvpos=&hvnetw=g&hvrand=9638894189169132171&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1031945&hvtargid=pla-903309823155&psc=1')
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# busca = driver.find_element(By.ID, 'twotabsearchtextbox')
# print(busca.tag_name)
# print(busca.get_attribute('placeholder'))
#
# teclado_imagem = driver.find_element(By.CLASS_NAME, 'imgTagWrapper')
# print(teclado_imagem.size)


driver.get('https://www.python.org/')

# doc_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a') # buscando classe com tag <a>
# print(doc_link.text)

# xpath_copia = driver.find_element(By.XPATH, '//*[@id="container"]/li[2]/ul/li[1]/a')
# print(xpath_copia.text)

links = driver.find_elements(By.CLASS_NAME, 'tier-1')

for link in links:
	print(link.text)

# driver.close() #fecha a aba
driver.quit() # fecha o navegador
