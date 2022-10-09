#Operator according to their precedence

#Exponential : **
#z = x ** y
#print (9 ** 0.5)

# Unary Operator: +, -, ~ (Bitwise Not)
a = 5 # a = 0101
#print(~a)

# Arithmetic opearator: *, /, // (Floor Division), % #All have same precedence, associativity left to
'''right
&#39;&#39;&#39;print(4 * 6)
print(12 / 5)
print(24.0 // 5) # 8.69, floor(8.69) = nearest lowest integerr
print(12.4 % 5)
print(4 * 6 / 8 // 2)&#39;&#39;&#39;'''

# + can work for concatenating two strings
'''s1 = &#39;Hello&#39;
s2 = &#39;World&#39;
s3 = 5
#print(s1+s2)'''

# *: Can be used to concatenate one string to itself &#39;n&#39; number of time
#print(s3*s1)
#&#39;&#39;&#39; One parameter must be integer and
#the other must be string&#39;&#39;&#39;

# Binaray Addition(+), Subtraction (-)

# Bitwise shift: &lt;&lt;, &gt;&gt; #All have same precedence, associativity left to right

#print( 5 &lt;&lt; 4) # Binary of 5 will be shifted left 4 times
#=&gt; 5 * (2 ** 4)
#print(16 &gt;&gt; 3)
#=&gt; 16 / (2 ** 3)

#Bitwise AND: &amp;
#Bitwise XOR: ^
#Bitwise OR: |
#print(5 &amp; 4) # 5 = 0101, 4 = 0100
#print(5 ^ 4)
#print(5 | 4)

# Camparison: &lt;, &lt;=, &gt;, &gt;=
# Equality: ==, !=
#print(5 != 5) # True or False
#print(type(5 &lt; 6))

# Assignment Operator: =, %=, /=, //=, -=, +=, *=, **= #All have same precedence, associativity
#Right to Left
#&#39;&#39;&#39;a, b, c = 12, 5, 16 # Multiple assignment
'''print(id(a))
print(id(b))
print(id(c))
print(a, b, c)
a, b, c = b, c, a
print(id(a))
print(id(b))
print(id(c))
print(a, b, c)

a = 50
b = 50
print(id(a))
print(id(b))

b = b + 1
print(id(a))
print(id(b))'''
#Mutable , Immutable&#39;&#39;&#39;

#Identity Operator: is, is not
#a = 5
#b = 5
#print(a is not b)

#Membership operator: in, not in
#s1 = &#39;12&#39;
#s2 = 1234
#print(s1 in s2) #s2 must be an iterable

#Boolean Not: Not
#Boolean AND: And (&amp;&amp; in C)
#Boolean OR: Or (|| in C)
#print(not 5 &gt; 4)

#Example of iterable using list
lst = [1, 2, 3, 5]