import json
from kem_utils import generate_keypair, encrypt
from cpabe_utils import encrypt_with_cpabe

def encrypt_records():
    with open('data/hospital_records.json', 'r') as file:
        records = json.load(file)

    public_key, private_key = generate_keypair()

    encrypted_records = []
    for record in records:
        encrypted_data = encrypt(record['data'], public_key)
        encrypted_record = encrypt_with_cpabe(encrypted_data, record['policy'])
        encrypted_records.append({
            'id': record['id'],
            'encrypted_data': encrypted_record,
            'policy': record['policy']
        })

    with open('data/encrypted_records.json', 'w') as file:
        json.dump(encrypted_records, file)

if __name__ == "__main__":
    encrypt_records()
    print("Records encrypted and policies applied.")
