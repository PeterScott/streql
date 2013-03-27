#include <Python.h>


static int equals_internal(const char *x, unsigned int xlen, const char *y, unsigned int ylen) {
  if (xlen != ylen) return 0;

  int i, result = 0;
  for (i = 0; i < xlen; i++) result |= x[i] ^ y[i];
  return result == 0;
}


static PyObject *equals(PyObject *self, PyObject *args) {
  const char *x, *y; unsigned int xlen, ylen;
  if (!PyArg_ParseTuple(args, "s#s#", &x, &xlen, &y, &ylen)) return NULL;
  
  if (equals_internal(x, xlen, y, ylen)) {
    Py_RETURN_TRUE;
  } else {
    Py_RETURN_FALSE;
  }
}


static PyMethodDef streql_methods[] = {
  {"equals",  equals, METH_VARARGS,
   "equals(x, y): does x == y?\nRuntime does not depend on the bytes in the strings."},
  {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
initstreql(void) {
  (void) Py_InitModule("streql", streql_methods);
}
