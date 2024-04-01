from flask import Flask, render_template, request, jsonify
from util import parse_target_address, parse_network
from disperse_eth import disperse
import requests
import os


# 创建flask对象
app = Flask(__name__)

@app.route("/")
def index():
    """
    这个函数用来完成一个url对应的逻辑处理
    :return:
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
        
    # 获取其他表单数据
    network = request.form.get('network')
    output_address = request.form.get('output_address')
    private_key = str(request.form.get('private_key'))
    values = request.form.get('values')
    custom_rpc = request.form.get('custom_rpc')
    custom_contract = request.form.get('custom_contract')
    
    # 传输私钥，输出地址，以及对应的value
    
        # 这里你可以调用你的Python脚本处理文件和网络信息
        # 例如，使用web3.py来处理以太坊交易
    try:
        print('network:', network)
        print('type(network):', type(network))
        print('custom_rpc:', custom_rpc)
        print('custom_contract:', custom_contract)
        print('output_address:', repr(output_address))
        print('private_key:', private_key)
        print('values:', values)
        # 拆解地址，私钥，值
        output_addresses = parse_target_address(output_address)
        print(output_addresses)
        value_list = [float(values) for _ in range(len(output_addresses))]
        print(value_list)
                
        abi, contract_address, rpc = parse_network(network=network)

        if network == 'CUSTOM':
            contract_address = custom_contract
            rpc = custom_rpc

        disperser = disperse(network=network, abi=abi, contract_address=contract_address, rpc=rpc, 
                             main_account_pk=private_key, target_address_list=output_addresses, values=value_list)
        tx_hash = disperser.disperse_eth_unique()
        
        # disperser = disperse(network, private_key, output_address, values)
        return jsonify({'message': f'Network:' + str(network) + 
                        '\n' + f'your txhash:' + str(tx_hash['transactionHash'].hex())}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run()
