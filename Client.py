from alpaca.trading.client import TradingClient
from Config import get_settings

class Trading_Account:
    def __init__(self):
        self.account = None

        self.api_key = None
        self.secret_key = None

        self.paper_trading = False

    def login(self, api_key: str, secret_key: str, paper_trading: bool):
        self.api_key = api_key
        self.secret_key = secret_key

        account = TradingClient(api_key = self.api_key, secret_key = self.secret_key, paper = self.paper_trading)
        self.account = account.get_account()

    def get_account(self):
        return self.account

    def get_id(self):
        return self.account.id

    def get_account_number(self):
        return self.account.account_number

    def get_status(self):
        return self.account.status

    def get_crypto_status(self):
        return self.account.crypto_status

    def get_currency(self):
        return self.account.currency

    def get_cash(self):
        return self.account.cash

    def get_portfolio_value(self):
        return self.account.portfolio_value

    # def get_non_marginable_buying_power(self):
    #     return self.non_marginable_buying_power

    def get_accrued_fees(self):
        return self.account.accrued_fees

    def get_pending_transfer_in(self):
        return self.account.pending_transfer_in

    def get_pending_transfer_out(self):
        return self.account.pending_transfer_out

    # def get_pattern_day_traders(self):
    #     return self.account.pattern_day_trader

    def get_trade_suspended_by_user(self):
        return self.account.trade_suspended_by_user

    def get_trading_blocked(self):
        return self.account.trading_blocked

    def get_transfers_blocked(self):
        return self.account.transfers_blocked

    def get_account_blocked(self):
        return self.account.account_blocked

    def get_created_at(self):
        return self.account.created_at

    # def get_shorting_enabled(self):
    #     return self.shorting_enabled

    def get_long_market_value(self):
        return self.account.long_market_value

    def get_short_market_value(self):
        return self.account.short_market_value

    def get_equity(self):
        return self.account.equity

    def get_last_equity(self):
        return self.account.last_equity

    def get_multiplier(self):
        return self.account.multiplier

    def get_buying_power(self):
        return self.account.buying_power

    def get_initial_margin(self):
        return self.account.initial_margin

    def get_maintenance_margin(self):
        return self.account.maintenance_margin

    def get_sma(self):
        return self.account.sma

    def get_daytrade_count(self):
        return self.account.daytrade_count

    def get_last_maintenance_margin(self):
        return self.account.last_maintenance_margin

    def get_daytrading_buying_power(self):
        return self.account.daytrading_buying_power

    def get_regt_buying_power(self):
        return self.account.regt_buying_power

    def print_account(self):
        if not self.account:
            print("Account is uninitialized")
            return
        
        print("id: {}".format(self.get_id()))
        print("account_number: {}".format(self.get_account_number()))
        print("status: {}".format(self.get_status()))
        print("crypto_status: {}".format(self.get_crypto_status()))
        print("currency: {}".format(self.get_currency()))
        print("cash: {}".format(self.get_cash()))
        print("portfolio_value: {}".format(self.get_portfolio_value()))
        # print("non_marginable_buying_power: {}".format(self.get_non_marginable_buying_power()))
        print("accrued_fees: {}".format(self.get_accrued_fees()))
        print("pending_transfer_in: {}".format(self.get_pending_transfer_in()))
        print("pending_transfer_out: {}".format(self.get_pending_transfer_out()))
        # print("pattern_day_trader: {}".format(self.get_pattern_day_trader()))
        print("trade_suspended_by_user: {}".format(self.get_trade_suspended_by_user()))
        print("trading_blocked: {}".format(self.get_trading_blocked()))
        print("transfers_blocked: {}".format(self.get_transfers_blocked()))
        print("account_blocked: {}".format(self.get_account_blocked()))
        print("created_at: {}".format(self.get_created_at()))
        # print("shorting_enabled: {}".format(self.get_shorting_enabled()))
        print("long_market_value: {}".format(self.get_long_market_value()))
        print("short_market_value: {}".format(self.get_short_market_value()))
        print("equity: {}".format(self.get_equity()))
        print("last_equity: {}".format(self.get_last_equity()))
        print("multiplier: {}".format(self.get_multiplier()))
        print("buying_power: {}".format(self.get_buying_power()))
        print("initial_margin: {}".format(self.get_initial_margin()))
        print("maintenance_margin: {}".format(self.get_maintenance_margin()))
        print("sma: {}".format(self.get_sma()))
        print("daytrade_count: {}".format(self.get_daytrade_count()))
        print("last_maintenance_margin: {}".format(self.get_last_maintenance_margin()))
        print("daytrading_buying_power: {}".format(self.get_daytrading_buying_power()))
        print("regt_buying_power: {}".format(self.get_regt_buying_power()))

def main():
    Settings = get_settings()

    Account = Trading_Account()

    Account.login(Settings.api_key, Settings.secret_key, Settings.paper_trading)

    Account.print_account()


main()