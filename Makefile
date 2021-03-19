.SUFFIXES:.c.o
CC=gcc
CFLAGS=-g -Wall -Werror -lreadline #-std=c99 -pedantic
EXEC=main
OBJS=main.o
CFILE=main.c
DSYM=main.dSYM

default:all

#all: esh.o
#	${CC} -o ${EXEC} ${OBJS} #-lreadline -ltinfo

all:
	${CC} ${CFILE} ${CFLAGS} -o ${EXEC}

${EXEC}: ${OBJS}
	        ${CC} ${CFILE} ${CFLAGS} -o ${EXEC}
%.c%.o:
	        ${CC} ${CFLAGS} -c $<

# run: clean cleanscr ${EXEC}
# 	        ./${EXEC}

run: ${EXEC}
	    ./${EXEC}

clean:
	        rm -r -f ${EXEC} ${OBJS} ${DSYM}
cleanscr:
	        clear

valgrind: clean ${EXEC}
		valgrind -s ./${EXEC}

gdb: clean ${EXEC}
		gdb ${EXEC}

main.o: main.c
