#Task 3

def Count(String ,given_chr):
    count = 0
    for i in String:
        if given_chr == i:
            count +=1
    print(given_chr, "Repeated:",count," time")
Count('YaseenIms' , 'e')