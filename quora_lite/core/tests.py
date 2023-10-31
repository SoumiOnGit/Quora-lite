from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Question, Answer
from .views import QuestionListView

class QuoraLikeAppTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create sample question
        self.question = Question.objects.create(
            user=self.user,
            title='Sample Question',
            text='This is a test question.'
        )

    def test_question_creation(self):
        question = Question.objects.get(id=1)
        self.assertEqual(question.title, 'Sample Question')
        self.assertEqual(question.text, 'This is a test question.')
        self.assertEqual(question.user, self.user)

    def test_answer_creation(self):
        answer = Answer.objects.create(
            user=self.user,
            question=self.question,
            text='This is a test answer.'
        )
        self.assertEqual(answer.text, 'This is a test answer.')
        self.assertEqual(answer.user, self.user)
        self.assertEqual(answer.question, self.question)

    def test_question_list_view(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['questions'],
            ['<Question: Sample Question>']
        )

    def test_question_detail_view(self):
        response = self.client.get(reverse('question_detail', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Question')
        self.assertContains(response, 'This is a test question.')

    def test_question_form_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('question_form'))
        self.assertEqual(response.status_code, 200)

    def test_answer_form_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('answer_form', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
