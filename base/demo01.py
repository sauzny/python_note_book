
def demo01():
    print("hello python")

    print("我是汉字")

    f = open('demo01.txt', 'rb')

    for line in f:
        print(line.decode('utf-8'))


def fibonacci():
    a, b = 0, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a+b


if __name__ == "__main__":
    demo01()
    fibonacci()
