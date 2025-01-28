import pytest

from models.teacher import Teacher
from pydantic import ValidationError


class TestStudentModel:

    def test_teacher_model(self):
        teacher_data = {"name": "John", "last_name": "Doe", "specialty": "physics", "age": 50}
        teacher = Teacher(**teacher_data)
        assert teacher.name == "John"
        assert teacher.last_name == "Doe"
        assert teacher.specialty == "physics"
        assert teacher.age == 50

    def test_teacher_model_invalid(self):
        teacher_data = {"name": "John", "last_name": "Doe"}
        # Needed because model is at table, and ignores validation the normal way
        # Missing arguments should raise ValidationError
        with pytest.raises(ValidationError):
            Teacher.validate(teacher_data)
