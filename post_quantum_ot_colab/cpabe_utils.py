# cpabe_utils.py (simulated CP-ABE using simple logic)

def encrypt_with_cpabe(data, policy):
    # Simulate CP-ABE encryption by packaging data with the policy
    return {
        "data": data,
        "policy": policy
    }

def decrypt_with_cpabe(ciphertext, attributes):
    policy = ciphertext["policy"]
    data = ciphertext["data"]

    # Simple policy check: all required attributes must be in user's attributes
    import re
    required_attrs = re.findall(r'(\w+)=([\w\s]+)', policy)

    attr_dict = {}
    for attr in attributes:
        if "=" in attr:
            k, v = attr.split("=")
            attr_dict[k.strip()] = v.strip()
        else:
            attr_dict[attr.strip()] = True  # handle basic attribute names

    for key, value in required_attrs:
        if attr_dict.get(key.strip()) != value.strip():
            return None

    return data
