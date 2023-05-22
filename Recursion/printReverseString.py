import sys

sys.setrecursionlimit(10**6);
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    def printReverse(s, l):
        if(l==0):
            print(s[0]);
            return;
        print(s[l], end='');
        printReverse(s, l-1);
    
    s = input();
    printReverse(s, len(s)-1);
    
            

    return 0

if __name__ == '__main__':
    main()