import sys
import json

def main():
    url = sys.argv[1]

    white_list_file = open('/mnt/neverdelete/projects/fyp/code/phish detector/whitelist.txt').read()
    white_list = white_list_file.split('\n')
    if url not in white_list:
        white_list_file=open('/mnt/neverdelete/projects/fyp/code/phish detector/whitelist.txt', "a+")
        white_list_file.write(url)
        white_list_file.write("\n")
        white_list_file.close()
        print("Whitelist Updated")
    else:
        print("Already present in Whitelist")

if __name__ == "__main__":
    main()
