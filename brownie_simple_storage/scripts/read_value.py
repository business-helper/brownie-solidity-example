from brownie import SimpleStorage, accounts, config

def read_contract():
  simple_storage = SimpleStorage[0]
  print(simple_storage.retrieve())
  pass

def main():
  read_contract()