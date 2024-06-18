import string
import random
import hashlib

def main(m):
    
    things = list(string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.hexdigits+string.octdigits+string.punctuation)

    while m  >= len(things):
        things += things
    random.shuffle(things)
    things =''.join(things)
    return ''.join(things[i] for i in range(m))
    
if __name__ == '__main__':
    while 1:
        try:
            m = int(input("How long do you want your password?:"))
            break
        except:
            pass
    print(main(m))
    
    print(f"This is the hex of the password: {hashlib.sha256(str(main(m)).encode()).hexdigest()}.")
