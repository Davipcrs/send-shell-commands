import subprocess

app = 'google-chrome'
site1 = 'https://web.whatsapp.com/'

process = subprocess.Popen([app, site1])
app = 'code'
site1 = '/home/davi/src'

process = subprocess.Popen([app, site1])

# https://janakiev.com/blog/python-shell-commands/
