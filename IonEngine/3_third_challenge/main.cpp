#include <stdio.h>
#include <iostream>
#include "model/initial_condition.h"
#include "model/field.h"

int main(int argc, const char *argv[])
{
    Field obj;
    int num;
    obj.set(1);
    obj.get();
    printf("m = %e\n", mass);

    return 0;
}