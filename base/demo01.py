
def demo01():
    print("hello python")

    print("我是汉字")

    f = open('demo01.txt', 'rb')

    for line in f:
        print(line.decode('utf-8'))


if __name__ == "__main__":
    demo01()
