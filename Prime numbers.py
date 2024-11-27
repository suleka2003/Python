def prime_range(lower,upper) :
    lower = int ( input ("Which number that you want to start :- ") )
    upper = int ( input (  "Which number that you're going to end :- " ) )
    for number in range ( lower , upper+1 ) :
        for i in range (2,number) :
            if ( number % i == 0 ) :
                break
        else :
            print (number)
prime_range(lower,upper)