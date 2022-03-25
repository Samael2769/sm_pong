##
## EPITECH PROJECT, 2021
## $(MAKE)file_105torus
## File description:
## ..
##

##COMMANDS###################################################
CP	=	cp
CHMOD	=	chmod
DISPLAY	=	echo

##LIB########################################################
LDFLAGS	=	--coverage -lcriterion
CFLAGS	=	-Wall -W
##DIRECTORIES################################################
DIR	=	sources/
DIR_TEST	=	tests/
##FILES######################################################
FILE	=	main.py
FILE_TEST	=	test_error.c\
##SOURCES####################################################
SRC		=	$(addprefix $(DIR), $(FILE))
SRC_TEST	=	$(addprefix $(DIR_TEST), $(FILE_TEST))
OBJ_TEST	=	$(SRC_TEST:.c=.o)
##BINARY#####################################################
NAME	=	pong
NAME_TEST	=	unit_test
##RULES######################################################

all: $(NAME)

$(NAME):
	@$(DISPLAY) -e "\e[31mMaking 108trigo...\e[0m"
	@$(CP) $(SRC) $(NAME)
	@$(CHMOD) +x $(NAME)
	@$(DISPLAY) -e "\e[32mCompilation succesfull\e[0m"

unit_test: fclean $(NAME)
	$(CC) -o $(NAME_TEST) $(SRC_TEST) $(LDFLAGS) $(CFLAGS)

tests_run: unit_test
	./$(NAME_TEST)
	gcovr
	gcovr -b
clean:
	@$(DISPLAY) -e "\e[31mRemove *gc* files\e[0m"
	@$(RM) *gc*
fclean: clean
	@$(DISPLAY) -e "\e[31mRemove binary file\e[0m"
	@$(RM) $(NAME)
	@$(RM) $(NAME_TEST)

re: fclean $(NAME)