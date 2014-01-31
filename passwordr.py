import sys, hashlib, time, random, string

class Passwordr(object):
	"""Initialize the class"""
	def __init__(self, base="", length=32):
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

	"""generate a new hash and return the string value"""
	def make_hash(self, length=0):
		_str = hashlib.sha224(str(int(time.time()))).hexdigest();

		if(length > 0 and len(_str) > length):
			_str = "".join(_str)[:length];

		return _str;

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
			"start": self.get_random_pos_from(self.password),
		};

		final = (_tmp["shuffled"] + _tmp["hash"])[_tmp["start"]:(self.length + _tmp["start"])];

		self.length = len(final);

		return str(final);

	def get_special(self):
		_seed = "_?+-.<?;:&#@";

		return "".join(random.sample(_seed, len(_seed)))[:1];


	"""takes confusitizer()'s array and a new random character to it, depending on the length of the array"""
	def rediscombobulator(self, source):
		_unique = self.array_unique(source);

		if(len(_unique) < self.length):
			_diff = self.length - len(_unique);
			_special = self.get_special();
			if(_diff > 0):
				_diff_chars = list(self.make_hash(_diff));
				print len(_diff_chars), len(_unique)
				_unique.insert(_diff, _special);
				_unique.extend(_diff_chars);
			else :
				_unique.insert(self.get_random_pos_from(_unique), _special);

		return _unique;

	def get_random_pos_from(self, _input):
		return random.randint(1,len(_input)) + 1;

	"""turns output from randomizer() and rediscombobulator() into a string"""
	def confusitizer(self, ret=False):
		_output = self.randomizer();
		_rediscombobulated = list();

		if(len(_output) <= self.length):
			_special = self.get_special();
			_source_array = list(_output);
			_rediscombobulated = self.rediscombobulator(_source_array);
			_rediscombobulated.insert(self.get_random_pos_from(_rediscombobulated), _special);
			_output = "".join(_rediscombobulated);


		print len(_output)
		if(ret):
			return _output;
		else:
			print _output;


# Instantiate the Passwordr class
pw = Passwordr()