    # a və b-nin ədəd olduğunu dəqiqləşdirin.a və ya b ədəd deyilsə "Düzgün dəyər daxil edilməyib" return edilsin
    # a b-dən kiçikdirsə ekrana "Daxil edilən dəyərlər tələblərə uyğun deyil" çap edin
    # a b-dən böyükdürsə a və b ədədləri arasında 5-ə bölünən amma 7-yə bölünməyən ədədləri ekrana çap edin.
    
    
a=input('eded daxil edin : ')
b=input('eded daxil edin : ')
def showFilteredNumbers():
    try:
        int(a)
        int(b)
        return True
    except:
        print("duzgun deyer daxil edilmeyib")
def showFilteredNumbers1():
    if b<a:
        return True 
    else:
        print("Daxil edilen deyerler teleblere uygun deyil")
def showFilteredNumbers2(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return "Duzgun deyer daxil edilmeyib"
    elif a<b:
        print("Daxil edilen deyerler teleblere uygun deyil")
    elif a>b:
        for i in range(b,a):
            if i % 5 ==0 and i % 7 !=0:
                print(i)
     


        



  
   
     