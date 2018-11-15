#include <time.h>

int is_sorted_normal(int *array, int length);
int is_sorted_fine(int *array, int length);

int main()
{
    const int test_length = 100000000;

    int a[test_length];
    for (int i = 0; i < test_length; i++)
    {
        a[i] = i;
    }

    time_t start,stop;

    start = time(NULL);
    is_sorted_normal(a, test_length);
    stop = time(NULL);
    printf("is_sorted_fine Use Time:%ld\n",(stop-start));

    start = time(NULL);
    is_sorted_normal(a, test_length);
    stop = time(NULL);
    printf("is_sorted_fine Use Time:%ld\n",(stop-start));

    return 0;
}