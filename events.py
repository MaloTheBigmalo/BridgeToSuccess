import sys


def main():
    if len(sys.argv) < 2:
        print("arguments insuffisant !")
        sys.exit(1)
    else:
        print("Hello " + sys.argv[1])
        sys.exit(0)

if __name__ == "__main__":
    main()