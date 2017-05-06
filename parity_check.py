def numzeros(str):
    if str == '':
        return 0
    else:
        if str[0]=='0':
            return 1 + numzeros(str[1:])
        else:
            return numzeros(str[1:])
        
def parity_recursion(str):
    '''  This function returns True if str contains and even number of zeros
         else it returns false'''
    
    return not (numzeros(str)%2)


def parity_loop(str):
    count =0
    for i in range(len(str)):
        if str[i] == '0':
            count= count +1

    return not count%2


def parity_FSM(str):

    state =0

    for i in range(len(str)):
    
    
        if state == 0 and str[i]=='0':
            state = 1
        elif state == 1 and str[i] =='0':
            state = 0


        if state == 0:
            print "Even number of zeros so far"
        else:
            print "Odd number of zeros so far"

    if state == 0:
        return True
    else:
        return False
    
            
        
    
