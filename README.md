# K2 Disperser

K2 Disperser 是一个用于分散网络上代币的工具。它允许用户上传一个包含当前 EVM 地址的 私钥，并为每个地址发送指定数量的代币。

## 环境安装

在开始使用 K2 Disperser 之前，请确保您的计算机上安装了以下软件：

- Python 3.6 或更高版本

## 安装步骤

1. 克隆仓库到本地：

```bash
git clone https://github.com/yourusername/k2-disperser.git
cd k2-disperser
```
2. 安装 Python 依赖：
```bash
pip install -r requirements.txt
```
3. 使用命令启动：
```bash
python app.py
```

4. 这将在 localhost:5000 上启动后端服务器。
- 选择网络（目前仅在Sepolia 进行测试）
- 输入主要钱包的私钥
- 输入要分散的钱包的地址
- 点击 "Send!!!" 按钮开始分散代币
- 在操作完成后，显示交易哈希

5. 如果你要自定义合约地址和网络，请部署主页中指示的合约代码

## TO-DO
- [x] EVM 单主地址分发
- [x] 支持自定义网络和合约地址
- [ ] 分地址设置分发代币数量
- [x] 地址拆分
- [ ] 支持ERC20 TOKEN 分发
- [ ] EVM 多主地址分批分发