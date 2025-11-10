#print(*objects, sep=' ',end='\n', file=sys.stdout, flush=False)   

#Ask user for their name
#name=input("What's ypur name? ")
#Remove whitespace from str
#name = name.strip()
#Capitalize user's name
#name = name.capitalize()
#Capitalize like title
#name = name.title()
#Both
#name = name.strip().title()
#Split user's name into first name and last name
#first, last = name.split(" ")

#Say hello to user
#print("Hello,", sep='',end="\n")

#def Hello(to="world"):
    #print("Hello,",to)
#Hello()
#name = input("What's your name? ")
#Hello(name)

def main():
    name=input("What's your name? ")
    Hello(name)

def Hello(to="world"):
    print("Hello,", to)

main()

##name = input("What's your name? ").strip().title()
##print(f"Hello, {name}" )