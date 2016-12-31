# Opens a text file of URLs (one per line), and opens a web browser window for each 
# URL line

import webbrowser

# The text file is 'urls.txt' by default
fname = 'urls.txt'

with open(fname, 'r') as fhandle:
    # Go through each line, opening the URL in a browser
    for urlline in fhandle:
        print 'opening ' + urlline + '...'
        webbrowser.open(urlline)
