from zope.interface import classImplements
from zope.interface import implementer
from zope.interface import Interface
from zope.interface.interfaces import IInterface
from zope.interface.interfaces import IMethod

from zope.schema import ASCIILine
from .interfaces import IISBNLine

@implementer(IISBNLine)
class ISBNLine(ASCIILine):
    def constraint(self,value):
        return super(ISBNLine,self).constraint(value)

