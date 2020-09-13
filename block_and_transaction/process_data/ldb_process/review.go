package main
import(
	"fmt"
	"github.com/syndtr/goleveldb/leveldb"
	"log"
	"os"
)

func read_leveldb(){
	fmt.Println("My first leveldb process")
	db, err := leveldb.OpenFile(os.Args[1], nil)
	if err != nil{
		log.Fatal("No!")
	}
	defer db.Close()

	iter := db.NewIterator(nil, nil)
	for iter.Next(){
		key := iter.Key()
		fmt.Println("key:%s", key)
	}
	fmt.Println("\n")
}

func main(){
	read_leveldb()
}