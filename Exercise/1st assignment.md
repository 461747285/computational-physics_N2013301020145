# The first assignment for **Level One** and **Level Two**
-------------------------
## chenfeng      school number: 2013301020145

##Abstract
**This is the programme I design for users to enter words and it will display what they input in a special letter format**

##Introduction
This is my first assignment of computational physics for Exercise1 level1 and level2. My programme aim to reproduce the
words that input by the user (gerenally, their names) in the monitor via special big letters which constructed by '#'. 
Instead of printing my name or designing those letters which only exist in my name, I worked out all the twenty six letters 
directly as well as a blank space, because people used to entering a blank space to seperate their first name and last 
name.

On the other hand, this programme can recognize low-case letters and capital letters. However, for convenience, I only 
designed the special capital letters. In other words, no matter what type of letters you input, it would only display special
capital letters in your screen.

As I have said before, I have only design 26 letters and a blank space, which means if you input other kinds of strings, 
such as numbers, symbols, it would produce errors in the programme.

##letter design
First of all, I need to design 26 letters in the same size. For convenience, my letter sizes is 7'#'*7'#'. Actually, we
can design such 26 special letters in a txt file and then using the programe to read the letters. Considering this process 
is comparably complicated for such small quantity of letters, I construct all the designs in the programe code directly.

##Code
**Here is my programe code**
```python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 9 09:12:16 2016
@author: AF
"""

def alphabet_combine(string,length):
    ####(('#######'),('#######'),('#######'),('#######'),('#######'),('#######'),('#######'))
    pa =(('   #    '),(' #   #  '),('#     # '),('# ### # '),('#     # '),('#     # '),('#     # '))
    pb =((' #####  '),('#     # '),('#     # '),('######  '),('#     # '),('#     # '),(' #####  '))
    pc =((' #####  '),('#     # '),('#       '),('#       '),('#       '),('#     # '),(' #####  '))
    pd =(('######  '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),('######  '))
    pe =(('####### '),('#       '),('#       '),('######  '),('#       '),('#       '),('####### ')) 
    pf =(('####### '),('#       '),('#       '),('#####   '),('#       '),('#       '),('#       '))
    pg =((' #####  '),('#       '),('#       '),('#   ### '),('#     # '),('#    ## '),(' #### # '))
    ph =(('#     # '),('#     # '),('#     # '),('####### '),('#     # '),('#     # '),('#     # '))
    pi =((' #####  '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    '),(' #####  '))
    pj =(('  ##### '),('     #  '),('     #  '),('     #  '),('     #  '),(' #   #  '),('  ###   '))
    pk =(('#     # '),('#    #  '),('#   #   '),('####    '),('#   #   '),('#    #  '),('#     # '))
    pl =((' #      '),(' #      '),(' #      '),(' #      '),(' #      '),(' #      '),(' #####  '))
    pm =(('#     # '),('##   ## '),('# # # # '),('#  #  # '),('#     # '),('#     # '),('#     # ')) 
    pn =(('#     # '),('##    # '),('# #   # '),('#  #  # '),('#   # # '),('#    ## '),('#     # ')) 
    po =((' #####  '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),(' #####  ')) 
    pp =(('######  '),('#     # '),('#     # '),('######  '),('#       '),('#       '),('#       ')) 
    pq =((' #####  '),('#     # '),('#     # '),('#     # '),('#   # # '),('#    #  '),(' #### # ')) 
    pr =(('######  '),('#     # '),('#     # '),('######  '),('#   #   '),('#    #  '),('#     # ')) 
    ps =((' ###### '),('#       '),('#       '),(' #####  '),('      # '),('      # '),('######  '))
    pt =(('####### '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    ')) 
    pu =(('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),(' #####  '))
    pv =(('#     # '),('#     # '),('#     # '),(' #   #  '),(' #   #  '),('  # #   '),('   #    '))
    pw =(('#     # '),('#     # '),('#  #  # '),('#  #  # '),('#  #  # '),('# # # # '),(' #   #  ')) 
    px =(('#     # '),(' #   #  '),('  # #   '),('   #    '),('  # #   '),(' #   #  '),('#     # ')) 
    py =(('#     # '),('#     # '),(' #   #  '),('  # #   '),('   #    '),('   #    '),('   #    '))
    pz =(('####### '),('     #  '),('    #   '),('   #    '),('  #     '),(' #      '),('####### '))
    p_ =(('        '),('        '),('        '),('        '),('        '),('        '),('        '))
    dictionary = {' ':p_,'a':pa,'b':pb,'c':pc,'d':pd,'e':pe,'f':pf,'g':pg,'h':ph,'i':pi,'j':pj,'k':pk,'l':pl,'m':pm,'n':pn,'o':po,'p':pp,'q':pq,'r':pr,'s':ps,'t':pt,'u':pu,'v':pv,'w':pw,'x':px,'y':py,'z':pz}
    screen = [' ']*7    
    for j in range(7):
        for i in range(length):
            screen[j] = screen[j] + dictionary[string[i]][j]
        print screen[j]    
    return screen    
    

def main():
    name = raw_input('please input your name:')
    length = len(name)
    name = name.lower()       
    alphabet_combine(name,length)

main()
```

##Figures
**Alphabet-design**
![alphabet]()

**Name:**
![name](https://raw.githubusercontent.com/chenfeng2013301020145/computational-physics_N2013301020145/master/Exercise/name.png)

**Name_reverse:**
![name-reverse](https://raw.githubusercontent.com/chenfeng2013301020145/computational-physics_N2013301020145/master/Exercise/name_reverse.png)

**Other_display:**
![helloworld](https://raw.githubusercontent.com/chenfeng2013301020145/computational-physics_N2013301020145/master/Exercise/hello_world.png)

##Conclusion
Although this programme is not difficult, it provides us with an opportunity to create our own screen to display what we
want to express. This is the first step to design a programme to control the monitor or some LED screens which we can usually
see in our daily life.


