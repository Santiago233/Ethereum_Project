firstbeginblock=1
mkdir -p block/${firstbeginblock}
path="./block/$firstbeginblock"
#echo $path
for((i=0;i<=5;i++));
do
beginblock=$(($i))
endblock=$(($beginblock))
beginblock_16=$(echo "obase=16;$beginblock" | bc)
endblock_16=$(echo "obase=16;$endblock" | bc)
curl --data '{"method":"eth_getBlockByNumber","params":["0x'$beginblock_16'",true],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -s -X POST localhost:8545 >> $beginblock.txt
size=$(ls -l $beginblock.txt | awk '{print $5}')
echo $beginblock" "$size
if [ $size = 0 ]
then
	exit
fi
done
#zip $firstbeginblock.zip *.txt
#find -name "*.txt" |xargs rm -rfv
all_files=$(find -name "*.txt")
for file in $all_files
do
	mv -v $file $path
done
#zip $firstbeginblock.zip *.txt
#find -maxdepth 1 -name "*.txt" |xargs rm -rfv
#cp $firstbeginblock.zip '/mnt/d/材料/毕业设计/Project/GraduationProject/get_data/block/1'