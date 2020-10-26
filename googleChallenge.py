
list1 = [1,2,3,9]

list2 = [1,4,2,4]

sum = int(input("Intruduz um valor : "))

intverifier = 0

counter=0
for i in range(len(list1)):
    for j in range(1 , len(list1)):
        if i+j < len(list1):
            if list1[i] + list1[i+j] == sum:
                counter = counter+1 
                print("The value in the position " +  str(i) + " add to the value in the position " +   str(list1[i+j]) + " results in  " +  str(list1[i] + list1[i+j]) + " which is the same as the value introduced by the user :  " + str(sum) )
        
if counter == 0:
    print("There is no combitation between 2 numembers in the list that result in  Não existe nenhuma combinação de 2 números na lista que originem o valor introduzido pelo utilizador : " + str(sum))
