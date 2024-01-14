from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CookiePlayerBot:
    def __init__(self, browser_setup):
        self.can_afford = False  # Variable if you can afford more of the current upgrades and products.
        self.prod_ids = []  # Current list of Product ID's in the HTML code.
        self.product_cost_ids = []  # List of IDs associated with the cost of the product.
        self.costs = []  # List of the costs of each product.
        self.cookie_amount = 0  # Amount of cookies you have.
        self.driver = browser_setup.driver
        self.cookie = None  # The big cookie you click on for the game.

        self.get_cookie()  # Get the cookie so you can click it.

    def get_product_ids(self):
        # Get product item ids.
        try:
            products = self.driver.find_elements(by=By.CLASS_NAME, value="product.unlocked")
            product_ids = [product.get_attribute("id") for product in products]
            self.prod_ids = [x[-1] for x in product_ids]
        except NoSuchElementException:
            print("No Products")

    def get_costs(self):
        # Get the costs of the current products. Make sure to remove commas.
        self.costs = []
        try:
            self.product_cost_ids = [f"productPrice{cost_id}" for cost_id in self.prod_ids]
            for price in self.product_cost_ids:
                cost_raw = self.driver.find_element(by=By.ID, value=price).text
                if "," in cost_raw:
                    cost_raw = cost_raw.replace(",", "")
                price_of_item = int(cost_raw)
                self.costs.append(price_of_item)
        except NoSuchElementException:
            print("Unable to find price")

    def buy_upgrade(self):
        # Purchase the first upgrade if it exists.
        try:
            upgrade = self.driver.find_element(By.ID, value="upgrade0")
            upgrade.click()
        except NoSuchElementException:
            print("UPGRADE NOT UNLOCKED YET")

    def get_cookie_amount(self):
        # Get your current amount of cookies.
        try:
            # Get the number of cookies you currently have.
            self.cookie_amount = self.driver.find_element(By.ID, value="cookies").text.split(" ")[0]
            if "," in self.cookie_amount:
                self.cookie_amount = self.cookie_amount.replace(',', "")  # Make sure to remove commas.
            self.cookie_amount = int(self.cookie_amount)
        except NoSuchElementException:
            print("Can't get cookie amount.")
            # Dictionary for costs and item.

    def purchase_products(self):
        # Purchase current available product that is the most money that you can afford.
        try:
            cookie_upgrades = {}
            for n in range(len(self.costs)):
                cookie_upgrades[self.costs[n]] = self.product_cost_ids[n]
            cookie_count = self.cookie_amount

            # Dictionary for the ones you can currently afford.
            affordable_upgrades = {}

            # Get ID of highest you can afford
            for cost, current_id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = current_id

            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            # CLick the highest item you can afford
            self.driver.find_element(by=By.ID, value=to_purchase_id.replace("Price", "")).click()
        except ValueError:
            print("Can't Afford anymore.")
            self.can_afford = False

    def click_cookie(self):
        # Click that big cookie
        try:
            self.cookie.click()
        except NoSuchElementException:
            print("CAN'T FIND THE COOKIE")

    def get_cookie(self):
        # Get the big cookie.
        try:
            self.cookie = self.driver.find_element(By.ID, value="bigCookie")
        except NoSuchElementException:
            print("CAN'T FIND THE COOKIE")
            self.cookie = None
