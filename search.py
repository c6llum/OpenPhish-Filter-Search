# Imports
import urllib

# Variables
filename = "feed1.txt"
online = open("online.txt", "w")
offline = open("offline.txt", "w")
fourofour = open("fourofour.txt", "w")

# Get the OpenPhish feed
urllib.urlretrieve ("https://openphish.com/feed.txt", filename)

# These are the keywords to search for when looking through the feed
sitescan = ['three', 'hsbc', 'my3', 'lloyds', 'hmrc', 'hm.rc', 'tax-refund', 'tax-return'
            'o2', 'tax', 'paypal', 'paypai', 'Login.php?', 'tsb', 'halifax', 'hmrefund',
            'tax', 'natwest', 'barclays']
            
# This opens the OpenPhish feed and sets it as f
f = open(filename)

try: 
 for line in f: # For each line in feed1.txt
     # find all lines with the keywords found in 'sitescan', detect the status then place them in the suitable text file.
     if any(keyword in line for keyword in sitescan): #
         mainstatus = urllib.urlopen(line).getcode() # Get the status code of the website
         if (mainstatus == 200): # If the site is online
             online.write(line) # Add the url to the online.txt file
             print line # Print the line in the text file
         elif (mainstatus == 404): # Checks if status code is 404
          fourofour.write(line) # Adds the url to fourofour.txt
          print "[404] " + line # Prints the line to the console
         else: # For anything else
          offline.write(line) # Place it into offline.txt
          print "[OFFLINE] " + line # And log into the console
except Exception: # If there is an error
 pass # Pass right through
