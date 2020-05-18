#ifndef _SAMPLE_H_
#define _SAMPLE_H_

#include "initial_condition.h"

class Field
{
public:
    void set(int num);
    int get();
private:
    int m_num;
};