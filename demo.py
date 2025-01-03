import base64, sys

obf = sys.argv[1]
obf = """
i = 0
while True:
    i += 1
    messagebox.showerror(__file__, "a" * i)
"""
obf = base64.b64encode(obf.encode()).decode()

deobf = base64.b64decode(obf.encode()).decode()

print(obf)
print(deobf)