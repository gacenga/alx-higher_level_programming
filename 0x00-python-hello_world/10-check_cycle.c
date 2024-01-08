#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* check_cycle - checks if a singly linked list has a cycle in it
*
* @list:list
* Return:0 if no cycle and 1 if cycle
*/
int check_cycle(listint_t *list)
{
  listint_t *fast;
  listint_t *slow;
  if (list == NULL)
    {
      return (0);
    }
  fast = list;
  slow = list;
  while (fast != NULL && fast->next != NULL)
    {
      slow = slow->next;
      fast = fast->next->next;
      if (fast == slow)
	{
	  return (1);
	}
    }
  return (0);
}
