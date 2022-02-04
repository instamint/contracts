from brownie import accounts

def deploy():
    print('it works')

def all_balances():
    decimals = 10 ** 18
    for a in accounts:
        print(a.address,':',a.balance() / decimals,'eth')
