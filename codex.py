
import sys

def main():
    
    checkCLI()
    filePath = sys.argv[1]

    try:
        
        with open(filePath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        counts = 0
        for line in lines:
            if not checkLine(line):
                counts += 1
        
        print(f"TheNumberOfLinesOfCodesIn; <{filePath}> Is: {counts}")
    
    except FileNotFoundError:
        sys.exit(f'NoSuchFile:// --> {filePath} <--')

def checkCLI():
    
    if len(sys.argv) != 2:
        sys.exit('NoCommandLineArg')
    
    if not sys.argv[1].endswith('.py'):
        sys.exit('filePathNotEndsWith_ --> |.py |')

def checkLine(line):
    #check if line empty or comment line //
    if line.isspace() or line.strip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()     