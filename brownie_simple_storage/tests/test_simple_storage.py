from brownie import SimpleStorage, accounts

def test_deploy():
  # Arrange
  account = accounts[0]
  # Act
  simple_storage = SimpleStorage.deploy({"from": account})
  starting_value = simple_storage.retrieve()
  expected = 0
  # Assset
  assert starting_value == expected

def test_updating_storage():
  account = accounts[0]
  simple_storage = SimpleStorage.deploy({"from": account})
  expected = 15
  tx = simple_storage.store(expected)
  tx.wait(1)

  assert expected == simple_storage.retrieve()