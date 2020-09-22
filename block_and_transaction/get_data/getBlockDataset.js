var fs = require("fs");
var web3 = require('web3');

var diyicengStart = 0;
var diyicengLength = 4794;
var diercengLength = 1000;
var shuchu = "Block_queMinnerReward_"+diyicengStart+"to"+(diyicengLength-1)+".csv";
var shuchu2 = "NormalTransaction_"+diyicengStart+"to"+(diyicengLength-1)+".csv";

var file1 = fs.createWriteStream(shuchu, {flag:"w"});
var file2 = fs.createWriteStream(shuchu2, {flag:"w"});
file1.write("blockNumber, timestamp, size, difficulty, transactionCount, minerAddress, minerExtra, gasLimit, gasUsed, gasPrices\n");
file2.write("blockNumber, timestamp, transactionHash, from, to, creates, value\n");

function dayin(wenzi) {
	var mydate = new Date();
	console.log(mydate.toGMTString().substr(17), wenzi);
}


function duqufenxi(diyiceng, blockNumber) {
	var dir = "J:/eth_block_unzip/"+diyiceng*1000+"/"+blockNumber+".txt";

	var data = fs.readFileSync(dir);
	var miaomi = JSON.parse(data).result;
	var timestamp = parseInt(miaomi.timestamp, 16);


	var gasPrices = [];

	for(i in miaomi.transactions) {
		gasPrices.push( parseInt(miaomi.transactions[i].gasPrice, 16) );

		var toWrite = [
			blockNumber,
			timestamp,
			miaomi.transactions[i].hash,
			miaomi.transactions[i].from,
			miaomi.transactions[i].to,
			miaomi.transactions[i].creates,
			web3.toBigNumber(miaomi.transactions[i].value).toString(10)
		];

		file2.write(toWrite.valueOf()+"\n");
	}

	
	var minerExtra;
	try {
		minerExtra = '"'+web3.toAscii(miaomi.extraData).replace(/"/g,'""')+'"';
	}
	catch(e) {
	}

	var toWrite = [
		blockNumber,
		timestamp,
		parseInt(miaomi.size, 16),
		parseInt(miaomi.totalDifficulty, 16),
		miaomi.transactions.length,
		miaomi.miner,
		minerExtra,
		parseInt(miaomi.gasLimit, 16),
		parseInt(miaomi.gasUsed, 16),
		'"'+gasPrices.valueOf()+'"',
	];
	file1.write(toWrite.valueOf()+"\n");

}


for(var diyiceng=diyicengStart; diyiceng<diyicengLength; ++diyiceng) {
	dayin(diyiceng);

	for(var dierceng=0; dierceng<diercengLength; ++dierceng) {

		var blockNumber = diyiceng*1000+dierceng;
		duqufenxi(diyiceng, blockNumber);

	}


}
