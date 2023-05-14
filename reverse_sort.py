def sort(sample):
    #Sorts numbers and characters in decending order
    #for any string value given based on ASCII code values on input.

    # Change string into array
    sample = list(sample)
    sample_copy= list(sample)
     
    # Sort the copy of the array
    sample_copy.sort()
 
    # count each group of character i.e numbers 
    # uppercase and lowercase
    spec_c1=0 
    nu_c = 0 #numbers
    spec_c2=0
    al_c = 0 #uppercase letters
    spec_c3=0 
    al_c2=0 # lowercase letters
    spec_c4=0
    
   
 
    # Get the index from where each type of
    # ASCII character starts in the sorted list
    for spec in range(len(sample_copy)):
        # print(spec_c4, "AL_c2 =", al_c2)
        #find the first number
        if ord(sample_copy[spec]) in range(0, 48):
           nu_c += 1
           spec_c2 += 1
           al_c += 1
           spec_c3 += 1
           al_c2 += 1
           spec_c4 += 1
        
        #find second set of special charters
        
        elif ord(sample_copy[spec]) in range(48, 58):
           spec_c2 += 1
           al_c += 1
           spec_c3 += 1
           al_c2 += 1
           spec_c4 += 1
        
        # find first location for sorted upperscase letters
        
        elif ord(sample_copy[spec]) in range(58, 65):
           al_c += 1
           spec_c3 += 1
           al_c2 += 1
           spec_c4 += 1
        
        #find third set of special charters
        
        elif ord(sample_copy[spec]) in range(65, 91):
           spec_c3 += 1
           al_c2 += 1
           spec_c4 += 1
        
        #find first location for sorted lowerscase letters

        elif ord(sample_copy[spec]) in range(91, 97):
           al_c2 += 1
           spec_c4 += 1

        #find forth set of special charters

        elif ord(sample_copy[spec]) in range(97, 123):
            spec_c4 += 1

    # print(c)
    # sample_copy = sample_copy[0:nu_c]+sorted(csample_copy[nu_c:spec_c2],reverse=True)+csample_copy[spec_c2:al_c]+sorted(sample_copy[al_c:spec_c3],reverse=True)+sample_copy[spec_c3:al_c2]+sorted(csample_copy[al_c2:spec_c4],reverse=True)
    # print('C sorted', c)
    #remove all special characters from the sorted
    sample_copy=sorted(sample_copy[nu_c:spec_c2],reverse=True)+sample_copy[al_c:spec_c3]+sample_copy[al_c2:spec_c4]
    # print(spec_c1,nu_c, spec_c2, al_c, spec_c3, al_c2,spec_c4)
    al_c=spec_c2-nu_c
    nu_c=0
   
    

    #sort the letters in reverse order

    new_c=sample_copy[0:al_c]+sorted(sample_copy[al_c:], reverse=True)
    

    # Now replace the string with sorted string
    for i in range(len(sample)):
       
       
 
        # If in this position there is a number 
        # then replace it with the a number from the sorted list
        
        if ord(sample[i]) in range(48,57):
            sample[i] = new_c[nu_c]
            nu_c += 1
 
        # If there is an uppercase letter 
        #then replace it with an upperscase letter from the 
        #sorted list
        elif ord(sample[i]) in range(65,90):
            sample[i] = new_c[al_c]
            al_c += 1
        # If there is an lowercase letter 
        #then replace it with an lowerscase letter from the 
        #sorted list
        elif ord(sample[i]) in range(97,123):
            sample[i] = new_c[al_c]
            al_c += 1
        #Else if there is any space or special character
        #then keep it the same 
        else :
            sample[i]=sample[i]
            # print(s)
 
    # Return the sorted string
    return ''.join(sample)
 
# Driver Code
if __name__ == "__main__":
    print('Here is a sample of an input \n 187A3b, 5c, 7de84!$')
    print('Below is the result out put \n')
    
    sample = "187A3b, 5c, 7de84!$"
    print(sort(sample))

    sample = input('\n Now, write your own input \n')
    print('\n', sort(sample))
    