#include <time.h>
#include <stdio.h>

int is_sorted_normal(int *array, int length);
int is_sorted_fine(int *array, int length);

int main()
{
    const int test_length = 100000;

    int a[test_length];

    for (int i = 0; i < test_length; i++)
    {
        a[i] = i;
    }

    clock_t start,stop;
    int result;



    start = clock();
    result = is_sorted_normal(a, test_length);
    stop = clock();
    printf("is_sorted_normal Use Time: %15.5f\n",(double)(stop-start));

    start = clock();
    result = is_sorted_fine(a, test_length);
    stop = clock();
    printf("is_sorted_fine Use Time: %15.5f\n",(double)(stop-start));
   
    return 0;
}