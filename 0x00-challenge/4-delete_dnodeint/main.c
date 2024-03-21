/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    dlistint_t *head = NULL;

    add_dnodeint_end(&head, 0);
    add_dnodeint_end(&head, 1);
    add_dnodeint_end(&head, 2);
    add_dnodeint_end(&head, 3);
    add_dnodeint_end(&head, 4);
    add_dnodeint_end(&head, 98);
    add_dnodeint_end(&head, 402);
    add_dnodeint_end(&head, 1024);

    printf("Original list:\n");
    print_dlistint(head);

    printf("\nAfter deleting node at index 5:\n");
    delete_dnodeint_at_index(&head, 5);
    print_dlistint(head);

    printf("\nAfter deleting node at index 0:\n");
    delete_dnodeint_at_index(&head, 0);
    print_dlistint(head);

    printf("\nAfter deleting node at index 0:\n");
    delete_dnodeint_at_index(&head, 0);
    print_dlistint(head);

    /* Continue testing other index deletions */

    printf("\nFreeing memory...\n");
    free_dlistint(head);

    return (EXIT_SUCCESS);
}
