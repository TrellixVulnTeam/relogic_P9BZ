import sys
import os
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Memoize(object):
  def __init__(self, f):
    self.f = f
    self.cache = {}

  def __call__(self, *args):
    if args not in self.cache:
      self.cache[args] = self.f(*args)
    return self.cache[args]

def load_pickle(path, memoized=True):
  return _load_pickle_memoize(path) if memoized else _load_pickle(path)

def _load_pickle(path):
  with open(path, 'rb') as f:
    return pickle.load(f)

@Memoize
def _load_pickle_memoize(path):
  return _load_pickle(path)


def write_pickle(o, path):
  dir = path.rsplit('/', 1)[0]
  if not os.path.exists(dir):
    os.mkdir(dir)
  with open(path, 'wb') as f:
    pickle.dump(o, f, -1)

def log(*args):
  msg = ' '.join(map(str, args))
  sys.stdout.write(msg + '\n')
  sys.stdout.flush()


def heading(*args):
  log()
  log(80 * '=')
  log(*args)
  log(80 * '=')