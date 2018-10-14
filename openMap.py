import webbrowser, os
url='file://' + os.path.realpath('page.html')
print(url)
url=url+'?lat=10&lon=20'
# webbrowser.open('file://' + os.path.realpath('page.html'))
webbrowser.open(url)