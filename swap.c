#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void)
{
<<<<<<< HEAD
    int x = 34;
=======
    int x = 1040;
>>>>>>> 356d19a11f4e6315d9e13d9d9f166e9ce94aad2c
    int y = 50;

    printf("x is %i\n", x);
    printf("y is %i\n", y);

    // swapping...
<<<<<<< HEAD
    swap(&x, &y);
=======


    // just to test what I am learning
>>>>>>> 356d19a11f4e6315d9e13d9d9f166e9ce94aad2c


    printf("x is now %i\n", x);
    printf("y is now %i\n", y);

    printf("End of the program. Day one")
}