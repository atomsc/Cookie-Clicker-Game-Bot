"""
COOKIE CLICKER BOT
What does this do?
It is a bot that automatically plays "The Cookie Clicker" game for you. It will click faster that a human could click
and then purchases upgrades and products to further your cookies per second and click efficiency. You can adjust the
settings of the game by changing WAIT_TIME_TO_PURCHASE. This variable is in seconds and adjusts how long the cookie
will be clicked until purchases of upgrades and products are made.
You can play this game manually at: https://orteil.dashnet.org/cookieclicker/ .
"""

# IMPORTS
import time
from CookiePlayerBot import CookiePlayerBot
from BrowserSetup import BrowserSetup

# TIME_TO_RUN = 1  # MINUTES - This sets the amount of time to run the whole game.
WAIT_TIME_TO_PURCHASE = 10  # Seconds - Amount of time you will click the cookie until you purchase upgrades.
URL = "https://orteil.dashnet.org/cookieclicker/"  # Cookie Clicker URL


def main():
    # Ask user how long they want to run the game.
    time_to_run = int(input("How many minutes would you like to run the game? "))

    # Convert to seconds for the python package.
    run_time = time.time() + 60 * time_to_run  # 5 minutes

    # Defines the browser setup. This will set up opening and clicking to get into the game.
    browser = BrowserSetup(URL)

    # Define the CookiePlayerBot.
    bot = CookiePlayerBot(browser)

    # Define the initial timeout to purchase.
    timeout = time.time() + WAIT_TIME_TO_PURCHASE

    # Main Loop for clicking the cookie
    while time.time() < run_time:
        bot.click_cookie()
        # Do this every x seconds defined by timeout.
        if time.time() > timeout:
            bot.buy_upgrade()  # Buy the upgrade first because it gets you more cookies per click.
            bot.can_afford = True
            # Loop through the products, purchasing the highest value one, until you are out of cookies.
            while bot.can_afford:
                bot.get_product_ids()  # Get ID's first.
                bot.get_costs()  # Get the costs of those ID's.
                bot.get_cookie_amount()  # Get how many cookies you have.
                bot.purchase_products()  # Purchase product with the highest value.
            timeout = time.time() + WAIT_TIME_TO_PURCHASE


if __name__ == "__main__":
    main()
