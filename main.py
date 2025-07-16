from pyscript import display, document # importing the display module

print('Hello Earth') # displayed in the console
display('Hello World!') # displayed in the webpage

def greeting_user(e): # creting function name
    document.getElementById('output').innerHTML =''
    username = document.getElementById('data1').value

    display(f'Welcome {username}!', target='output')
    