from django.views.generic import ListView
from school.models import Student


class StudentsList(ListView):
	model = Student
	paginate_by = 10
	template_name = 'school/students_list.html'
	ordering = 'group'

