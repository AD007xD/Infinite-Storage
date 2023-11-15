def main():
    bin_data = ''
    with open('sample.txt', 'rb') as f:
        bin_data = f.readline()

    print(bin_data)

if __name__ == '__main__':
    main()