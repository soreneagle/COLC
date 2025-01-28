delta = float(input("What is the delta (\u0394) of the option? "))
option_price = float(input("What is the current option price? "))
stock_price = float(input("What is the current price of the stock? "))

leverage = round(delta/option_price*stock_price, 2)

print(f"Your current call option leverage is: {leverage}")