#include <stdio.h>
void main(int argc, char const *argv[]){
	
	printf("No.of elements:%d\n",argc-1);

	if (argv[1]<argv[2])
	{
		printf("Second Number is Greater\n");
	}
	else{
		printf("First Number is Greater\n");
	}
}