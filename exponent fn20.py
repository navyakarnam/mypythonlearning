def exponent(base,power):#we took a fn called exponent along with parameters
    #Note that the power parameter is decided by the user to square or to cube
    result=1

    for index in range(power):#for loop and index is a variable                #for eg:if the power is 3, it loops thrice:
                                                                                 #result=1*2
       result=result*base        #multiplying the base to itself                 #result=2*2
    return result#return stmt
    #print (exponent(3,2))                                                 #result=4*2
print(exponent(2,3))                            #2**3=8(cube)
