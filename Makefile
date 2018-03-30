##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

CC 		= 	gcc

TESTS 	=	tests/108trigo_basics_tests.c 			\
			tests/108trigo_cos_tests.c 				\
			tests/108trigo_utils.c

CFLAGS 	= 	-Wall -Wextra -I./include

LDFLAGS	=	-lcriterion

OBJ 	= 	$(TESTS:.c=.o)

all: ## tests_run

clean:
		rm -rf $(OBJ)

fclean: clean
		rm -rf units

tests_run: fclean $(OBJ)
		$(CC) $(CFLAGS) $(LDFLAGS) $(OBJ) -o units
		./units
