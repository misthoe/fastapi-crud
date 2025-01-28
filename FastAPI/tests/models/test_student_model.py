import pytest

from models.student import Student
from pydantic import ValidationError


class TestStudentModel:
    def test_student_model(self):
        student = Student(name="John", last_name="Doe", major="math", age=30)
        assert student.name == "John"
        assert student.last_name == "Doe"
        assert student.major == "math"
        assert student.age == 30

    def test_student_model_invalid(self):
        student_data = {"name": "John", "last_name": "Doe"}
        # Needed because model is at table, and ignores validation the normal way
        # Missing arguments should raise ValidationError
        with pytest.raises(ValidationError):
            Student.model_validate(student_data)
