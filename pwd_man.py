from cryptography.fernet import Fernet
import pass_cre

# def gen_key(k):
#     k = k.encode()
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as key_f:
#         key_f.write(key + b"\n" + k)


def load_key():
    file = open("key.key", 'rb')
    mas_key = file.read()
    file.close()
    return mas_key.decode()


key = load_key()
fer = Fernet(key)


def view():
    with open("/home/sami/Desktop/beg-python/text_file/pwd.txt", 'r') as f:
        print("\nThe pass words are below:")
        for line in f.readlines():
            data = line.rstrip()
            usr, password = data.split(":")
            password = fer.decrypt(password.encode()).decode()
            print("User: ", usr, ", Password: ", password)


def add():
    usr_n = input("Please, enter your account name: ")
    choice = input("Would like to enter a password or generate one?(cre/gen) ")
    pwd = None
    while True:
        if choice == "cre":
            pwd = input("Enter your password: ")
            break
        elif choice == "gen":
            pwd = pass_cre.gen()
            break
        else:
            print("Invalid!!")
            break

    with open("/home/sami/Desktop/beg-python/text_file/pwd.txt", 'a') as f:
        f.write(f"{usr_n} : {fer.encrypt(pwd.encode()).decode()}\n")


while True:
    mode = input("Would you like to add a new password, view the stored ones or would like to quit? (add/ view/ q)\n")

    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid request.")
        continue


