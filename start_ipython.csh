#!/usr/bin/csh

zcat $VERDI_HOME/doc/.tcl.txt.gz | grep -A 1 'Syntax$' | grep -v Syntax | grep -v "\-\-" | grep -o "^[a-zA-Z]*" | sort | uniq | sed 's/\(.*\)/    def \1(self,args):\n        self.wish(["\1"] + args)/' | sed '1 i\class verdi_tcl(verdi):' | sed '1 i\from verdi import *' > verdi_tcl.py   

setenv PYTHONSTARTUP `pwd`/verdi_tcl.py

ipython 
