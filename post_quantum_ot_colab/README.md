Here is the complete `README.md` for your GitHub repository:

```markdown
# 🔐 Post-Quantum Secure Oblivious Transfer with Fine-Grained Access Control

This project implements a **Post-Quantum Secure Oblivious Transfer (OT)** protocol with **Fine-Grained Access Control** using Ciphertext-Policy Attribute-Based Encryption (CP-ABE). It enhances the Zhang et al. OT protocol by integrating **quantum-safe cryptographic primitives** such as **Kyber KEM** and simulated **Ring-LWE encryption**.

---

## 📌 Features

- 🛡️ **Quantum Resistance**: Uses Kyber KEM (NIST PQC standard) for key exchange.
- 🎯 **Attribute-Based Access Control**: Incorporates CP-ABE for policy-based access.
- 📄 **Sample Healthcare Use Case**: Simulates patient record encryption with access control.
- 💻 **Prototype in Python**: Compatible with Google Colab and local environments.

---

## 📁 Project Structure

```
post_quantum_ot/
├── sender.py               # Encrypts hospital records with OT + access control
├── receiver.py             # Decrypts records based on user's attributes
├── cpabe_utils.py          # Simulated CP-ABE logic
├── kem_utils.py            # Kyber-based KEM functions using liboqs
├── data/
│   ├── hospital_records.json     # Input: sample hospital records
│   └── encrypted_records.json    # Output: encrypted records with policies
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Requirements

- Python 3.7 or higher
- Linux/macOS or Google Colab
- Recommended: virtual environment

### Installation

```bash
# Create and activate virtual environment
python3 -m venv pqot-env
source pqot-env/bin/activate  # or .\pqot-env\Scripts\activate (Windows)

# Install dependencies
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
oqs
pycryptodome
```

> ⚠️ Note: `charm-crypto` was removed due to installation issues on Colab. CP-ABE logic is simulated.

---

## 🚀 How to Run

### Step 1: Encrypt Hospital Records

```bash
python sender.py
```

Expected output:

```
Records encrypted and policies applied.
```

### Step 2: Decrypt with User Attributes

```bash
python receiver.py
```

Example output (if access is granted):

```
Record 001: Cardiac arrhythmia
```

If no access:

```
No records accessible with the given attributes.
```

---

## 🗃️ Example Data

`data/hospital_records.json`

```json
[
  {
    "id": "001",
    "data": "Cardiac arrhythmia",
    "policy": "((role=Doctor) AND (department=Cardiology))"
  }
]
```

User attributes inside `receiver.py`:

```python
user_attributes = ['role=Doctor', 'department=Cardiology']
```

---

## 🧠 Use Cases

- 🔐 Privacy-preserving access to medical records
- ☁️ Secure and policy-controlled cloud storage
- 🏛 Government or legal data access control

---

## 📊 Comparative Highlights

| Protocol              | PQ Secure | Access Control | Performance | Key Size |
|----------------------|-----------|----------------|-------------|----------|
| Zhang et al. (2018)  | ❌        | ✅             | ⚡ Fast     | Small    |
| Naor-Pinkas OT        | ❌        | ❌             | ⚡ Fast     | Small    |
| Kyber OT (2023)       | ✅        | ❌             | ⚡ Fast     | Medium   |
| **This Protocol**     | ✅        | ✅             | ⚠ Moderate | Medium   |

---

## 📚 Reference

This project is based on the research paper:

> **Vinayagam N**, *Post-Quantum Secure Oblivious Transfer with Fine-Grained Access Control: An Enhancement of the Zhang et al. Protocol*, 2025.  
> [See full paper in `/docs/` or included in this repository.]

---

## 📅 Future Work

- Integrate real CP-ABE libraries (e.g., via Charm Crypto offline or alternative)
- Add Zero-Knowledge Proofs for auditability
- Optimize for edge/IoT devices
- Explore hybrid schemes with homomorphic encryption

---

## 🧾 License

MIT License. See `LICENSE` file for more details.

---

## 🤝 Contributing

Open to issues, pull requests, or suggestions. For academic citations, refer to the included research paper.
```
