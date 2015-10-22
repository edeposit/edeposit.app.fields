from zope.schema.interfaces import IASCIILine, ITextLine, IChoice
from z3c.form.interfaces import ITextWidget, ISelectWidget

class IISBNLine(IASCIILine):
    pass

class IISBNWidget(ITextWidget):
    pass

class IPeriodicity(IChoice):
    pass

class IPeriodicityWidget(ISelectWidget):
    pass
