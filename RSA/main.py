"""
N = pq	p、q分別都是隨意挑的質數，N是p、q的乘積。
φ(N) = (p-1)(q-1)	φ(N)的意思是小於 N 的質數，(p-1)(q-1) 是φ(N)的公式算法。
gcd( e , φ(N) ) = 1	找出一個和 φ(N) 這個數互質的 e 。
d*e ≡ 1 (mod φ(N))	找到 d ，條件如下，使得 d*e 之乘積除以 φ(N) 的餘數等於 1 ！也就是說， ( d*e -1 ) 是 φ(N) 的整數倍！
Me≡C (mod N)	M 代表原文，Me除以 N 取餘數，餘數即為密文！
Cd≡M (mod N)	C 代表密文，Cd除以 N 取餘數，餘數即為密文！
"""
def read_txt_file(TXT):
    f_ = open(TXT)
    file_ = f_.read()
    f_.close()
    return file_ #type string

def write_txt_file(str_,filename):
    f_ = open(f"{filename}","w",encoding="UTF-8")
    f_.write(str_)
    f_.close()

def gcd(x,y):#
    if x < y:
        temp = x
        x = y
        y = temp
    if(y == 0):
        return x
    else:
        return gcd(y,x % y)

def find_gcd_Euler_Totient(Euler_Totient):
    for i in range(2,Euler_Totient):
        if gcd(i,Euler_Totient)==1:
            return i

def find_d(e,Euler_Totient):
    for d in range(100000):
        if((d * e -1) % Euler_Totient == 0):
            return d

def encryption(str_,e,N):
    encryption_str = ""
    for i in str_:
        encryption_str += chr((ord(i) ** e) % N)
    return  encryption_str

def decryption(str_,d,N):
    decryption_str = ""
    for i in str_:
        decryption_str += chr((ord(i) ** d) % N)
    return  decryption_str

if __name__ == '__main__':
    file_name = input("Input file name:")
    Plaintext = read_txt_file(file_name)

    p = int(input("Input p:"))
    q =  int(input("Input q:"))
    N = p * q

    Euler_Totient = (p-1) * (q-1)
    e = find_gcd_Euler_Totient(Euler_Totient)
    d = find_d(e,Euler_Totient)

    Ciphertext = encryption(Plaintext, e, N)
    print("Encryption save in Ciphertext.txt")
    write_txt_file(Ciphertext,"Ciphertext.txt")
    DecryptionCiphertext = decryption(Ciphertext, d ,N)
    write_txt_file(DecryptionCiphertext,"DecryptionCiphertext.txt")
    print(f"Decryption save in DecryptionCiphertext.txt")
