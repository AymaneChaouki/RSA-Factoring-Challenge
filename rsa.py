#!/usr/bin/python3

# library to get arguments
import sys


# fn unpack number factorial
def fc():
    """
    function fc to search file to convert number and format n=p*q
    """
    try:
        revfile = sys.argv[1]
        with open(revfile) as f:
            for revnumber in f:
                revnumber = int(revnumber)
                if revnumber % 2 == 0:
                        print("{}={}*{}".format(revnumber, revnumber // 2, 2))
                        continue
                i = 3
                while i < revnumber // 2:
                    if revnumber % i == 0:
                        print("{}={}*{}".format(revnumber, revnumber // i, i))
                        break
                    i = i + 2
                if i == (revnumber // 2) + 1:
                    print("{}={}*{}".format(revnumber, revnumber, 1))
    except (IndexError):
        pass


# autostart
fc()
