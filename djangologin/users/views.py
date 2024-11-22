from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'hide_nav':True})

def signup(request):
    if request.method=='POST':
        '''
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 폼 검증 성공
            user = form.save()  # 사용자 저장
            home(request, user)  # 로그인 처리
            return redirect('home')  # 회원가입 후 홈으로 리디렉션
        '''
    elif request.method=='GET':
        return render(request,'signup.html',{'hide_nav':True})
# Create your views here.
