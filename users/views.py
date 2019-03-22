from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# '/users/' => 홈페이지
# '/users/login' => 로그인 화면


def home(request):
    return render(request, 'users/home.html')


def login_user(request):
    if request.method == "POST":
        # /users/login GET
        # -> 로그인 창 render
        # /users/login POST
        # -> 로그인(유저 검증)
        # 만약에 username, password 넘어온 값이 DB에 저장된 값과 같다면,
        #   로그인
        # 아니면
        #   X
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 1. 사용자가 로그인 되었을 때
            messages.success(request, "성공적으로 로그인 되었습니다")
            # Redirect to a success page.
            return redirect('home')
        else:
            # 2. 사용자가 로그인 되지 않았을 때
            messages.success(request, "로그인이 되지 않았습니다. 다시 시도해 주세요")
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    # 유저를 로그아웃 시킨다.
    logout(request)
    # 유저에게 로그아웃이 되었다는 메시지를 전달한다.
    messages.success(request, "성공적으로 로그아웃 되었습니다")
    return redirect('home')


def register(request):
    if request.method == "POST":
        # 회원가입 시키기(DB에 사용자 정보를 저장)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        pass
    else:
        # 회원정보를 받는 form 보여주기
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    