cd ~/Documents/GitHub/Compilers-COP4620/prj2/reject_test/
alias ls='ls'
for i in `ls`;
do
python ~/Documents/GitHub/Compilers-COP4620/prj2/parser.py $i;
done;
rm tokens.txt
python ~/Documents/GitHub/Compilers-COP4620/prj2/parser.py
