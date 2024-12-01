def two2one(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b


def two2one2(a):
    return [i for i in a if i % 2 == 0]  # Списковое включение для фильтрации четных чисел


def main():
    x = [5, 7, 10, 13, 18, 22, 24]
    print(two2one(x))


if __name__ == '__main__':
    main()
