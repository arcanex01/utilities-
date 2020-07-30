#A script to permutate a given string based on a given length. This script is really good for brute-forcing. 

#Wordlist generator 

from itertools import permutations



def floxy_gen(length_of_password, password_init):
    comb = permutations(list(password_init),int(length_of_password))
    count =0
    for i in list(comb):
        print(''.join(i))
        count +=1
    print('Total List is ------->',count,'<----------------------Good Luck')


if __name__ == "__main__":
    length_of_password = input("Length of Password:")
    password_init = input("Enter String to Generate Password From:")

    print(floxy_gen(length_of_password, password_init))
