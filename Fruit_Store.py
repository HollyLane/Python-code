money = 10
orange = 3
apple = 2
banana = 2

def oranges():
    global money
    global orange
    print ('you have $' + str(money - orange) + ' left.')
    money = money - orange
def apples():
    global money
    global apple
    print ('you have $' + str(money - apple) + ' left.')
    money = money - apple
def bananas():
    global money
    global banana
    print ('you have $' + str(money - banana) + ' left.')
    money = money - banana

def main():
    global money
    print ('Oranges cost $3, apples cost $2, and bananas cost $2.')
    while money > 1:
        print ('Would you like to buy oranges, apples, or bananas?')
        choice = input()
        if (choice.lower() == 'apple') or (choice.lower() == 'apples'):
            apples()
        elif (choice.lower() == 'orange') or (choice.lower() == 'oranges'):
            if money == 2:
                print ('You don\'t have enough money! You can either buy an apple or a banana.')
            else:
                oranges()
        elif (choice.lower() == 'banana') or (choice.lower() == 'bananas'):
            bananas()
        print ('Would you like to buy more?')
        if input().lower() != ('yes'):
            print ('Thank you for shopping with us.')
            break
        if money < 2:
            print ('You don\'t have enough money! Thank you for shopping with us.')
            break
        
main()
