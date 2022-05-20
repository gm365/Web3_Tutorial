# Web3 科学家 🧵 演示代码

from web3 import Web3

# Your Infura Project ID
INFURA_SECRET_KEY = '7fe353dd8591489db345b657ebe5c910'


# get w3 endpoint by network name
def get_w3_by_network(network='mainnet'):
    # 接入 Infura 节点
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}'
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3


# bridge eth from rinkeby to arbitrum testnet
def bridge_arbitrum_eth(w3, from_address, private_key, contract_address, amount_in_ether, chainId):
    from_address = Web3.toChecksumAddress(from_address)
    contract_address = Web3.toChecksumAddress(contract_address)

    ABI = '[{"inputs":[{"internalType":"uint256","name":"maxSubmissionCost","type":"uint256"}],"name":"depositEth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"}]'
    
    amount_in_wei = w3.toWei(amount_in_ether, 'ether')
    maxSubmissionCost = int(amount_in_wei * 0.01) # 定义参数值
    nonce = w3.eth.getTransactionCount(from_address)

    params = {
        'chainId': chainId,
        'gas': 250000,
        'nonce': nonce,
        'from': from_address,
        'value': amount_in_wei,
        # 'gasPrice': w3.toWei('5', 'gwei'),
        'maxFeePerGas': w3.toWei(5, 'gwei'),
        'maxPriorityFeePerGas': w3.toWei(5, 'gwei'),
        'chainId': chainId,
    }
    contract = w3.eth.contract(address=contract_address, abi=ABI)

    # 调用合约的 depositEth 函数，参数为 maxSubmissionCost
    func = contract.functions.depositEth(maxSubmissionCost)
    try:
        tx = func.buildTransaction(params)
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
        txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return {'status': 'succeed', 'txn_hash': w3.toHex(txn), 'task': 'Bridge ETH'}
    except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'Bridge ETH'}


def main():

    # 🐳 Task 3: Arbitrum 跨链 ETH

    # 接入 Arbiturm Rinkeby Testnet
    w3 = get_w3_by_network('rinkeby')

    # 测试地址
    from_address = '0x365a800a3c6a6B73B29E052fd4F7e68BFD45A086'

    # 测试私钥， 千万不能泄漏你自己的私钥信息
    private_key = 'e2facfbd1f0736318382d87b81029b05b7650ba17467c844cea5998a40e5bbc2'

    # Arbitrum 测试网跨链桥合约地址
    contract_address = '0x578BAde599406A8fE3d24Fd7f7211c0911F5B29e'

    # 跨链 ETH 金额
    amount_in_ether = 0.088

    # Rinkeby Chain ID
    chainId = 4

    # 查询地址 ETH余额
    balance = w3.eth.get_balance(from_address) / 1e18
    print(f'当前地址余额: {balance = } ETH')

    result = bridge_arbitrum_eth(w3, from_address, private_key, contract_address, amount_in_ether, chainId)
    print(result)



if __name__ == "__main__":
    main()
