import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser import widget

from .interfaces import IISBNWidget
from z3c.form.browser.text import TextWidget

@zope.interface.implementer_only(IISBNWidget)
class ISBNWidget(TextWidget):
    """Input type text widget implementation."""

    klass = u'isbn-widget'

    def update(self):
        super(ISBNWidget, self).update()


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def ISBNFieldWidget(field, request):
    return FieldWidget(field, ISBNWidget(request))
