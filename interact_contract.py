from web3 import *
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from eth_account import Account
import time
import json

# 1) Upload the contracts to Remix IDE
# 2) Compile and download the ABIs
# 3) Use ganacho-cli for local debugging and testing

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('http://94.237.52.105:59685'))  # Use the appropriate RPC URL
chainid = w3.net.version
print(f"Chain id: {chainid}")

# Private key and address
private_key = '0x950947268985ab632398f6787ea5921c16b790d467202c41c7298028320eee2e'
account = w3.eth.account.from_key(private_key)

# Recruitment contract details
recruitment_address = '0xa2d962a6D9669660Ff16Eccb77dcd0f88814093e'
sender_address = '0xFa5fA5c5C20C749201eBb15D02a83bDA3853A2Be'
setup_contract = '0xdbCCCD98B94f1Ec695B292a359e5960E70fb4F1d'

# Load contract ABI and address
with open('./recr_abi.json') as f:
    contract_abi = json.load(f)

with open('./setup_abi.json') as f:
    setup_abi = json.load(f)

# Create a contract object
setup_contract = w3.eth.contract(address=setup_contract, abi=setup_abi)
recruitment_contract = w3.eth.contract(address=recruitment_address, abi=contract_abi)

def check_conditions():
    current_block_number = w3.eth.block_number
    current_timestamp = int(time.time())
    print(f"Block number: {current_block_number}")
    print(f"Timestamp: {current_timestamp}")
    # Check conditions
    if current_block_number >= 20 or current_timestamp % 2!= 0:
        print(f"Conditions not met: {current_block_number} and timestamp: {current_timestamp}")
        return False
    else:
        return True

def apply_to_recruitment():
    if not check_conditions():
        return

    # Estimate gas
    nonce = w3.eth.get_transaction_count(account.address)
    gas_price = w3.eth.gas_price
    chain_id = w3.eth.chain_id
    gas_limit = 55000

    #tx = recruitment_contract.functions.application(1337, "BOOM").transact({'to': recruitment_address, 'from': sender_address, 'chainId': 31337, 'nonce': nonce})
    #tx = {
     #   'to': recruitment_address,
      #  'from': account.address,
       # 'data': recruitment_contract.functions.application(1337,"BOOM").build_transaction({'from': account.address})['data'],
        #'gas': gas_limit,
        #'gasPrice': w3.toWei('1', 'gwei'),
        #'nonce': w3.eth.getTransactionCount(account.address),
        #'chainId': w3.eth.chainId
    #}

    tx = recruitment_contract.functions.application(1337, "BOOM").build_transaction({'from': account.address, 'gas': gas_limit, 'gasPrice': gas_price, 'nonce': nonce, 'chainId': chain_id})


    signed_txn = w3.eth.account.sign_transaction(tx, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Wait for the transaction to be mined
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    
    print(f"Is Recruited?: {recruitment_contract.functions.isRecruited(sender_address).call()}")
    print(f"Is Recruited2: {setup_contract.functions.isSolved().call()}")

if __name__ == "__main__":
    apply_to_recruitment()
