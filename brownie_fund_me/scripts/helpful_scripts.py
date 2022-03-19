from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "ganache-gui"]

DECIMALS = 8 #18
DEFAULT_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    account = get_account()
    print(f"Ths active network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, DEFAULT_PRICE, {"from": account})

    print("Mocks Deployed!")
