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
        
        
        abi, contract_address, rpc = parse_network(network=network)

        if network == 'CUSTOM':
            contract_address = custom_contract
            rpc = custom_rpc
        
        # 经过处理之后的output_addresses是一个地址列表，检测一下列表里地址的数量，然后如果超过 150 个地址，就每 150 个地址分一组，最后每组循环调用 disperse 
        
        disperser = disperse(network=network, abi=abi, contract_address=contract_address, rpc=rpc, 
                             main_account_pk=private_key)
        
        tx_hash_list = []
        
        if len(output_addresses) <= 150:
            value_list = [float(values) for _ in range(len(output_addresses))]
            tx_hash = disperser.disperse_eth_unique(output_addresses, value_list)
            tx_hash_list.append(tx_hash['transactionHash'].hex())
                
        if len(output_addresses) > 150:
            # 分组
            output_addresses = [output_addresses[i:i+150] for i in range(0, len(output_addresses), 150)]
            print(output_addresses)
            # 循环调用 disperse
            for i in range(len(output_addresses)):
                value_list = [float(values) for _ in range(len(output_addresses[i]))]
                tx_hash = disperser.disperse_eth_unique(output_addresses[i], value_list)
                tx_hash_list.append(tx_hash['transactionHash'].hex())                
        
        tx_hash_dict = {str(i + 1): hash for i, hash in enumerate(tx_hash_list)}
        
        return jsonify({'message': tx_hash_dict}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run()
