import numpy as np
from qiskit import QuantumCircuit, Aer, execute

def generate_random_bits(length):
    return np.random.randint(2, size=length)

def generate_random_bases(length):
    return np.random.choice(['X', 'Z'], size=length)

def encode_qubits(bits, bases):
    qubits = []
    for bit, basis in zip(bits, bases):
        qc = QuantumCircuit(1, 1)
        if bit == 1:
            qc.x(0)
        if basis == 'X':
            qc.h(0)
        qubits.append(qc)
    return qubits

def measure_qubits(qubits, bases):
    backend = Aer.get_backend('qasm_simulator')
    results = []
    for qc, basis in zip(qubits, bases):
        if basis == 'X':
            qc.h(0)
        qc.measure(0, 0)
        result = execute(qc, backend, shots=1).result().get_counts()
        results.append(int(list(result.keys())[0]))
    return results

def sift_keys(sender_bases, receiver_bases, sender_bits, receiver_bits):
    sifted_key = [sender_bits[i] for i in range(len(sender_bits)) if sender_bases[i] == receiver_bases[i]]
    return sifted_key

def simulate_bb84(n=100):
    sender_bits = generate_random_bits(n)
    sender_bases = generate_random_bases(n)
    qubits = encode_qubits(sender_bits, sender_bases)

    receiver_bases = generate_random_bases(n)
    receiver_bits = measure_qubits(qubits, receiver_bases)

    sifted_key = sift_keys(sender_bases, receiver_bases, sender_bits, receiver_bits)

    print(f"Sender Bits: {sender_bits}")
    print(f"Sender Bases: {sender_bases}")
    print(f"Receiver Bases: {receiver_bases}")
    print(f"Receiver Bits: {receiver_bits}")
    print(f"Sifted Key: {sifted_key}")

if __name__ == '__main__':
    simulate_bb84()