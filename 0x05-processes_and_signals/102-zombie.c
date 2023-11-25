#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Function to run an infinite while loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point to creating a zombie process
 *
 * Return: 0 success
 */
int main(void)
{
	pid_t c_pid;
	char ch = 0;

	while (ch < 5)
	{
		c_pid = fork();

		if (c_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", c_pid);
			sleep(1);
			ch++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
