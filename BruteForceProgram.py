import time

time.sleep(0.1)

password = "*@&#*&#*@&#%@^!%#^%@^#&#^#%^!#%@#aheytaefggaeyu@&^#&#^32676371382738GEYAGEYAFG72367236723623"

def bruteForce():
    attempts = 0
    guessDict = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","+","=","/",".",",","<",">","?",";",":","'",'"',"[","]","{","}","|","`","~"}
    guess = ""
    for a in password:
        for b in guessDict:
            if b == a:
                guess = guess + b

                if guess == password:
                    print(f"Password Cracked : {password} : Attempts : {attempts}")
            else:
                time.sleep(0.0002)
                attempts += 1
                if attempts >= 20000:
                    print("Attempts has reached its limit : 20000")

bruteForce()