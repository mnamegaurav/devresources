import copy
from django.test import TestCase

from accounts.forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.valid_form_data = {
            'email': 'test@test.com',
            'password1': 'Testing321',
            'password2': 'Testing321'
        }

    def test_form_validates_if_correct_data_is_supplied(self):
        form = CustomUserCreationForm(self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_email_is_a_mandatory_field(self):
        valid_form_data_copy = copy.deepcopy(self.valid_form_data)
        del valid_form_data_copy['email']
        form = CustomUserCreationForm(valid_form_data_copy)
        self.assertFalse(form.is_valid())

    def test_password1_is_a_mandatory_field(self):
        valid_form_data_copy = copy.deepcopy(self.valid_form_data)
        del valid_form_data_copy['password1']
        form = CustomUserCreationForm(valid_form_data_copy)
        self.assertFalse(form.is_valid())

    def test_password2_is_a_mandatory_field(self):
        valid_form_data_copy = copy.deepcopy(self.valid_form_data)
        del valid_form_data_copy['password2']
        form = CustomUserCreationForm(valid_form_data_copy)
        self.assertFalse(form.is_valid())
