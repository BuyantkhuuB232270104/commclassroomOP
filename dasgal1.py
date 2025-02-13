def printSpring():
    print("Хавар болж цэцгэс цэцэглэлээ.")
def printSummer():
    print("Зун болж халуун боллоо.")
def printAutumn():
    print("Намар болж навч уналаа.")
def printWinter():
    print("Өвөл болж цас орлоо.")
aa=int(input("Улирал аа оруулна уу 1-хавар 2-зун 3-намар 4-өвөл: "))
if aa==1 :
    printSpring()
elif aa==2 :
    printSummer()
elif aa==3 :
    printAutumn()
elif aa==4 :
    printWinter()
else:
    print("Буруу утга оруулсан байна")