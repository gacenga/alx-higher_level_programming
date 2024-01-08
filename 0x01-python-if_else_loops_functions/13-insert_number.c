#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* insert_node - inserts a number to a singly linked list
*
* @head:pointer to pointer of the first node
* @number:number to be inserted
* Return:address of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current;
listint_t *new;
listint_t *more;
current = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = number;
new->next = NULL;
if (*head == NULL)
{
*head = new;
}
else
{
if (current->n < number)
{
while (current != NULL && current->n < number)
{
more = current;
current = current->next;
}
more->next = new;
new->next = current;
}
else
{
new->next = *head;
*head = new;
}
}
return (new);
}
