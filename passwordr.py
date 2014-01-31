import sys, hashlib, time, random, string

class Passwordr(object):
	def __init__(self, base="", length=32):
		"""Initialize the class"""

		super(Passwordr, self).__init__();

		if(sys.argv[1]):
			self.base = sys.argv[1];
		else:
			self.base = base;

		if(sys.argv[2]):
			self.length = int(sys.argv[2]);
		else:
			self.length = length;

		self.password = self.make_hash();

		return self.confusitizer();

	def make_hash(self, length=0):
		"""generate a new hash and return the string value"""
		
		_str = hashlib.sha224(str(int(time.time()))).hexdigest();

		if(length > 0 and len(_str) > length):
			_str = "".join(_str)[:length];

		return _str;

	def array_unique(self, arr):
		"""get the unique values from an array"""
		"""http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order"""

		_seen = set();
		_seen_add = _seen.add;

		return [_x for _x in arr if _x not in _seen and not _seen_add(_x)];

	def randomizer(self):
		"""gets the ball rolling by taking a randomly generated string and running it through a hash generator (sha1 in this case)"""

		seed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		_tmp = {
			"shuffled": "".join(random.sample(seed, len(seed))),
			"hash": self.password,
			"start": self.get_random_pos_from(self.password),
		};

		final = (_tmp["shuffled"] + _tmp["hash"])[_tmp["start"]:(self.length + _tmp["start"])];

		self.length = len(final);

		return str(final);

	def get_specials(self, num=1, rand=True, inputLen=10):
		"""Get a variable number of special characters (symbols)"""

		_seed = "_?+-~.<>^*$;:&#@";
		_minNumberChars = 5;

		if(rand):
			num = random.randint(1, inputLen) - _minNumberChars;

		return random.sample(_seed, len(_seed))[:num];

	def rediscombobulator(self, source):
		"""takes confusitizer()'s array and a new random character to it, depending on the length of the array"""

		_unique = self.array_unique(source);

		_diff = self.length - len(_unique);
		#_special = self.get_specials(rand=True, inputLen=self.length);

		if(_diff < 0):
			_diff_chars = list(self.make_hash(_diff));
			_unique.extend(_diff_chars);

		return _unique;

	def get_random_pos_from(self, _input):
		"""Get a random position from the input string"""

		if(_input):
			return random.randint(1,len(_input)) + 1;

	def confusitizer(self, ret=False):
		"""turns output from randomizer() and rediscombobulator() into a string"""

		_output = self.randomizer();
		_rediscombobulated = list();

		if(len(_output) <= self.length):
			_special = self.get_specials(rand=True, inputLen=self.length);
			_source_array = list(_output);
			_rediscombobulated = self.rediscombobulator(_source_array);
			_randPos = self.get_random_pos_from(_rediscombobulated);

			for item in _special:
				if(_randPos < len(_rediscombobulated)):
					_rediscombobulated.pop(_randPos);

				_rediscombobulated.insert(_randPos, item);

			_rediscombobulated.pop();
			_output = "".join(_rediscombobulated);

		if(ret):
			return _output;
		else:
			print _output;


# Instantiate the Passwordr class
pw = Passwordr()