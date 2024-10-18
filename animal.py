import sys

def dog():
    print('Baw')

def default():
    print('Hello')

def main():
    default()

if __name__=='__main__':
    if sys.argv[1] == 'dog':
        dog()
    else:
        main()
