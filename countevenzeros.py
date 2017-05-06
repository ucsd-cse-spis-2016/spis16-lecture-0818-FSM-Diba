
def evenzeros(str):
    numzero = 0
    for i in range(len(str)):
        if str[i] == '0':
            numzero = numzero +1

    return (numzero%2 == 0)

def countzeros(str):
    if len(str) == 0:
        return 0
    else:
        if str[0] == '0':
            return 1+ countzeros(str[1:])
        else:
            return countzeros(str[1:])

def evenzeros_r(str):

    return (countzeros(str)%2 ==0)


def evenzeros_FSM(str):

    state = 0
    for i in range(len(str)):
        input_c = str[i]

      
        
        if state == 0 and input_c == '0':
            state = 1
        elif state == 1 and input_c == '0':
            state = 0

        if state == 0:
            print "Even number of zeros"
        else:
            print "Odd number of zeros"

        
    return (state == 0)

            












    
