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

		return str(final);

	def get_special(self):
		_seed = "_?+-.<?;:&#@";

		return "".join(random.sample(_seed, len(_seed)))[:1];


	"""takes confusitizer()'s array and adds some new random characters to it, depending on the length of the array"""
	def rediscombobulator(self, source):
		_unique = self.array_unique(source);

		if(len(_unique) == self.length):
			_diff = self.length - len(_unique);
			_special = self.get_special();
			
			if(_diff > 0):
				_unique.insert(_diff, _special);
			else :
				_unique.insert(self.get_random_pos_from(_unique), _special);

			_unique.pop();

		return _unique;

	"""chooses a random starting point for randomizer()'s string"""
	def startmajigger(self):
		_seed = "123456789"; #todo: refactor so it takes the length of the password string instead of these random numbers

		return "".join(random.sample(_seed, len(_seed)))[:1]

	def get_random_pos_from(self, _input):
		return random.randint(1,len(_input)) + 1;

	"""turns output from randomizer() and rediscombobulator() into a string"""
	def confusitizer(self):
		_output = self.randomizer();
		_rediscombobulated = list();

		if(len(_output) <= self.length):
			_special = self.get_special();
			_source_array = list(_output);
			_rediscombobulated = self.rediscombobulator(_source_array);
			_rediscombobulated.insert(self.get_random_pos_from(_rediscombobulated), _special);

			_output = "".join(_rediscombobulated);

		print _output;

			
# Instantiate the Passwordr class
pw = Passwordr('test', 10)