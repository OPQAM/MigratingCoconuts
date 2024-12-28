#include <stdio.h>

// Function to multiply two numbers
int multiply(int a, int b) {
    return a * b;
}

int main() {
    int num1 = 5;
    int num2 = 3;

    int result = multiply(num1, num2);
    printf("The result of %d * %d is %d\n", num1, num2, result);

    return 0;
}

