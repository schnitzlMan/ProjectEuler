// Problem1.cpp 
#include "stdafx.h"


int main()
{
	int currentSum = 0;
	for (int i = 0; i < 1000; i++)
		if (i % 3 == 0 || i % 5 == 0)
			currentSum += i;
	printf("result is %i \n", currentSum);
	return 0;
}

