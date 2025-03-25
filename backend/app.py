from flask import Flask, request, jsonify
from qkd_simulation import simulate_bb84
from kyber_encryption import generate_kyber_keys, encrypt_message, decrypt_message

app = Flask(__name__)

public_key, private_key = generate_kyber_keys()

@app.route('/qkd', methods=['GET'])
def qkd_simulation():
    simulate_bb84()
    return jsonify({"status": "QKD Simulation completed"})

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    message = data.get('message').encode()
    ciphertext, shared_secret = encrypt_message(message, public_key)
    return jsonify({"ciphertext": ciphertext.hex(), "shared_secret": shared_secret.hex()})

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.get_json()
    ciphertext = bytes.fromhex(data.get('ciphertext'))
    shared_secret = decrypt_message(ciphertext, private_key)
    return jsonify({"shared_secret": shared_secret.hex()})

if __name__ == '__main__':
    app.run(debug=True)