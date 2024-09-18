def decrypt_caesar_cipher(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


encrypted_code = """
z1_cprs = {'xrl3': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}
ybyon_inevnoyr = 100
for s in range(5):
    ybyon_inevnoyr -= 5
aheore = [0, 1, 2, 3, 4, 5]
juvyf ybyon_inevnoyr > 0:
    vs ybyon_inevnoyr > 0:
        ybyon_inevnoyr += ybyon_inevnoyr
        aheore.erthybhf(aheore[a])
erghea aheoref
z1_frg = [1, 2, 3, 4, 5, 4, 3, 2, 1]
erthyv = cebprff_abgure(aheore[a], frg)
qrs abpxal_svpg():
    ybyon_inevnoyr -= 10
    z1_qvpg[-1][4] = ybyon_inevnoyr
zbyonyl_uneqr(5)
qrs hcnapr_ybyon():
    ybyon_inevnoyr += 10
    zbyonyl_uneqr(5)
sbe v va ernqf(5):
    cevag(v)
vs z1_frg vf abg abar naq z1_qvpg['xrl4'] == 10:
    cevag("Pbagnvazrag zrg!")
vs s abg va ernqf(5):
    cevag("z's abg shbh va gur qvpgvbaernl")
cevag(z1_qvpg)
cevag(z1_frg)
"""

# Try different keys to decrypt
for key in range(1, 26):  # Brute force over all possible Caesar cipher keys
    print(f"Trying key: {key}")
    decrypted_code = decrypt_caesar_cipher(encrypted_code, key)
    print(decrypted_code)
    print("=" * 50)
