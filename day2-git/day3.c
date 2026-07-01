/*  

#include <stdio.h>

void modify(int x) {
    x = x + 10;
}

int main() {
    int a = 5;
    modify(a);
    printf("%d\n", a);
    return 0;
}


This should print 5.
I think that is cause we are using void, hence we are not returning anything. 
Any change x will have in the function block will die the moment it leaves the function.
Most of the time void type functions are used for printing something.
Or doing a task that needs to done without involvement of the main block. 


*/

#include <stdio.h>


int main()
{

    // Taking the string from the user. 
    char arr[101] ; 
    printf("Enter the string: ");
    scanf("%100s", &arr);

    // Here i am not able to think of any logic for length of the string
    // I cannot use strlen() and i know that strings have null terminating character. 
    // Perhaps I can search for that and get to know the length of the string user has input.
    // Even i recognise the flaw in this as 
    // Reversing the string.
    
    int len = 0;

    for(int i = 0; i <101 ; i++)
    {
        if( arr[i] != '\0')
        {
            len = len + 1;
        }

        else
        {
            break;
        }

    }

    char *p = &arr[0];
    char *q = &arr[len-1];
    char temp;

    for(int i = 0; i < len ; i ++)
    {

        if( p == q || q < p )
        {
            break;
        }
   
        temp = *p;
        *p = *q;
        *q = temp;

        p = p + 1;
        q = q - 1;
        temp = p;
        

    }

    printf("The reversed string is : " );
    printf("%s", &arr);



    return 0;
}