#Templete of EOF error exception handling
while True:  
    try:
        a, b = map(int, input().split())
        
        print(a + b)
    
    except EOFError:
        # If no more input is available (EOF reached), break out of the loop.
        break