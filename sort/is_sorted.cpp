int is_sorted_normal(int *array, int length)
{
    int index;

    for (index = 0; index < length -1 ; index ++)
    {
        if (array[index] > array[index + 1])
        {
            return 0;
        }
    }

    return 1;
}

int is_sorted_fine(int *array, int length)
{
    int index;

    for (index = 0; index < length -1 ;)
    {
        if (array[index] > array[++index])
        {
            return 0;
        }
    }

    return 1;
}