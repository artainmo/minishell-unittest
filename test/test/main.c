#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>

int main(int argc, char **argv)
{
	char *line;
	int fd;
	int fd1;
	int ret;

	fd = open("text.txt", O_RDONLY);
	fd1 = open("text2.txt", O_RDONLY);
    fd = 0;
	if (argc == 2)
	{
		if (argv[1][0] == '0') //cat get_next_line.c | cat.out 0
				fd = 0;
		if (argv[1][0] == '1')
			fd = open("text.txt", O_RDONLY);
		if (argv[1][0] == '2')
			fd = open("text2.txt", O_RDONLY);
		if (argv[1][0] == '3')
			fd = open("textv.txt", O_RDONLY);
		if (argv[1][0] == '4')
			fd = 1233;
	}

	if (argc != 3)
	{
		while((ret = get_next_line(fd, &line)) > 0)
		{
			printf("%d | %s\n", ret, line);
			free(line);
		}
		printf("%d | %s\n", ret, line);
		free(line);
	}

	if (argc == 3)
	{
	  get_next_line(fd1, &line);
	  printf("%s\n", line);
	  get_next_line(fd, &line);
	  printf("%s\n", line);
	  get_next_line(fd, &line);
	  printf("%s\n", line);
	  get_next_line(fd1, &line);
	  printf("%s\n", line);
	  get_next_line(fd1, &line);
	  printf("%s\n", line);
	  get_next_line(fd, &line);
	  printf("%s\n", line);
	}

	if (argc == 4)
  	system("leaks a.out");

	close(fd);
	close(fd1);

	return 0;
}
