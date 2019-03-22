from django.shortcuts import render, redirect
from .models import Shout
# from .forms import ShoutForm
from .forms import ShoutModelForm

# Create your views here.
def home(request):
    # if request.method == 'POST':
    # # POST
    #     # 고객센터 문의 작성하기
    form = ShoutModelForm(request.POST)
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # # title = request.POST.get('title')
        # # content = request.POST.get('content')
        # Shout.objects.create(title=title, content=content)
        form.save()

    # 너무 길다
    # if title == "" or content == "":
    #     messages.success

        return redirect('shouts:home')
    else:
        # GET
        # 고객센터 form 보여하기
        # 문의사항 전부 보여주기
        # form = ShoutForm()
        form = ShoutModelForm()
        shouts = Shout.objects.all()
        context = {
            'shouts': shouts,
            # 'form': form
        }
        return render(request, 'shouts/home.html', context)


def create(request):
    if request.method == "POST":

        # POST 글을 DB에 저장
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')
    else:
        # GET 글 작성할 수 있는 form
        form = ShoutModelForm()
        return render(request, 'shouts/form.html', {'form': form})




def update(request, id):
    shout = Shout.objects.get(pk=id)

    if request.method == "POST":
        # 수정하기
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
            return redirect('shouts:home')

    else:
        # 편집하기
        form = ShoutModelForm(instance=shout)
        context = {
            # 'shout': shout,
            'form': form
        }
        return render(request, 'shouts/form.html', context)
