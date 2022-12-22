def main():
    x = convert(input())
    print(x)

def convert(x):
    x = str(x).replace(":)", "🙂").replace(":(", "🙁")
    return(x)

main()
