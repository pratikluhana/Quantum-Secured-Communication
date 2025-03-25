import React, { useState } from 'react';
import axios from './api';

function Dashboard() {
  const [message, setMessage] = useState('');
  const [ciphertext, setCiphertext] = useState('');
  const [sharedSecret, setSharedSecret] = useState('');

  const handleEncrypt = async () => {
    try {
      const response = await axios.post('/encrypt', { message });
      setCiphertext(response.data.ciphertext);
      setSharedSecret(response.data.shared_secret);
    } catch (error) {
      console.error('Encryption failed:', error);
    }
  };

  const handleDecrypt = async () => {
    try {
      const response = await axios.post('/decrypt', { ciphertext });
      setSharedSecret(response.data.shared_secret);
    } catch (error) {
      console.error('Decryption failed:', error);
    }
  };

  return (
    <div className="text-center">
      <h1 className="text-3xl font-bold mb-4">Quantum Secure Communication</h1>
      <input
        className="p-2 border rounded-lg text-black"
        type="text"
        placeholder="Enter message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleEncrypt} className="ml-2 p-2 bg-blue-500 rounded-lg">Encrypt</button>
      <button onClick={handleDecrypt} className="ml-2 p-2 bg-green-500 rounded-lg">Decrypt</button>

      {ciphertext && <p className="mt-4">Encrypted Message: {ciphertext}</p>}
      {sharedSecret && <p>Shared Secret: {sharedSecret}</p>}
    </div>
  );
}

export default Dashboard;