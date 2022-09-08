import os
import sys


def compare(file_path1: str, file_path2: str):
    f1open = open(file_path1, "r")
    f2open = open(file_path2, "r")
    f1str = f1open.read()
    f2str = f2open.read()
    if (f1str == f2str):
        print("Equal")
    else:
        print("Not Equal")


def compare_detail(file_path1: str, file_path2: str):
    f1open = open(file_path1, "r")
    f2open = open(file_path2, "r")
    f1str = f1open.readlines()
    f2str = f2open.readlines()
    for i in range(max(len(f1str), len(f2str))):
        line1 = f1str[i].strip(os.linesep) if i < len(f1str) else ""
        line2 = f2str[i].strip(os.linesep) if i < len(f2str) else ""
        if line1 != line2:
            print(f"{i+1} || {line1} || {line2}")


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error: Invalid arguments")
        exit(1)
    if (sys.argv[1] == '-d' or sys.argv[1] == '--detailed'):
        compare_detail(sys.argv[2], sys.argv[3])
        exit(0)
    compare(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
