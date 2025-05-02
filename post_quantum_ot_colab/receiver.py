import json
from kem_utils import decrypt
from cpabe_utils import decrypt_with_cpabe

def decrypt_records():
    with open('data/encrypted_records.json', 'r') as file:
        encrypted_records = json.load(file)

    user_attributes = ['role=Doctor', 'department=Cardiology'] # Customize these

    decrypted_records = []
    for record in encrypted_records:
        decrypted_data = decrypt_with_cpabe(record['encrypted_data'], user_attributes)
        if decrypted_data is not None:
            data = decrypt(decrypted_data)
            decrypted_records.append({
                'id': record['id'],
                'data': data
            })

    if decrypted_records:
        for record in decrypted_records:
            print(f"Record {record['id']}: {record['data']}")
    else:
        print("No records accessible with the given attributes.")

if __name__ == "__main__":
    decrypt_records()
