username = "punit"
print(username)     
# punit

username = "goyal"
print(username)
# goyal
# string is immutable in general... as shown above, username is storing punit and another username is storing goyal... this is because they are referring to different memories.

x = 10
print(x)
# 10
y = x
print(y)
# 10
x = 20
print(x)
print(y)
# 20
# 10