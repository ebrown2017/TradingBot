import configparser
from Paths import *

class Account_Settings:
    def __init__(self):
        # Keys
        self.api_key = None
        self.secret_key = None

        # Account Config
        self.paper_trading = None

        # Paths
        self.config_path = "config.ini"

    def set_api_key(self, api_key : str):
        self.api_key = api_key

    def set_secret_key(self, secret_key : str):
        self.secret_key = secret_key

    def set_paper_trading(self, paper_trading : bool):
        self.paper_trading = paper_trading

    def set_config_path(self, config_path : str):
        self.config_path = config_path
    
def get_settings():
    config = configparser.ConfigParser()
    config.read(CONFIG_INI_PATH)

    settings = Account_Settings()

    # Set Keys
    try:
        settings.set_api_key(config.get("Keys", "api_key"))
        settings.set_secret_key(config.get("Keys", "secret_key"))
    except:
        print("Issue parsing in Key settings from config file, check all entries present")
        return

    # Set Account
    try:
        settings.set_paper_trading(config.getboolean("Account", "paper_trading"))
    except:
        print("Issue parsing in Account settings from config file, check all entries present")
        return
    
    # Set Paths
    try:
        settings.set_config_path(config.get("Paths", "config_path"))
    except:
        print("Issue parsing in Paths settings from config file, check all entries present")
        return

    return settings