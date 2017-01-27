import webbrowser, sys


a_url = 'https://www.google.com/q=' + " ".join(sys.argv[1:])
print ("url=" + a_url)
webbrowser.open(a_url)
