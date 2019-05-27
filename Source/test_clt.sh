if [ -f "clt.py" ]
then
	echo "Test CLT mode"

	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/input.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/input.txt"
	
	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_new_line.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_new_line.txt"
	
	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_new_polygon.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_new_polygon.txt"
	
	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_new_ellipse.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_new_ellipse.txt"
	
	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_translate.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_translate.txt"
	
	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_rotate.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_rotate.txt"

	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_scale.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_scale.txt"

	echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_clip.txt\""
	python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_clip.txt"
	
	# echo -e "\npython clt.py --path \"../CLT_test_scripts/res/\" --script \"../CLT_test_scripts/test_load.txt\""
	# python clt.py --path "../CLT_test_scripts/res/" --script "../CLT_test_scripts/test_load.txt"

fi
