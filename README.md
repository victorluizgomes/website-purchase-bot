# website-purchase-bot
Bot to buy Xbox Series X from Walmart US 
NOTE: It was made for Nov. 25 restock

## Steps to make sure it works
1. Create an account at Walmart.com, add prefered Address and Payment option there
2. Update EMAIL, PASSWORD, and CVV (Credit card CVV) constants. (Make sure to not post these anywhere)
3. Comment get_xbox_direct_link() and uncomment get_test_url() with some product link to test, it should get all the way to Place Order button but not actually place it. (Make sure you have click_button(PLACE_ORDER) commented out in order_item() when testing)
4. Uncomment get_xbox_direct_link() for the real deal, and uncomment click_button(PLACE_ORDER)
5. It will refresh the page until it finds an Add to Cart button

## Useful links:
Selenium - https://selenium-python.readthedocs.io/
ChromeDriver - https://sites.google.com/a/chromium.org/chromedriver/downloads
