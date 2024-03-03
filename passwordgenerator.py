import random
import string

def generate_password(length=11, include_special=True):
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def strong(password):
    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    c = 0
    for character in password:
        if character in special_characters:
            c += 1
    if c > 3:
        print("Strong password")
    else:
        print("Weak password")

# Example usage
n = int(input("Enter the no of passwords to be generated"))
for i in range(n):
    generated_password = generate_password()
    print("Generated Password:", generated_password)
    strong(generated_password)

        
    
    
        

# Example usage



