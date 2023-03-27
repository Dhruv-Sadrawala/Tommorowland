#include <stdio.h>
struct rectangle{
	int length;
	int breath;
};
void main(){
	struct rectangle variable;
	int no_of,area;

	printf("enter the number of rectangles: ");
	scanf("%d",&no_of);

	for (int i = 0; i < no_of; ++i)
	{
		printf("Enter the Length Of Reactangle %d: ",i);
		scanf("%d",&variable.length);
		printf("Enter the Breath Of Reactangle %d: ",i);
		scanf("%d",&variable.breath);
	}

	for (int i = 0; i < no_of; ++i)
	{
		area=variable.length*variable.breath;
		printf("Area of Rectange %d:%d\n",i,area);
	}
}