import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2 and sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
else:
    x = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = r["bpi"]["USD"]["rate"].replace(",", "")
    price = float(rate) * x
    print(f"${price:,.4f}")
