import time             #Added this for a sense of realism with processing time, and to keep the console from becoming overwhelming for the user
import random           #imported random for my prime numbers finder to work, since I wanted it to have a random feature to it allow the user to enter the range min and max.

def factorize(n):           
    i = 2                   #finding a prime number that is a divisor of n-1. This will return a value that can be assigned to either p or q. This program will assign to p
    while (i < (n-1)):      #iterates through values of i until it finds a value that will divide n evenly, otherwise the function will return false. 
        if n % i == 0:
            return i
        else:
            i += 1    
    return False

def gcd(a, b):
    if(a < 0 or b < 0):         #checks input numbers for negative integers. If TRUE then it will terminate the function with an error message. 
        return "Please reinitiate function with positive integers only"
    
    (s1, t1) = (1,0)    #simultaneous assignment for later calculation.
    (s2, t2) = (0,1)    #simultaneous assignment for later calculation.

    while (b > 0):          #Current value of m =s1*m0 +t1*n0   &   n=s2*m0 + t2*n0
        k = a % b           #assigning k to the result of m mod n
        q = a // b          #floor division of m by n to keep the euclidian algorithm moving along. 
        a = b                 #assigning the value of n to m
        b = k                 #assigning the value of k (the result of m mod n) which will continue to decrease n each loop until it reaches 0 at the end of euclidian alg. 

        (s1hat, t1hat) = (s2,t2)        #initializing s1hat,s2hat and updating it with s2,t2 values each loop.
        (s2hat, t2hat) = (s1-q*s2, t1-q*t2) #s2hat,t2hat which are initialized with the 'recipe' that will be used to update s2,t2 this round.
        (s1,t1) = (s1hat,t1hat)         #global s1,t1 values updated using the 'hat' variables
        (s2,t2) = (s2hat,t2hat)         #global s2,t2 values updated using the 'hat' variables

    return a, (s1,t1)             #returning m (gcd) and the final Bezout's coefficients

def Euclidean_Alg(a, b):
    if(a < 0 or b < 0):         #checks input numbers for negative integers. If TRUE then it will terminate the function with an error message. 
        return "Please reinitiate function with positive integers only"
    while (b > 0):              #initiates a loop based off of the value of b
        k = a % b               #initializes in k to be the result of a mod b
        a = b                   #updates the value of 'a' to be the old value of b
        b = k                   #updates the value of 'b' to the value of k (the result of the modulus operation)
    return a                    #final value of 'a' is returned which is the GCD

def Convert_Text(_string):                  #takes a string argument
    integer_list = []                       #initializes an empty list for integer_list
    for letter in _string:                  #a loop that will iterate through the entered string, letter by letter.
        integer_list.append(ord(letter))    #ord() returns the unicode code for each given letter, and this will append the code to the integer_list which will then be returned.
    return integer_list

def Convert_Num(_list):                     #takes a list argument of a set of integers
    _string = ''                            #initializes an empty string variable
    for i in _list:                         #iterates a loop to go over each item in the list
        _string += chr(i)                   #chr() obtains the character associated with specific Unicode value, and then adds that letter to the string variable.
    return _string

def Encode(n, e, message):                  #this will take a string message, and encode it as a list of integers to the corresponding ASCII values
    cipher_text = []                        #initializes empty cipher_text list for end result to be placed within
    m = Convert_Text(message)               #initializes 'm' which is the numerical list of the entered string to be encoded.
    for i in m:                             #loop iterates through each item in the new list 'm'
        c = (i ** e) % n                    #uses the encoding algorithm for each item and adds it to the cipher_text list. 
        cipher_text.append(c)
    return cipher_text

def Decode(n, d, cipher_text):              #this function will take the list that was given as encoded list of characters, n, and d(decryption key) and returns the original message as string
    message = ''                            #initializes the message variable as an empty string    
    for i in cipher_text:                   #iterates through each integer in the cypher_text list
        m = chr((i ** d) % n)               #algorithm for decrypting a message that is enclosed within the chr() function that will return a string value for the resulting integer.
        message += m                        #adds 'm' resulting string to the message that will be returned.
    return message

def fast_mod_expo(a, n, b):
    #first convert n to binary with a while loop
    result = 1     #initializing result with the value of 1
    while (n > 0): #This loop will take n and return a binary string
        k = n % 2   #assigning the value of k to be the mod of n per time through the loop
        n = n // 2  #reducing n per iteration in order to not create an infinite loop
        if k == 1:  #if the result of the mod operation is 1, then we will go through and square the result with mod operation, as well as modifying the value of square.
            result = (result * a) % b #the overall product to the result only when n mod 2 == 1
        a = (a * a) % b #squaring a, each iteration regardless of whether k == 1 or == 0
    return result       #returning the final result

def Find_Public_Key_e(p, q):
    gcd = Euclidean_Alg(p, q)                   #checking to see if integers that have been entered are prime. If the GCD is other than 1, the function will return an error.
    if (gcd != 1):
        return "Not prime numbers, please try again."
    n = p * q                                   #assigning n to the product of p * q
    k = (p - 1)*(q - 1)
    q = 0
    e = 2
    while(q != 1):
        q = Euclidean_Alg(e,k)
        if (q == 1):
            return n,e 
        else:
            e += 1

def Find_Private_Key_d(e, p, q):
    k = (p - 1) * (q - 1)           #initializes k as phi of n (p-1)(q-1)
    q = 0                           #initializing q as our iteration variable
    d = 1                           #d is initialized at 1 and will be incremented +1 per loop until e * d mod k is equal to 1
    while(q != 1):                  #checking that q is not prime
        q = (d * e) % k             #modulus operation checking for inverse of mod
        if(q == 1):                 #conditional - if prime, condition is met and will return d!
            return int(d)
        else:                       #condition has not been met and will increase d by 1 and repeat the loop.
            d += 1
    return d

def find_a_prime(a, b):                                         #Custom feature for plugging in a min and max number and returning a random prime number within that range
    prime_divisors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                    73, 79, 83, 89, 97]                         #I found having a list of prime divisors up to 100 was sufficient for numbers well above the range needed
    ahat = random.randint(a, b-3)

    while(ahat < b):                                        #This first loop is based off of 'ahat' the random value assigned between a and b.
        noPrime = True                                      #The loop will iterate adding +1 to ahat for every time it finds a prime_divisor divides evenly into ahat.
        i = 0
        while(noPrime):                                     #This is a loop for each ahat value and will iterate each number of the prime_divisor list < value of ahat.
            if(prime_divisors[i] < ahat):
                if(ahat % prime_divisors[i] == 0):          #It found a divisor! Time to add to the ahat value and try another number because this one isn't prime.
                    ahat += 1
                    break
                else:
                    i += 1                                  #This prime_divisor doesn't go evenly into ahat but we need to iterate through and check the rest
                if(i == len(prime_divisors)):
                    return ahat
            else:                                           #Unable to find a prime divisor for the number therefore the number is prime and it will return the ahat value.
                return ahat

def menu():                                                 #Custom feature to create a menu for an interactive userface and allow for an easier user experience
    print("[0] Exit the program")                           #The menu is called in the Program_start function and the menu will have the user follow prompts to complete the program.
    print("[1] Encode a message")
    print("[2] Decode a message")

# def encoding_option():

def prime_option0(_string):                                                     #This function follows after user puts in that they do not know a prime number to use
    print('Directing you to the prime number generator! Please wait...\n')      #The program will prompt them for a range between 2 integers, and then will call the Find_a_prime function.
    prime_range_min = int(input("Prime range ~ Enter minimum number: "))        
    prime_range_max = int(input("Prime range ~ Enter maximum number: "))    
    print("Thank you, please wait while I cook up your prime numbers...")
    p = find_a_prime(prime_range_min, prime_range_max)
    q = find_a_prime(prime_range_min, prime_range_max)
    time.sleep(3)
    n,e = Find_Public_Key_e(p,q)
    d = Find_Private_Key_d(e,p,q)
    print("\nYour reference values:\np={}\nq={}\nn={}\ne={}\nd={}".format(p,q,n,e,d))
    print("I am now going to going to process your message...\n")
    time.sleep(3)
    output_code = Encode(n, e, _string)
    return output_code

def prime_option1(_string):                     #This is the option that follows when the user states that they know prime numbers to use. It have them input those numbers and call the rest of the encoding sequence.
    print("\n")
    print("Please ensure your provided numbers are prime otherwise you may not encrypt properly!")
    p = int(input("Enter key p: "))
    q = int(input("Enter key q: "))
    n,e = Find_Public_Key_e(p,q)
    print("Taking your new n and e values {} and {} and plugging them into the RSA algorithm!".format(n, e))
    print("Processing...\n")
    time.sleep(3)
    output_code = Encode(n, e, _string)
    return output_code

def known_primes(_string):      #This is when the public keys are already known. It will prompt user to input key's n and e and then process the encoding sequence. 
    print("\n")
    n = int(input("Enter key n: "))
    e = int(input("Enter key e: "))
    print("Processing...\n")
    time.sleep(3)
    output_code = Encode(n, e, _string)
    return(output_code)

def decoding_menu1():       #When user selects the decoding option on the main menu. It will prompt to enter coded message, and then whether they know private keys or not.
    incoming_message = (str(input("Enter your encrypted message here: ")))
    incoming_message = incoming_message.strip('[]')
    message_listed = [int(num) for num in incoming_message.split(',')]
    incoming_message = incoming_message.split()
    option_keys = (int(input("Do you have a Private key available? (n and d):   [1] Yes   or   [2] No only Public Keys: ")))
    return message_listed, option_keys

def decoding_option1(_string):      #private keys are known for the coded message, this will simply run the decoding sequence and return the message in plain text. 
    n = int(input("Enter key n: "))
    d = int(input("Enter key d: "))
    print("Processing...\n\n")
    time.sleep(3)
    outgoing_message = Decode(n, d, _string)
    return outgoing_message

def code_breaker(_string):      #Code break sequence for when private keys are unknown but public keys are provided. Instructs members to stand by because this can take seconds to many minutes to process. 
    print("Opening Brute-Force Code Breaker...")
    time.sleep(3)
    n = int(input("Enter key given n: "))
    e = int(input("Enter key given e: "))
    print("Stand by while Code Breaker works! This can take a couple of minutes...\n")
    time.sleep(3)
    p = factorize(n)
    q = n / p
    d = Find_Private_Key_d(e, p, q)
    outgoing_message = Decode(n, d, _string)
    return outgoing_message

def Program_Start():                        #This is the main operation center of the code. It is directed by the menu, and allows the user to navigate using the console.
    menu()                                  #Each option will have follow on prompts and different options until the program is eventually terminated.
    option = int(input("Enter your option: "))
    while option != 0:

        if option == 1:         #Option for encrypting message -- user will be prompted for message and keys and will output encrypted code list.
            outgoing_message = str(input("Please enter string you would like encrypted: "))
            option_keys = int(input("Do you know your public keys (n and e)?    [1] Yes   or  [0] No: "))

            if(option_keys == 0):
                option_primes = int(input("Do you know two prime numbers you can use?    [1] Yes   or  [0] No: "))

                if(option_primes == 0):
                    print(prime_option0(outgoing_message))

                elif(option_primes == 1):
                    print(prime_option1(outgoing_message))

            elif(option_keys == 1):
                print(known_primes(outgoing_message))

        elif option == 2:   #Decoding a message - ask for message input and public keys for decoding
            message_listed, option_keys = decoding_menu1()

            if(option_keys == 1):
                print(decoding_option1(message_listed))
                
            elif (option == 2):     #Open Code Breaker
                print(code_breaker(message_listed))
                
        else:
            print("Invalid option.")

        print()
        menu()
        option = int(input("Enter your option: "))

    print("Program Terminated\n")       #End of program output to show user they will need to restart for another processing. Should only occur when user prompts main menu to exit program.




def main():                                 #main function - serves as the first function that is called when the program is run as the main body 
    Program_Start()

if __name__ == "__main__":                  #Also enables program to be run through command prompt and once program is run as main program, it will initialize main() and start the program.
    main()