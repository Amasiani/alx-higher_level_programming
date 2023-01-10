#include "lists.h"

int len_list(listint_t **head)
{
	int i = 0;
	listint_t *h = head;

	while (head != NULL)
	{
		h = h->next;
		i++;
	}
	return (i);
}

/**
* is_palindrome - check if list is empty
* @head: point to the list head
*
* Return: 0 if not palindrome else 1
*/

int is_palindrome(listint_t **head)
{
	int a, i;
	listint_t *tmp = *head;
	int array;

	l = len_list(*head);
	array = malloc(sizeof(int) * l);

	if (array == NULL)
		exit(-1);

	i = 0;
	while (temp != NULL)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}
}
