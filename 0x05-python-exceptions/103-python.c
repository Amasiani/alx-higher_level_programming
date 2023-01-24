#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_list - Prints basic info about Python lists
* @p: A PyObject list object
*/

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyListObject *item;
	int i = 0;


	fflush(stdout);
	printf("[*] Python list info\n");
	if (Pylist_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFlost_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf(" [ERROR] Invalid List Object\n");
}

/**
* print_python_bytes - Prints basic info about  Python bytes object
* @p: A PyObject bytes object
*/

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf(" size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf(" trying string: %s\n", string);
	printf(" first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

/**
* print_python_float - Prints basic info about Python float object
* @p: A PyObject float object
*/

void print_python_float(PyObject *p)
{
	char *string = NULL;
	double value  = 0;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf(" [ERROR] invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, PY_DTSF_AD_DOT_0, NULL);
	printf(" value: %s\n", string);
}
