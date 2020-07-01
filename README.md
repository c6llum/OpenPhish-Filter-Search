# OpenPhish-Filter-Search
Filter through OpenPhish.com phishing feed for specific sites

```
Are you a business trying to protect your company from cyber crime and fraud?
With this tool, you can continously monitor if your site has been targetted by hackers (phishing attempts) through the use of this tool
```

# Prerequisites
- You'll need urllib and Python 2.7 to use this tool

# How to install urllib?
- Execute `python -m pip install urllib`

# How to run this script?
- Upload all files to your server
- Give the permissions `755` to the `fourofour.txt`, `offline.txt` and `online.txt`
- Once all of the above is complete execute: `python search.py`

# Where do the results appear?
- The results will appear in `real time` in the python `console`.
- All scanned websites over the lifetime will be saved in 'feed1.txt'.
- Websites with the status code: 200 will show up in `online.txt`.
- Websites with the status code: 404 will show up in `fourofour.txt`.
- Any other status code website is found in `offline.txt`
