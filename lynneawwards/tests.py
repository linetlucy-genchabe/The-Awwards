from django.test import TestCase

from .models import *

# Create your tests here.



class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='lynne', password='linet.2211')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class ProjectsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='lynne')
        self.project = Projects.objects.create(id=1, title='test project', project_image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='nice',
                                        user=self.user, url='https://lynneawwards.herokuapp.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

    def test_save_project(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_projects(self):
        self.project.save()
        projects = Projects.all_projects()
        self.assertTrue(len(projects) > 0)

    def test_search_projects(self):
        self.project.save()
        project = Projects.search_projects('test')
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = Projects.search_projects('test')
        self.assertTrue(len(project) < 1)

