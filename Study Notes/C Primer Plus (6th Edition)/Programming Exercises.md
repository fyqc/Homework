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
    float TSP_PER_CUP = 3 * TBS_PER_CUP; // teaspoons/tablespoon * tablespoons/ounce * ounces/cup
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
    printf("\"%s\"\n", name); // a. enclosed in double quotes
    printf("\"%20s\"\n", name); // b. double quotes, 20 char wide, right-justified
    printf("\"%-20s\"\n", name); // c. double quotes, 20 char wide, left-justified
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
           " downloads in %.2f seconds.\n", download_speed_Mps, file_size_MB,
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
           (int) strlen(first_name), strlen(first_name),
           (int) strlen(last_name), strlen(last_name));
    printf("\n");
    printf("%s %s\n", first_name, last_name);
    printf("%-*lu %-*lu\n", // left justified
           (int) strlen(first_name), strlen(first_name),
           (int) strlen(last_name), strlen(last_name));
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
