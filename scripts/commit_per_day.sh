for i in {01..28}
do	
	git add *hydrator-2022-02-"$i"*.csv

	for j in {0..6}
	do
		git add *2022-02-"$i"*_"$j".csv
		git commit -m "update 2022-02-$i $j"
		git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data
	done
done
for i in {01..10}
do
	        git add *hydrator-2022-03-"$i"*.csv

	for j in {0..6}
	do
	       git add *2022-03-"$i"*_"$j".csv
	       git commit -m "update 2022-03-$i $j"
 	       git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data
        done
done


