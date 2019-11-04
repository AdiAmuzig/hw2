#include <stdio.h>
#include <math.h>

int ValidateInputSize(int size_of_input);

int AddAndValidateInputValues(int numbers[], int size_of_input);

int PowerOfTwo(int numbers[], int size_of_input);

int main() {
    // part 1 - Adding and Validating size of input
    int size_of_input;
    printf("Enter size of input: ");
    scanf("%d", &size_of_input);
    if (size_of_input <= 0) {
        printf("Invalid size");
        return 0;
    }

    // part 2 - Adding and Validating input
    int numbers[size_of_input];
    if (AddAndValidateInputValues(numbers, size_of_input) == 0) {
        return 0;
    }

    // part 3 - checking for numbers that are a power of 2 + printing
    printf("Total exponent sum is %d", PowerOfTwo(numbers, size_of_input));

    return 0;
}


int AddAndValidateInputValues(int *numbers, int size_of_input) {
    int i;

    printf("Enter numbers:\n");
    for (i = 0; i < size_of_input; ++i) {
        if (scanf("%d", numbers + i) != 1) {
            printf("Invalid number");
            return 0;
        }
    }
}

int PowerOfTwo(int *numbers, int size_of_input) {
    int i;
    int divided_number;
    int power_of_2;
    int sum_of_power = 0;

    for (i = 0; i < size_of_input; ++i) {
        divided_number = *(numbers + i);
        power_of_2 = 0;
        while (divided_number > 1) {
            if ((divided_number % 2) != 0) {
                power_of_2 = 0;
                break;
            }
            divided_number = divided_number / 2;
            power_of_2++;
        }
        if (power_of_2 > 0) {
            sum_of_power = sum_of_power + power_of_2;
            printf("The number %d is a power of 2: %d=2^%d\n", *(numbers + i), *(numbers + i), power_of_2);
        }
    }
    return sum_of_power;
}