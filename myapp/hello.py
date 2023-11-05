import fire

def hello(name="Worlds"):
  return "Hello %s! and T1 fighting" % name

if __name__ == '__main__':
  fire.Fire(hello)
