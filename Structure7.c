#include <stdio.h>

struct items_list{
	int item[100];
};

void main(){

	struct items_list variable;

	int no_of_items,no_of_friends,sum,outcome;

	printf("Enter number of items: ");
	scanf("%d",&no_of_items);

	printf("Enter number of friends: ");
	scanf("%d",&no_of_friends);

	for (int i = 0; i < no_of_items; ++i)
	{
		printf("Enter the value of item %d: ",i+1);
		scanf("%d",&variable.item[i]);
		sum=sum+variable.item[i];
	}

	outcome=sum/no_of_friends;

	printf("Each friend have to give: %d\n",outcome);
}