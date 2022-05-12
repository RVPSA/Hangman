word="Bananna"
print(word)
length=len(word)

g=1
b=[]
answer=""
for y in range(length):
    b.append('_')

while g<=5:
    answer=""
    input1=str(input("Enter a letter: "))
    if(input1 in word):
        for i in range(length):
            if(input1 == word[i]):
                #b=b+input1
                b[i]=input1
    for x in b:
        answer=answer+x
    print(answer)
    if(answer == word):
        print('You win')
        break
    g=g+1

if(answer != word):
    print("You loss")