from selenium import webdriver
from selenium.webdriver.common.by import By

user = ["axel_villeret@orange.fr", "q*$8enV2oGVHLb"]
code = input("Saisir votre code d'authentification : ")

driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=webdriver.ChromeOptions().add_argument('headless'))
driver.minimize_window()
driver.get("https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

driver.find_element(By.ID, "ap_email").send_keys(user[0])
driver.find_element(By.ID, "continue").click()

driver.find_element(By.ID, "ap_password").send_keys(user[1])
driver.find_element(By.ID, "signInSubmit").click()

driver.find_element(By.NAME, "otpCode").send_keys(code)
driver.find_element(By.ID, "auth-signin-button").click()

while(driver.current_url != "https://www.amazon.fr/ref=nav_signin"):
    code = input("Votre code est invalide, veuillez le resaisir : ")
    driver.find_element(By.NAME, "otpCode").send_keys(code)
    driver.find_element(By.ID, "auth-signin-button").click()

driver.find_element(By.ID, "nav-orders").click()
driver.find_element(By.CLASS_NAME, "your-orders-content-container__content").screenshot("commandes.png")

driver.quit()