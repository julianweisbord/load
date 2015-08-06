import sys
import time
import urllib2

def find_size(website):
    opens = urllib2.urlopen(website)
    maxLength = 40
    end_arrow = ">"
    s = "="
    contentLength = 0
    total_contentLength = 0
    numBytes = 1
    #find out size of web page and put that in content length
    #need to specify int on a lot of these so that the output will round the number.
    while True:
        chunk = opens.read(numBytes)
        if not chunk:
            total_contentLength = int(contentLength)
            break
        contentLength+=int(numBytes)

    contentLength = 0
    opens2 = urllib2.urlopen(website)
    #load webpage with accurate percentage and download bar
    while True:
        CHUNK = opens2.read(numBytes)
        if not CHUNK:
            break
        contentLength+=int(numBytes)
        #make download bar
        bar_length = maxLength * contentLength / total_contentLength
        bar = s*(bar_length) + end_arrow
        sys.stdout.write ("Downloading "+ str(100 *contentLength/total_contentLength) + "% " + bar + "\r")
    sys.stdout.flush()

    return contentLength

def main():
    try:
        url = sys.argv[1]
    except (IndexError, ValueError):
        print "No arguments were supplied so we will default to youtube.com"
        url = "http://youtube.com/"
    try:
        contentLength = find_size(url)
        print ("\n" + url + " has loaded " + str(contentLength) + " bytes\n")
    except (IndexError, urllib2.HTTPError, ValueError) as error:
        print error

if __name__ == "__main__":
    main()
