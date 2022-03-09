for i in {01..08}
do
	for j in {0..6}
	do
		git add *2022-03-"$i"*_"$j".csv
		git commit -m "update 2022-03-$i $j"
		git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data
	done
done
