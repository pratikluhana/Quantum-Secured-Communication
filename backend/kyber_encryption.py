from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt

def generate_kyber_keys():
    public_key, private_key = generate_keypair()
    return public_key, private_key

def encrypt_message(message, public_key):
    ciphertext, shared_secret = encrypt(public_key)
    print(f"Encrypted Message: {ciphertext}")
    return ciphertext, shared_secret

def decrypt_message(ciphertext, private_key):
    shared_secret = decrypt(ciphertext, private_key)
    print(f"Decrypted Shared Secret: {shared_secret}")
    return shared_secret

if __name__ == '__main__':
    public_key, private_key = generate_kyber_keys()
    message = b"Hello, Quantum Secure World!"
    ciphertext, _ = encrypt_message(message, public_key)
    decrypt_message(ciphertext, private_key)