from zope.interface import implementer, implements, implementsOnly
from zope.component import adapter

from z3c.form.interfaces import IFieldWidget, IFormLayer, IDataManager, NOVALUE
from z3c.form.widget import FieldWidget
from interfaces import IISBN
from widgets import ISBNWidget
from plone.z3cform.layout import FormWrapper

class ISBNWidget(NamedFileWidget):
    implements(IVoucherFileWidget)
    pass

@implementer(IFieldWidget)
@adapter(IISBNField, IFormLayer)
def ISBNFieldWidget(field, request):
    return FieldWidget(field, ISBNWidget(request))
