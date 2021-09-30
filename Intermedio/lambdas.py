def run():
    palindrome_lambda = lambda word: word == word[::-1]
    print('\nPalabra palíndroma con lambda:', palindrome_lambda('arenera'))


if __name__ == '__main__':
    run()