#选取其中前7000000块block
for((i=0;i<2;i++));
do
	firstbeginblock=$(($i*10))
	mkdir -p receipt/${firstbeginblock}
	path="./receipt/$firstbeginblock"
	for((j=0;j<=9;j++));
	do
		beginblock=$(($i*10+$j))
		endblock=$(($beginblock))
		beginblock_16=$(echo "obase=16;$beginblock" | bc)
		endblock_16=$(echo "obase=16;$endblock" | bc)
		#curl --data '{"method":"parity_getBlockReceipts","params":["0x'$beginblock_16'",true],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -s -X POST localhost:8545 >> $beginblock.txt
		size=$(ls -l $beginblock.txt | awk '{print $5}')
		echo $beginblock" "$size
		if [ $size = 0 ]
		then
			exit
		fi
	done
	all_files=$(find -maxdepth 1 -name "*.txt")
	for file in $all_files
	do
		mv -v $file $path
	done
done