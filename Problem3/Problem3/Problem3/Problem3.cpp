// Problem3.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"
#include <iostream> // system pause

#define goal 600851475143  

int main()
{
	int i = 2;
	long long curVal = goal;
	while (i < sqrt(curVal)) {
		while (curVal%i == 0) {
			// printf("curVal %i %llu \n", i, curVal);
			curVal /= i;
		}
		i++;
	}
	printf("largest prime devisor %i \n",curVal);
	system("pause");
    return 0;
}

