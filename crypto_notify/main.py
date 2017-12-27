from coinbase.wallet.client import Client
import os

cb_client = Client(os.getenv("CB_KEY"), os.getenv("CB_SECRET"))

rates = client.get_exchange_rates(currency='BTC')


if __name__ == "__main__":

    CRYPTO_CURRENCY = os.getenv("CB_CRYPTO_CURRENCY")
    REAL_CURRENCY = os.getenv("CB_REAL_CURRENCY")
    THRESHOLD = os.getenv("CB_DESIRED_RATE")
    ALERT_TO = os.getenv("ALERT_TO")

    exchange_pair = "{}-{}".format(CRYPTO_CURRENCY, REAL_CURRENCY)

    try:
        spot_price = client.get_spot_price(currency_pair=exchange_pair)
        if spot_price <= THRESHOLD:
            notify.send_alert(ALERT_TO, exchange_pair, spot_price)
    except Exception as e:
        print("Looks exchange_pair is invalid.")
