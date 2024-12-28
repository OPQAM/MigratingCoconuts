#include<stdio.h>

#define X_VAL 33
#define Y_VAL 22

int adder_function(int value_a, int value_b) {
	return value_a + value_b;
}
	
int main(){
	printf("Simple adding machine.\n");

	int final_result = adder_function(X_VAL, Y_VAL);

	printf("Final result: %d\n", final_result);

	return 0;
}
