def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    di = dict()

    for lin in handle:

        if lin.startswith("From "):
            lin = lin.split()
            sender = lin[1]
            
            if sender in di:
                di[sender] = di[sender] + 1
            else: 
                di[sender] = 1

    #print(di) This is how I check if it counted it correctly

    largest = -1
    value = None
    for k,v in di.items():
        if v > largest:
            largest = v
            value = k
    print (value, largest)

        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()

