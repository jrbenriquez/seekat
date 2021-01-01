import factory
import factory.fuzzy

from factory import django as django_factory

from authentication.models import User
from django_countries import countries

from se_core.models import Category
from se_core.models import Seek
from se_core.models import Seeker
from se_core.models import Seekat
from se_core.models import SeekatAddress


class UserFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class SeekerFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = Seeker

    user = factory.SubFactory(UserFactory)


class SeekatAddressFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = SeekatAddress

    name = factory.Faker('city')
    address1 = factory.Faker('street_name')
    address2 = factory.Faker('street_address')
    zip_code = factory.Faker('postcode')
    city = factory.Faker('city')
    state = factory.Faker('city')
    country = factory.fuzzy.FuzzyChoice([x[0] for x in countries])


class SeekatFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = Seekat

    name = factory.Faker('company')
    description = factory.Faker('bs')
    address = factory.SubFactory(SeekatAddressFactory)


class CategoryFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class SeekFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = Seek

    seeker = factory.SubFactory(SeekerFactory)
    seekat = factory.SubFactory(SeekatFactory)
    category = factory.SubFactory(CategoryFactory)


