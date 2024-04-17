from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choices
from django.db.models import F
from django.views import generic
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import QuestionForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# Home View:
class IndexView(generic.ListView):
    template_name='poll/index.html'
    context_object_name='question_posted'
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.order_by('-question')
# Poll View:
class DetailView(generic.DetailView):
    model=Question
    template_name='poll/detail.html'
# Voting Logic:
def Vote(request,pk):
   question = get_object_or_404(Question, pk=pk)
   if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choices, pk=selected_choice_id)
        selected_choice.votes += 1
        selected_choice.save()

        return redirect('result', pk=question.pk)

   return HttpResponse("Invalid request")
# Voting Result view:
class ResultView(generic.DetailView):
    model=Question
    template_name='poll/result.html'


def Login(request):
    global user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            msg=messages.add_message(request,messages.ERROR,'Invalid Email or Password')
            return render(request,'poll/login.html')
    else:
        return redirect('home')
# Add Question Form:
@method_decorator(login_required, name='dispatch')
class Add_question(generic.FormView):
    template_name = 'poll/question_form.html'
    form_class = QuestionForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def Authenticate(request):
    return render(request,'poll/login.html')
def SignUp(request):
    return render(request,'poll/sign_up.html')
def Registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('registration')
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()
        return redirect('login')
    else:
        return redirect('add_question')
def Profile(request):
   return redirect('home')

def signout(request):
    messages.add_message(request,level=messages.INFO,message=f'logged out !')
    logout(request)
    return redirect('home')