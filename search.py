import urllib

filename = "feed1.txt"
online = open("online.txt", "w")
offline = open("offline.txt", "w")
fourofour = open("fourofour.txt", "w")

urllib.urlretrieve ("https://openphish.com/feed.txt", filename)

sitescan = ['three', 'hsbc', 'my3', 'lloyds', 'hmrc', 'hm.rc', 'tax-refund', 'tax-return'
            'o2', 'tax', 'paypal', 'paypai', 'Login.php?', 'tsb', 'halifax', 'hmrefund',
            'tax', 'natwest', 'barclays']
            

f = open(filename)


try:
 for line in f:
     if any(keyword in line for keyword in sitescan):
         mainstatus = urllib.urlopen(line).getcode()
         if (mainstatus == 200):
             online.write(line)
             print line
         elif (mainstatus == 404):
          fourofour.write(line)
          print "[404] " + line
         else:
          offline.write(line)
          print "[OFFLINE] " + line
except Exception:
 pass