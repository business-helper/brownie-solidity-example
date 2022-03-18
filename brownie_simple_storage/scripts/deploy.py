from brownie import accounts, config
# import os


def deploy_simple_storage():
  # account = accounts[0]
  # print(account)
  # account = accounts.load('my-account')
  # account =  accounts.add(os.getenv("PRIVATE_KEY"))
  account =  accounts.add(config["wallets"]["from_key"])
  print(account)
  pass

def main():
  deploy_simple_storage()
