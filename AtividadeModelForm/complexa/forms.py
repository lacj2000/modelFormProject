from django.forms import ModelForm
from complexa.models import Author, PublishingCompany, Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PublishingCompanyForm(ModelForm):
    class Meta:
        model = PublishingCompany
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'