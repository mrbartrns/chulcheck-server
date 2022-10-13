from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumMaximumLengthValidator:
    min_length = 8
    max_length = 20

    def validate_minimum_maximum_length(self, username):
        if len(username) < self.min_length:
            raise ValidationError(f"username must be longer than {self.min_length}.")

        if self.max_length and len(username) > self.max_length:
            raise ValidationError(
                _(
                    f"username must be longer than {self.min_length} and shorter than {self.max_length}."
                )
            )

    def validate(self, username):
        self.validate_minimum_maximum_length(username)


class NumericUsernameValidator:
    def validate_numeric_username(self, username):
        if username.isdigit():
            raise ValidationError(_("This username is entirely numeric."))

    def validate(self, username):
        self.validate_numeric_username(username)


def validate_username(username):
    errors = []
    validators = [MinimumMaximumLengthValidator, NumericUsernameValidator]

    for validator in validators:
        try:
            validator().validate(username)
        except ValidationError as error:
            print("raise validation error")
            errors.append(error)

    if errors:
        raise ValidationError(errors)
