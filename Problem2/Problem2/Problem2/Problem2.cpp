// Problem2.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"

#define FIB_MAX 4000000

int main()
{
	int prev = 0;
	int temp_prev = 0;
	int curr = 1;
	int even_fib_sum = 0;
	while (curr < FIB_MAX) {
		printf("curr %i \n", curr);
		if (curr % 2 == 0) {
			even_fib_sum += curr;
		}
		temp_prev = curr;
		curr += prev;
		prev = temp_prev;
	}
	printf("Ergebnis = %i \n", even_fib_sum);
    return 0;
}

