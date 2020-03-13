import sys
import leveldb
def read_data():
	if len(sys.argv) < 2:
		print "pls input leveldb dir"
		return -1
	db = leveldb.LevelDB(sys.argv[1])
	for k in db.RangeIter(include_value = False):
			print db.Get(k)
if __name__ == '__main__':
	read_data()
	print "read end"