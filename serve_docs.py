import SimpleHTTPServer
import os

def main():
    pwd = os.getcwd()

    try:
        os.chdir("./docs")
        SimpleHTTPServer.test()
    finally:
        os.chdir(pwd)

if __name__ == "__main__":
    main()
