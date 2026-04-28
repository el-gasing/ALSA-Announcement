from django.shortcuts import redirect, render


VALID_NAME = 'Yanto'
VALID_NIM = 'B011241037'


def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('nama', '').strip()
        nim = request.POST.get('nim', '').strip()

        if name == VALID_NAME and nim == VALID_NIM:
            request.session['loading_allowed'] = True
            request.session['participant_name'] = name
            return redirect('announcements:loading')

        return render(request, 'announcements/index.html', {'invalid_login': True})

    return render(request, 'announcements/index.html')


def loading_page(request):
    if not request.session.get('loading_allowed'):
        return redirect('announcements:login')

    return render(request, 'announcements/loading.html')


def department_page(request):
    if not request.session.get('loading_allowed'):
        return redirect('announcements:login')

    return render(request, 'announcements/department.html', {
        'participant_name': request.session.get('participant_name', VALID_NAME),
        'department_name': 'HUMAN RESOURCE DEVELOPMENT DEPARTMENT',
        'quote': 'Work Hard in Silence, Let Your Succeed be Noise',
    })

# Create your views here.
