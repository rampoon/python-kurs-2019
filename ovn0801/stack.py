#!/usr/bin/python3
# coding: utf-8

"""Övning 8.1

* Skapa en klass Stack.

* Konstruktorn ska skapa en tom stack.

* Metoden push(value) ska lägga till ett element.

* Metoden pop() ska ta bort och returnera senaste elementet.

* Om man försöker göra pop på en tom stack så ska ett exception av typen
  TomStack genereras.

* Det ska gå att skriva ut stackinnehållet med print.
  (Dvs. metoden __str__ ska finnas i klassen.)

"""





# Här nedan är lite exempel på klientkod som använder klassen Stack:
if __name__ == '__main__':

    st = Stack()
    st.push("Bill")
    st.push("Steve")

    namn = st.pop()
    if namn == "Steve":
        print("OK: fick Steve")
    else:
        print("Fel: skulle fått Steve, men fick", namn)

    namn = st.pop()
    if namn == "Bill":
        print("OK: fick Bill")
    else:
        print("Fel: skulle fått Bill, men fick", namn)

    try:
        namn = st.pop()
    except TomStack:
        print("OK: fick TomStack")
    except:
        print("Fel, undantaget var inte av typen TomStack")
    else:
        print("Fel, fick inget undantag trots att stacken var tom")

    print(st)
