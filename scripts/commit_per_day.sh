for i in {01..31}
do	
	git add *hydrator-2022-03-"$i"*.csv

	for j in {0..6}
	do
		git add *2022-03-"$i"*_"$j".csv
		git commit -m "update 2022-03-$i bucha all languages"
		git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data
	done
done
for i in {01..12}
do
        git add *hydrator-2022-04-"$i"*.csv

	for j in {0..6}
	do
	       git add *2022-04-"$i"*_"$j".csv
	       git commit -m "update 2022-04-$i bucha all languages"
 	       git push git@github.com-ukraine_data:Leibniz-HBI/ukraine_data
    done
done


