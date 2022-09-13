"""Until now:

inputting a negative percetage when you want the price to go up will
convert the negative to positive using absolute value.


input 'fast' to deposit some money quickly

input 'test' to buy some shares and then test it be playing around with price manipulation


average price when you 'view returns' (enter 'v') is still in development (should work most of the time but still not ready)


"""
import random


class stock:
    balance = 0
    cash = 0
    instances = {} # dictionrary style: {"name_of_stock": "instance (self var)"}

    def __init__(self, name, price, market_cap): # all 'stocks' will be initiated here. to add new ones, simply create a new object of the 'stock'
        self.name = name
        self.price = price
        self.market_cap = market_cap * 1000000000
        self.shares = 0
        __class__.instances[self.name] = self  # setting a dictionary that includes the objects that were initialized
        self.total_money_invested = 0

    @property
    def shares_outstanding(self):
        num_shares = self.market_cap / self.price
        return f"Current number of {self.name} shares is {num_shares}"

    def buy(self, amt_shares):
        price = self.price * amt_shares

        price = round(price, 2)
        if amt_shares < 0:
            print(f"Nice try! You cannot buy a negative amount of shares! Your input was {amt_shares}")

        elif amt_shares == 0:
            raise ValueError(
                f"Increase the amount of shares that you would like to purchase!\n\nYou tried to purchase {amt_shares} of {self.name}")
        elif stock.balance < price:
            print(f"insufficient funds!\n\nYou tried to purchase ${price} worth of {self.name} stock but you "
                  f"currently hold ${stock.balance}")
        else:
            self.total_money_invested += price  # check for later
            stock.balance -= price
            self.round_balance()
            self.shares += amt_shares
            print(
                f"Congrats! You have just bought ${price} worth of {self.name} stock for a total of {amt_shares} shares. You currently own {self.shares} shares")

    def all_in_buy(self):
        if stock.balance == 0:
            print(
                f"You must have cash in order to use all of it to buy shares of ${self.name}. Deposit some funds!\nCurrent balance: ${stock.balance}")

        else:
            amt_shares = stock.balance / self.price
            self.total_money_invested += stock.balance  # check for later
            self.shares += amt_shares
            stock.balance = 0
            print(f"You have just bought {amt_shares} shares of {self.name} at ${self.price}")

    def buy_in_dollars(self, dollars):
        if dollars < 0:
            print(f"There is no such thing as having ${dollars}!")
        elif dollars == 0:
            raise ValueError("You cannot buy with $0.0 dollars!")
        elif dollars > stock.balance:
            print(
                f"Insufficient funds! You tried to purchase ${dollars} of {self.name} but you only have ${stock.balance} in your account. Deposit more funds to buy.")
        else:
            amt_shares = dollars / self.price
            self.total_money_invested += dollars  # check for later
            self.shares += amt_shares
            stock.balance -= dollars
            self.round_balance()
            print(
                f"Congrats! You just bought {amt_shares} shares of {self.name} at ${self.price}. You currently own {self.shares} shares of {self.name} and have ${stock.balance} of cash in your account.")

    def sell(self, amt_shares):
        price = amt_shares * self.price
        price = round(price, 2)
        if amt_shares <= 0:
            print(f"Whoops! You entered an invalid amount of shares! Your input was {amt_shares}")

        elif amt_shares > self.shares:
            print(f"Sorry! You tried to sell {amt_shares} shares but you only own {self.shares}")
        else:
            self.shares -= amt_shares
            stock.balance += price
            self.total_money_invested -= price  # check for later
            self.round_balance()
            print(f"Success! You have sold {amt_shares} shares of {self.name} stock for a total of ${price}. You "
                  f"currently own {self.shares} shares of {self.name}")

    def sell_all(self):
        if self.shares > 0:
            price = self.price * self.shares
            self.total_money_invested -= price  # check for later
            og_amt = self.shares
            stock.balance += price
            self.shares -= self.shares
            print(
                f"You have sold all of your {self.name} holdings! Sold {og_amt} shares for ${price}. You currently have {self.shares} shares of {self.name}")
        else:
            print(f"You do not own any shares of {self.name}!")

    def sell_in_dollars(self, dollars):
        current_shares_in_dollars = self.shares * self.price
        shares_to_sell = dollars / self.price
        if dollars <= 0:
            print(
                f"You cannot sell shares in the amount of dollars that you provided! Your dollar amount was ${dollars} ")


        elif dollars > current_shares_in_dollars:
            print(
                f"Sorry! You do not own enough {self.name} stock to sell ${dollars} worth of them. You currently own ${current_shares_in_dollars} worth of {self.name} stock for a total of {self.shares}.")
        else:
            money_earned_selling = shares_to_sell * self.price
            self.shares -= shares_to_sell
            self.total_money_invested -= dollars  # check for later
            stock.balance += money_earned_selling
            self.round_balance()
            print(f"Woohoo! You just sold {shares_to_sell} shares of {self.name} priced at ${self.price}. Your sale "
                  f"was worth ${money_earned_selling} and your current cash position is ${stock.balance}. You "
                  f"currently own {self.shares} shares of {self.name}.")

    def deposit(self, amt):

        if amt > 0:
            stock.balance += amt
            stock.cash += amt

            print(f"You successfully deposited ${amt}! Current balance is: ${stock.balance}")

        else:
            print(f"Oh No! Your deposit value is not supported. Your value was {amt}")
            return stock.balance

    def withdraw(self, amt):
        if amt == 0:
            print(
                f"Invalid withdrawal amount! You tried to withdraw ${amt}. Your balance has remained the same at: ${stock.balance}")

        elif amt <= stock.balance:
            stock.balance -= amt
            self.round_balance()
            stock.cash -= amt
            print(f"You successfully withdrew ${amt}! Current balance is: ${stock.balance}")
            return stock.balance
        else:
            print(
                f"You do not have enough funds!\n\nYou currently have ${stock.balance} and you tried to withdraw ${amt}")

    def withdraw_all(self):
        if stock.balance > 0:
            og_amt = stock.balance
            stock.balance -= stock.balance
            stock.cash -= og_amt
            return f"You withdrew ${og_amt} from your account! You currently have ${stock.balance} in cash."
        else:
            return f"You cannot withdraw any cash from your account because your balance is ${stock.balance}!"

    @property
    def money_in_asset(self):
        return self.price * self.shares

    @property
    def portfolio(self):

        invested = 0
        for x in apple.stocks_owned:
            invested += x.money_in_asset

        portfolio = invested + stock.balance
        return portfolio

    @property
    def stocks_owned(self):

        assets_owned = [stock.instances[x] for x in stock.instances if
                        stock.instances[x].shares != 0]  # x stands for each
        #  equity (or stock) in the dictionary called stock.instances. You own the asset if you have more than 0 shares

        return assets_owned

    @property
    def view_assets(self):
        enter_portal("Investments")
        print(f"Cash:\n${stock.balance}")
        print(f"\nStocks:\n$Ticker\t\tShares\t\tCurrent Price\tMarket Value\tAvg. Price\n")


        for num in range(len(apple.stocks_owned)):
            ticker = apple.stocks_owned[num]
            market_value = ticker.price * ticker.shares
            avg = ticker.total_money_invested / ticker.shares
            print(f"${ticker.name}\t\t{round(ticker.shares, 2)}\t\t${round(ticker.price, 2)}\t\t\t\t${market_value:.2f}\t\t{avg}")
        print(f"\n\nYour portfolio is worth ${self.portfolio} with ${stock.balance} in cash")

    def view_returns(self):
        try:
            change = (self.portfolio / stock.cash)
            if change > 1:
                change = round((100 * change - 100), 2)
                return f"Your portfolio has gone up {change}%! You started with {stock.cash} cash and now you have {self.portfolio} in assets!"
            elif change == 0:
                return f"You have sold all your assets and withdrawn your cash! Portfolio performance cannot be calculated"
            elif change < 1:
                change = round((100 - (change * 100)), 2)
                return f"Your portfolio has gone down {change}% :(   You started with ${stock.cash} cash and now you have ${self.portfolio} in assets! "

            else:
                return f"Portfolio value has remained the same! CHECK FOR BUG. CHANGE VARIBALE IS: {change}"
        except ZeroDivisionError:
            return "Looks like you have not bought anything! Performance is not calculated until you invest!"

    @classmethod
    def round_balance(cls):
        cls.balance = round(cls.balance, 2)

    def change_price(self, percent_change):
        if self.price == 0:
            print(f"It appears that ${self.name} is worthless at ${self.price}\n\n Its price CANNOT be manipulated!")

        elif percent_change == 0:
            print(f"{self.name} has remained at the same price of ${self.price} with a {percent_change}% change")
        elif percent_change < -100:
            print("A stock cannot go DOWN more than 100%!")
            raise ValueError
        elif percent_change == -100:
            self.price *= (100 + percent_change) / 100
            print(f"Oh No! ${self.name} has gone bankrupt! ${self.name} is now worthless at ${self.price}")
        elif percent_change < 0:
            og_change = abs(percent_change)
            percent_change = (100 + percent_change) / 100
            self.price *= percent_change
            print(f"{self.name} has gone down {og_change}%! Current price is: ${self.price}")
            return self.price

        else:
            og_change = percent_change
            percent_change = 1 + (percent_change / 100)
            self.price *= percent_change
            print(f"{self.name} has gone up {og_change}%! Current price is: ${self.price}")
            return self.price

    def __repr__(self):
        return self.name

    def print_instances(self):
        print(stock.instances)

    def display_market(self):
        print("------|_______|------|_______|------|_______|------")
        print("Market is currently open! Prices displayed below:\n")
        for x in stock.instances:
            print(f"{x} -------> ${stock.instances[x].price:.2f}")# change was made here

    def market_rally(self, percentage_up):
        for x in stock.instances:
            stock.instances[x].change_price(percentage_up)

        print(f"A Bull Market has occurred! All stocks are up {percentage_up}%!")

    def bear_market(self, percentage_down):
        if percentage_down > 0:
            percentage_down = -percentage_down

            if percentage_down >= 100:
                print(f"Unrealistic Manipulation! Not all stocks can go down {percentage_down}%!")
                raise ValueError

        for x in stock.instances:
            stock.instances[x].change_price(percentage_down)

        print(f"A Bear Market has occurred! All stocks are down {percentage_down}%!")

    def show_price(self):
        print(f"Current price of ${self.name} is ${self.price}")

    def display_stocks_and_prices(self):
        dash = "-" * 10
        print(f"{dash}Stocks for Trade{dash}\n\n")
        for equity in stock.instances:
            ticker = stock.instances[equity]
            print(f"${ticker.name} <------> {ticker.price}")


# order: stock("name", price, market_cap (in billions) )

apple = stock("APPLE", 182.67, 2984) # initiating stock objects here
amc = stock("AMC", 26.52, 13.36)
baba = stock("BABA", 117.77, 320.12)
gamestop = stock("GME", 140.63, 6.20)
microsoft = stock("MSFT", 333.28, 2503)


def page_separator():
    return "\n----------------------------------\n"


def goodbye():
    print("Here is how you did!\n")
    print(apple.view_returns())
    print("\nProgram has ended.")


def enter_portal(message):
    print(f"---------------{message.upper()}---------------\n")
    print(f"You have entered the {message.title()} portal!\n")


while True:
    print("\n---------------MENU---------------\n")
    print("Press 'e' to BUY or SELL (Enter the market) \nPress 'v' to view your portfolio {assets and cash}")
    print(
        "\nPress 'd' to deposit funds\nPress 'w' to withdraw funds\n\nPress 'm' for market manipulation (change prices)")
    print("\nPress 'x' to exit the simulator")

    inpt = input("Input goes here:").lower()
    if inpt == "e":
        print("---------------MARKET---------------")
        apple.display_market()

        ticker = input("\n\nType ticker to buy or sell said asset:").upper()

        if ticker in stock.instances:
            print(page_separator())
            print("\nYou entered the loop and your input was:", ticker)

            self_variable = stock.instances[ticker]
            print(f"You have selected ${ticker}")
            print(f"Would you like to buy or sell ${ticker}?")
            enter_buy_or_sell = input("Enter 'b' to buy\n\nEnter 's' to sell").lower()

            if enter_buy_or_sell == "b":
                exit_val = 0
                while exit_val == 0:

                    try:
                        print(page_separator())
                        print(
                            f"You have entered the buying portal for ${ticker}\n\n-----Choose your buying method:-----\n")
                        buying_method = input(
                            "Enter 's' to BUY IN SHARES\n\nEnter 'd' to BUY IN DOLLARS\n\nEnter 'a' to "
                            "go ALL IN (use all of your cash to buy as many shares)").lower()
                        print(page_separator())
                        if buying_method == "s":
                            self_variable.show_price()
                            dollars = input(
                                "Enter amount of shares of {ticker} that you would like to purchase\nAmount: ").replace(
                                "$", "")
                            self_variable.buy(
                                float(dollars))
                            exit_val += 1
                        elif buying_method == "d":
                            self_variable.show_price()
                            dollars = input(
                                f"Enter amount of dollars that you would like to purchase of ${ticker} shares\nAmount: $").replace(
                                "$", "")
                            self_variable.buy_in_dollars(float(dollars))
                            exit_val += 1
                        elif buying_method == "a":
                            self_variable.show_price()
                            self_variable.all_in_buy()
                            exit_val += 1

                        else:
                            print(
                                f"Oh No! You entered an option that was not available! Your input was {buying_method}")
                            option = input(
                                f"Enter 'b' to continue in the BUY PORTAL for ${ticker}\nEnter anything else to go back to MENU").lower()
                            if option == "b":
                                pass
                            else:
                                print("\n\nTransferring to MENU...")
                                exit_val += 1
                    except ValueError:
                        print(page_separator())
                        print(f"\nYikes! It looks like you did not enter a valid number!\n")
                        option = input(
                            f"Enter 'b' to continue in the BUY PORTAL for ${ticker}\nEnter anything else to go back to MENU").lower()
                        if option == "b":
                            pass
                        else:
                            print("\n\nTransferring to MENU...")
                            exit_val += 1

            elif enter_buy_or_sell == "s":
                self_var = stock.instances[ticker]
                if self_var in apple.stocks_owned:

                    exit__ = 0
                    while exit__ == 0:
                        enter_portal("Sell")
                        print("Choose sellling method:")
                        sell_method = input(
                            "\nEnter 's' to sell in SHARES\n\nEnter 'd' to sell in DOLLARS\n\nEnter 'a' to sell ALL "
                            "of your shares")
                        try:
                            if sell_method == "s":
                                self_var.show_price()
                                self_var.sell(
                                    float(input(
                                        f"\nEnter amount of shares that you would like to sell of ${ticker}\nAmount of shares: ")))

                            elif sell_method == "d":
                                self_var.show_price()
                                self_var.sell_in_dollars(
                                    float(input(
                                        f"\nEnter amount of DOLLARS that you would like to sell of ${ticker}\nAmount: $")))

                            elif sell_method == "a":
                                self_var.show_price()
                                self_var.sell_all()

                            else:
                                print(f"\nYour input was invalid! Input was: {sell_method}")
                            exit__ += 1

                        except ValueError:
                            print(f"\n\nYour input was invalid! Input was: {sell_method}\nEnter 'x' to go back to "
                                  f"MENU.\nEnter ANY OTHER KEY to continue in ${ticker} SELL PORTAL")
                            option = input().lower()
                            if option == "x":
                                exit__ += 1
                            else:
                                print(page_separator())
                                pass






                else:
                    print(f"You do not own any shares of {self_var.name}! You must buy shares before selling")
            elif ticker == "X":
                goodbye()
                break

            else:
                pass

        else:
            print(f"{ticker} is not available in the market")
            print("Will I go back to menu???---------------------------------------452352523626")

    elif inpt == "v" or inpt == "portfolio":
        apple.view_assets

    elif inpt == "test":
        apple.deposit(1000)
        apple.buy(2)
        amc.buy(2)
        microsoft.buy(0.5)




    elif inpt == "d":
        print(page_separator())
        enter_portal("Deposit")
        Star_Value = 0
        while Star_Value == 0:
            try:
                og_amt = stock.balance
                deposit_amt = (input("Enter the amount of dollars that you would like to deposit: \n\n$"))
                deposit_amt = float(deposit_amt)
                apple.deposit(deposit_amt)

                if stock.balance > og_amt:  #  watch out for potential error later on.
                    Star_Value += 1
                    print(page_separator())

                else:
                    if deposit_amt == 0:
                        print(f"\n\nGoing back to menu...")
                        Star_Value += 1

                    else:
                        print("Please Try again.\n\n")



            except ValueError:
                print(page_separator())
                print("Whoops it looks like you did not enter a number! Your input was: ", deposit_amt)
                exit_or_continue = input(
                    "\n\nEnter 'x' if you would like to go back to menu.\n\nEnter ANY KEY to continue in deposit portal.").lower()

                if exit_or_continue == "x":
                    Star_Value += 1
                    print("\n\nExiting Deposit Portal...")
                    print(page_separator())

                else:
                    print(page_separator())
                    print("Transferring Back to Deposit Portal...\n")

    elif inpt == "w":
        if stock.balance == 0:
            print(f"\n\nYou CANNOT ENTER the withdrawal portal if you have a balance of ${stock.balance}\n")
            print("Deposit some funds to your account!")


        else:
            print(page_separator())
            enter_portal("Withdrawal")
            exit_withdrawal = 0
            while exit_withdrawal == 0:

                try:
                    print(f"Current account balance is: ${stock.balance}\n")
                    withdrawal_amt = input("Enter the amount of dollars that you would like to withdraw: \n\n$").lower()
                    withdrawal_amt = abs(float(withdrawal_amt))

                    compare_var = stock.balance

                    apple.withdraw(withdrawal_amt)

                    if stock.balance < compare_var:
                        exit_withdrawal += 1

                    elif withdrawal_amt == 0:
                        print(
                            f"\n\nInvalid Amount! You tried to withdraw ${withdrawal_amt} from you "
                            f"account.\n\nTransferring to MENU...")
                        exit_withdrawal += 1

                except ValueError:
                    if withdrawal_amt == "all":
                        print(apple.withdraw_all())
                        exit_withdrawal += 1

                    else:
                        print(page_separator())
                        print(f"Oh No! It looks you did not enter a number! Your input was: {withdrawal_amt}")

                        exit_ = input(
                            "\n\nEnter 'x' to go back to MENU.\n\nEnter ANY KEY to continue in withdrawal portal.").lower()

                        if exit_ == "x":
                            print("Exiting Withdrawal Portal...\n\n")
                            print(page_separator())
                            exit_withdrawal += 1
                        else:
                            print(page_separator())
                            print("\n\n Continuing in Withdrawal Portal...")



    elif inpt == "m":

        exit_manipulation = 0
        while exit_manipulation == 0:
            enter_portal("Market Manipulation")
            print("Below are the current prices of the respective equities!")
            apple.display_stocks_and_prices()
            enter_market_or_ticker = input(
                "\nEnter 'i' to manipulate the price of an INDIVIDUAL STOCK\n\nEnter'm' to manipulate the price of the ENTIRE MARKET\n").lower()

            if enter_market_or_ticker == "i":
                print(page_separator())
                ticker_string = input(
                    "Enter the ticker symbol for the stock that you would like to manipulate!\n$").upper()
                try:
                    if ticker_string in stock.instances:
                        enter_portal(f"{ticker_string} price manipulation")
                        self_var2 = stock.instances[ticker_string]
                        print(
                            f"If you want {ticker_string} to go down, just type a NEGATIVE PERCENTAGE\n\nIf you want it to go up, just type a POSITIVE PERCENTAGE\n")

                        percent_change = input(
                            f"Enter the percent change for {ticker_string}\nPercent Change:").replace("%",
                                                                                                      "")
                        self_var2.change_price(float(percent_change))
                        exit_manipulation += 1

                    else:
                        print(
                            f"It looks like {ticker_string} is not currently trading in the market. Try trading supported assets!")

                except ValueError:
                    print(page_separator())
                    print(f"You entered an invalid percentage! Your input was: {percent_change}")
                    leave_manipulation = input(
                        "\nEnter 'm' to continue in Market Manipulation Portal\nEnter ANY OTHER KEY to go back to MENU\n").lower()

                    if leave_manipulation == "m":
                        pass
                    else:
                        print("Transferring back to MENU...")
                        exit_manipulation += 1
            elif enter_market_or_ticker == "m":
                try:
                    enter_portal("Market-WIDE Manipulation")
                    apple.display_stocks_and_prices()

                    bull_or_bear = input(
                        "\nEnter 'bull' or 'up' to enter a BULL Market (all stock prices go up)\nEnter 'bear' or 'down' to enter a BEAR MARKET (all stock prices go down)\nEnter 'r' to generate a RANDOM outcome\n").lower()
                    if bull_or_bear == "bull" or bull_or_bear == "up":
                        percent_up = input(
                            "\nEnter the percentage that you would like all stock prices to RISE BY:\n").replace("%",
                                                                                                                 "")
                        percent_up = float(percent_up)
                        if percent_up < 0:
                            percent_up = -percent_up
                        apple.market_rally(percent_up)
                        exit_manipulation += 1

                    elif bull_or_bear == "bear" or bull_or_bear == "down":
                        percent_down = input(
                            "Enter the percentage that you would like all stock prices to DECREASE BY:\n")
                        percent_down = float(percent_down)
                        if percent_down > 0:
                            percent_down = -percent_down
                        apple.bear_market(percent_down)
                        exit_manipulation += 1

                    elif bull_or_bear == "r" or bull_or_bear == "random":
                        randomized = random.randint(-85, 85)
                        leave_loop = 0
                        while leave_loop == 0:

                            if randomized > 0:
                                apple.market_rally(randomized)
                                leave_loop += 1
                                exit_manipulation += 1
                            elif randomized < 0:
                                apple.bear_market(randomized)
                                leave_loop += 1
                                exit_manipulation += 1
                            else:
                                randomized = random.randint(-85, 85)

                    else:
                        print(f"It appears that your input was not an option! Your input was: {bull_or_bear}\n")
                        menu_or_mm = input("Enter 'm' to continue in MARKET MANIPULATION PORTAL\n\nEnter ANY OTHER "
                                           "KEY to transfer to MENU").lower()
                        if menu_or_mm == "m":
                            pass
                        else:
                            print("Transferring to MENU...")
                            exit_manipulation += 1
                except ValueError:
                    print(page_separator())
                    print("You provided an invalid input!")

                    menu_or_continue = input(
                        "Enter 'm' to continue in MARKET MANIPULATION PORTAL\n\nEnter ANY OTHER KEY to transfer to MENU").lower()

                    if menu_or_continue == "m":
                        pass
                    else:
                        print("Transferring to MENU...")
                        exit_manipulation += 1

            else:
                print("It seems like your input was not an option!\nTransferring back to MENU...")
                exit_manipulation += 1



    elif inpt == "x":
        print(page_separator())
        goodbye()
        break
    elif inpt == "fast":
        apple.deposit(100000)
    else:
        print(page_separator())
        print("\nYour input was not part of the options! Your input was", inpt, "\n")
        print(page_separator())
