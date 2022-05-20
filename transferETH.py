# Web3 科学家 🧵 演示代码

from web3 import Web3

# Your Infura Project ID
INFURA_SECRET_KEY = '7fe353dd8591489db345b657ebe5c910'


# get w3 endpoint by network name
def get_w3_by_network(network='mainnet'):
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}' # 接入 Infura 节点
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3


def transfer_eth(w3,from_address,private_key,target_address,amount,gas_price=5,gas_limit=21000,chainId=4):
    from_address = Web3.toChecksumAddress(from_address)
    target_address = Web3.toChecksumAddress(target_address)
    nonce = w3.eth.getTransactionCount(from_address) # 获取 nonce 值
    params = {
        'from': from_address,
        'nonce': nonce,
        'to': target_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': gas_limit,
        # 'gasPrice': w3.toWei(gas_price, 'gwei'),
        'maxFeePerGas': w3.toWei(gas_price, 'gwei'),
        'maxPriorityFeePerGas': w3.toWei(gas_price, 'gwei'),
        'chainId': chainId,
        
    }
    try:
        signed_tx = w3.eth.account.signTransaction(params, private_key=private_key)
        txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return {'status': 'succeed', 'txn_hash': w3.toHex(txn), 'task': 'Transfer ETH'}
    except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'Transfer ETH'}


def main():

    # 🐳 Task 2: ETH 转账

    # 接入 Rinkeby Testnet
    w3 = get_w3_by_network('rinkeby')

    # 测试地址
    from_address = '0x365a800a3c6a6B73B29E052fd4F7e68BFD45A086'

    # 测试私钥， 千万不能泄漏你自己的私钥信息
    private_key = 'e2facfbd1f0736318382d87b81029b05b7650ba17467c844cea5998a40e5bbc2'

    # 测试转入地址
    target_address = '0x8888a4E88f66f9C9FCE8c25F193617F3a3aB0760'

    # 转账 ETH 金额
    amount = 0.008

    # Rinkeby Chain ID
    chainId = 4

    # 查询地址 ETH余额
    balance = w3.eth.get_balance(from_address) / 1e18
    print(f'当前地址余额: {balance = } ETH')

    result = transfer_eth(w3, from_address, private_key, target_address, amount, chainId=chainId)
    print(result)
    

if __name__ == "__main__":
    main()
