import rsa

def digital_signature(text, private_key):
    signature = rsa.sign(text.encode(), private_key, "SHA-256")
    return signature

public_key, private_key = rsa.newkeys(512)
text = "Aravinth_aj"
signature = digital_signature(text, private_key)
print(f"Digital signature: {signature}")