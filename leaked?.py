from haveibeenpwnd import check_password

print("""
    __            _            _ ___
   / /  ___  __ _| | _____  __| / _ \
  / /  / _ \/ _` | |/ / _ \/ _` \// /
 / /__|  __/ (_| |   <  __/ (_| | \/
 \____/\___|\__,_|_|\_\___|\__,_| ()

""")

print("programmer:yahya")
print("instagram:iq4.p")

password = input("enter your password:")
passwords =check_password(f'{password}')
print("how many times have been you password in used in have i been pwned database:")
print(passwords)
