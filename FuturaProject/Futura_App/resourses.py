from import_export import resources
from Futura_App.models import Person


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
