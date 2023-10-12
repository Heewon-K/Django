from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Question
from .forms import QuestionForm

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    render 함수는 context에 있는 모델 데이터를 pybo/quesion_list.html(템플렛이라고 부른다)파일에 적용하여 HTML코드로 변환
    """
    question_list = Question.objects.order_by('-create_date')  # 작성일시 역순으로
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    # return HttpResponse("안녕하세요! pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)  # Question.objects.get(id=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    question.answer_set.create(content = request.POST.get('content'),
                               create_date = timezone.now())
    return redirect('pybo:detail', question_id = question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() # request.method가 'GET'인 경우 호출
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)