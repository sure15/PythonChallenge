#http://www.pythonchallenge.com/pc/def/map.html
def danci(a):
    f=''
    for b in a:
        if b=='y':
            e='a'
        elif b=='z':
            e='b'
        elif ord(b)>122 or ord(b)<97:
            e=b
        else:
            c=ord(b)+2
            e=chr(c)
        f=f+e
    return(f)
s=input('请输入您所要翻译的句子： ')
s=s.strip()
s=s.split(' ')
a=len(s)
b=0
while b<a:
    s[b]=danci(s[b])
    b=b+1
for each in s :
    print(each,'',end='')
