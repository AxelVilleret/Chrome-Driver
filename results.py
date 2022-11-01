from selenium import webdriver
from selenium.webdriver.common.by import By

# creer une variable pour declencher le driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.kubii.fr/")

# recuperer la barre de recherche
search_bar = driver.find_element(By.ID, "search_query_top")
search_bar.send_keys("Rasberry")

# recuperer le bouton pour lancer la recherche
search_btn = driver.find_element(By.NAME, "submit_search")
search_btn.click()

# recuperer tous les noms de produits
all_titles = driver.find_elements(By.CSS_SELECTOR, "h5.product-name")
for e in all_titles:
    print(e.text)
