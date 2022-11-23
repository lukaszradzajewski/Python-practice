from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/')

# example 1 - placeholder

search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
asd = search_field.get_attribute('placeholder')
print(asd)
if asd != "Search products…":
    raise Exception("Place holder for search field is not as expected.")
else:
    print("PASS")

# example 2 - which tab is selected

my_account = driver.find_element('css selector', 'li.page-item-9')
my_account.click()

nav_items = driver.find_elements('css selector', '.nav-menu li')
for item in nav_items:
    item_class = item.get_attribute('class')
    if 'current_page_item' in item_class:
        print(f"The selected tab is: {item.text}")

# example 3 - get link url

driver.get('http://demostore.supersqa.com/')

product = driver.find_element('css selector', 'li.product a')
product_url = product.get_attribute('href')
print(f'The url for the first product is : {product_url}')
