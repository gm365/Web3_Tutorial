# Web3 科学家 🧵 演示代码

from web3 import Web3
from web3.middleware import geth_poa_middleware


# Your Infura Project ID
INFURA_SECRET_KEY = '7fe353dd8591489db345b657ebe5c910'


# get w3 endpoint by network name
def get_w3_by_network(network='goerli'):
    # 接入 Infura 节点
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}'
    w3 = Web3(Web3.HTTPProvider(infura_url))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)  # goerli 需要添加这句
    return w3


# bridge eth from goerli to zkSync 2.0 testnet
def bridge_zkSync_eth(w3, from_address, private_key, contract_address, amount_in_ether, chainId):
    from_address = Web3.toChecksumAddress(from_address)
    contract_address = Web3.toChecksumAddress(contract_address)

    # Deposit ETH ABI
    ABI = '[{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"address","name":"_zkSyncAddress","type":"address"},{"internalType":"enum Operations.QueueType","name":"_queueType","type":"uint8"},{"internalType":"enum Operations.OpTree","name":"_opTree","type":"uint8"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"emergencyFreezeDiamond","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

    amount_in_wei = w3.toWei(amount_in_ether, 'ether')
    nonce = w3.eth.getTransactionCount(from_address)

    # goerli链：无须设置 gas, gas price , chainId, 会自动计算并配置为 EIP 1559 类型
    tx_params = {
        'value': amount_in_wei,
        "nonce": nonce,
        # 'gas': 150000,
        # 'gasPrice': w3.toWei(2, 'gwei'),
        # 'maxFeePerGas': w3.toWei(8, 'gwei'),
        # 'maxPriorityFeePerGas': w3.toWei(2, 'gwei'),
        # 'chainId': chainId,
    }

    contract = w3.eth.contract(address=contract_address, abi=ABI)

    try:
        raw_txn = contract.functions.depositETH(amount_in_wei, from_address, 0, 0).buildTransaction(tx_params)
        signed_txn = w3.eth.account.sign_transaction(raw_txn, private_key=private_key)
        txn = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return {'status': 'succeed', 'txn_hash': w3.toHex(txn), 'task': 'zkSync Bridge ETH'}
    except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'zkSync Bridge ETH'}


def main():

    # 🐳 Task 4: zkSync 跨链 ETH

    # 接入 goerli  Testnet
    w3 = get_w3_by_network('goerli')

    # 测试地址
    from_address = '0x365a800a3c6a6B73B29E052fd4F7e68BFD45A086'

    # 测试私钥， 千万不能泄漏你自己的私钥信息
    private_key = 'e2facfbd1f0736318382d87b81029b05b7650ba17467c844cea5998a40e5bbc2'

    # zkSync 测试网跨链桥合约地址
    contract_address = '0x0e9B63A28d26180DBf40E8c579af3aBf98aE05C5'

    # 跨链 ETH 金额
    amount_in_ether = 0.0188

    # goerli Testnet ChainID
    chainId = 5

    # 查询地址 ETH余额
    balance = w3.eth.get_balance(from_address) / 1e18
    print(f'当前地址余额: {balance = } ETH')

    result = bridge_zkSync_eth(w3, from_address, private_key, contract_address, amount_in_ether, chainId)
    print(result)


if __name__ == "__main__":
    main()
