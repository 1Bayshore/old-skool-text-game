import os
import importlib
from debug import dbg

gameroot = os.path.dirname(__file__) 

def clone(obj_module):
    '''Load specified module, call its clone() method, and return the resulting object.
    The object's module should be specified in python package format relative to the
    root of the game source tree, e.g. "domains.school.sword" refers to the python module
        ${gameroot}/domains/school/sword.py.'''
    try: 
        mod = importlib.import_module(obj_module)
        obj = mod.clone()  # TODO: allow pass-through parameters
    except ImportError:
        dbg.debug("Error importing module %s" % obj_module, 0)
        return None
    except AttributeError:
        dbg.debug("Error cloning from module %s: no clone() method" % obj_module)
        return None
    if obj == None:
        dbg.debug("Error cloning from module %s: clone() return None" % obj_module)
    return obj

def findGamePath(filepath):
    gamePath = os.path.relpath(filepath, gameroot).replace("\\", ".").replace("/", ".")
    (head, sep, tail) = gamePath.partition(".py")
    gamePath = head
    return gamePath
