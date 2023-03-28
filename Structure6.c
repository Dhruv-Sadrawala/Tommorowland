#include <stdio.h>

struct date{
	int dd[2],mm[2],yyyy[2];
};

void main(){

	struct date value;
	int flag=0;

	printf("You can enter two dates in following program\n");
	printf("=====================================================\n\n");

	for (int i = 0; i < 2; ++i)
	{
		printf("Enter the day: ");
		scanf("%d",&value.dd[i]);
		printf("Enter the month: ");
		scanf("%d",&value.mm[i]);
		printf("Enter the year: ");
		scanf("%d",&value.yyyy[i]);
	}

	for (int i = 0; i < 2; ++i)
	{
		if (value.dd[0]==value.dd[1] && value.mm[0]==value.mm[1] && value.yyyy[0]==value.yyyy[1])
		{
			flag++;
		}
		else{
			flag=0;
		}
	}

	if (flag>0)
	{
		printf("\nDates are same.\n");
	}
	else{
		printf("\nDates are not same.\n");
	}
}
