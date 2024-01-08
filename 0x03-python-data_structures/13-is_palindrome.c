#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* is_palindrome - checks if a singly linked list is a palindrome
*
* @head:pointer to the pointer of the first node
* Return:0 if not palindrome 1 if palindrome
*/
int is_palindrome(listint_t **head)
{
int *arr;
int *arr2;
int n = 0;
int i, result;
int p = 0;
listint_t *current;
current = *head;
while (current != NULL)
{
current = current->next;
p++;
}
arr = (int *)malloc(p * sizeof(int));
arr2 = (int *)malloc(p * sizeof(int));
if (arr == NULL || arr2 == NULL)
{
return (0);
}
current = *head;
while (current != NULL)
{
arr[n] = current->n;
current = current->next;
n++;
}
for (i = 0; i < n; i++)
{
arr2[i] = arr[n - 1 - i];
}
result = areArraysEqual(&arr[0], &arr2[0], n);
free(arr);
free(arr2);
return (result);
}
/**
* areArraysEqual - checks if arrays are equal
*
* @arr:array 1
* @arr2:array 2
* @n:size of array
* Return:0 if arrays are not equal and 1 if arrays are equal
*/
int areArraysEqual(int arr[], int arr2[], int n)
{
int i;
for (i = 0; i < n; i++)
{
if (arr[i] != arr2[i])
{
return (0);
}
}
return (1);
}
