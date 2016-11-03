import urllib
url = input('Enter url for downloading ')
print ("DOWNLOADING...")
urllib.urlretrieve(url, "file.jpg")
print ("DOWNLOADING COMPLETE")
