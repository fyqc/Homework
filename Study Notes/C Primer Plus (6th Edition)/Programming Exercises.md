- [Chapter 1 Getting Ready](#chapter-1-getting-ready)
    + [Question 1](#question-1)
- [Chapter 2 Introducing C](#chapter-2-introducing-c)
    + [Question 1](#question-1-1)
    + [Question 2](#question-2)
    + [Question 3](#question-3)
    + [Question 4](#question-4)
    + [Question 5](#question-5)
    + [Question 6](#question-6)
    + [Question 7](#question-7)
    + [Question 8](#question-8)



# C Primer Plus (6th Edition) Study Notes

## Programmng Exercises

Reading about C isn’t enough. You should try writing one or two simple programs to see  
whether writing a program goes as smoothly as it looks in this chapter. A few suggestions  
follow, but you should also try to think up some problems yourself. You’ll find answers to  
selected programming exercises on the publisher’s website.

## Chapter 1 Getting Ready
#### Page 25

#### Question 1

You have just been employed by MacroMuscle, Inc. (Software for Hard Bodies). The  
company is entering the European market and wants a program that converts inches  
to centimeters (1 inch = 2.54 cm). The company wants the program set up so that it  
prompts the user to enter an inch value. Your assignment is to define the program  
objectives and to design the program (steps 1 and 2 of the programming process).  

**C**
```C
#include <stdio.h>

int main(void)
{
    float inch_value;

    printf("Please enter the value of Inches: \n");
    scanf("%f", &inch_value);
    printf("%f in = %f cm", inch_value, inch_value * 2.54);

    return 0;
}
```

**Python**
```Python
inch_value = float(input("Please enter the value of Inches: "))
cm_value = inch_value * 2.54
print(f'{str(inch_value)} in = {str(cm_value)} cm')
```

## Chapter 2 Introducing C
#### Page 53

#### Question 1
Write a program that uses one printf() call to print your first name and last name on  
one line, uses a second printf() call to print your first and last names on two separate  
lines, and uses a pair of printf() calls to print your first and last names on one line.  
The output should look like this (but using your name):  
```
Gustav Mahler     <- First print statement  
Gustav            <- Second print statement  
Mahler            <- Still the second print statement  
Gustav Mahler     <- Third and fourth print statements  
```

**C**
```C
#include <stdio.h>
    
int main()
{
    printf("Tomoyo Sakagami\n");    /*Clannad A masterpiece*/
    printf("Tomoyo\nSakagami\n");
    printf("Tomoyo");
    printf(" Sakagami");
    
    return 0;
}
```

**Python**
```Python
# Clannad A masterpiece
print("Tomoyo Sakagami")
print("Tomoyo\nSakagami")
print("Tomoyo Sakagami")
```

#### Question 2
Write a program to print your name and address.

**C**
```C
int main(void)
{
    printf("Name\n");
    printf("Address");

    return 0;
}
```

**Python**
```Python
print("Name")
print("Address")
```

#### Question 3
Write a program that converts your age in years to days and displays both values. At this  
point, don’t worry about fractional years and leap years. 

**C**
```C
#include <stdio.h>

int main(void)
{
    int age;

    printf("Please enter your age: ");
    scanf("%d", &age);
    printf("Your age of %d years are %d days\n", age, age * 365);
    
    return 0;
}
```

**Python**
```Python
age = int(input("Please enter your age: "))
print("Your age of %d years are %d days" % (age, age * 365))
```

#### Question 4
Write a program that produces the following output:    
```
For he's a jolly good fellow!  
For he's a jolly good fellow!  
For he's a jolly good fellow!  
Which nobody can deny!   
```
Have the program use two user-defined functions in addition to main(): one named  
jolly() that prints the “jolly good” message once, and one named deny() that prints  
the final line once.   
 
**C**
```C
#include <stdio.h>
void jolly(void);
void deny(void);

int main(void)
{  
    jolly();
    jolly();
    jolly();
    deny();
    
    return 0;
}

     
void jolly(void)
{
    printf("For he is a jolly good fellow!\n");
}
    
void deny(void)
{
    printf("Which nobody can deny!\n");
}
```

**Python**
```Python
def jolly():
    print("For he is a jolly good fellow!")

def deny():
    print("Which nobody can deny!")

if __name__ == "__main__":
    [jolly() for _ in range(3)]    # Call jolly() 3 times.
    deny()
```

#### Page 54
#### Question 5
Write a program that produces the following output:  
```
Brazil, Russia, India, China
India, China,
Brazil, Russia   
```
Have the program use two user-defined functions in addition to main(): one named  
br() that prints "Brazil, Russia" once, and one named ic() that prints "India, China" 
once. Let main() take care of any additional printing tasks.  

**C**
```C
#include <stdio.h>
void br(void);
void ic(void);

int main(void)
{  
    br();
    printf(", ");
    ic();
    printf("\n");
    ic();
    printf(",\n");
    br();
    
    return 0;
}

void br(void)
{
    printf("Brazil, Russia");
}
 
void ic(void)
{
    printf("India, China");
}
```

**Python**
```Python
def br():
    print("Brazil, Russia", end="")

def ic():
    print("India, China", end="")

if __name__ == "__main__":
    br()
    print(", ", end="")
    ic()
    print()
    ic()
    print(",")
    br()
```

#### Question 6
Write a program that creates an integer variable called toes. Have the program set toes  
to 10. Also have the program calculate what twice toes is and what toes squared is. The  
program should print all three values, identifying them.  

**C**
```C
#include <stdio.h>

int main(void)
{  
    int toes = 10;
    printf(
    "toes: %d\n"
    "twice toes: %d\n"
    "toes squared: %d\n", 
    toes, toes * 2, toes * toes
    );
    
    return 0;
}

```

**Python**
```Python
toes = 10
print(f'toes: {toes}\ntwice toes: {toes * 2}\ntoes squared: {toes ** 2}')

```

#### Question 7
Many studies suggest that smiling has benefits. Write a program that produces the  
following output: 
```
Smile!Smile!Smile!  
Smile!Smile!  
Smile!   
```
Have the program define a function that displays the string Smile! once, and have the  
program use the function as often as needed. 

**C**
```C
#include <stdio.h>
void smile(void);	/* ANSI/ISO C function prototyping */
int main(void)
{
    smile();
    smile();
    smile();
    printf("\n");
    smile();
    smile();
    printf("\n");
    smile();
    
	return 0;
}
 
void smile(void)	/* start of function definition */
{
    printf("Smile!");
}
```

**Python**
```Python
def smile():
    print("Smile!", end="")

smile()
smile()
smile()
print()
smile()
smile()
print()
smile()

```

#### Question 8
In C, one function can call another. Write a program that calls a function named one_  
three(). This function should display the word one on one line, call a second function  
named two(), and then display the word three on one line. The function two() should  
display the word two on one line. The main() function should display the phrase  
starting now: before calling one_three() and display done! after calling it. Thus, the  
output should look like the following: 
```
starting now:  
one
two  
three
done!   
```

**C**
```C
#include <stdio.h>
void one_three(void);	/* ANSI/ISO C function prototyping */
void two(void);
int main()
{
    printf("starting now:\n");
    one_three();
    printf("done!\n");

    return 0;
}

void one_three(void)	/* start of function definition */
{
    printf("one\n");
    two();
    printf("three\n");
}
    
void two(void)
{
    printf("two\n");
}
```

**Python**
```Python
def one_three():
    print("one")
    two()
    print("three")

def two():
    print("two")

if __name__ == "__main__":
    print("starting now:")
    one_three()
    print("done!")
```
