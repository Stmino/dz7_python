a = ''
b = ''
c= ''
d=''
def init(id,fi,num,comment):
    global a 
    global b
    global c
    global d
    a = id
    b = fi
    c = num
    d = comment
   
def do_it(a,b,c,d):
    f = open( 'file.txt', 'a+' )
    f.write(a),f.write(' ')
    f.write(b),f.write(' ')
    f.write(c),f.write(' ')
    f.write(d),f.write('\n')
    f.close()


