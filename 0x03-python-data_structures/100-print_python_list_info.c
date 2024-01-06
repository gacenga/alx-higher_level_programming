#include "Cpython.h"
#include <stdio.h>
#include <Python.h>
#include <object.h>
/**
* print_python_list_info - function
*
* p: pointer
*/
void print_python_list_info(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;
size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
