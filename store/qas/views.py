from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import QuestionForm, AnswerForm
from .models import Question
from store.products.models import Product


class QuestionCreateView(generic.CreateView):
    form_class = QuestionForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)


class AnswerCreateView(generic.CreateView):
    form_class = AnswerForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(Question, id=question_id)
        obj.question = question

        return super().form_valid(form)