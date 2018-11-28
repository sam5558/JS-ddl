import glob, os, os.path
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import sys
import zipfile

def write(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()

def cancel(msg):
    write('\x08' * len(msg))

def makecbz(dirname, file_name):
    for cd, dirs, files in os.walk(dirname):
        images = [os.path.join(cd, f) for f in files if f.lower().endswith(
                ('.jpg', '.jpeg'))]
        if images:
            out = dirname + '/' + file_name + '.cbz'
            write('Writing %s [0000]' % out)
            z = zipfile.ZipFile(out, 'w')
            try:
                for i, img in enumerate(images):
                    msg = '[%04d]' % (i+1)
                    cancel(msg)
                    z.write(img)
                    write(msg)
            finally:
                write('\n')
                z.close()

#url = "http://www.japscan.cc/lecture-en-ligne/kingdom/1/1.html"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#req = urllib2.urlopen(urllib2.Request(url, None, hdr)).read()

page_exist = True
counter = 1
pages = []

print "=====================Download====================================================="
link = sys.argv[1]
scan_name = link.split('/')[4]
file_name = link.split('/')[5]

if not os.path.exists(scan_name):
    os.makedirs(scan_name)

pghtml = urllib2.urlopen(urllib2.Request(link, None, hdr)).read()
soupy = BeautifulSoup(pghtml, 'lxml')
pgnb = soupy.findAll("a",{"class": "pagi"})
lastpgnb = pgnb[len(pgnb)-1]
#print pgnb
nb = lastpgnb.getText()
print nb
while page_exist and counter <= int(nb):
    url = link+"/"+str(counter)+".html"
    print "link ======>",url
    try:
        html = urllib2.urlopen(urllib2.Request(url, None, hdr)).read()
#        contents = html.read()
#        print html.getcode()
#       html = contents
        soup = BeautifulSoup(html, 'lxml')
        imgs = soup.find("img", {"id": "image"})
        if imgs:
            print imgs["src"]
            pages.append(imgs["src"])

            f = open(scan_name+'/'+str(counter)+'.jpg','wb')
            f.write(requests.get(imgs["src"]).content)
            f.close()
        else:
            page_exist = False



        counter = counter + 1
    except urllib2.HTTPError, e:
        page_exist = False

print "=====================Create CBZ====================================================="
makecbz(scan_name, file_name)


print "=====================Clean=========================================================="

filelist = glob.glob(os.path.join(scan_name, "*.jpg"))
for f in filelist:
    os.remove(f)
