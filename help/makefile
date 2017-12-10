DPACKBASE	=  /home/boehm/maple/packages/dpack4


all:  *.hlp dall.txt
			rm -rf dummy.xxx
			remtabs 4 dall.txt | chophelp
			echo 'readlib(makehelp);' > helpmake
			for X in *.hlp; do \
			echo "makehelp ( " %`basename $$X .hlp`% ' , ' >> dummy.xxx; \
			echo '%'$$X'% , %$(DPACKBASE)% ): ' >> dummy.xxx; \
			done
			sed -e 's/%/\`/g' dummy.xxx >> helpmake
			rm dummy.xxx

