import sys
import fileinput
import hashlib
import time
import random
import string

#if __name__ == "__main__":
class Passwordr(object):
	"""Initialize the class"""
	def __init__(self, base, length=32):
		super(Passwordr, self).__init__();

		if(base):
			self.base = base;

		if(sys.argv[2]):
			self.length = int(sys.argv[2]);
		else:
			self.length = length;

		self.password = self.make_hash();

		return self.confusitizer();

	"""generate a new hash and return the string value"""
	def make_hash(self):
		return hashlib.sha224(str(int(time.time()))).hexdigest();

	"""get the unique values from an array"""
	"""http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order"""
	def array_unique(self, arr):
		_seen = set();
		_seen_add = _seen.add;

		return [_x for _x in arr if _x not in _seen and not _seen_add(_x)];

	"""gets the ball rolling by taking a randomly generated string and running it through a hash generator (sha1 in this case)"""
	def randomizer(self):
		seed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		_tmp = {
			"shuffled": "".join(random.sample(seed, len(seed))),
			"hash": self.password,
			"start": int(self.startmajigger()),
		};

		final = (_tmp["shuffled"] + _tmp["hash"])[_tmp["start"]:(self.length + _tmp["start"])];

		self.length = len(final);

		return final;

	def get_special(self):
		_seed = "_?+-.<?;:&#@";

		return "".join(random.sample(_seed, len(_seed)))[:1];


	"""takes confusitizer()'s array and adds some new random characters to it, depending on the length of the array"""
	def rediscombobulator(self, source):
		_unique = self.array_unique(source);

		print len(_unique);

	"""chooses a random starting point for randomizer()'s string"""
	def startmajigger(self):
		seed = "123456789"; #todo: refactor so it takes the length of the password string instead of these random numbers

		return "".join(random.sample(seed, len(seed)))[:1]

	"""turns output from randomizer() and rediscombobulator() into a string"""
	def confusitizer(self):
		_output = self.randomizer();
		_rediscombobulated = [];

		if(len(_output) <= self.length):
			_special = self.get_special();
			_source_array = list(_output);

			if(_special in _source_array):
				print "nope"
		
		return _output;

			
# Instantiate the Passwordr class
pw = Passwordr('test', 10)
