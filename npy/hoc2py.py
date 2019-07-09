import hoc

class HocToPy:
    """Static class to simplify getting variables from hoc."""
    hocvar = None
   
    def get(name,return_type):
        """Return a variable from hoc.
           name can be a hoc variable (int, float, string) or a function/method
           that returns such a variable.
        """
        fmt_dict = {'int' : '%d', 'float' : '%g', 'string' : '\\"%s\\"'}
        hoc_commands = ['strdef cmd',
                        '{sprint(cmd,"HocToPy.hocvar = %s",%s)}' % (fmt_dict[return_type],name),
                        '{nrnpython(cmd)}']
        for cmd in hoc_commands:
            hoc.execute(cmd)
        return HocToPy.hocvar
    get = staticmethod(get)
   
hoc.execute("a = 2")
hoc.execute("pi = 3.14159")
hoc.execute("strdef hello")
hoc.execute('hello = "Hello World"')

a     = HocToPy.get('a','int')
pi    = HocToPy.get('pi','float')
hello = HocToPy.get('hello','string')

print("a = ", a)
print("pi = ", pi)
print(hello)

hoc.execute('create soma')
hoc.execute('{finitialize(-70)}')
v = HocToPy.get('soma.v(.5)', 'float')
print('v = ', v)

