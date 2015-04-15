#Intro

Many languages have a switch statement, python does not natively.  But now it does :)

Inspired By [Mariusz Wisniewski](https://github.com/lifcio)

##Useage

```
from switch import switch

cases = ["first","second","third"]
for case in switch(cases[0]):
  if case("first"):
    print "first case found"
    break
  if case("second"):
    print "second case found"
    break
  if case("third"):
    print "third case found"
    break
  if case():
    print "default case found, whoops"
```

		 
