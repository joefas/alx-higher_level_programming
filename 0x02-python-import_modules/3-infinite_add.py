#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totaladd = 0
    for i in range(len(sys.arg) - 1):
        totaladd += int(sys.argv[i + 1])
        print("{}".format(totaladd))