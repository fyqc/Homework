- [C Primer Plus (6th Edition) Study Notes](#c-primer-plus--6th-edition--study-notes)
  * [Programming Exercises](#programming-exercises)
  * [Chapter 1 Getting Ready](#chapter-1-getting-ready)
      - [Page 25](#page-25)
      - [Question 1](#question-1)
  * [Chapter 2 Introducing C](#chapter-2-introducing-c)
      - [Page 53](#page-53)
      - [Question 1](#question-1-1)
      - [Question 2](#question-2)
      - [Question 3](#question-3)
      - [Question 4](#question-4)
      - [Page 54](#page-54)
      - [Question 5](#question-5)
      - [Question 6](#question-6)
      - [Question 7](#question-7)
      - [Question 8](#question-8)
  * [Chapter 3 Data and C](#chapter-3-data-and-c)
      - [Page 97](#page-97)
      - [Question 1](#question-1-2)
      - [Question 2](#question-2-1)
      - [Question 3](#question-3-1)
      - [Question 4](#question-4-1)
      - [Question 5](#question-5-1)
      - [Question 6](#question-6-1)
      - [Question 7](#question-7-1)
      - [Question 8](#question-8-1)
  * [Chapter 4 Character Strings and Formatted Input/Output](#chapter-4-character-strings-and-formatted-input-output)
      - [Page 140](#page-140)
      - [Question 1](#question-1-3)
      - [Question 2](#question-2-2)
      - [Page 141](#page-141)
      - [Question 3](#question-3-2)
      - [Question 4](#question-4-2)
      - [Question 5](#question-5-2)
      - [Question 6](#question-6-2)
      - [Question 7](#question-7-2)
      - [Page 142](#page-142)
      - [Question 8](#question-8-2)
  * [Chapter 5 Operators, Expressions, and Statements](#chapter-5-operators--expressions--and-statements)
      - [Page 187](#page-187)
      - [Question 1](#question-1-4)
      - [Question 2](#question-2-3)
      - [Question 3](#question-3-3)
      - [Question 4](#question-4-3)
      - [Question 5](#question-5-3)
      - [Question 6](#question-6-3)
      - [Page 188](#page-188)
      - [Question 7](#question-7-3)
      - [Question 8](#question-8-3)
      - [Question 9](#question-9)
  * [Chapter 6 Control Statements: Looping](#chapter-6-control-statements--looping)
      - [Page 241](#page-241)
      - [Question 1](#question-1-5)
      - [Question 2](#question-2-4)
      - [Question 3](#question-3-4)
      - [Question 4](#question-4-4)
      - [Page 242](#page-242)
      - [Question 5](#question-5-4)
      - [Question 6](#question-6-4)
      - [Question 7](#question-7-4)
      - [Question 8](#question-8-4)
      - [Question 9](#question-9-1)
      - [Question 10](#question-10)
      - [Page 243](#page-243)
      - [Question 11](#question-11)
      - [Question 12](#question-12)
      - [Question 13](#question-13)
      - [Question 14](#question-14)
      - [Question 15](#question-15)
      - [Question 16](#question-16)
      - [Page 244](#page-244)
      - [Question 17](#question-17)
      - [Page 241](#page-241-1)
      - [Question 18](#question-18)
  * [Chapter 7 C Control Statements: Branching and Jumps](#chapter-7-c-control-statements--branching-and-jumps)
      - [Page 296](#page-296)
      - [Question 1](#question-1-6)
      - [Question 2](#question-2-5)
      - [Question 3](#question-3-5)
      - [Question 4](#question-4-5)
      - [Question 5](#question-5-5)
      - [Question 6](#question-6-5)
      - [Question 7](#question-7-5)
      - [Question 8](#question-8-5)
      - [Question 9](#question-9-2)
      - [Question 10](#question-10-1)
      - [Question 11](#question-11-1)
  * [Chapter 8 Character Input/Output and Input Validation](#chapter-8-character-input-output-and-input-validation)
      - [Page 332](#page-332)
      - [Question 1](#question-1-7)
      - [Page 333](#page-333)
      - [Question 2](#question-2-6)
      - [Question 3](#question-3-6)
      - [Question 4](#question-4-6)
      - [Question 5](#question-5-6)
      - [Question 6](#question-6-6)
      - [Question 7](#question-7-6)
      - [Question 8](#question-8-6)
  * [Chapter 9 Functions](#chapter-9-functions)
      - [Page 380](#page-380)
      - [Question 1](#question-1-8)
      - [Question 2](#question-2-7)
      - [Question 3](#question-3-7)
      - [Question 4](#question-4-7)
      - [Question 5](#question-5-7)
      - [Page 381](#page-381)
      - [Question 6](#question-6-7)
      - [Question 7](#question-7-7)
      - [Question 8](#question-8-7)
      - [Question 9](#question-9-3)
      - [Question 10](#question-10-2)
      - [Question 11](#question-11-2)


# C Primer Plus (6th Edition) Study Notes

## Programming Exercises

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
    printf("Tomoyo Sakagami\n"); /*Clannad A masterpiece*/
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
void smile(void); /* ANSI/ISO C function prototyping */
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

void smile(void) /* start of function definition */
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
void one_three(void); /* ANSI/ISO C function prototyping */
void two(void);
int main()
{
    printf("starting now:\n");
    one_three();
    printf("done!\n");

    return 0;
}

void one_three(void) /* start of function definition */
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

## Chapter 3 Data and C

#### Page 97
#### Question 1
Find out what your system does with integer overflow, floating-point overflow, and  
floating point underflow by using the experimental approach; that is, write programs  
having these problems. (You can chek the discussion in Chapter 4 of *limits.h* and  
*float.h* to get guidance on the largest and smallest values.)

**C**
```C
#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(void)
{
    int int_overflow;
    int MAX_INTEGER = INT_MAX;
    float flt_overflow, flt_underflow;
    float MIN_FLOAT = FLT_MIN;
    float MAX_FLOAT = FLT_MAX;
    
    // artificially create over/underflow
    int_overflow = INT_MAX + 1;
    flt_overflow = FLT_MAX * 2.;
    flt_underflow = FLT_MIN / 2.;
    
    // print results
    printf("Max integer: %d \tMax integer + 1: %d\n", INT_MAX, int_overflow);
    printf("Max float: %f \tMax float * 2: %f\n", FLT_MAX, flt_overflow);
    printf("Min float: %f \tMin float / 2: %f\n", FLT_MIN, flt_underflow);

    return 0;
}
```

**Python**
```Python
# In Python 3, this question doesn't apply.
# However, you might actually be looking for information about the current 
# interpreter's word size, which will be the same as the machine's word size
# in most cases.
import sys
maxint = sys.maxsize
minint = -sys.maxsize - 1

int_overflow = maxint +1
flt_overflow = float(maxint) * 2.
flt_underflow = float(minint) / 2.

# print results

print("Max integer: %d \tMax integer + 1: %d\n" % (maxint, int_overflow))
print("Max float: %f \tMax float * 2: %f\n" % (float(maxint), flt_overflow))
print("Min float: %f \tMin float / 2: %f\n" % (float(minint), flt_underflow))
```

#### Question 2
Write a program that asks you to enter an ASCII code value, such as 66, and then prints  
the character having that ASCII code.

**C**
```C
#include <stdio.h>

int main(void) 
{
    int ascii_code;
    
    printf("Enter an ASCII code: ");
    scanf("%d", &ascii_code);
    printf("Character for ASCII code %d: %c\n", ascii_code, ascii_code);

    return 0;
}
```

**Python**
```Python
ascii_code = int(input("Enter an ASCII code: "))
print("Character for ASCII code %d: %c" % (ascii_code, ascii_code))
```

#### Question 3
Write a program that sounds an alert and then prints the following text:  
```
Startled by the sudden sound, Sally shouted,
"By the Great Pumpkin, what was that!"
```

**C**
```C
#include <stdio.h>
int main(void)

{
    printf("\aStartled by the sudden sound, Sally shouted,\n");
    // '\a' here is for generate a beep sound.
    // '\a' is equivalent to '\007'
    printf("\"By the Great Pumpkin, what was that!\"\n");

    return 0;
}
```

**Python**
```Python
print('\aStartled by the sudden sound, Sally shouted, \
    \n"By the Great Pumpkin, what was that!"')
# Same thing in Python code, '\a' is for beep, and use '\' to break lines.
```

#### Question 4
Write a program that reads in a floating-point number and prints it first in decimal-point  
notation, then in exponential notation, and then, if your system supports it, p notation.  
Have the output use the following format (the actual number of digits displayed for the  
exponent depends on the system):
```
Enter a floating-point value: 64.25  
fixed-point notation: 64.250000  
exponential notation: 6.425000e+01  
p notation: 0x1.01p+6   
```

**C**
```C
#include <stdio.h>
int main(void)
{
    float flt_input;

    printf("Enter a floating-point value: ");
    scanf("%f", &flt_input);
    printf("Fixed-point notation: %f\n", flt_input);
    printf("Exponential notation: %e\n", flt_input);
    printf("P notation: %a\n", flt_input);

    return 0;
}
```

**Python**
```Python
flt_input = float(input("Enter a floating-point value: "))
print("Fixed-point notation: %f" % flt_input)
print("Exponential notation: %e" % flt_input)
# Python seems not suppot P notation.
```

#### Question 5
There are approximately 3.156 × 10^7 seconds in a year. Write a program that requests  
your age in years and then displays the equivalent number of seconds.

**C**
```C
#include <stdio.h>

int main(void)
{
    int age;

    printf("What is your age (in years)?: ");
    scanf("%d", &age);
    printf("You are %d seconds old!\n", 3.156E7 * age);

    return 0;
}
```

**Python**
```Python
age = int(input("What is your age (in years)?: "))
print("You are %d seconds old!" % (age * 3.156E7))
```

#### Question 6
The mass of a single molecule of water is about 3.0×10^-23 grams. A quart of water is  
about 950 grams. Write a program that requests an amount of water, in quarts, and  
displays the number of water molecules in that amount.

**C**
```C
#include <stdio.h>

int main(void)
{
    float H20_MASS = 3.0e-23;
    float GRAMS_H20_PER_QUART = 950;
    float quarts;

    printf("Enter an amount of water (in quarts): ");
    scanf("%f", &quarts);
    printf("There are %f molecules in %f quarts of water.\n",
           quarts * GRAMS_H20_PER_QUART / H20_MASS, quarts);

    return 0;
}
/*
Enter an amount of water (in quarts): 1
There are 31666665471894751000000000.000000 molecules in 1.000000 quarts of water.
*/
```

**Python**
```Python
H20_MASS = 3.0e-23
GRAMS_H20_PER_QUART = 950
quarts = float(input("Enter an amount of water (in quarts): "))

print("There are %f molecules in %f quarts of water." \
     % (quarts * GRAMS_H20_PER_QUART / H20_MASS, quarts))
'''
Enter an amount of water (in quarts): 1
There are 31666666666666665598517248.000000 molecules in 1.000000 quarts of water.
'''
```

#### Question 7
There are 2.54 centimeters to the inch. Write a program that asks you to enter your  
height in inches and then displays your height in centimeters. Or, if you prefer, ask for  
the height in centimeters and convert that to inches.

**C**
```C
#include <stdio.h>

int main(void)
{
    float CM_PER_INCH = 2.54;
    float height;

    printf("Enter your height (in inches): ");
    scanf("%f", &height);
    printf("You are %f centimeters tall.\n", height * CM_PER_INCH);

    return 0;
}
```

**Python**
```Python
height = float(input("Enter your height (in inches): "))
print("You are %f centimeters tall." % (height * 2.54))
```

#### Question 8
In the U.S. system of volume measurements, a pint is 2 cups, a cup is 8 ounces, an  
ounce is 2 tablespoons, and a tablespoon is 3 teaspoons. Write a program that requests a  
volume in cups and that displays the equivalent volumes in pints, ounces, tablespoons,  
and teaspoons. Why does a floating-point type make more sense for this application than  
an integer type? 

**C**
```C
#include <stdio.h>

int main(void)
{

    /* If the number of cups is not an even whole number, then the number of
        pints will not be a whole number. */
    float PINTS_PER_CUP = .5;
    float OUNCES_PER_CUP = 8;
    float TBS_PER_CUP = 2 * OUNCES_PER_CUP; // tablespoons/ounce * ounces/cup
    float TSP_PER_CUP = 3 * TBS_PER_CUP;    // teaspoons/tablespoon * tablespoons/ounce * ounces/cup
    float cups;

    printf("Enter an amount in cups:");
    scanf("%f", &cups);
    printf("%f cups is equivalent to:\n", cups);
    printf("%f pints\n", cups * PINTS_PER_CUP);
    printf("%f ounces\n", cups * OUNCES_PER_CUP);
    printf("%f tablespoons\n", cups * TBS_PER_CUP);
    printf("%f teaspoons\n", cups * TSP_PER_CUP);

    return 0;
}
```
**Python**
```Python
PINTS_PER_CUP = .5
OUNCES_PER_CUP = 8
TBS_PER_CUP = 2 * OUNCES_PER_CUP # tablespoons/ounce * ounces/cup
TSP_PER_CUP = 3 * TBS_PER_CUP # teaspoons/tablespoon * tablespoons/ounce * ounces/cup
cups = float(input("Enter an amount in cups:"))

print("%f cups is equivalent to:" % cups)
print("%f pints" % (cups * PINTS_PER_CUP))
print("%f ounces" % (cups * OUNCES_PER_CUP))
print("%f tablespoons" % (cups * TBS_PER_CUP))
print("%f teaspoons" % (cups * TSP_PER_CUP))
```

## Chapter 4 Character Strings and Formatted Input/Output
#### Page 140
#### Question 1
Write a program that asks for your first name, your last name, and then prints the names  
in the format last, first.

**C**
```C
#include <stdio.h>

int main(void)
{
    char first_name[20];
    char last_name[20];

    printf("Enter your first and last name (e.g.: Tomoyo Sakagami): ");
    scanf("%s %s", first_name, last_name);
    printf("%s, %s\n", last_name, first_name);

    return 0;
}
```

**Python**
```Python
first_name, last_name = input("Enter your first and last name (e.g.: Tomoyo Sakagami): ").split()
# Use split() to get two variant inputs.
print("%s, %s" % (last_name, first_name))
```

#### Question 2
Write a program that requests your **first name** and does the following with it:  
a. Prints it enclosed in double quotation marks  
b. Prints it in a field 20 characters wide, with the whole field in quotes and the name  
at the right end of the field  
c. Prints it at the left end of a field 20 characters wide, with the whole field enclosed  
in quotes  
d. Prints it in a field three characters wider than the name 

*Note:  
Chinese version (姜佑 译, 人民邮电出版社 ISBN 9787115390592) has an error in translation here (Page 120).  
In English version, it requires only "First name".  
In Chinese version, it requires you to input "First and Last Name"  
I believe "copy and paste" key words from Question 1 is the root cause.   
Therefore the solution won't work.*

**C**
```C
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[20];
    int name_length;

    printf("Enter your first name: ");
    scanf("%s", name);
    name_length = strlen(name);
    printf("\"%s\"\n", name);                   // a. enclosed in double quotes
    printf("\"%20s\"\n", name);                 // b. double quotes, 20 char wide, right-justified
    printf("\"%-20s\"\n", name);                // c. double quotes, 20 char wide, left-justified
    printf("\"%*s\"\n", name_length + 3, name); // d. double quotes, 3 char wider than name

    return 0;
}
```
**Python**
```Python
name = input("Enter your first name: ")
print('"%s"' % name) # a. enclosed in double quotes
print('"%20s"' % name) # b. double quotes, 20 char wide, right-justified
print('"%-20s"' % name) # c. double quotes, 20 char wide, left-justified
print('"%*s"' % (len(name)+3, name)) # d. double quotes, 3 char wider than name
```

#### Page 141
#### Question 3
Write a program that reads in a floating-point number and prints it first in decimal-point  
notation and then in exponential notation. Have the output use the following formats  
(the number of digits shown in the exponent may bedifferent for your system):  
a. The input is 21.3 or 2.1e+001.  
b. The input is +21.290 or 2.129E+001. 

**C**
```C
#include <stdio.h>

int main(void)
{
    float num;

    printf("Enter a number: ");
    scanf("%f", &num);
    printf("The input is %.1f or %.1e\n", num, num);
    printf("The input is %+.3f or %.3E\n", num, num);

    return 0;
}
```

**Python**
```Python
num = float(input("Enter a number: "))
print("The input is %.1f or %.1e" % (num, num))
print("The input is %+.3f or %.3E" % (num, num))
```

#### Question 4
Write a program that requests your height in inches and your name, and then displays  
the information in the following form:
```
Dabney, you are 6.208 feet tall
```

Use type float, and use / for division. If you prefer, request the height in centimeters  
and display it in meters.

**C**
```C
#include <stdio.h>

int main(void)
{
    const float INCHES_PER_FEET = 12;
    float height;
    char name[40];

    printf("What is your name?: ");
    scanf("%s", name);
    printf("What is your height in inches?: ");
    scanf("%f", &height);
    printf("%s, you are %.3f feet tall.\n", name, height / INCHES_PER_FEET);

    return 0;
}
```

**Python**
```Python
name = input("What is your name?: ")
height = float(input("What is your height in inches?: "))
print("%s, you are %.3f feet tall." % (name, height / 12))
```

#### Question 5
Write a program that requests the download speed in megabits per second (Mbs) and  
the size of a file in megabytes (MB). The program should calculate the download time  
for the file. Note that in this context one byte is eight bits. Use type float, and use /  
for division. The program should report all three values (download speed, file size, and  
download time) showing two digits to the right of the decimal point, as in the following:  
```
At 18.12 megabits per second, a file of 2.20 megabytes  
downloads in 0.97 seconds. 
```
**C**
```C
#include <stdio.h>

int main(void)
{
    const float BITS_PER_BYTE = 8;
    float download_speed_Mps;
    float file_size_MB;

    printf("Enter the download speed (in megabits/second): ");
    scanf("%f", &download_speed_Mps);
    printf("Enter the file size (in megabytes): ");
    scanf("%f", &file_size_MB);
    printf("At %.2f megabits per second, a file of %.2f megabytes"
           " downloads in %.2f seconds.\n",
           download_speed_Mps, file_size_MB,
           file_size_MB * BITS_PER_BYTE / download_speed_Mps);

    return 0;
}
```

**Python**
```Python
download_speed_Mps = float(input("Enter the download speed (in megabits/second): "))
file_size_MB = float(input("Enter the file size (in megabytes): "))
BITS_PER_BYTE = 8
print("At %.2f megabits per second, a file of %.2f megabytes" \
        " downloads in %.2f seconds." %
        (download_speed_Mps, file_size_MB,
        file_size_MB * BITS_PER_BYTE / download_speed_Mps))
```

#### Question 6
Write a program that requests the user’s first name and then the user’s last name. Have  
it print the entered names on one line and the number of letters in each name on the  
following line. Align each letter count with the end of the corresponding name, as in the  
following:  
```
Melissa Honeybee   
      7        8  
```
Next, have it print the same information, but with the counts aligned with the beginning  
of each name.
```
Melissa Honeybee 
7       8
```
**C**
```C
#include <stdio.h>
#include <string.h>

int main(void)
{
    char first_name[20];
    char last_name[20];

    printf("Enter your first and last name: ");
    scanf("%s %s", first_name, last_name);
    printf("\n");
    printf("%s %s\n", first_name, last_name);
    printf("%*lu %*lu\n", // right justified
           (int)strlen(first_name), strlen(first_name),
           (int)strlen(last_name), strlen(last_name));
    printf("\n");
    printf("%s %s\n", first_name, last_name);
    printf("%-*lu %-*lu\n", // left justified
           (int)strlen(first_name), strlen(first_name),
           (int)strlen(last_name), strlen(last_name));
    printf("\n");

    return 0;
}
```

**Python**
```Python
first_name, last_name = input("Enter your first and \
last name(e.g.: Tomoyo Sakagami): ").split()

print(first_name + " " + last_name)

print("%*lu %*lu" % 
        (
        int(len(first_name)), len(first_name), 
        int(len(last_name)), len(last_name))
        )

print()

print("%s %s" % (first_name, last_name))

print("%-*lu %-*lu" % 
        (
        int(len(first_name)), len(first_name), 
        int(len(last_name)), len(last_name))
        )
```

#### Question 7
Write a program that sets a type double variable to 1.0/3.0 and a type float variable  
to 1.0/3.0. Display each result three times—once showing four digits to the right of the  
decimal, once showing 12 digits to the right of the decimal, and once showing 16 digits  
to the right of the decimal. Also have the program include float.h and display the  
values of FLT_DIG and DBL_DIG. Are the displayed values of 1.0/3.0 consistent with these  
values?

**C**
```C
#include <stdio.h>
#include <float.h>

int main(void)
{
    double db = 1.0 / 3.0;
    float ft = 1.0 / 3.0;

    printf("%10s   %-20s   %-20s\n", "DIGITS", "FLOAT", "DOUBLE");
    printf("%10s   %-20.4f   %-20.4f\n", "4 Digits", ft, db);
    printf("%10s   %-20.12f   %-20.12f\n", "12 Digits", ft, db);
    printf("%10s   %-20.16f   %-20.16f\n", "16 Digits", ft, db);

    printf("\n");
    printf("FLT_DIG: %d\n", FLT_DIG);
    printf("DBL_DIG: %d\n", DBL_DIG);

    /* results: both float and double are accurate to at least the amount of sig
    figs specified by FLT_DIG and DBL_DIG */

    return 0;
}
```

**Python**
```Python
# Python's built-in float type has double precision.
```

#### Page 142
#### Question 8
Write a program that asks the user to enter the number of miles traveled and the number  
of gallons of gasoline consumed. It should then calculate and display the miles-per-gallon  
value, showing one place to the right of the decimal. Next, using the fact that one gallon  
is about 3.785 liters and one mile is about 1.609 kilometers, it should convert the mile-  
per-gallon value to a liters-per-100-km value, the usual European way of expressing fuel  
consumption, and display the result, showing one place to the right of the decimal. Note  
that the U. S. scheme measures the distance traveled per amount of fuel (higher is better),  
whereas the European scheme measures the amount of fuel per distance (lower is better).  
Use symbolic constants (using const or #define) for the two conversion factors.

**C**
```C
#include <stdio.h>
#define KM_PER_MILE 1.609
#define LT_PER_GALLON 3.785
int main(void)
{
    float miles_travelled, gallons_gas_consumed;
    float miles_per_gallon, liters_per_100km;

    printf("Enter your distance travelled in miles: ");
    scanf("%f", &miles_travelled);
    printf("Enter the amount of gas consumed in gallons: ");
    scanf("%f", &gallons_gas_consumed);

    // calculate miles per gallon and liters per km
    miles_per_gallon = miles_travelled / gallons_gas_consumed;
    liters_per_100km = 100.0 / miles_per_gallon * LT_PER_GALLON / KM_PER_MILE;

    printf("Miles per gallon: %.1f\n", miles_per_gallon);
    printf("Liters per 100 kilometers: %.1f\n", liters_per_100km);

    return 0;
}
```
**Python**
```Python
KM_PER_MILE = 1.609
LT_PER_GALLON = 3.785

miles_travelled = float(input("Enter your distance travelled in miles: "))
gallons_gas_consumed = float(input("Enter the amount of gas consumed in gallons: "))

# calculate miles per gallon and liters per km
miles_per_gallon = miles_travelled / gallons_gas_consumed
liters_per_100km = 100 / miles_per_gallon * LT_PER_GALLON / KM_PER_MILE

print("Miles per gallon: %.1f" % miles_per_gallon)
print("Liters per 100 kilometers: %.1f" % liters_per_100km)
```

## Chapter 5 Operators, Expressions, and Statements
#### Page 187
#### Question 1
Write a program that converts time in minutes to time in hours and minutes. Use  
#define or const to create a symbolic constant for 60. Use a while loop to allow the  
user to enter values repeatedly and terminate the loop if a value for the time of 0 or less  
is entered.

**C**
```C
#include <stdio.h>
#define MINUTES_PER_HOUR 60

int main(void)
{
    int minutes = 1;

    while (minutes > 0)
    {
        printf("Enter an amount of time in minutes: "); // get first input
        scanf("%d", &minutes);
        printf("%d minute(s) is %d hour(s) and %d minute(s).\n",
               minutes,
               minutes / MINUTES_PER_HOUR,  // hours
               minutes % MINUTES_PER_HOUR); // minutes
    }

    return 0;
}
```

**Python**
```Python
MINUTES_PER_HOUR = 60
minutes = 1
while minutes > 0:
    minutes = int(input("Enter an amount of time in minutes: "))
    print("%d minute(s) is %d hour(s) and %d minute(s)." % 
    (minutes, minutes / MINUTES_PER_HOUR, minutes % MINUTES_PER_HOUR))
```

#### Question 2
Write a program that asks for an integer and then prints all the integers from (and  
including) that value up to (and including) a value larger by 10. (That is, if the input is 5,  
the output runs from 5 to 15.) Be sure to separate each output value by a space or tab or  
newline.

**C**
```C
#include <stdio.h>

int main(void)
{
    int integer;
    int i = 0;

    printf("please enter an integer: ");
    scanf("%d", &integer);
    while (i <= 10)
    {
        printf("%d\t", integer + i);
        i++;
    }

    return 0;
}
```

**Python**
```Python
integer = int(input("please enter an integer: "))
i = 0
while i <= 10:
    print("%d\t" % (integer + i), end='')
    i += 1
```

#### Question 3
Write a program that asks the user to enter the number of days and then converts that  
value to weeks and days. For example, it would convert 18 days to 2 weeks, 4 days.  
Display results in the following format:  
```
18 days are 2 weeks, 4 days.
```
Use a while loop to allow the user to repeatedly enter day values; terminate the loop  
when the user enters a nonpositive value, such as 0 or -20.

**C**
```C
#include <stdio.h>
#define DAYS_PER_WEEK 7

int main(void)
{
    int days;

    printf("Enter a number of days (or enter 0 to quit): ");
    scanf("%d", &days);
    while (days > 0)
    {
        printf("%d days are %d weeks, %d days.\n",
               days, days / DAYS_PER_WEEK, days % DAYS_PER_WEEK);

        printf("Enter a number of days (or enter 0 to quit): ");
        scanf("%d", &days);
    }

    return 0;
}
```

**Python**
```Python
DAYS_PER_WEEK = 7
days = int(input("Enter a number of days (or enter 0 to quit): "))
while days > 0:
    print("%d days are %d weeks, %d days." %
        (days, days / DAYS_PER_WEEK, days % DAYS_PER_WEEK))
    days = int(input("Enter a number of days (or enter 0 to quit): "))
```

#### Question 4
Write a program that asks the user to enter a height in centimeters and then displays the  
height in centimeters and in feet and inches. Fractional centimeters and inches should  
be allowed, and the program should allow the user to continue entering heights until a  
nonpositive value is entered. A sample run should look like this:  
```
Enter a height in centimeters: 182
182.0 cm = 5 feet, 11.7 inches
Enter a height in centimeters (<=0 to quit): 168.7 
168.0 cm = 5 feet, 6.4 inches
Enter a height in centimeters (<=0 to quit): 0
bye
```

**C**
```C
#include <stdio.h>
const float CM_PER_IN = 2.54;
const int IN_PER_FT = 12;

int main(void)
{
    float height_cm, height_in, inches;
    int feet;

    printf("Enter a height in centimeters: ");
    scanf("%f", &height_cm);

    while (height_cm > 0)
    {
        height_in = height_cm / CM_PER_IN;     // convert height to inches
        feet = (int)height_in / IN_PER_FT;     // get number of feet in height
        inches = height_in - feet * IN_PER_FT; // get remaining inches

        printf("%.1f cm = %d feet, %.1f inches\n",
               height_cm, feet, inches);

        printf("Enter a height in centimeters (<= 0 to quit): ");
        scanf("%f", &height_cm);
    }

    printf("bye\n");
    return 0;
}
```

**Python**
```Python
CM_PER_IN = 2.54
IN_PER_FT = 12

height_cm = float(input("Enter a height in centimeters: "))

while height_cm > 0:
    height_in = height_cm / CM_PER_IN # convert height to inches
    feet = int(height_in / IN_PER_FT) # get number of feet in height
    inches = height_in - feet * IN_PER_FT # get remaining inches

    print("%.1f cm = %d feet, %.1f inches" %
            (height_cm, feet, inches))
    height_cm = float(input(("Enter a height in centimeters (<= 0 to quit): ")))

print("bye")
```

#### Question 5
Change the program addemup.c (Listing 5.13), which found the sum of the first 20  
integers. (If you prefer, you can think of addemup.c as a program that calculates how  
much money you get in 20 days if you receive $1 the first day, $2 the second day, $3 the  
third day, and so on.) Modify the program so that you can tell it interactively how far  
the calculation should proceed. That is, replace the 20 with a variable that is read in.

**C**
```C
#include <stdio.h>
int main(void)
{
    int count, sum, max_count; 
    
    count = 0; 
    sum = 0; 
    
    printf("Pleaes enter a integer that you would expect to calculate: ");
    scanf("%d", &max_count);

    while (count++ < max_count) 
        sum = sum + count; 
    printf("sum = %d\n", sum);
    
    return 0; 
}
```

**Python**
```Python
count = 0
v_sum = 0
max_count = int(input("Pleaes enter a integer that you would expect to calculate: "))

while count <= max_count:
    v_sum = v_sum + count
    count += 1
print(v_sum)
```

#### Question 6
Now modify the program of Programming Exercise 5 so that it computes the sum of the  
squares of the integers. (If you prefer, how much money you receive if you get $1 the  
first day, $4 the second day, $9 the third day, and so on. This looks like a much better  
deal!) C doesn’t have a squaring function, but you can use the fact that the square of n is  
n * n.

**C**
```C
#include <stdio.h>
int main(void) 
{
    int count, sum, max_count; 
    
    count = 0;  
    sum = 0; 
    
    printf("Pleaes enter a integer that you would expect to calculate: ");
    scanf("%d", &max_count);

    while (count++ < max_count) 
        sum = sum + count * count; 
    printf("sum = %d\n", sum);
    
    return 0;  
}
```

**Python**
```Python
count = 0
v_sum = 0
max_count = int(input("Pleaes enter a integer that you would expect to calculate: "))

while count <= max_count:
    v_sum = v_sum + count * count
    count += 1
print(v_sum)
```

#### Page 188
#### Question 7
Write a program that requests a type double number and prints the value of the number  
cubed. Use a function of your own design to cube the value and print it. The main()  
program should pass the entered value to this function.

**C**
```C
#include <stdio.h>

double cubed(double n); // prototype declaration for cubed

int main(void)
{
    double input;
    printf("Enter a number to cube: ");
    scanf("%lf", &input);

    printf("%.3f cubed is %.3f\n", input, cubed(input));

    return 0;
}

double cubed(double n)
{
    return n * n * n;
}
```

**Python**
```Python
def cubed(n):
    return n ** 3

n = float(input("Please enter a number to be cube: "))
print("%.3f cubed is %.3f" % (n, cubed(n)))
```

#### Question 8
Write a program that displays the results of applying the modulus operation. The user  
should first enter an integer to be used as the second operand, which will then remain  
unchanged. Then the user enters the numbers for which the modulus will be computed,  
terminating the process by entering 0 or less. A sample run should look like this:  
```
This program computes moduli. 
Enter an integer to serve as the second operand: 256
Now enter the first operand: 438
438 % 256 is 182
Enter next number for first operand (<= 0 to quit): 1234567
1234567 % 256 is 135
Enter next number for first operand (<= 0 to quit): 0
Done
```

**C**
```C
#include <stdio.h>

int main(void)
{
    int first, second;
    printf("This program computes moduli.\n");
    printf("Enter an integer to serve as the second operand: ");
    scanf("%d", &second);
    printf("Now enter the first operand: ");
    scanf("%d", &first);
    while (first > 0)
    {
        printf("%d %% %d is %d\n", first, second, first % second); //print results

        printf("Enter next number for first operand (<= 0 to quit): ");
        scanf("%d", &first); // get new input
    }
    printf("Done\n");
    return 0;
}
```

**Python**
```Python
print("This program computes moduli.")
second = int(input("Enter an integer to serve as the second operand: "))
first = int(input("Now enter the first operand: "))

while first > 0:
    print(f"{first} % {second} is {first % second}") # print results
    first = int(input("Enter next number for first operand (<= 0 to quit): ")) # get new input

print("Done")
```

#### Question 9
Write a program that requests the user to enter a Fahrenheit temperature. The program  
should read the temperature as a type double number and pass it as an argument to  
a user-supplied function called Temperatures(). This function should calculate the  
Celsius equivalent and the Kelvin equivalent and display all three temperatures with a  
precision of two places to the right of the decimal. It should identify each value with the  
temperature scale it represents. Here is the formula for converting Fahrenheit to Celsius:  
Celsius = 5.0 / 9.0 * (Fahrenheit - 32.0)  
The Kelvin scale, commonly used in science, is a scale in which 0 represents absolute  
zero, the lower limit to possible temperatures. Here is the formula for converting Celsius  
to Kelvin:  
Kelvin = Celsius + 273.16  
The Temperatures() function should use const to create symbolic representations of  
the three constants that appear in the conversions. The main() function should use  
a loop to allow the user to enter temperatures repeatedly, stopping when a q or other  
nonnumeric value is entered. Use the fact that scanf() returns the number of items  
read, so it will return 1 if it reads a number, but it won’t return 1 if the user enters q. The  
== operator tests for equality, so you can use it to compare the return value of scanf()  
with 1.

**C**
```C
#include <stdio.h>
const double FAHR_TO_CEL_SCALE = 5.0 / 9.0;
const double FAHR_TO_CEL_OFFSET = -32.0;
const double CEL_TO_KEL_OFFSET = 273.16;

void Temperatures(double Fahrenheit);
int main(void)
{
    double Fahrenheit;
    printf("Enter a Fahrenheit temperature(q to quit): \n");

    while (scanf("%lf", &Fahrenheit) == 1) // continue executing loop if user enters valid number
    {
        Temperatures(Fahrenheit);

        printf("Enter a Fahrenheit temperature(q to quit): \n");
    }
    return 0;
}

void Temperatures(double Fahrenheit)
{
    const double FAHR_TO_CEL_SCALE = 5.0 / 9.0;
    const double FAHR_TO_CEL_OFFSET = -32.0;
    const double CEL_TO_KEL_OFFSET = 273.16;

    double Celsius = (Fahrenheit + FAHR_TO_CEL_OFFSET) * FAHR_TO_CEL_SCALE;
    double Kelvin = Celsius + CEL_TO_KEL_OFFSET;

    printf("%.2f degrees fahrenheit is %.2f degrees celsius or %.2f degrees kelvin.\n",
           Fahrenheit, Celsius, Kelvin);
}
```

**Python**
```Python
def Temperatures(Fahrenheit):
    Celsius =  5.0 / 9.0 * (Fahrenheit - 32.0)
    Kelvin = Celsius + 273.16
    print("%.2f degrees fahrenheit is %.2f degrees celsius or %.2f degrees kelvin." 
    % (Fahrenheit, Celsius, Kelvin))

if __name__ == '__main__':
    while True:
        Fahrenheit = input("Enter a Fahrenheit temperature(q to quit): ")
        try:
            while float(Fahrenheit):
                Temperatures(float(Fahrenheit))
                Fahrenheit = input("Enter a Fahrenheit temperature(q to quit): ")
        except ValueError:
            break
```

## Chapter 6 Control Statements: Looping
#### Page 241
#### Question 1
Write a program that creates an array with 26 elements and stores the 26 lowercase  
letters in it. Also have it show the array contents.

**C**
```C
#include <stdio.h>
#define ALPHABET_LENGTH 26

int main(void)
{
    char alphabet_lowercase[ALPHABET_LENGTH];
    char letter;
    int i;

    // initialize array
    for (letter = 'a'; letter - 'a' < ALPHABET_LENGTH; letter++)
    {
        alphabet_lowercase[letter - 'a'] = letter; // store letter in array
    }

    printf("The lowercase letters of the alphabet are:\n");
    // print each item in array
    for (i = 0; i < ALPHABET_LENGTH; i++)
    {
        printf("%c ", alphabet_lowercase[i]);
    }
    printf("\n");

    return 0;
}
```

**Python**
```Python
import string
alphabet = string.ascii_lowercase[:]
for n in alphabet:
    print(n, end=' ')
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
```

#### Question 2
Use nested loops to produce the following pattern:
```
$
$$
$$$
$$$$
$$$$$
```

**C**
```C
#include <stdio.h>

int main(void)
{
    for (int i = 1; i < 6; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("$");
        }
        printf("\n");
    }

    return 0;
}
```

**Python**
```Python
i = 1
while i < 6:
    j = 1
    while j <= i:
        print('$', end='')
        j += 1
    print()
    i += 1
```

#### Question 3
Use nested loops to produce the following pattern:
```
F
FE
FED
FEDC
FEDCB
FEDCBA
```
Note: If your system doesn't use ASCII or some other code that encodes letters in numeric order, you can use the following to initialize a character array to the letters of the alphabet:
```
char lets[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
```
Then you can use the array index to select individual etters; for example, lets[0] is 'A', and so on.

**C**
```C
#include <stdio.h>

int main(void)
{
    for (int i = 1; i < 7; i++)
    {
        for (char c = 'F'; 'F' - c < i; c--)
        {
            printf("%c", c);
        }
        printf("\n");
    }

    return 0;
}
```

**Python**
```Python
i = 1
while i < 7:
    c = 'F'
    while ord('F') - ord(c) < i:
        print("%c" % c, end='')
        c = chr(ord(c) - 1)
    print()
    i = i + 1
```

#### Question 4
Use nested loops to produce the following pattern:
```
A
BC
DEF
GHIJ
KLMNO
PQRSTU
```
**C**
```C
#include <stdio.h>

int main(void)
{
    char c = 'A';

    for (int i = 1; i < 7; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("%c", c++); // print and THEN increment c
        }
        printf("\n");
    }

    return 0;
}
```

**Python**
```Python
i = 1
c = 'A'

while i < 7:
    j = 1
    while j <= i:
        print("%c" % c, end='')
        c = chr(ord(c) + 1)
        j += 1
    print()
    i += 1
```

#### Page 242
#### Question 5
Write a program that converts time in minutes to time 
Have a program request the user to enter an uppercase letter. Use nested loops to produce  
a pyramid pattern like this:
```
     A 
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
```
The pattern should extend to the character entered. For example, the preceding pattern  
would result from an input value of E. Hint: Use an outer loop to handle the rows. Use  
three inner loops in a row, one to handle the spaces, one for printing letters in ascending  
order, and one for printing letters in descending order. If your system doesn't use ASCII  
or a similar system that represents letters in strict number order, see the suggestion in   
programming exercise 3.

**C**
```C
#include <stdio.h>

void print_spaces(unsigned int n);

int main(void)
{
    char uppercase_letter;
    char c1, c2;

    do // get uppercase letter from user
    {
        printf("Enter an uppercase letter: ");
        scanf(" %c", &uppercase_letter);
    } while (uppercase_letter < 'A' || 'Z' < uppercase_letter);

    for (c1 = 'A'; c1 <= uppercase_letter; c1++)
    {
        // print opening spaces
        print_spaces(uppercase_letter - c1);

        // print letters
        // ascending
        for (c2 = 'A'; c2 < c1; c2++)
        {
            printf("%c", c2);
        }
        // descending
        for (; 'A' <= c2; c2--)
        {
            printf("%c", c2);
        }

        // print closing spaces
        print_spaces(uppercase_letter - c1);
        printf("\n");
    }

    return 0;
}

void print_spaces(unsigned int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}
```

**Python**
```Python
uppercase_letter = input("Enter an uppercase letter: ")

def print_spaces(n):
    i = 0
    while i < n:
        print(" ", end='')
        i = i + 1

if not (uppercase_letter < 'A' and 'Z' < uppercase_letter):
    c1 = 'A'
    
    while c1 <= uppercase_letter:
        
        # print opening spaces
        print_spaces(ord(uppercase_letter) - ord(c1))

        # print letters
        # ascending
        c2 = 'A'
        while c2 < c1:
            print(c2, end='')
            c2 = chr(ord(c2) + 1)
        
        # descending
        while 'A' <= c2:
            print(c2, end='')
            c2 = chr(ord(c2) - 1)
        
        # print closing spaces
        print_spaces(ord(uppercase_letter) - ord(c1))
        print()

        c1 = chr(ord(c1) + 1)
```

#### Question 6
Write a program that prints a table with each line giving an integer, its square, and its  
cube. Ask the user to input the lower and upper limits for the table. Use a for loop. 

**C**
```C
#include <stdio.h>

int main(void)
{
    long upper = -1, lower = 0;
    int reads;

    printf("This program prints a table of integers with their "
           "squares and cubes.\n");
    do
    {
        printf("Enter lower and upper integer limits (in that order): ");
        reads = scanf("%ld%ld", &lower, &upper);
        if (reads != 2)
        {
            while (getchar() != '\n')
                ; // if read fails, clear input buffer
        }
    } while (lower > upper); // if lower is greater than upper, get new input

    printf("\n");
    // table header
    printf(" Integer       | Square        | Cube          \n");
    printf("---------------|---------------|---------------\n");
    for (long int i = lower; i <= upper; i++)
    {
        printf(" %-14ld| %-14ld| %-14ld\n", i, i * i, i * i * i);
    }
    printf("\n");

    return 0;
}
```

**Python**
```Python
# List comprehension is an elegant way to define and create list in Python. 
# We can create lists just like mathematical statements in one line only. 
# It is also used in getting multiple inputs from a user. 
print("This program prints a table of integers with their \
squares and cubes.")

lower, upper = [int(x) for x in input("Enter lower and upper \
integer limits (in that order): ").split()]

if not lower > upper:
    print(" Integer       | Square        | Cube          ")
    print("---------------|---------------|---------------")

    i = lower
    while i <= upper:
        print(" %-14ld| %-14ld| %-14ld\n" % (i, i * i, i * i * i), end='')
        i += 1
```

#### Question 7
Write a program that reads a single word into a character array and then prints the word  
backward. Hint: Use strlen() (Chapter 4) to compute the index of the last character in  
the array.

**C**
```C
#include <stdio.h>
#include <string.h>

int main(void)
{
    char word[30];

    printf("Enter a string: ");
    scanf("%s", word);
    for (int i = strlen(word) - 1; i >= 0; i--)
    {
        printf("%c", word[i]);
    }
    printf("\n");

    return 0;
}
```

**Python**
```Python
word = input("Enter a string: ")

i = len(word) - 1

while i >= 0:
    print(word[i], end='')
    i -= 1
```

#### Question 8
Write a program that requests two floating-point numbers and prints the value of their  
difference divided by their product. Have the program loop through pairs of input values  
until the user enters nonnumeric input. 

**C**
```C
#include <stdio.h>

int main(void)
{
    float num1, num2;
    int reads;

    printf("Enter two floating-point numbers: ");
    while (scanf(" %f %f", &num1, &num2) == 2)
    {
        printf("(%.3f - %.3f)/(%.3f * %.3f) = %.3f\n", num1, num2, num1, num2,
               (num1 - num2) / (num1 * num2));
        printf("Enter two floating-point numbers (enter non-numeric to quit): ");
    }

    return 0;
}
```

**Python**
```Python
try:
    num1, num2 = [float(x) for x in input(
        "Enter two floating-point numbers: ").split()]
    while True:
        try:
            if num2 != 0:
                print("(%.3f - %.3f)/(%.3f * %.3f) = %.3f"
                      % (num1, num2, num1, num2, (num1 - num2)/(num1 * num2)))
            else:
                print("Mathematical division by zero shall not allowed.")
            num1, num2 = [float(x) for x in input(
                "Enter two floating-point numbers: ").split()]
        except:
            break
except:
    pass
```

#### Question 9
Modify exercise 8 so that it uses a function to return the value of the calculation.

**C**
```C
#include <stdio.h>

float calculate(float n1, float n2);

int main(void)
{
    float num1, num2;
    int reads;
    
    printf("Enter two floating-point numbers: ");
    while (scanf(" %f %f", &num1, &num2) == 2)
    {
        printf("(%.3f - %.3f)/(%.3f * %.3f) = %.3f\n", num1, num2, num1, num2,
               calculate(num1, num2));
        printf("Enter two floating-point numbers (enter non-numeric to quit): ");
    }

    return 0;
}

float calculate(float n1, float n2)
{
    return (n1 - n2) / (n1 * n2);
}
```

**Python**
```Python
'''
Developer often wants a user to enter multiple values or inputs in one line. In C++/C user can take multiple inputs in one line using scanf but in Python user can take multiple values or inputs in one line by two methods. 
    Using split() method
    Using List comprehension
'''

def calculate(n1, n2):
    return (n1 - n2) / (n1 * n2)

try:
    num1, num2 = [float(x) for x in input(
        "Enter two floating-point numbers: ").split()]
    while True:
        try:
            if num2 != 0:
                print("(%.3f - %.3f)/(%.3f * %.3f) = %.3f"
                      % (num1, num2, num1, num2, calculate(num1, num2)))
            else:
                print("Mathematical division by zero shall not allowed.")
            num1, num2 = [float(x) for x in input(
                "Enter two floating-point numbers: ").split()]
        except:
            break
except:
    pass
```

#### Question 10
Write a program that requests lower and upper integer limits, calculates the sum of all  
the integer squares from the square of the lower limit to the square of the upper limit,  
and displays the answer. The program should then continue to prompt for limits and  
display answers until the user enters an upper limit that is equal to or less than the lower  
limit. A sample run should look something like this:
```
Enter lower and upper integer limits: 5 9
The sums of the squares from 25 to 81 is 255
Enter next set of limits: 3 25
The sums of the squares from 9 to 625 is 5520
Enter next set of limits: 5 5
Done
```
**C**
```C
#include <stdio.h>

int sum_of_squares(int lower, int upper);

int main(void)
{
    int upper, lower, reads;

    printf("Enter lower and upper integer limits: ");
    while (reads = scanf("%d%d", &lower, &upper), reads == 2 && lower < upper)
    {
        printf("The sums of the squares from %d to %d is %d\n",
               lower * lower, upper * upper, sum_of_squares(lower, upper));
        printf("Enter next set of limits: ");
    }
    printf("Done\n");

    return 0;
}

int sum_of_squares(int lower, int upper) // calculate sum of squares from lower to upper
{
    int sum = 0;

    for (int i = lower; i <= upper; i++)
    {
        sum += i * i;
    }

    return sum;
}
```

**Python**
```Python
lower, upper = [int(x) for x in input("Enter two value: ").split()]

def sum_of_squares(lower, upper):
    p_sum = 0
    for i in range(lower, upper+1):
        p_sum += i*i
    return p_sum


while lower != upper:
    print("The sums of the squares from %d to %d is %d" %
          (lower * lower, upper * upper, sum_of_squares(lower, upper)))
    lower, upper = [int(x) for x in input("Enter two value: ").split()]
```

#### Page 243
#### Question 11
Write a program that reads eight integers into an array and then prints them in reverse  
order.

**C**
```C
#include <stdio.h>

int main(void)
{
    int int_array[8];
    int i; // array index

    printf("Enter 8 integers:\n");
    for (i = 0; i < 8; i++) // read ints into array
    {
        scanf("%d", &int_array[i]);
    }
    for (i--; i >= 0; i--) // decrement i to 7 to initialize loop
    {
        printf("%d", int_array[i]);
    }
    printf("\n");

    return 0;
}
```

**Python**
```Python
# Create a slice that starts at the end of the string, and moves backwards.
# In this particular example, the slice statement [::-1] means start at the 
# end of the string and end at position 0, move with the step -1, negative one, 
# which means one step backwards. 
int_ = input("Enter 8 integers:")[::-1]
print(int_)
```

#### Question 12
Consider these two infinite series:
```
1.0 + 1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ...
1.0 - 1.0/2.0 + 1.0/3.0 - 1.0/4.0 + ...
```
Write a program that evaluates running totals of these two series up to some limit of number of  
terms. Hint: –1 times itself an odd number of times is –1, and –1 times itself  
an even number of times is 1. Have the user enter the limit interactively; let a zero or  
negative value terminate input. Look at the running totals after 100 terms, 1000 terms,  
10,000 terms. Does either series appear to be converging to some value? 

**C**
```C
#include <stdio.h>

int main(void)
{
    long int limit;
    float sign = 1.0f;
    float series1 = 0, series2 = 0;

    printf("Enter a number of terms to sum: ");
    scanf("%ld", &limit);

    for (long int i = 1; i <= limit; i++)
    {
        series1 += 1.0f / i;
        series2 += (1.0f / i) * sign;
        sign = -sign; // toggle sign
    }

    printf("The %ldth partial sum for series 1 is: %.5f\n", limit, series1);
    printf("The %ldth partial sum for series 2 is: %.5f\n", limit, series2);

    // Answer: Series 1 has no limit. Series 2 appears to be bounded above

    return 0;
}
```

**Python**
```Python
i = 1
sign = 1.0
series1, series2 = 0, 0

limit = int(input("Enter a number of terms to sum: "))

while i <= limit:
    series1 += 1.0/i
    series2 += 1.0/i * sign
    sign = -sign
    i += 1

print("The %ldth partial sum for series 1 is: %.5f" % (limit, series1))
print("The %ldth partial sum for series 2 is: %.5f" % (limit, series2))
```

#### Question 13
Write a program that creates an eight-element array of ints and sets the elements to the  
first eight powers of 2 and then prints the values. Use a for loop to set the values, and,  
for variety, use a do while loop to display the values.

**C**
```C
#include <stdio.h>

int main(void)
{
    int powers_of_2[8];
    int power = 1;
    int i;

    for (int i = 0; i < 8; i++)
    {
        power *= 2;
        powers_of_2[i] = power;
    }
    printf("Powers of 2:\n");
    i = 0;
    do
    {
        printf("%d ", powers_of_2[i]);
        i++;
    } while (i < 8);
    printf("\n");

    return 0;
}
```

**Python**
```Python
print("Powers of 2:")
x = []
for i in range(1, 9):
    n = 2**i
    x.append(n)

for n in x:
    print(n, end=' ')
```

#### Question 14
Write a program that creates two eight-element arrays of doubles and uses a loop to let  
the user enter values for the eight elements of the first array. Have the program set  
the elements of the second array to the cumulative totals of the elements of the first array.  
For example, the fourth element of the second array should equal the sum of the first  
four elements of the first array, and the fifth element of the second array should equal  
the sum of the first five elements of the first array. (It’s possible to do this with nested  
loops, but by using the fact that the fifth element of the second array equals the fourth  
element of the second array plus the fifth element of the first array, you can avoid  
nesting and just use a single loop for this task.) Finally, use loops to display the contents  
of the two arrays, with the first array displayed on one line and with each element of the  
second array displayed below the corresponding element of the first array.

**C**
```C
#include <stdio.h>

int main(void)
{
    int int_array[8], cumulative_sum[8];
    int sum = 0;

    printf("Enter 8 integers:\n");
    for (int i = 0; i < 8; i++)
    {
        scanf("%d", &int_array[i]);
        sum += int_array[i];
        cumulative_sum[i] = sum;
    }
    printf("\n");
    // display loops
    printf("      Integers:");
    for (int i = 0; i < 8; i++)
    {
        printf("%6d ", int_array[i]);
    }
    printf("\n");
    printf("Cumulative sum:");
    for (int i = 0; i < 8; i++)
    {
        printf("%6d ", cumulative_sum[i]);
    }
    printf("\n");

    return 0;
}
```

**Python**
```Python
x = [int(x) for x in input("Enter multiple value: ").split(" ")]

# First line
int_array = [int(a) for a in x]
print("      Integers:", end=' ')
for n in int_array:
    print("%6d" % n, end='')

# Second Line
print("\nCumulative sum:", end=' ')
p_sum = 0
for n in int_array:
    p_sum += int_array[n-1]
    print("%6d" % p_sum, end='')
```

#### Question 15
Write a program that reads in a line of input and then prints the line in reverse order.  
You can store the input in an array of char; assume that the line is no longer than 255  
characters. Recall that you can use scanf() with the %c specifier to read a character at  
a time from input and that the newline character (\n) is generated when you press the  
Enter key.

**C**
```C
#include <stdio.h>

int main(void)
{
    char line[255];
    int i = 0; // array index
    printf("Enter a line to reverse:\n");
    while (scanf("%c", &line[i]), line[i] != '\n')
        i++;

    for (; 0 <= i; i--) // previous loop leaves i in right position
        printf("%c", line[i]);

    printf("\n");

    return 0;
}
```

**Python**
```Python
line = input("Enter a line to reverse:")[::-1]
print(line)
```

#### Question 16
Daphne invests $100 at 10% simple interest. (That is, every year, the investment earns  
an interest equal to 10% of the original investment.) Deirdre invests $100 at 5% interest  
compounded annually. (That is, interest is 5% of the current balance, including previous  
addition of interest.) Write a program that finds how many years it takes for the value  
of Deirdre’s investment to exceed the value of Daphne’s investment. Also show the two  
values at that time.

**C**
```C
#include <stdio.h>

int main(void)
{
    const float DEIRDE_PRINCIPLE = 100.0f;
    const float DAPHNE_PRINCIPLE = 100.0f;
    const float DEIRDE_INTEREST = 0.05f;
    const float DAPHNE_INTEREST = 0.10f;

    // initialize years and balances
    int years = 0;
    float daphne_balance = DAPHNE_PRINCIPLE;
    float deirdre_balance = DEIRDE_PRINCIPLE;

    while (deirdre_balance <= daphne_balance)
    {
        // eq. for compound interest
        deirdre_balance *= 1.0f + DEIRDE_INTEREST;
        // eq. for simple interest
        daphne_balance += DAPHNE_PRINCIPLE * DAPHNE_INTEREST;
        years++;
    }
    printf("After %d years, Daphne's investment is worth $%.2f and "
           "Deirdre’s investment is worth $%.2f.\n",
           years,
           daphne_balance, deirdre_balance);

    return 0;
}
```

**Python**
```Python
DEIRDE_PRINCIPLE = 100
DAPHNE_PRINCIPLE = 100

DEIRDE_INTEREST = 0.05
DAPHNE_INTEREST = 0.10

daphne_balance = DAPHNE_PRINCIPLE
deirdre_balance = DEIRDE_PRINCIPLE

years = 0
while deirdre_balance <= daphne_balance:
    deirdre_balance *= 1.0 + DEIRDE_INTEREST
    daphne_balance += DAPHNE_PRINCIPLE * DAPHNE_INTEREST
    years += 1

print("After %d years, Daphne's investment is worth $%.2f and "
      "Deirdre’s investment is worth $%.2f." %
      (years, daphne_balance, deirdre_balance))
```

#### Page 244
#### Question 17
Chuckie Lucky won a million dollars (after taxes), which he places in an account that  
earns 8% a year. On the last day of each year, Chuckie withdraws $100,000. Write a  
program that finds out how many years it takes for Chuckie to empty his account.

**C**
```C
#include <stdio.h>

int main(void)
{
    const float WINNINGS = 1000000.0f;
    const float INTEREST = 0.08f;
    const float SPENDING = 100000.0f;

    int years = 0;
    float balance = WINNINGS;

    // the problem is not quite clear, but I'm assuming
    // Chuckie makes his first withdrawal before collecting
    // any interest
    while (balance > 0)
    {
        balance -= SPENDING;
        balance *= 1.0f + INTEREST;
        years++;
    }

    printf("After %d years, Chuckie is in the red with a balance of"
           " %.2f USD.\n",
           years, balance);

    return 0;
}
```

**Python**
```Python
WINNINGS = 1000000
INTEREST = 0.08
SPENDING = 100000

years = 0
balance = WINNINGS

while balance > 0:
    balance -= SPENDING
    balance *= 1.0 + INTEREST
    years += 1

print("After %d years, Chuckie is in the red with a balance of"
      " %.2f USD." % (years, balance))
```

#### Page 241
#### Question 18
Professor Rabnud joined a social media group. Initially he had five friends. He noticed  
that his friend count grew in the following fashion. The first week one friend dropped  
out and the remaining number of friends doubled. The second week two friends dropped  
out and the remaining number of friends doubled. In general, in the Nth week, N friends  
dropped out and the remaining number doubled. Write a program that computes and  
displays the number of friends each week. The program should continue until the count  
exceeds Dunbar’s number. Dunbar’s number is a rough estimate of the maximum size of  
a cohesive social group in which each member knows every other member and how they  
relate to one another. Its approximate value is 150.


**C**
```C
#include <stdio.h>

int main(void)
{
    const int DUNBARS_NUMBER = 150;

    int friends = 5, week = 0;

    printf("Week | Friends\n");
    printf("-----+--------\n");
    while (friends < DUNBARS_NUMBER)
    {
        printf("%4d | %7d\n", week, friends);
        week++;
        friends -= week;
        friends *= 2;
    }

    return 0;
}
```

**Python**
```Python
DUNBARS_NUMBER = 150
friends = 5
week = 0
print("Week | Friends")
print("-----+--------")

while friends < DUNBARS_NUMBER:
    print("%4d | %7d" % (week, friends))
    week += 1
    friends -= week
    friends *= 2
```

## Chapter 7 C Control Statements: Branching and Jumps
#### Page 296
#### Question 1
Write a program that reads input until encountering the # character and then reports  
the number of spaces read, the number of newline characters read, and the number of all  
other characters read.

**C**
```C
#include <stdio.h>
#define STOP '#'

int main(void)
{
    char ch;
    unsigned int spaces = 0, newlines = 0, other = 0;
    printf("Enter input (%c to stop):\n", STOP);
    while ((ch = getchar()) != STOP)
    {
        if (ch == ' ')
            spaces++;
        else if (ch == '\n')
            newlines++;
        else
            other++;
    }
    printf("\n");
    printf("Character Count:\n");
    printf("\n");
    printf("Spaces: %u\n"
           "Newlines: %u\n"
           "Other: %u\n",
           spaces, newlines, other);

    return 0;
}
```

**Python**
```Python
lines = []
while True:
    line = input("Enter input (# to stop):")
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

spaces = text.count(' ')
newlines = text.count('\n')
other = len(text) - spaces - newlines
print("Character Count:")
print()
print("Spaces: %u\n"
      "Newlines: %u\n"
      "Other: %u" % (spaces, newlines, other))
```

#### Question 2
Write a program that reads input until encountering #. Have the program print each  
input character and its ASCII decimal code. Print eight character-code pairs per line.  
Suggestion: Use a character count and the modulus operator (%) to print a newline  
character for every eight cycles of the loop.

**C**
```C
#include <stdio.h>
#define STOP '#'

#define SPACE ' '
#define TAB '\t'
#define NEWLINE '\n'
#define BACKSPACE '\b'

int main(void)
{
    unsigned int count = 0;
    char ch;
    printf("ASCII Character Codes\n");
    printf("Enter input (%c to stop):\n", STOP);
    while ((ch = getchar()) != STOP)
    {
        switch (ch)
        {
        case SPACE:
            printf("' ': %3d ", ch);
            break;
        case TAB:
            printf("'\\t': %3d ", ch);
            break;
        case NEWLINE:
            printf("'\\n': %3d ", ch);
            break;
        case BACKSPACE:
            printf("'\\b': %3d ", ch);
            break;
        default:
            printf(" %c : %3d ", ch, ch);
        }
        count++;
        if (count % 8 == 0)
            printf("\n");
    }
    printf("\n");
    return 0;
}
```

**Python**
```Python
count = 0
ch = input("Enter input: ")

for n in ch:
    if n == '#':
        break
    else:
        print(n + ':', ord(n), end=' ')
        count += 1
        if count % 8 == 0:
            print("\n")
```

#### Question 3
Write a program that reads integers until 0 is entered. After input terminates, the  
program should report the total number of even integers (excluding the 0) entered, the  
average value of the even integers, the total number of odd integers entered, and the  
average value of the odd integers.

**C**
```C
#include <stdio.h>
#include <ctype.h>

#define STOP 0

int main(void)
{
    int even_count = 0, even_sum = 0, odd_count = 0, odd_sum = 0;
    float even_avg, odd_avg;
    int input;

    printf("Enter integers (0 to stop):\n");
    while (scanf("%d", &input) == 1 && input != STOP)
    {
        if (input % 2 == 0)
        {
            even_count++;
            even_sum += input;
        }
        else
        {
            odd_count++;
            odd_sum += input;
        }
    }

    even_avg = even_sum / (float)even_count;
    odd_avg = odd_sum / (float)odd_count;

    printf("Number of even integers: %d\n", even_count);
    printf("Average value of even integers: %.2f\n", even_avg);
    printf("Number of odd integers: %d\n", odd_count);
    printf("Average value of odd integers: %.2f\n", odd_avg);

    return 0;
}
```

**Python**
```Python
word = '0'
ch = input("Enter integers (0 to stop):")
even = []
odd = []
while ch != word:
    if int(ch) % 2 == 0:
        even.append(int(ch))
    elif int(ch) % 2 == 1:
        odd.append(int(ch))
    else:
        pass
    ch = input("Enter integers (0 to stop):")

if len(even) > 0:
    even_avg = sum(even)/len(even)
if len(odd) > 0:
    odd_avg = sum(odd)/len(odd)

print("Number of even integers: ", len(even))
print("Average value of even integers: %.2f" % even_avg)
print("Number of odd integers: ", len(odd))
print("Average value of odd integers: %.2f" % odd_avg)
```

#### Question 4
Using if else statements, write a program that reads input up to #, replaces each period  
with an exclamation mark, replaces each exclamation mark initially present with two  
exclamation marks, and reports at the end the number of substitutions it has made.

**C**
```C
#include <stdio.h>
#define STOP '#'

int main(void)
{
    char ch;
    int substitutions = 0;

    printf("Enter input (%c to exit):\n", STOP);
    while ((ch = getchar()) != STOP)
    {
        if (ch == '.')
        {
            printf("!");
            substitutions++;
        }
        else if (ch == '!')
        {
            printf("!!");
            substitutions++;
        }
        else
            printf("%c", ch);
    }

    printf("\nThe number of substitutionsit has made: %d", substitutions);

    return 0;
}
```

**Python**
```Python
ch = input("Enter input: ").split('#')
a = ch[0].replace('!', '!!').replace('.', '!')
print()
print(a)
print()
substitutions = ch[0].count('.') + ch[0].count('!')
print("The number of substitutionsit has made: %d" % substitutions)
```

#### Question 5
Redo exercise 4 using a *switch*. 

**C**
```C
#include <stdio.h>
#define STOP '#'

int main(void)
{
    char ch;
    int substitutions = 0;

    printf("Enter input (%c to exit):\n", STOP);
    while ((ch = getchar()) != STOP)
    {
        switch (ch)
        {
        case '.':
        {
            printf("!");
            substitutions++;
        }
        break;
        case '!':
        {
            printf("!!");
            substitutions++;
        }
        break;
        default:
            printf("%c", ch);
        }
    }

    printf("\nThe number of substitutionsit has made: %d", substitutions);

    return 0;
}
```

**Python**

[Why isn’t there a switch or case statement in Python?](https://docs.python.org/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python)

You can do this easily enough with a sequence of <kbd>if... elif... elif... else</kbd>. There have been some proposals for switch statement syntax, but there is no consensus (yet) on whether and how to do range tests. See [PEP 275](https://www.python.org/dev/peps/pep-0275) for complete details and the current status.

For cases where you need to choose from a very large number of possibilities, you can create a dictionary mapping case values to functions to call. For example:

```Python
def function_1(...):
    ...

functions = {'a': function_1,
             'b': function_2,
             'c': self.method_1, ...}

func = functions[value]
func() 
```

#### Question 6
Write a program that reads input up to # and reports the number of times that the  
sequence ei occurs.

**C**
```C
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

#define STOP '#'

int main(void)
{
    char ch;
    unsigned int ei_count = 0;
    bool e_flag = false;

    printf("This program reads input and counts the number of times the\n"
           "sequence 'ei' occurs (case insensitive).\n");
    printf("Enter input (%c to stop):\n", STOP);

    while ((ch = getchar()) != STOP)
    {
        ch = tolower(ch);
        if (ch == 'e')
            e_flag = true;
        else if (ch == 'i')
        {
            if (e_flag)
                ei_count++;
            e_flag = false;
        }
        else
            e_flag = false;
    }

    printf("The sequence 'ei' occurs %u times.\n", ei_count);

    return 0;
}
```

**Python**
```Python
ch = input("Enter input: ").split('#')
occur = ch[0].count('ei') 
print("The sequence 'ei' occurs %d times. " % occur)
```

#### Question 7
Write a program that requests the hours worked in a week and then prints the gross pay,  
the taxes, and the net pay. Assume the following:  
a. Basic pay rate = $10.00/hr  
b. Overtime (in excess of 40 hours) = time and a half  
c. Tax rate: #15% of the first $300  
20% of the next $150  
25% of the rest  
Use #define constants, and don’t worry if the example does not conform to current  
tax law. 

*Note:  
Chinese version (姜佑 译, 人民邮电出版社 ISBN 9787115390592) has an error in translation here (Page 215).  
In English version, Basic pay rate = $10.00/hr.  
In Chinese version, Basic pay rate = $1000/hr.  
Since a period is missing, that value will lead you to a totally different answer.*

**C**
```C
#include <stdio.h>

#define BASIC_RATE 10.0
#define OVERTIME_HOURS 40.0
#define OVERTIME_MULTIPLIER 1.5
#define TAX_RATE_1 0.15
#define TAX_BRACKET_1 300.0
#define TAX_RATE_2 0.20
#define TAX_BRACKET_2 450.0
#define TAX_RATE_3 0.25

float calculate_gross_pay(float hours);
float calculate_taxes(float gross_pay);

int main(void)
{
    float hours, gross_pay, taxes, net_income;

    printf("Enter number of hours worked in a week: ");

    if (scanf("%f", &hours) == 1)
    {
        gross_pay = calculate_gross_pay(hours);
        taxes = calculate_taxes(gross_pay);
        net_income = gross_pay - taxes;
        printf("For %.1f hours of work you make $%.2f and pay $%.2f in taxes.\n",
               hours, gross_pay, taxes);
        printf("And your netincome: $%.2f", net_income);
    }
    else
        printf("Invalid input...terminating.\n");

    return 0;
}

float calculate_gross_pay(float hours)
{
    if (hours > OVERTIME_HOURS)
        return OVERTIME_HOURS * BASIC_RATE + (hours - OVERTIME_HOURS) * BASIC_RATE * OVERTIME_MULTIPLIER;
    else
        return hours * BASIC_RATE;
}

float calculate_taxes(float gross_pay)
{
    if (gross_pay > TAX_BRACKET_2)
        return TAX_RATE_3 * (gross_pay - TAX_BRACKET_2) + TAX_RATE_2 * (TAX_BRACKET_2 - TAX_BRACKET_1) + TAX_RATE_1 * TAX_BRACKET_1;
    else if (gross_pay > TAX_BRACKET_1)
        return TAX_RATE_2 * (gross_pay - TAX_BRACKET_1) + TAX_RATE_1 * TAX_BRACKET_1;
    else
        return TAX_RATE_1 * gross_pay;
}
```

**Python**
```Python
basic_salary = 10.00
over_time = 1.5

working_hour = float(input("Enter your working hours (per week): "))
total_income = 0
if working_hour <= 40:
    total_income = basic_salary * working_hour
else:
    total_income = basic_salary * 40 + basic_salary * over_time * (working_hour - 40)

if total_income <= 300:
    tax_rate = .15
    tax = total_income * tax_rate

elif total_income > 300 and total_income <= 450:
    tax_rate = .2
    tax = 300 * .15 + (total_income - 300) * tax_rate

else:
    tax_rate = .25
    tax = 300 * .15 + 150 * .2 + (total_income - 450) * tax_rate

net_income = total_income - tax

print("Your total income: $%.2f" % total_income)
print("Your tax: $%.2f" % tax)
print("Your net income: $%.2f" % net_income) 
```

#### Question 8
Modify assumption a. in exercise 7 so that the program presents a menu of pay rates  
from which to choose. Use a switch to select the pay rate. The beginning of a run  
should look something like this:

```
*****************************************************************
Enter the number corresponding to the desired pay rate or action:
1) $8.75/hr 							2) $9.33/hr
3) $10.00/hr 						4) $11.20/hr
5) quit 
*****************************************************************
```

If choices 1 through 4 are selected, the program should request the hours worked. The  
program should recycle until 5 is entered. If something other than choices 1 through 5  
is entered, the program should remind the user what the proper choices are and then  
recycle. Use #defined constants for the various earning rates and tax rates.

**C**
```C
#include <stdio.h>
#include <stdbool.h>

#define RATE_1 8.75
#define RATE_2 9.33
#define RATE_3 10.00
#define RATE_4 11.20

#define OVERTIME_HOURS 40.0
#define OVERTIME_MULTIPLIER 1.5
#define TAX_RATE_1 0.15
#define TAX_BRACKET_1 300.0
#define TAX_RATE_2 0.20
#define TAX_BRACKET_2 450.0
#define TAX_RATE_3 0.25

void flush_input_buffer(void);
float calculate_gross_pay(float hours, float rate);
float calulate_taxes(float gross_pay);

int main(void)
{
    bool exit_flag = false;
    int rate_option;
    float rate, hours, gross_pay, taxes;

    while (1) // main program loop
    {

        // print usage instructions
        printf("*****************************************************************\n");
        printf("Enter the number corresponding to the desired pay rate or action:\n");
        printf("1) $%.2f/hr 				2) $%.2f/hr\n", RATE_1, RATE_2);
        printf("3) $%.2f/hr 				4) $%.2f/hr\n", RATE_3, RATE_4);
        printf("5) quit \n");
        printf("*****************************************************************\n");

        scanf("%d", &rate_option);
        switch (rate_option)
        {
        case (1):
            rate = RATE_1;
            break;
        case (2):
            rate = RATE_2;
            break;
        case (3):
            rate = RATE_3;
            break;
        case (4):
            rate = RATE_4;
            break;
        case (5):
            exit_flag = true;
            break;
        default: // invalid input
            flush_input_buffer();
            printf("Please enter an integer between 1 and 5.\n\n");
            continue; // repeat main program loop
        }

        if (exit_flag)
            break; // exit program

        printf("Enter number of hours worked in a week: ");
        while (scanf("%f", &hours) != 1 || hours <= 0)
        {
            flush_input_buffer();
            printf("Please enter a positive number. \n");
            printf("Enter number of hours worked in a week: ");
        }

        gross_pay = calculate_gross_pay(hours, rate);
        taxes = calulate_taxes(gross_pay);

        printf("For %.1f hours of work at $%.2f/hr, you make $%.2f and pay"
               " $%.2f in taxes.\n",
               hours, rate, gross_pay, taxes);
        printf("\n");
    }

    printf("Bye.\n");

    return 0;
}

void flush_input_buffer(void)
{
    while (getchar() != '\n')
        ;
}

float calculate_gross_pay(float hours, float rate)
{
    if (hours > OVERTIME_HOURS)
        return OVERTIME_HOURS * rate + (hours - OVERTIME_HOURS) * rate * OVERTIME_MULTIPLIER;
    else
        return hours * rate;
}

float calulate_taxes(float gross_pay)
{
    if (gross_pay > TAX_BRACKET_2)
        return TAX_RATE_3 * (gross_pay - TAX_BRACKET_2) + TAX_RATE_2 * (TAX_BRACKET_2 - TAX_BRACKET_1) + TAX_RATE_1 * TAX_BRACKET_1;
    else if (gross_pay > TAX_BRACKET_1)
        return TAX_RATE_2 * (gross_pay - TAX_BRACKET_1) + TAX_RATE_1 * TAX_BRACKET_1;
    else
        return TAX_RATE_1 * gross_pay;
}
```

**Python**
```Python
RATE_1 = 8.75
RATE_2 = 9.33
RATE_3 = 10.00
RATE_4 = 11.20

over_time = 1.5


def Clannad(basic_salary):
    working_hour = float(input("Enter your working hours (per week): "))
    total_income = 0

    if working_hour <= 40:
        total_income = basic_salary * working_hour
    else:
        total_income = basic_salary * 40 + \
            basic_salary * over_time * (working_hour - 40)

    if total_income <= 300:
        tax_rate = .15
        tax = total_income * tax_rate

    elif total_income > 300 and total_income <= 450:
        tax_rate = .2
        tax = 300 * .15 + (total_income - 300) * tax_rate

    else:
        tax_rate = .25
        tax = 300 * .15 + 150 * .2 + (total_income - 450) * tax_rate

    net_income = total_income - tax

    print("Your total income: $%.2f" % total_income)
    print("Your tax: $%.2f" % tax)
    print("Your net income: $%.2f" % net_income)


def menu():
    print("*****************************************************************")
    print("Enter the number corresponding to the desired pay rate or action:")
    print("1) $%.2f/hr 				2) $%.2f/hr" % (RATE_1, RATE_2))
    print("3) $%.2f/hr 				4) $%.2f/hr" % (RATE_3, RATE_4))
    print("5) quit")
    print("*****************************************************************")


menu()
choice = input()
while choice != '5':
    if choice.isdecimal():
        choice = int(choice)
        if choice == 1:
            Clannad(RATE_1)
        elif choice == 2:
            Clannad(RATE_2)
        elif choice == 3:
            Clannad(RATE_3)
        elif choice == 4:
            Clannad(RATE_4)
        else:
            print("Input the right option, please.")
    else:
        print("Input the right option, please.")
    print()
    menu()
    choice = input()
```

#### Question 9
Write a program that accepts a positive integer as input and then displays all the prime  
numbers smaller than or equal to that number.

**C**
```C
#include <stdio.h>
#include <stdbool.h>

void flush_input_buffer(void);

int main(void)
{
    bool prime_flag;
    int limit;
    printf("Primes: this program prints all primes less than or equal to any positive integer.\n");
    printf("Enter a positive integer: \n");
    while (scanf("%d", &limit) != 1 || limit < 1)
    {
        flush_input_buffer();
        printf("Enter a positive integer: \n");
    }

    for (int i = 2; i <= limit; i++)
    {
        prime_flag = true;
        for (int j = 2; j < i; j++) // for all j less than i ...
        {
            if (i % j == 0) // if i is divisible by j ...
            {
                prime_flag = false; // then i is not prime
                break;              // break out of inner loop
            }
        }
        if (prime_flag)
            printf("%d is prime.\n", i);
    }

    return 0;
}

void flush_input_buffer(void)
{
    while (getchar() != '\n')
        ;
}
```

**Python**
```Python
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


number = input("Please enter a positive integer: ")

if number.isdecimal():
    number = int(number)
    if number >= 0:
        for i in range(1, number):
            if is_prime(i):
                print(f'{i} is prime')
    else:
        pass
```

#### Question 10
The 1988 United States Federal Tax Schedule was the simplest in recent times. It had  
four categories, and each category had two rates. Here is a summary (dollar amounts are  
taxable income):
```
Category					Tax
Single						15% of first $17,850 plus 28% of excess
Head of Household			15% of first $23,900 plus 28% of excess
Married, Joint				15% of first $29,750 plus 28% of excess
Married, Separate			15% of first $14,875 plus 28% of excess
```
For example, a single wage earner with a taxable income of $20,000 owes 0.15 × $17,850  
\+ 0.28 × ($20,000−$17,850). Write a program that lets the user specify the tax category  
and the taxable income and that then calculates the tax. Use a loop so that the user can  
enter several tax cases.

**C**
```C
#include <stdio.h>

#define SINGLE 1
#define HEAD_OF_HOUSEHOLD 2
#define MARRIED_JOINT 3
#define MARRIED_SEPARATE 4
#define EXIT 5

#define RATE_1 0.15f
#define RATE_2 0.28f

void flush_input_buffer(void);

int main(void)
{
    int category;
    float income, bracket, taxes;

    printf("US 1988 Tax Calculator\n");

    while(1)
    {
        printf("1) Single  2) Head of Household  3) Married, Joint  4) Married Separate\n");
        printf("Enter your tax category (1-4) or 5 to quit: ");
        scanf("%d", &category);

        switch (category)
        {
            case (SINGLE) :	
                    bracket = 17850.0;
                    break;
            case (HEAD_OF_HOUSEHOLD) :
                    bracket = 23900.0;
                    break;
            case (MARRIED_JOINT) :
                    bracket = 29750.0;
                    break;
            case (MARRIED_SEPARATE) :
                    bracket = 14875.0;
                    break;
            case (EXIT) : 
                    printf("Bye.\n");
                    return 0; // Exit Program
            default :
                    flush_input_buffer();
                    printf("Invalid input: please enter an integer between 1 and 5.\n");
                    continue;
        }
        printf("Enter your income: ");
        while (scanf("%f", &income) != 1 || income < 0)
        {
            flush_input_buffer();
            printf("Invalid input: please enter a positive number.\n");
            printf("Enter your income: ");
        }

        if (income > bracket)
            taxes = RATE_2 * (income - bracket) + RATE_1 * bracket;
        else
            taxes = RATE_1 * income;

        printf("You will owe $%.2f in taxes.\n\n", taxes);
    }
}

void flush_input_buffer(void)
{
    while (getchar() != '\n')
        ;
}
```

**Python**
```Python
tax_rate_1 = .15
tax_rate_2 = .28

print("US 1988 Tax Calculator")
print("1) Single  2) Head of Household  3) Married, Joint  4) Married Separate")
category = input("Enter your tax category (1-4) or 5 to quit: ")

def Clannad(bracket):
    taxable_income = int(input("Enter your income: "))
    if taxable_income > 0:
        tax = (taxable_income - bracket) * tax_rate_2 + bracket * tax_rate_1
        print("You will owe $%.2f in taxes." % tax)

while category != '5':
    if category.isdecimal():
        if category == '1':
            bracket = 17850
            Clannad(bracket)
        elif category == '2':
            bracket = 23900
            Clannad(bracket)
        elif category == '3':
            bracket = 29750
            Clannad(bracket)
        elif category == '4':
            bracket = 14875
            Clannad(bracket)
        else:
            print("Input the right option, please.")
    else:
        print("Input the right option, please.")
    print()
    print("1) Single  2) Head of Household  3) Married, Joint  4) Married Separate")
    category = input("Enter your tax category (1-4) or 5 to quit: ")
```

#### Question 11
The ABC Mail Order Grocery sells artichokes for $2.05 per pound, beets for $1.15 per  
pound, and carrots for $1.09 per pound. It gives a 5% discount for orders of $100 or  
more prior to adding shipping costs. It charges $6.50 shipping and handling for any  
order of 5 pounds or under, $14.00 shipping and handling for orders over 5 pounds  
and under 20 pounds, and $14.00 plus $0.50 per pound for shipments of 20 pounds or  
more. Write a program that uses a switch statement in a loop such that a response of a  
lets the user enter the pounds of artichokes desired, b the pounds of beets, c the pounds  
of carrots, and q allows the user to exit the ordering process. The program should keep  
track of cumulative totals. That is, if the user enters 4 pounds of beets and later enters  
5 pounds of beets, the program should use report 9 pounds of beets. The program then  
should compute the total charges, the discount, if any, the shipping charges, and the  
grand total. The program then should display all the purchase information: the cost per  
pound, the pounds ordered, and the cost for that order for each vegetable, the total cost  
of the order, the discount (if there is one), the shipping charge, and the grand total of all  
the charges.

**C**
```C
#include <stdio.h>
#include <stdbool.h>

#define ARTICHOKE_PRICE_PER_LB 2.05
#define BEET_PRICE_PER_LB 1.15
#define CARROT_PRICE_PER_LB 1.09

#define SHIPPING_5LB 6.50
#define SHIPPING_20LB 14.00
#define SHIPPING_OVER_20LB_RATE 0.5

#define DISCOUNT_RATE 0.05

void flush_input_buffer(void);
float calculate_shipping(float weight);

int main(void)
{
    float artichoke_weight = 0, beet_weight = 0, carrot_weight = 0, total_weight;
    float artichoke_price, beet_price, carrot_price, subtotal, discount, shipping, total;
    bool discount_flag;
    float weight;
    char option;

    printf("ABC Mail Order Grocery\n");
    while (1)
    {
        printf("What would you like to order?\n");
        printf("a) artichokes  b) beets  c) carrots  q) quit\n");
        option = getchar();
        switch (option)
        {
        case ('q'):
            printf("Bye.\n");
            return 0; // exit program

        case ('a'): // artichokes
            printf("How many pounds of artichokes would you like to add? ");
            if (scanf("%f", &weight) == 1)
                artichoke_weight += weight;
            else
            {
                flush_input_buffer();
                printf("Invalid input. Try again.\n");
                continue; // repeat main program loop
            }
            break;

        case ('b'): // beets
            printf("How many pounds of beets would you like to add? ");
            if (scanf("%f", &weight) == 1)
                beet_weight += weight;
            else
            {
                flush_input_buffer();
                printf("Invalid input. Try again.\n");
                continue; // repeat main program loop
            }
            break;

        case ('c'): // carrots
            printf("How many pounds of carrots would you like to add? ");
            if (scanf("%f", &weight) == 1)
                carrot_weight += weight;
            else
            {
                flush_input_buffer();
                printf("Invalid input. Try again.\n");
                continue; // repeat main program loop
            }
            break;

        default:
            printf("Invalid input. Try again.\n");
            continue; // repeat main program loop
        }

        // calculate subtotal
        artichoke_price = artichoke_weight * ARTICHOKE_PRICE_PER_LB;
        beet_price = beet_weight * BEET_PRICE_PER_LB;
        carrot_price = carrot_weight * CARROT_PRICE_PER_LB;
        subtotal = artichoke_price + beet_price + carrot_price;

        // calculate discount
        if (subtotal >= 100)
        {
            discount_flag = true;
            discount = DISCOUNT_RATE * subtotal;
        }
        else
            discount_flag = false;

        // calculate shipping
        total_weight = artichoke_weight + beet_weight + carrot_weight;
        shipping = calculate_shipping(total_weight);

        // grand total
        total = subtotal + shipping - (discount_flag ? discount : 0.0);

        printf("\n");
        printf("Your order summary:\n\n");
        printf("Artichokes: %.2flbs @ $%.2f/lb: $%.2f\n",
               artichoke_weight, ARTICHOKE_PRICE_PER_LB, artichoke_price);
        printf("Beets: %.2flbs @ $%.2f/lb: $%.2f\n",
               beet_weight, BEET_PRICE_PER_LB, beet_price);
        printf("Carrots: %.2flbs @ $%.2f/lb: $%.2f\n",
               carrot_weight, CARROT_PRICE_PER_LB, carrot_price);
        printf("\n");
        printf("Subtotal: $%.2f\n", subtotal);
        if (discount_flag)
            printf("%.0f%% discount: $%.2f\n", DISCOUNT_RATE * 100, discount);
        printf("Shipping charges: $%.2f\n", shipping);
        printf("Grand total: $%.2f\n", total);
        printf("\n");

        flush_input_buffer();
    }
}

void flush_input_buffer(void)
{
    while (getchar() != '\n')
        ;
}

float calculate_shipping(float weight)
{
    if (weight < 5.0)
        return SHIPPING_5LB;
    else if (weight < 20.0)
        return SHIPPING_20LB;
    else
        return SHIPPING_20LB + SHIPPING_OVER_20LB_RATE * (weight - 20.0);
}
```

**Python**
```Python
ARTICHOKE_PRICE_PER_LB = 2.05
BEET_PRICE_PER_LB = 1.15
CARROT_PRICE_PER_LB = 1.09

SHIPPING_5LB = 6.50
SHIPPING_20LB = 14.00
SHIPPING_OVER_20LB_RATE = 0.5

DISCOUNT_RATE = 0.05

artichoke = 0
beet = 0
carrot = 0


def calculate_shipping(weight):
    if weight < 5.0:
        return SHIPPING_5LB
    elif weight < 20.0:
        return SHIPPING_20LB
    else:
        return SHIPPING_20LB + SHIPPING_OVER_20LB_RATE * (weight - 20.0)


def summary():
    # calculate subtotal
    artichoke_price = artichoke * ARTICHOKE_PRICE_PER_LB
    beet_price = beet * BEET_PRICE_PER_LB
    carrot_price = carrot * CARROT_PRICE_PER_LB
    subtotal = artichoke_price + beet_price + carrot_price

    # calculate shipping
    total_weight = artichoke + beet + carrot
    shipping = calculate_shipping(total_weight)

    # calculate discount
    if subtotal >= 100:
        discount = DISCOUNT_RATE * subtotal
        total = subtotal + shipping - discount
        discount_flag = True
    else:
        total = subtotal + shipping
        discount_flag = False

    print()
    print("Your order summary:\n")
    print("Artichokes: %.2flbs @ $%.2f/lb: $%.2f" %
          (artichoke, ARTICHOKE_PRICE_PER_LB, artichoke_price))
    print("Beets: %.2flbs @ $%.2f/lb: $%.2f" %
          (beet, BEET_PRICE_PER_LB, beet_price))
    print("Carrots: %.2flbs @ $%.2f/lb: $%.2f" %
          (carrot, CARROT_PRICE_PER_LB, carrot_price))
    print()
    print("Subtotal: $%.2f" % subtotal)
    print()
    if discount_flag:
        print("%.0f%% discount: \t\t$%.2f" % (DISCOUNT_RATE * 100, discount))
    print("Shipping charges: \t$%.2f" % shipping)
    print("Grand total: \t\t$%.2f" % total)
    print()


def order():
    print("What would you like to order?")
    print("a) artichokes  b) beets  c) carrots  q) quit")


order()
option = input()
while option != 'q':
    if option == 'a':
        weight = int(
            input("How many pounds of artichokes would you like to add? "))
        artichoke += weight

    elif option == 'b':
        weight = int(input("How many pounds of beets would you like to add? "))
        beet += weight

    elif option == 'c':
        weight = int(
            input("How many pounds of carrots would you like to add? "))
        carrot += weight

    else:
        print("Invalid input. please try again.")

    summary()
    order()
    option = input()

print('Bye!')
```

## Chapter 8 Character Input/Output and Input Validation
#### Page 332
Several of the following programs ask for input to be terminated by EOF. If your operating system makes redirection awkward or impossible, use some other test for terminating input, such as reading the & character.

#### Question 1
Devise a program that counts the number of characters in its input up to the end of file.

**C**
```C
#include <stdio.h>

int main(void)
{
    int count = 0;

    while (getchar() != EOF)
    {
        count++;
    }
    printf("Character count: %d\n", count);

    return 0;
}
```

**Python**
```Python
# Reference:
# https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof
# File objects are iterable and yield lines until EOF.
# Using the file object as an iterable uses a buffer to ensure performant reads.
# You can do the same with the stdin:

import sys

for line in sys.stdin:
    count = len(line)

print(count)
```

#### Page 333
#### Question 2
Write a program that reads input as a stream of characters untilencountering EOF. Have  
the program print each input character and its ASCIIdecimal value. Note that characters  
preceding the space character in theASCII sequence are nonprinting characters.  
Treat them specially. If thenonprinting character is a newline or tab, print \n or \t,  
respectively.Otherwise, use control-character notation. For instance, ASCII 1 is Ctrl+A,  
which can be displayed as ^A. Note that the ASCII value for A is the value for Ctrl+A  
plus 64. A similar relation holds for the other nonprintingcharacters. Print 10 pairs per  
line, except start a fresh line each time anewline character is encountered. (Note: The  
operating system may havespecial interpretations for some control characters and keep  
them fromreaching the program.)

**C**
```C
#include <stdio.h>

int main(void)
{
    int ch, char_count = 0;

    while ((ch = getchar()) != EOF)
    {
        if (ch >= ' ')
            printf("\'%c\': %d", ch, ch);
        else if (ch == '\n')
            printf("\'\\n\': %d", ch);
        else if (ch == '\t')
            printf("\'\\t\': %d", ch);
        else // ascii control characters
            printf("\'^%c\': %d", ch + 64, ch);

        char_count++;
        if (char_count % 10 == 0)
            printf("\n"); // print new line for every 10 characters
        else
            printf("  "); // otherwise, print spaces
    }

    printf("\n");

    return 0;
}
```

**Python**
```Python
import sys

counter = 0

for line in sys.stdin:
    for ch in line:
        counter += 1
        # Dealing with '\t'
        if ord(ch) == 9:
            print(r"'\t': 9", end=' ' if counter % 10 != 0 else '\n')
        # Dealing with '\n'
        elif ord(ch) == 10:
            print(r"'\n': 10")
        else:
            print("'%c': %d" % (ch, ord(ch)),
                  end=' ' if counter % 10 != 0 else '\n')
```

#### Question 3
Write a program that reads input as a stream of characters untilencountering EOF.  
Have it report the number of uppercase letters, the numberof lowercase letters, and the  
number of other characters in the input. Youmay assume that the numeric values for the  
lowercase letters are sequentialand assume the same for uppercase. Or, more portably,  
you can useappropriate classification functions from the ctype.h library.

**C**
```C
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int ch;
    int uppercase_count = 0, lowercase_count = 0, other_count = 0;

    while ((ch = getchar()) != EOF)
    {
        if (isupper(ch))
            uppercase_count++;
        else if (islower(ch))
            lowercase_count++;
        else
            other_count++;
    }

    printf("Character Counts\n");
    printf("Uppercase letters: %d\n", uppercase_count);
    printf("Lowercase letters: %d\n", lowercase_count);
    printf("Other: %d\n", other_count);

    return 0;
}
```

**Python**
```Python
import sys

upper = 0
lower = 0
other = 0

for line in sys.stdin:
    for ch in line:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        else:
            other += 1

print("Character Counts")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Other: {other}")
```

#### Question 4
Write a program that reads input as a stream of characters untilencountering EOF. Have  
it report the average number of letters per word.Don’t count whitespace as being letters  
in a word. Actually, punctuationshouldn’t be counted either, but don’t worry about that  
now. (If you do wantto worry about it, consider using the ispunct() function from the  
ctype.hfamily.)

**C**
```C
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int main(void)
{
    int ch;
    bool in_word = false;
    int letter_count = 0, word_count = 0;

    while ((ch = getchar()) != EOF)
    {
        if (isalpha(ch)) // if ch is a letter
        {
            letter_count++;
            // if not currently in a word, then switch state to in word
            // and increment the word count
            if (!in_word)
            {
                in_word = true;
                word_count++;
            }
        }
        // if ch is not a letter, set program state to out of word
        else
            in_word = false;
    }
    // divide letter count by word count to get average letters/word
    printf("Average letters per word: %.2f\n", (float)letter_count / word_count);

    return 0;
}
```

**Python**
```Python
import sys

letter = 0

for line in sys.stdin:
    # str.split() without any arguments splits on runs of whitespace characters
    word = len(line.split())

    for ch in line:
        if ch.isalpha():
            letter += 1

print("Average letters per word: %.2f" % (letter / word))
```

#### Question 5
Modify the guessing program of Listing 8.4 so that it uses a more intelligent guessing  
strategy. For example, have the program initially guess50, and have it ask the user  
whether the guess is high, low, or correct. If,say, the guess is low, have the next guess  
be halfway between 50 and 100,that is, 75. If that guess is high, let the next guess be  
halfway between 75and 50, and so on. Using this binary search strategy, the program  
quicklyzeros in on the correct answer, at least if the user does not cheat.

**C**
```C
#include <stdio.h>

int main(void)
{
    // initial search parameters
    int upper_bound = 100;
    int lower_bound = 0;
    int guess = 50;

    char ch;

    printf("Pick an integer from 1 to 100. I will try to guess ");
    printf("it.\nRespond with a y if my guess is right, with a h if it's");
    printf("\ntoo high and an l if it's too low.\n");
    printf("Uh...is your number %d?\n", guess);

    while ((ch = getchar()) != 'y')
    {
        while (getchar() != '\n') // clear input stream
            ;
        if (ch == 'h')
            upper_bound = guess;
        else if (ch == 'l')
            lower_bound = guess;
        else
        {
            printf("Invalid valid input. Try again.\n");
            continue;
        }
        guess = (upper_bound + lower_bound) / 2.0;
        printf("Well, then, is it %d?\n", guess);
    }

    printf("I knew I could do it!\n");
    return 0;
}
```

**Python**
```Python
upper_bound = 100
lower_bound = 0
guess = 50

print(f"""Pick an integer from 1 to 100. I will try to guess it. 
Respond with a y if my guess is right, with a h if it's
too high and an l if it's too low.
Uh...is your number {guess}?""")

ch = input()

while ch[0] != 'y':
    if ch == 'h':
        upper_bound = guess
    elif ch == 'l':
        lower_bound = guess
    else:
        print("Invalid valid input. Try again.")
        ch = input()
        continue
    guess = (upper_bound + lower_bound) / 2
    print("Well, then, is it %d?" % guess)
    ch = input()

print("I knew I could do it!")
```

#### Question 6
Modify the get_first() function of Listing 8.8 so that it returns the first non-  
whitespace character encountered. Test it in a simple program.

**C**
```C
#include <stdio.h>
#include <ctype.h>

int get_first(void);

int main(void)
{
    int ch;

    printf("Test program for get_first():\n");
    printf("Enter a line; you should see the first non-whitespace\n");
    printf("character echoed in the terminal:\n");

    ch = get_first();
    printf("%c\n", ch);

    return 0;
}

int get_first(void)
{
    // returns first non-whitespace character and clears
    // remaining input until next line break or EOF

    int ch, garbage;

    do
    {
        ch = getchar();
    } while (isspace(ch));

    while ((garbage = getchar()) != '\n' && garbage != EOF)
        ;

    return ch;
}
```

**Python**
```Python
import sys

def get_first():
    for line in sys.stdin:
        for ch in line:
            if ch != ' ':
                return ch
print("""Test program for get_first():
Enter a line; you should see the first non-whitespace
character echoed in the terminal:""")
print(get_first())
```

#### Question 7
Modify Programming Exercise 8 from Chapter 7 so that the menu choices are labeled by  
characters instead of by numbers; use q instead of 5 as the cueto terminate input.

**C**
```C
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

#define RATE_1 8.75
#define RATE_2 9.33
#define RATE_3 10.00
#define RATE_4 11.20

#define OVERTIME_HOURS 40.0
#define OVERTIME_MULTIPLIER 1.5
#define TAX_RATE_1 0.15
#define TAX_BRACKET_1 300.0
#define TAX_RATE_2 0.20
#define TAX_BRACKET_2 450.0
#define TAX_RATE_3 0.25

void flush_input_buffer(void);
float calculate_gross_pay(float hours, float rate);
float calulate_taxes(float gross_pay);
int get_first(void);

int main(void)
{
    bool exit_flag = false;
    int rate_option;
    float rate, hours, gross_pay, taxes;

    while (1) // main program loop
    {

        // print usage instructions
        printf("********************************************************************\n");
        printf("Enter the character corresponding to the desired pay rate or action:\n");
        printf("a) $%.2f/hr 				b) $%.2f/hr\n", RATE_1, RATE_2);
        printf("c) $%.2f/hr 				d) $%.2f/hr\n", RATE_3, RATE_4);
        printf("q) quit \n");
        printf("********************************************************************\n");

        rate_option = get_first();
        switch (rate_option)
        {
        case ('a'):
            rate = RATE_1;
            break;
        case ('b'):
            rate = RATE_2;
            break;
        case ('c'):
            rate = RATE_3;
            break;
        case ('d'):
            rate = RATE_4;
            break;
        case ('q'):
            printf("Bye.\n");
            return 0; // exit program
        default:      // invalid input
            printf("Invalid input. Try again.\n\n");
            continue; // repeat main program loop
        }

        printf("Enter number of hours worked in a week: ");
        while (scanf("%f", &hours) != 1 || hours <= 0)
        {
            flush_input_buffer();
            printf("Please enter a positive number. \n");
            printf("Enter number of hours worked in a week: ");
        }

        gross_pay = calculate_gross_pay(hours, rate);
        taxes = calulate_taxes(gross_pay);

        printf("For %.1f hours of work at $%.2f/hr, you make $%.2f and pay"
               " $%.2f in taxes.\n",
               hours, rate, gross_pay, taxes);
        printf("\n");
    }
}

void flush_input_buffer(void)
{
    while (getchar() != '\n')
        ;
}

float calculate_gross_pay(float hours, float rate)
{
    if (hours > OVERTIME_HOURS)
        return OVERTIME_HOURS * rate + (hours - OVERTIME_HOURS) * rate * OVERTIME_MULTIPLIER;
    else
        return hours * rate;
}

float calulate_taxes(float gross_pay)
{
    if (gross_pay > TAX_BRACKET_2)
        return TAX_RATE_3 * (gross_pay - TAX_BRACKET_2) + TAX_RATE_2 * (TAX_BRACKET_2 - TAX_BRACKET_1) + TAX_RATE_1 * TAX_BRACKET_1;
    else if (gross_pay > TAX_BRACKET_1)
        return TAX_RATE_2 * (gross_pay - TAX_BRACKET_1) + TAX_RATE_1 * TAX_BRACKET_1;
    else
        return TAX_RATE_1 * gross_pay;
}

int get_first(void)
{
    // returns first non-whitespace character and clears
    // remaining input until next line break or EOF

    int ch, garbage;

    do
    {
        ch = getchar();
    } while (isspace(ch));

    while ((garbage = getchar()) != '\n' && garbage != EOF)
        ;

    return ch;
}
```

**Python**
```Python
RATE_1 = 8.75
RATE_2 = 9.33
RATE_3 = 10.00
RATE_4 = 11.20

over_time = 1.5

def Clannad(basic_salary):
    working_hour = float(input("Enter your working hours (per week): "))
    total_income = 0

    if working_hour <= 40:
        total_income = basic_salary * working_hour
    else:
        total_income = basic_salary * 40 + basic_salary * over_time * (working_hour - 40)

    if total_income <= 300:
        tax_rate = .15
        tax = total_income * tax_rate

    elif total_income > 300 and total_income <= 450:
        tax_rate = .2
        tax = 300 * .15 + (total_income - 300) * tax_rate

    else:
        tax_rate = .25
        tax = 300 * .15 + 150 * .2 + (total_income - 450) * tax_rate

    net_income = total_income - tax

    print("Your total income: $%.2f" % total_income)
    print("Your tax: $%.2f" % tax)
    print("Your net income: $%.2f" % net_income)

def menu():
    print("*****************************************************************")
    print("Enter the number corresponding to the desired pay rate or action:")
    print("a) $%.2f/hr 				b) $%.2f/hr" % (RATE_1, RATE_2))
    print("c) $%.2f/hr 				d) $%.2f/hr" % (RATE_3, RATE_4))
    print("q) quit")
    print("*****************************************************************")

menu()
choice = input()
while choice != 'q':
    if choice.isalpha():
        if choice == 'a':
            Clannad(RATE_1)
        elif choice == 'b':
            Clannad(RATE_2)
        elif choice == 'c':
            Clannad(RATE_3)
        elif choice == 'd':
            Clannad(RATE_4)
        else:
            print("Input the right option, please.")
    else:
        print("Input the right option, please.")
    print()
    menu()
    choice = input()
```

#### Question 8
Write a program that shows you a menu offering you the choice of addition,subtraction,  
multiplication, or division. After getting your choice, theprogram asks for two numbers,  
then performs the requested operation. Theprogram should accept only the offered  
menu choices. It should use typefloat for the numbers and allow the user to try again  
if he or she fails toenter a number. In the case of division, the program should prompt  
the userto enter a new value if 0 is entered as the value for the second number. A typical  
program run should look like this:
```
Enter the operation of your choice:
a. add          s. subtract
m. multiply     d. divide
q. quit
a
Enter first number: 22.4
Enter second number: one
one is not an number.
Please enter a number, such as 2.5, -1.78E8, or 3: 1
22.4 + 1 = 23.4
Enter the operation of your choice:
a. add          s. subtract
m. multiply     d. divide
q. quit
d
Enter first number: 18.4
Enter second number: 0
Enter a number other than 0: 0.2
18.4 / 0.2 = 92
a. add          s. subtract
m. multiply     d. divide
q. quit
q
Bye.
```

**C**
```C
#include <stdio.h>
#include <ctype.h>

int get_first(void);
void print_menu(void);
float get_number(void);

int main(void)
{
    int operation;
    float num1, num2;

    print_menu();
    while ((operation = get_first()) != 'q')
    {
        printf("Enter first number: ");
        num1 = get_number();
        printf("Enter second number: ");
        num2 = get_number();

        switch (operation)
        {
        case ('a'):
            printf("%.3f + %.3f = %.3f\n", num1, num2, num1 + num2);
            break;
        case ('s'):
            printf("%.3f - %.3f = %.3f\n", num1, num2, num1 - num2);
            break;
        case ('m'):
            printf("%.3f * %.3f = %.3f\n", num1, num2, num1 * num2);
            break;
        case ('d'):
            while (num2 == 0)
            {
                printf("Enter a number other than 0: ");
                num2 = get_number();
            }
            printf("%.3f / %.3f = %.3f\n", num1, num2, num1 / num2);
            break;
        default:
            printf("I do not recognize that input. Try again.");
        }
        print_menu();
    }
}

int get_first(void)
{
    // return first non-whitespace character
    int ch;

    do
        ch = getchar();
    while (isspace(ch));

    while (getchar() != '\n')
        ;

    return ch;
}

void print_menu(void)
{
    printf("Enter the operation of your choice:\n");
    printf("a. add            s. subtract\n");
    printf("m. multiply       d. divide\n");
    printf("q. quit\n");
}

float get_number(void)
{
    int ch;
    float num;

    while (scanf("%f", &num) != 1)
    {
        while ((ch = getchar()) != '\n') // echo user input and clear stream
            putchar(ch);

        printf(" is not a number.\n");
        printf("Please enter a number, such as 2.5, -1.78E8, or 3: ");
    }

    return num;
}
```

**Python**
```Python
operation = True


def choice():
    print("Enter the operation of your choice:")
    print("a. add       s. subtract")
    print("m. multiply  d. divide")
    print('q. quit')
    text = input()
    return text


def two_number():
    first = input("Enter first number:")
    second = input("Enter second number:")
    while first.lstrip('-').replace('.', '', 1).replace('E-', '', 1).replace('E', '', 1).replace('e-', '', 1).replace('e', '', 1).isdigit() is False:
        print(f"{first} is not an number.")
        print("Please enter a number, such as 2.5, -1.78E8, or 3:")
        first = input()
    while second.lstrip('-').replace('.', '', 1).replace('E-', '', 1).replace('E', '', 1).replace('e-', '', 1).replace('e', '', 1).isdigit() is False:
        print(f"{second} is not an number.")
        print("Please enter a number, such as 2.5, -1.78E8, or 3:")
        second = input()
    return first, second


while operation == True:
    ans = choice()
    if ans == 'q':
        print('Bye.')
        operation = False
    elif ans == 'a':
        first, second = two_number()
        print("%s + %s = %.1f" % (first, second, float(first)+float(second)))
    elif ans == 's':
        first, second = two_number()
        print("%s - %s = %.1f" % (first, second, float(first)-float(second)))
    elif ans == 'm':
        first, second = two_number()
        print("%s * %s = %.1f" % (first, second, float(first)*float(second)))
    elif ans == 'd':
        first, second = two_number()
        while second == '0':
            second = input("Enter a number other than 0:")
        print("%s / %s = %.1f" % (first, second, float(first)/float(second)))
    else:
        print('invalid choice, try again.')
```

## Chapter 9 Functions
#### Page 380
#### Question 1
Devise a function called min(x,y) that returns the smaller of two double values. Test  
the function with a simple driver.

**C**
```C
#include <stdio.h>

double min(double x, double y);

int main(void)
{
    double x, y;

    printf("Enter two doubles: ");
    scanf("%lf %lf", &x, &y);
    printf("The minimum of %.3f and %.3f is %.3f.\n", x, y, min(x, y));

    return 0;
}

double min(double x, double y)
{
    return x < y ? x : y;
}
```

**Python**
```python
def min(x,y):
    x = float(x)
    y = float(y)
    if x < y:
        return x
    else:
        return y

if __name__ == "__main__":
    x, y = [float(x) for x in input("Enter two doubles: ").split()]
    print("The minimum of %.3f and %.3f is %.3f." % (x, y, (min(x, y))))
```

#### Question 2
Devise a function chline(ch,i,j) that prints the requested character in columns i  
through j. Test it in a simple driver.

*Note*:  
Chinese version (姜佑 译, 人民邮电出版社 ISBN 9787115390592) has an error  
in translation here (Page 276).  
In Chinese version, it request you to print character in i COLUMNS and j LINES.  
Therefore, chline('k', 6, 3) will looks like:    
```
kkkkkk
kkkkkk
kkkkkk
```

Here I write both answers as below:  

**S.Prata Version** 

**C**
```C
#include <stdio.h>

void chline(char ch, int i, int j);

int main(void)
{
    chline('k', 3, 5);
    return 0;
}

void chline(char ch, int i, int j)
{
    int x = 0, y = 0;
    while (x < j)
    {
        printf(" ");
        x++;
    }
    while (y < i)
    {
        putchar(ch);
        y++;
    }
}
```

**Python**
```python
def chline(ch, i, j):
    x = 0
    y = 0
    while x < j:
        print(' ', end='')
        x += 1
    while y < i:
        print(ch, end='')
        y += 1

chline('k', 3, 5)
```

**姜佑 version**  
**C**  
```C
#include <stdio.h>

void chline(char ch, int i, int j);

int main(void)
{
    chline('9', 3, 5);
    return 0;
}

void chline(char ch, int i, int j)
{
    int x = 0;
    while (x < j)
    {
        int y = 0;
        while (y < i)
        {
            putchar(ch);
            y++;
        }
        printf("\n");
        x++;
    }
}
```

**Python**
```python
def chline(ch, i, j):
    x = 0

    while x < j:
        y = 0
        while y < i:
            print(ch, end='')
            y += 1
        print()
        x += 1

chline('kk',3,5)
```

#### Question 3
Write a function that takes three arguments: a character and two integers. The character  
is to be printed. The first integer specifies the number oftimes that the character is to  
be printed on a line, and the second integer specifies the number of lines that are to be  
printed. Write a program thatmakes use of this function.

**C**
```C
#include <stdio.h>

void printgrid(char ch, unsigned int cols, unsigned int rows);

int main(void)
{
    char ch;
    unsigned int rows, cols;

    printf("Enter a character, number of rows and number of columns: ");
    while (scanf("%c %u %u", &ch, &rows, &cols) == 3)
    {
        printgrid(ch, cols, rows);
        printf("Enter a character, number of rows and number of columns: ");
    }

    return 0;
}

void printgrid(char ch, unsigned int cols, unsigned int rows)
{
    // prints given character in a block sized rows x cols
    for (unsigned int i = 0; i < rows; i++)
    {
        for (unsigned int j = 0; j < cols; j++)
        {
            putchar(ch);
        }
        putchar('\n');
    }
}
```

**Python**
```Python
ch, x, y = [x for x in input(
    "Enter a character, number of rows and number of columns: ").split()]

def chline(ch, i, j):
    x = 0
    ch = str(ch)
    while x < int(i):
        y = 0
        while y < int(j):
            print(ch, end='')
            y += 1
        print()
        x += 1

chline(ch, x, y)
```

#### Question 4
The harmonic mean of two numbers is obtained by taking the inverses of the two  
numbers, averaging them, and taking the inverse of the result. Write a function that  
takes two double arguments and returns the harmonic mean of the two numbers.

**C**
```C
#include <stdio.h>

double harmonic_mean(double, double);

int main(void)
{
    double x, y;

    printf("Harmonic means\n");
    printf("Enter two numbers: ");
    while (scanf("%lf %lf", &x, &y) == 2)
    {
        printf("%f\n", harmonic_mean(x, y));

        printf("Enter two numbers: ");
    }

    return 0;
}

double harmonic_mean(double x, double y)
{
    return 2 / (1 / x + 1 / y);
}
```

**Python**
```Python
def harmonic_mean(x, y):
    return 2 / (1 / x + 1 / y)

if __name__ == "__main__":
    print("Harmonic means")
    x, y = [float(x) for x in input("Enter two numbers: ").split()]
    print(f"{harmonic_mean(x, y):.6f}")
```

#### Question 5
Write and test a function called larger_of() that replaces the contents of two double  
variables with the maximum of the two values. For example, larger_of(x,y) would  
reset both x and y to the larger of the two.

**C**
```C
#include <stdio.h>

void larger_of(double *x, double *y);

int main(void)
{
    double x, y;

    printf("Test larger_of() function\n");
    printf("=========================\n");
    printf("Enter two numbers x and y: ");
    while (scanf("%lf %lf", &x, &y) == 2)
    {
        printf("Before calling larger_of():\n");
        printf("x = %f, y = %f\n", x, y);

        larger_of(&x, &y);

        printf("After calling larger_of():\n");
        printf("x = %f, y = %f\n", x, y);

        printf("Enter two numbers x and y: ");
    }

    return 0;
}

void larger_of(double *x, double *y)
{
    // replace contents of
    if (*x > *y)
        *y = *x;
    else
        *x = *y;
}
```

**Python**
```Python
def large_of(x, y):
    return max(x, y)

if __name__ == "__main__":
    print("Test larger_of() function")
    print("=========================")
    x, y = [float(x) for x in input("Enter two numbers: ").split()]
    print("Before calling large_of():")
    print(f"x = {x:.6f}, y = {y:.6f}")
    x = y = large_of(x, y)
    print("After calling larger_of():")
    print(f"x = {x:.6f}, y = {y:.6f}")
```

#### Page 381
#### Question 6
Write and test a function that takes the addresses of three double variables as arguments  
and that moves the value of the smallest variable into the first variable, the middle value  
to the second variable, and the largest value into the third variable.

**C**
```C
#include <stdio.h>

void sort_variables(double *x, double *y, double *z);

int main(void)
{
    double x, y, z;

    printf("Test sort_variables():\n");
    printf("Enter three numbers x, y and z:\n");
    while (scanf("%lf %lf %lf", &x, &y, &z) == 3)
    {
        putchar('\n');
        printf("Before calling sort_variables:\n");
        printf("x = %f, y = %f, z = %f\n", x, y, z);

        sort_variables(&x, &y, &z);

        putchar('\n');
        printf("After calling sort_variables:\n");
        printf("x = %f, y = %f, z = %f\n", x, y, z);

        putchar('\n');

        printf("Enter three numbers x, y and z:\n");
    }

    return 0;
}

void sort_variables(double *x, double *y, double *z)
{
    double tmp;

    if (*x > *y)
    {
        // switch x and y
        tmp = *y;
        *y = *x;
        *x = tmp;
    }

    if (*y > *z)
    {
        // switch y and z
        tmp = *z;
        *z = *y;
        *y = tmp;

        if (*x > *y)
        {
            // switch x and y
            tmp = *y;
            *y = *x;
            *x = tmp;
        }
    }
}
```

**Python**
```Python
def sort_variables(x, y, z):
    t = sorted([x, y, z])
    return t[0], t[1], t[2]

print("Before calling sort_variables:")
x, y, z = [float(x) for x in input("Enter three value: ").split()]
print(f"x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")
print("After calling sort_variables:")
a, b, c = sort_variables(x, y, z)
print(f"x = {a:.6f}, y = {b:.6f}, z = {c:.6f}")
```

#### Question 7
Write a program that reads characters from the standard input to  end-of-file. For each  
character, have the program report whether it is a  letter. If it is a letter, also report  
its numerical location in the  alphabet. For example, c and C would both be letter 3.  
Incorporate a  function that takes a character as an argument and returns the numerical  
location if the character is a letter and that returns –1 otherwise.

**C**
```C
#include <stdio.h>
#include <ctype.h>

int letter_location(char ch);

int main(void)
{
    char ch;
    int location;

    while ((ch = getchar()) != EOF)
    {
        if ((location = letter_location(ch)) == -1)
            printf("%c is not a letter\n", ch);
        else
            printf("%c is a letter: location = %d\n", ch, location);
    } 

    return 0;
}

int letter_location(char ch)
{
    if (isalpha(ch))
    {
        ch = tolower(ch);
        return (ch - 'a' + 1);
    }
    else
        return -1;
}
```

**Python**
```Python
import sys

def letter_location(ch):
    if ch.isalpha():
        return ord(ch.lower()) - ord('a') + 1
    else:
        return -1

for line in sys.stdin:
    for ch in line:
        location = letter_location(ch)
        if location == -1:
            print(f"{ch} is not a letter.")
        else:
            print(f"{ch} is a ltter: location = {location}")
```

#### Question 8
Chapter 6, “C Control Statements: Looping,” (Listing 6.20) shows a power() function  
that returned the result of raising a type double number to a positive integer value.  
Improve the function so that it correctly handles negative powers. Also, build into the  
function that 0 to any power other than 0 is 0 and that any number to the 0 power is 1.  
(It should report that 0 to the 0 is undefined, then say it’s using a value of 1.) Use a loop.  
Test the function in a program.

**C**
```C
#include <stdio.h>
#include <stdlib.h> // prototype for abs()

double power(double base, int exponent);

int main(void)
{
    double base, output;
    int exponent;

    printf("Test power() function:\n");
    printf("Enter a :double: base and :int: exponent: ");
    while (scanf("%lf %d", &base, &exponent) == 2)
    {
        output = power(base, exponent);

        printf("%f ^ %d = %f \n", base, exponent, output);

        printf("Enter a :double: base and :int: exponent: ");
    }

    return 0;
}

double power(double base, int exponent)
{
    double power = base;

    if (base == 0)
    {
        if (exponent == 0)
        {
            printf("Warning: 0 ^ 0 is undefined. Using 1.\n");
            return 1.0;
        }
        else
            return 0;
    }

    for (int i = 1; i < abs(exponent); i++)
    {
        power *= base;
    }

    if (exponent < 0)
        power = 1 / power;

    return power;
}
```

**Python**
```Python
def power(decimal, integer):
    num = 1
    if integer > 0:
        for _ in range(integer):
            num = num*decimal
    if integer < 0:
        num = 1.0  # force floating point division
        for _ in range(-integer):
            num = num/decimal
    return num

On = True
while On:
    try:
        base, exponent = [_ for _ in input(
            "Enter a :double: base and :int: exponent: ").split()]
        base = float(base)
        exponent = int(exponent)
        print(f"{base} ^ {exponent} = {power(base, exponent):.6f}")
    except:
        On = False
```

#### Question 9
Redo Programming Exercise 8, but this time use a recursive function.

**C**
```C
#include <stdio.h>
#include <stdlib.h> // prototype for abs() 

double power(double base, int exponent);

int main(void)
{
    double base, output;
    int exponent;

    printf("Test power() function:\n");
    printf("Enter a :double: base and :int: exponent: ");
    while (scanf("%lf %d", &base, &exponent) == 2)
    {
        output = power(base, exponent);

        printf("%f ^ %d = %f \n", base, exponent, output);

        printf("Enter a :double: base and :int: exponent: ");
    }

    return 0;
}

double power(double base, int exponent)
{
    double dbl_power;

    // handle powers of zero
    if (base == 0)
    {
        if (exponent == 0)
        {
            printf("Warning: 0 ^ 0 is undefined. Using 1.\n");
            return 1.0;
        }
        else
            return 0;
    }

    if (exponent == 0) return 1; // stop recursion

    dbl_power = base * power(base, abs(exponent) - 1); // recursion step

    // if exponent is negative, take reciprocal
    if (exponent < 0) dbl_power = 1 / dbl_power;

    return dbl_power;
}
```

**Python**
```Python
def power(base, exponent):
    # handle powers of zero
    if base == 0:
        if exponent == 0:
            return 1.0 # 0 ^ 0 is undefined. Using 1.
        else:
            return 0

    if exponent == 0:
        return 1 # stop recursion

    dbl_power = base * power(base, abs(exponent) - 1)

    # if exponent is negative, take reciprocal
    if exponent < 0:
        dbl_power = 1 / dbl_power

    return dbl_power

On = True
while On:
    try:
        base, exponent = [_ for _ in input(
            "Enter a :double: base and :int: exponent: ").split()]
        base = float(base)
        exponent = int(exponent)
        print(f"{base} ^ {exponent} = {power(base, exponent):.6f}")
    except:
        On = False
```

#### Question 10
Generalize the to_binary() function of Listing 9.8 to a to_base_n() function that  
takes a second argument in the range 2–10. It then should print thenumber that is its  
first argument to the number base given by the second argument. For example, to_  
base_n(129,8) would display 201, the base-8equivalent of 129. Test the function in a  
complete program.

*Note*:  
Chinese version (姜佑 译, 人民邮电出版社 ISBN 9787115390592) has an error  
in translation here (Page 276).  
It was printed as both two argument shall falls in the range 2 - 10.  

**C**
```C
#include <stdio.h>
#include <stdlib.h>

void to_base_n(int integer, int base);

int main(void)
{
    int integer, base;

    printf("Test to_base_n() function\n");
    printf("Enter an integer in base 10 and a base to convert to: ");
    while (scanf("%d %d", &integer, &base) == 2)
    {
        to_base_n(integer, base);
        putchar('\n');

        printf("Enter an integer in base 10 and a base to convert to: ");
    }

    return 0;
}

void to_base_n(int integer, int base)
{
    // handle invalid bases
    if (base < 2 || 10 < base)
    {
        printf("Error: base must be between 2 and 10.");
        return;
    }

    // stop recursion
    if (integer == 0)
        return;

    // handle negative integers
    if (integer < 0)
    {
        putchar('-');
        integer = abs(integer);
    }

    to_base_n(integer / base, base);
    printf("%d", integer % base);
    return;
}
```

**Python**

```Python
'''
Convert the decimal integer n to an integer in any base. The base of the base is denoted as base, base=8 means octal, base=10 means decimal.


ANALYSE PROBLEM


There are ten different symbols in the decimal system, resulting in a "table" related to the conversion of the decimal system: convSring = "0123456789".

Decimal integers smaller than ten, convert to decimal, just check the "table" directly: convString[n]. For example, if the 7 base is converted to the decimal base, convString[7] = 7 is obtained by looking up the table.

It is relatively troublesome to convert integers larger than ten to decimal. Our method is to divide the integers larger than ten into a series of integers smaller than ten, and then look up the "table" one by one. For example, the integer 769 is divided into three numbers smaller than ten, 7, 6, and 9, and then look up the "table" one by one to get 769.


THE BASIC END CONDITION OF THE RECURSION OF THIS PROBLEM


Through the above analysis, we know that whether it is an integer greater than ten or an integer less than ten, there is one thing in common, that is, we must eventually achieve the condition that the integer is less than ten.

Therefore, in the three laws of recursion, we have found the "basic end condition", that is, an integer less than ten. The process of continuously disassembling integers is the process of evolving to the "basic end condition" in recursion.


PROBLEM BREAKDOWN

We use integer division (//) and remainder (%) operators to separate integers step by step to achieve our goal:

    Divide by "base base" (//base).
    Find the remainder (% base) of the "base".

So the problem is broken down into:

The remainder is always less than the base of the hexadecimal system, which is the "basic end condition" and can be directly converted to the "table".
The integer quotient becomes a "smaller scale" problem, which is solved by recursively calling itself.

According to the above analysis and problem decomposition, directly apply the three laws of recursion:

1) Establish a minimum basic end condition. Just let the integer n be less than 10.

2) Break down the problem into the same problems on a smaller scale. Use two calculation methods to divide integers and find the remainder to disassemble the integer n step by step:

    Divide by "base base" (//base).
    Find the remainder (% base) of the "base".

3) Call itself. When n // base, use this function again, the previous n becomes n//base, and the previous base is still base.

So it is easy to write the code:
'''

def to_base_n(n, base):
    '''
    n:      int type, decimal integer.
    base:   The base to be converted.
    '''
    convertString = "0123456789"
    if n < base:
        return convertString[n]
    else:
        # the floor division // rounds the result down to the nearest whole number
        return to_base_n(n//base, base) + convertString[n % base]

print("Test to_base_n() function")
On = True
while On:
    try:
        n, base = [int(_) for _ in input(
            "Enter an integer in base 10 and a base to convert to: ").split()]
        if base > 10 or base < 2:
            print("Error: base must be between 2 and 10.")
            continue
        ans = to_base_n(n, base)
        print(ans)
    except:
        On = False
```

#### Question 11
Write and test a Fibonacci() function that uses a loop instead of recursion to calculate  
Fibonacci numbers.

**C**
```C
/*
C often represents integers with a sequence of 32 bits, 
and the range of values they can take on are from -2,147,483,648 to 2,147,483,647.
Notice what the 47th Fibonacci number is? 2,971,215,073
After they overflow, they wrap around to the smallest integer possible; 
*/

#include <stdio.h>

int Fibonacci(int n);

int main(void)
{
    int n;

    printf("How many terms?");
    scanf("%d", &n);
    Fibonacci(n);

    return 0;
}

int Fibonacci(int n)
{
    int first = 0, second = 1, next, c;

    for (c = 0; c < n; c++)
    {
        if (c <= 1)
            next = c;
        else
        {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%d ", next);
    }
}
```

**Python**
```Python
def Fibonacci(num):
    result = [0, 1]
    # _ is a standard placeholder name for ignored members in a for-loop and tuple assignment
    for _ in range(num-2):
        result.append(result[-2] + result[-1])
    return result

nterms = int(input("How many terms?"))
result = Fibonacci(nterms)
for x in result:
    print(x, end=' ')
```
