#print(3+'3') #TypeError: unsupported operand type(s) for +: 'int' and 'str'(Yeni burda biri int digeri string oldugu uchun sehv veririr)
#print(3+int('3'))#Bele eledikde ise cavab str-i int-e cevirerek duzgun cavab almaq olur.
#print(true+1)#NameError: name 'true' is not defined. Did you mean: 'True'?(Burda true-nu reqeme chevrilmediyi uchun hesablama etmir sehv verir)
#print(bool('true')+1)# True-nu reqem sayina chevrerek bele hesablama etdim
#print(3>4 and 3+4/2)#burda 3 reqemi 4 den boyuk olmadigi uchun false verdi (eger print(5>4 and 3+4/2) olsaydi o zaman 5 reqemi netice verecekdi)
#print(type(int(float('3'))))#burda reqemin novu gosterir class 'int' type la float metnden ve kesr varsa onu int chevirir
#print(3.14+int(3.14))#burda int ederek kesr reqemdeki kesri legv ederek toplayir
#print(False+True>int(False))# burda 1>0 oldugundan True 