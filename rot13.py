def rot13(message):
  return ''.join(list(map(cipher_char, message)))

def cipher_char(ch):
  capital_letters = range(ord('A'), ord('Z') + 1)
  small_letters = range(ord('a'), ord('z') + 1)
  ord_ch = ord(ch)

  if ord_ch in capital_letters:
    return chr(capital_letters[(ord_ch - capital_letters[0] + 13) % 26])
  elif ord_ch in small_letters:
    return chr(small_letters[(ord_ch - small_letters[0] + 13)  % 26])

  return ch

print(rot13("test"), "grfg")
print(rot13("Test"), "Grfg")