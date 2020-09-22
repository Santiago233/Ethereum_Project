#选取其中前7000000块block
#部分区块中有交易的receipt，部分区块中没有，没有的区块就是result[]；特别注意区块0不报result[]，而是报error[]
for((i=0;i<7000;i++));
do
	firstbeginblock=$(($i*1000))
	mkdir -p receipt/${firstbeginblock}
	path="./receipt/$firstbeginblock"
	for((j=0;j<1000;j++));
	do
		beginblock=$(($i*1000+$j))
		endblock=$(($beginblock))
		beginblock_16=$(echo "obase=16;$beginblock" | bc)
		endblock_16=$(echo "obase=16;$endblock" | bc)
		#echo $beginblock_16
		curl --data '{"method":"parity_getBlockReceipts","params":["0x'$beginblock_16'"],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -s -X POST localhost:8545 >> $beginblock.txt
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