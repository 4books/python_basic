def write_file(path):
    f = open(path, 'w', encoding='UTF-8')
    for i in range(1, 5):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

    return 'success'


if __name__ == '__main__':
    print("=== start ===")
    result = write_file('../my-app/sample.txt')
    print(result)
    print("=== end ===")

