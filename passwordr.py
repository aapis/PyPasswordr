import sys
import hashlib
import time
import random
import string

#if __name__ == "__main__":
class Passwordr(object):
	"""Initialize the class"""
	def __init__(self, base, length, salt):
		super(Passwordr, self).__init__();

		if(base):
			self.base = base;

		if(salt):
			self.salt = salt;

		self.length = length;

		self.password = self.makeHash();

		print self.randomizer();

	"""generate a new hash and return the string value"""
	def makeHash(self):
		return hashlib.sha224(str(int(time.time()))).hexdigest();

	"""gets the ball rolling by taking a randomly generated string and running it through a hash generator (sha1 in this case)"""
	def randomizer(self):
		seed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		_tmp = {
			"shuffled": "".join(random.sample(seed, len(seed))),
			"hash": self.password,
			"start": int(self.startmajigger()),
		};

		final = (_tmp["shuffled"] + _tmp["hash"])[_tmp["start"]:self.length];
		#_tmp = self.makeHash();

		return final;

	"""takes confusitizer()'s array and adds some new random characters to it, depending on the length of the array"""
	def rediscombobulator(self):
		pass

	"""chooses a random starting point for randomizer()'s string"""
	def startmajigger(self):
		seed = "123456789"; #todo: refactor so it takes the length of the password string instead of these random numbers

		return "".join(random.sample(seed, len(seed)))[:1]

	"""turns output from randomizer() and rediscombobulator() into a string"""
	def confusitizer(self):
		pass

			
# Instantiate the Passwordr class
pw = Passwordr('test', 32, "test2")
