# Web3_Tutorial

Web3科学家极简入门指南

目标：学习并使用 Web3.py 模块实现链上数据查询、转账、合约交互等简单功能


## 00: 前期准备工作

1. 安装 Python3
2. 安装 web3.py 库 `pip install web3`


## 01: 读取链上信息

* 目标：通过 Infura 接入以太坊主网并查询钱包余额信息
* 代码： https://github.com/gm365/Web3_Tutorial/blob/main/Tutorial.py



## 02: Rinkeby 测试网转账 ETH

* 目标：接入 Rinkeby 测试网并完成一笔转账交易

* 代码: https://github.com/gm365/Web3_Tutorial/blob/main/transferETH.py

* 测试地址：0x365a800a3c6a6B73B29E052fd4F7e68BFD45A086
* 测试私钥：e2facfbd1f0736318382d87b81029b05b7650ba17467c844cea5998a40e5bbc2

* 转账 Hash：0x70a71693e5f6158788847de8c56ab18479c47c1524c2970c2890175fb33adb58
* 区块链浏览器结果查询：https://rinkeby.etherscan.io/address/0x365a800a3c6a6B73B29E052fd4F7e68BFD45A086


## 03: Arbitrum 测试网跨链桥交互

* 目标： 完成 Arbitrum 测试网的跨链桥存入 ETH 的交互

* 代码： https://github.com/gm365/Web3_Tutorial/blob/main/ArbitrumBridge.py
* 交互记录 Hash： https://rinkeby.etherscan.io/tx/0x417f85a41d70ee619d9ff2c17051ed8ac56205e1ac232dd10966cd4b8dccdb43


## 04: zkSync 测试网跨链桥交互

* 目标： 完成 zkSync 测试网的跨链桥存入 ETH 交互

* 代码： https://github.com/gm365/Web3_Tutorial/blob/main/zkSyncBridge.py
* 交互记录 Hash： https://goerli.etherscan.io/tx/0x4dbe6b9e52c3c401d80d5d585a03d0850d999c67a9aedbe54a23400d6b906005
