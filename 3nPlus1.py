"""3nPlus1"""
def main():
    """main function"""
    counter = 1
    stock = []
    while True:
        stock.append(int(input()))
        '''for i in stock:
            if int(i) == 0 or int(i) == 1:
                print(counter)
                break
            elif int(i) %2 == 0:
                ans = i//2
                counter += 1
            elif int(i) % 2 != 0:
                ans = num*3+1
                counter += 1'''
    print(stock)
main()
