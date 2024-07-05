import re

print("輸入要組譯的文檔編號：")
t_n = str(input())
path = 'testcase/test0'+ t_n +'.txt'

def hb4_t0_hb2(n):
    n = str(n)
    n = re.sub('#','', n)
    n = re.sub('H','', n)
    n = n.replace(" ","")
    #print(n[0])
    #if n[0]=='0' and n[1]!='0':n[1:]
    n = n.lstrip('0')
    if len(n) == 1 : '0' + n
    return n

def XRL(IC):
    #XRL 4AH,A
    #XRL 5DH,#7CH
    #XRL 65H,#0C3H
    if IC[2] == 'A':
        MC = '62'+ ' ' + hb4_t0_hb2(IC[1]) + ' '
    else :
        MC = '63'+ ' ' + hb4_t0_hb2(IC[1]) + ' ' + hb4_t0_hb2(IC[2]) + ' '
    return MC.upper()

def DEC(IC):
    #DEC  A
    #DEC  @R0
    if IC[1] == 'A':
        MC = '14'+ ' '
    elif IC[1][0:2] == '@R':
        i = int(str('0001011' + IC[1][-1]),2)
        #print (i)
        MC = str(hex(i))[-2:]+ ' '
    else: pass
    return MC.upper()

def CJNE(IC):
    #CJNE  R2,#37H,16H
    #CJNE  A,#95H,47H
    if IC[1] == 'A':
        MC = 'B4'+ ' ' + hb4_t0_hb2(IC[2]) + ' ' + hb4_t0_hb2(IC[3]) + ' '
    elif IC[1][0:1] == 'R':
        i = int(IC[1][-1])
        if i<2:
            i = bin(i)[-1:]
            i = '00' + i
        elif (i>1 and i<4):
            i = bin(i)[-2:]	
            i = '0' + i
        else: i = bin(i)[-3:]

        i = int('10111' + i,2)
        MC = str(hex(i))[-2:] + ' ' + hb4_t0_hb2(IC[2]) + ' ' + hb4_t0_hb2(IC[3]) + ' '
    return MC.upper()

MC = ""
with open(path) as f:
    for line in f.readlines():
        opcode = line.split(' ')[0]
        #print(opcode)
        if opcode != ('\n' or " " or ""):
            IC = re.sub(opcode, '', line)
            IC = re.sub('\n', '', IC)
            IC = IC.replace(" ","")
            IC = IC.split(',')
            IC.insert(0,opcode)

            if opcode == "XRL": 
                print(IC, '>>' ,XRL(IC))
                MC = MC + XRL(IC)
            elif opcode == "DEC": 
                print(IC, '>>' ,DEC(IC))
                MC = MC + DEC(IC)
            elif opcode == "CJNE": 
                print(IC, '>>' ,CJNE(IC))
                MC = MC + CJNE(IC)
            else: pass

        else:
            pass

print("----------------------------------")
print('MC:',MC)

