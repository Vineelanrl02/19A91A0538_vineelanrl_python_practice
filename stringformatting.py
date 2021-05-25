"""%s-for formatting string value
%d=integer
%f=float
%o=octal
%c=character
%x=hex value for lower case
%X=hex value for uppercase"""

name="cse"#for string
print("hello %s!how are you?"%(name))
age=19#for integer value
print("age is %d" %(age))
#combining the %s & %d
print("hello %s! your age is %d"%(name,age))
percentage=7.5
print("my percentage is %f"%(percentage))
# for three formats in a single line
print("hello i am %s my age is %d and my percentage is %f"%(name,age,percentage))
#formatting of X hex
o=16
print("Number is %X"%(o))
print("Number is %x"%(o))
#formatting of octal
p=7
print("Number is %o"%(p))
#formatting of character
i="h"
print("the character is %c"%(i))

"""output:
hello cse how are you?
age is 19
hello cse your age is 19
my percentage is 7.500000
hello i am cse my age is 19 and my percentage is 7.500000
Number is 10
Number is 7
the character is h"""
