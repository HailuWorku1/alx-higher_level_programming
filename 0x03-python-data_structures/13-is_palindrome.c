#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if palindrome
 * @head: head of node
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *temp;

	if (head == NULL|| *head == NULL)
		return (1);

	temp = *head;
	while (temp) /* get len of list */
	{
		temp = temp->next;
		len++;
	}
	return (0);
}

/**
 * reverse_list - Reverse a linked list
 * @head: The list
 *
 * Return: Pointer to the new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
