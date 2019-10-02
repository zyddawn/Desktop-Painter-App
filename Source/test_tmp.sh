if [ -f "clt.py" ]
then
	echo "Test CLT mode"

	echo -e "\npython clt.py --path \"../../MyReport/\" --script \"../CLT_test_scripts/tmp.txt\""
	python clt.py --path "../../MyReport/images/" --script "../CLT_test_scripts/tmp.txt"
	
fi
