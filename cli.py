import typer
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

app = typer.Typer()

API_KEY = "2fb5SoewjFlgmDWBtNwR7KN0G8sPFuyiohZfsnaCKig7rsM5EeECsQDTJGtOlXLK"
API_SECRET = "EV9tMre7wSCWTFacByjn3o1CVEmd3aTRezBDPORnblQvU84l1LjJ1HyIv9HXU8fE"

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    
    setup_logging()

    validate_order(symbol, side, order_type, quantity, price)

    client = get_client(API_KEY, API_SECRET)

    print("\nOrder Request")
    print("----------------")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")

    order = place_order(client, symbol, side, order_type, quantity, price)

    print("\nOrder Response")
    print("----------------")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))

    print("\n✅ Order placed successfully!")

if __name__ == "__main__":
    app()