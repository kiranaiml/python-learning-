import json
import requests 

class CryptoTerminal:
    def __init__(self):
        self.filename = "my_wallet.json"
        
        try:
            with open(self.filename, "r") as file:
                self.wallet = json.load(file)
        except FileNotFoundError:
            self.wallet = {"bitcoin": 0.5, "ethereum": 2.0}

    def get_live_price(self, coin_id):
        try: 
            response = requests.get(f"https://api.coincap.io/v2/assets/{coin_id}")
            data = response.json() 
        except Exception as e:
            print(f"Warning: Connection Error - {e}")
            return 0
        else:
            price = float(data["data"]["priceUsd"])
            return price

    def buy_coin(self, coin_id, amount):
        if coin_id in self.wallet:
            self.wallet[coin_id] = self.wallet[coin_id] + amount
        else:
            self.wallet[coin_id] = amount
        self.save_wallet()

    def save_wallet(self):
        with open(self.filename, "w") as file:
            json.dump(self.wallet, file)

    def view_dashboard(self):
        print("\n==================================================")
        print("             🌐 LIVE CRYPTO DASHBOARD             ")
        print("==================================================")
        
        for coin_id, amount in self.wallet.items():
            live_price = self.get_live_price(coin_id)
            total_value = amount * live_price
            
            print(f"🪙 {coin_id.upper()}")
            print(f"   Owned:       {amount}")
            print(f"   Live Price: ${live_price:.2f}")
            print(f"   Total Value: ${total_value:.2f}")
            print("--------------------------------------------------")
my_terminal = CryptoTerminal()
my_terminal.buy_coin("dogecoin", 1500)
my_terminal.buy_coin("solana", 5)
my_terminal.view_dashboard()