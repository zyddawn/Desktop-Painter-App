import argparse
import os
import sys

class OPs(object):
	def __init__(self, cmds):
		self._action = cmds[0]
		self._params = cmds[1:]

	@property
	def action(self):
		return self._action

	@property
	def params(self):
		return self._params



def parseArgs(argv):
	parser = argparse.ArgumentParser(description='Command Line Arguments for Yudong\'s Mini CG System', 
									add_help=False)
	parser.add_argument('--script', default='', type=str, dest='script')
	parser.add_argument('--path', default='', type=str, dest='path')
	args = parser.parse_args(argv[1:])
	return args


def parseScript(path):
	if os.path.exists(path):
		try:
			f = open(path, 'r')
			rl = f.readlines()
			op_arr = []
			for l in rl:
				cmd = l.strip("\n\t").split(" ")
				if '' in cmd:
					cmd = cmd.remove('')
				if cmd:
					new_op = OPs(cmd)
					op_arr.append(new_op)
			return op_arr
		except:
			raise RuntimeError("Can't read file.")
	else:
		raise RuntimeError("Script path doesn't exist.")


if __name__ == '__main__':
	args = parseArgs(sys.argv)
	if args.script:
		op_arr = parseScript(args.script)
		for i, x in enumerate(op_arr):
			print("{0}: {1}".format(i, x.action))

