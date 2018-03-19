origin = []
n = int(input())
for _ in range(n):
    code = input().split()
    cmd = code[0]
    agrs = code[1:]
    if cmd != 'print':
        cmd += '(' + ",".join(agrs)+')'
        eval('origin.'+cmd)
    else:
        print (origin)
