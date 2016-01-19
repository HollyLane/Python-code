from random import randint

def main():
    while True:
        print ('Would you like to roll the dice?')
        if input() == 'yes':
            print (randint ( 1 , 6 ) )
        else:
            print ('okay')

main()

