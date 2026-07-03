/*

#include <stdio.h>

int main() {
    char str[] = "cat";
    char *p = str;

    printf("%c\n", *p);
    printf("%c\n", *(p + 1));
    printf("%c\n", *(p + 2));

    return 0;
}

The strings in C are basically arrays of characters. Which is not different for other coding languages
But in C we can consider it as an array. And hence treat it like it. Except the '0\' , the null terminating character.
so here it will print 
c
a
t

p is storing address of the 0th element. 
As p is pointer to 0th element of str array. and while printing, we are dereferencing p. 
and then the increment and printing. which gives 1st and 2nd elements. 
though i am unsure if this array/string will have a null terminating character.  
but perhaps since it is an dynamic array, C may just automatically add it. 

*/


#include <stdio.h>


// the functions. 


 void printStudent(int roll, char name[], float marks)
    {
        printf("The random print is: ");

        printf("Student name: %s\n", name);

        printf("Student roll: %d", roll);

        printf("Student marks: %f", marks);
    

    }


float findTopper(float a, float b, float c)
{
    if( a == b || a == c || b == c || ( a == b && a == c ))
    {
        printf(" There multiple students with same marks! ");
    }

    if( a >= b ) // here i am giving priority to a cause a is coming chronologically first. 
    {
        if (a >= c)
        {  return a;  }

        else
        {  return c;  }
        
    }

    else if( b >= c )
    {
        return b;
    }

    else return c;  

    
}



int main()
{

    // the structure.
    struct student
    {
        char name[30];
        float marks;
        int roll;
    };

    
    

    // the input layer. 

    // this can of course be made dynamic by having upper limit of the loop as n. but that would complicate things a bit cause we would the have to do input validation.
    // and since question itself say 3 students specifically. i am keep the upperlimit same. 

    // the array
       struct student CSE[3];


       for(int i = 0; i < 3; i++)
       {
        printf("Name: ");
        fgets(CSE[i].name, sizeof(CSE[i].name), stdin);

        // the code for fgets. i had to look up a bit. 

        printf("Marks: ");
        scanf("%f", &CSE[i].marks);

        printf("Roll: ");
        scanf("%d", &CSE[i].roll);

        }



   
    printStudent(CSE[2].roll, CSE[2].name, CSE[2].marks);


    float topper = findTopper(CSE[0].marks, CSE[1].marks, CSE[2].marks);

    for( int i= 0; i < 3; i ++)
    {
        if( CSE[i].marks == topper)
        {
            printf("Topper is: ");
            printf("Student name: %s\n", CSE[i].name);
            printf("Student roll: %d", CSE[i].roll);
            printf("Student marks: %f", CSE[i].marks);
            
        }


    }


    return 0;
}


