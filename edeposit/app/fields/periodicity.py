import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser import widget

from .interfaces import IPeriodicityWidget
from z3c.form.browser.select import  SelectWidget

@zope.interface.implementer_only(IPeriodicityWidget)
class PeriodicityWidget(SelectWidget):
    """Input type text widget implementation."""

    klass = u'periodicity-widget'
    
    def canChange(self):
        return True


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def PeriodicityFieldWidget(field, request):
    return FieldWidget(field, PeriodicityWidget(request))
