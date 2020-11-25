import time
from selenium import webdriver

# Needs to have filled out credit card info and address info in account already
# Update hard coded data bellow (Make sure to not post those anywhere)

XBOX_SERIES_X_URL = 'https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645'

# inputs
SIGN_IN_EMAIL = "/html//input[@id='sign-in-email']"
SIGN_IN_PASSWORD = "/html/body/div[@class='js-content']/div[@class='use-new-orange']/div[@class='checkout-wrapper']/div/div[@class='accordion-inner-wrapper']/div[@class='checkout-accordion']/div[@class='accordion-wrapper responsive-container-full']/div/div/div[@class='CXO_module_container']/div/div//div[@class='CXO_module_body_content']/div[3]/div/div[4]/div[@class='CXO_module_column']/section/div/section/form[@method='post']//div[@class='js-password']/label[@class='form-group']/div[@class='validation-group validation-group-with-label']/div/input[@name='password']"
CVV_INPUT = "/html//input[@id='cvv-confirm']"

# buttons
ADD_TO_CART = "/html//div[@id='add-on-atc-container']/div[1]/section//button[@type='button']//span[@class='spin-button-children']"
CHECK_OUT = "/html//div[@id='cart-root-container-content-skip']//div[@class='cart-content']/div[2]/div/div/div[@class='Cart-PACModal-Body']/div[@class='Grid']//div[@class='cart-pos-main-actions s-margin-top']/div[2]/div/button[1]"
SIGN_IN_BUTTON = "/html/body/div[@class='js-content']/div[@class='use-new-orange']/div[@class='checkout-wrapper']/div//div[@class='accordion']/div/div[@class='CXO_module_container']/div/div//div[@class='CXO_module_body_content']/div[3]/div/div[4]/div[@class='CXO_module_column']/section/div/section/form[@method='post']//button[@type='submit']"
DELIVERY_CONTINUE = "/html/body/div[@class='js-content']/div[@class='use-new-orange']/div[@class='checkout-wrapper']/div[@class='accordion-outer-wrapper']/div[@class='accordion-inner-wrapper']/div[@class='checkout-accordion']//div[@class='accordion']/div/div[1]/div[@class='CXO_module_container']/div[@class='CXO_module_body ResponsiveContainer']/div//div[@class='CXO_fulfillment_continue']/button[@type='button']/span[@class='button-wrapper']"
CONFIRM_DELIVERY_CONTINUE = "/html/body/div[@class='js-content']/div[@class='use-new-orange']/div[@class='checkout-wrapper']/div[@class='accordion-outer-wrapper']/div[@class='accordion-inner-wrapper']/div[@class='checkout-accordion']/div[@class='accordion-wrapper responsive-container-full']/div/div/div[2]/div[@class='CXO_module_container']/div[@class='CXO_module_body ResponsiveContainer']/div//button[@class='button button--primary']/span[@class='button-wrapper']"
REVIEW_YOUR_ORDER = "/html/body/div[@class='js-content']/div[@class='use-new-orange']/div[@class='checkout-wrapper']/div[@class='accordion-outer-wrapper']/div[@class='accordion-inner-wrapper']//div[@class='accordion']/div/div[3]/div[@class='CXO_module_container']/div[@class='CXO_module_body ResponsiveContainer']/div//div[@class='CXO_module_body_content']/div[3]/div[2]/div/button[@type='button']/span/span[.='Review your order']"
PLACE_ORDER = "/html/body/div[@class='js-content']/div[@class='use-new-orange']/div[@class='checkout-wrapper']/div[@class='accordion-outer-wrapper']/div[@class='accordion-inner-wrapper']//div[@class='accordion review']/div[2]/div[1]/div[2]/div/div//form[@name='order']//button[@type='submit']/span[@class='button-wrapper']"

# hard coded data
EMAIL = ""
PASSWORD = ""
CVV = ""

def order_item(driver):
    add_to_cart_refresh(ADD_TO_CART, driver)
    click_button(CHECK_OUT, driver)
    fill_out_form(SIGN_IN_EMAIL, EMAIL, driver)
    fill_out_form(SIGN_IN_PASSWORD, PASSWORD, driver)
    click_button(SIGN_IN_BUTTON, driver)
    click_button(DELIVERY_CONTINUE, driver)
    click_button(CONFIRM_DELIVERY_CONTINUE, driver)
    fill_out_form(CVV_INPUT, CVV, driver)
    click_button(REVIEW_YOUR_ORDER, driver)

    # Remove comment bellow when ready to place order or not testing
    # click_button(PLACE_ORDER, driver)

# this will refresh if the button wasn't found until it's there
def add_to_cart_refresh(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(1)
        driver.refresh()
        add_to_cart_refresh(xpath, driver)

def click_button(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(1)
        click_button(xpath, driver)

def fill_out_form(xpath, data, driver):
    try:
        driver.find_element_by_xpath(xpath).send_keys(data)
        pass
    except Exception:
        time.sleep(1)
        fill_out_form(xpath, data, driver)

# xbox series x link url
def get_xbox_direct_link(driver):
    driver.get(XBOX_SERIES_X_URL)
    print('Accessing URL: ', XBOX_SERIES_X_URL)

# test url for testing it goes through, careful to not actually place order
def get_test_url(driver, url):
    driver.get(url)
    print('Accessing URL: ', url)

# accessing xbox series X from walmart.com @deprecated
def get_xbox_from_homepage(driver):
    driver.get('https://www.walmart.com/') # visit Walmart
    
    search_box = driver.find_element_by_name('query') # Search for Xbox Series X
    search_box.send_keys('Xbox Series X')
    search_box.submit()

    time.sleep(2)
    xbox_link = driver.find_element_by_link_text('XB1 Xbox Series X').click() # Click on first result with title

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    #get_test_url(driver, 'https://www.walmart.com/ip/Assassin-s-Creed-Valhalla-Ubisoft-Xbox-One/171315679'); 
    get_xbox_direct_link(driver)
    order_item(driver)
    print('** Succesfully finished purchase **')
