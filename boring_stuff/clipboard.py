import pyperclip

pyperclip.copy('The text to be copied to the clipboard.')

data = pyperclip.paste()

print("data=" + data)
