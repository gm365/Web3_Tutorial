# Web3 科学家 🧵 演示代码

from web3 import Web3

# Your Infura Project ID
INFURA_SECRET_KEY = '7fe353dd8591489db345b657ebe5c910'

# get w3 endpoint by network name
def get_w3_by_network(network='mainnet'):
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}' # 接入 Infura 节点
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3


def main():

    # 接入 Web3
    w3 = get_w3_by_network(network='mainnet')

    # 检查接入状态
    print(w3.isConnected())

    # 当前区块高度
    print(w3.eth.block_number)

    # V神 3号钱包地址
    vb = '0x220866b1a2219f40e72f5c628b65d54268ca3a9d'

    # 地址格式转换
    address = Web3.toChecksumAddress(vb)

    # 查询地址 ETH余额
    balance = w3.eth.get_balance(address) / 1e18
    print(f'V神地址余额: {balance = } ETH')

if __name__ == "__main__":
    main()
