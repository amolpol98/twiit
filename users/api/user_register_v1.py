from django.contrib.auth import get_user_model

from core.api.decorators.validators import allowed_methods
import core.api.responses.error_codes as error_codes
from .user_register import UserRegister

User = get_user_model()


class UserRegisterV1(UserRegister):
    __versions_compatible__ = ('1', '1.0')
    template_name = 'registration/user_register_form.html'

    def __init__(self, **kwargs):
        super(UserRegisterV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt
        request = self.request

        print ('entered register')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            self.set_bad_req('passwords dont match', error_codes.DEFAULT_ERROR_CODE)
            return self._data

        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        print (new_user.username, new_user.id)
        return self._data
