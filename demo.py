import base64, sys

obf = sys.argv[1]
obf = "return int('O0')"
obf = base64.b64encode(obf.encode()).decode()

deobf = base64.b64decode(obf.encode()).decode()

print(obf)
print(deobf)