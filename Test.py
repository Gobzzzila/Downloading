import urllib
url = input('Enter url for downloading ')
print ("DOWNLOADING...")
urllib.urlretrieve(url, "code.html")
print ("DOWNLOADING COMPLETE")
