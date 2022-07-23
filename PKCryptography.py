from sympy.ntheory.factor_ import totient

p = int(input("Enter a the value of P: "))
q = int(input("Enter a the value of Q: "))
b = int(input("Enter a the value of B: "))
n = p*q;
phi = totient(n);
y = pow(b, -1, phi);
print(y);
