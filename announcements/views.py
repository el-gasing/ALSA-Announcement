from django.shortcuts import redirect, render

from .departments import DEPARTMENTS
from .models import Participant


def render_department(request, dept_key):
    department = DEPARTMENTS.get(dept_key, DEPARTMENTS['hrd'])
    return render(request, 'announcements/department.html', {
        'participant_name': request.session.get('participant_name', ''),
        'department_name': department['department_name'],
        'title_lines': department['title_lines'],
        'quote': department['quote'],
        'logo_file': department['logo_file'],
        'greeting_department': department['greeting_department'],
        'welcome_department': department['welcome_department'],
    })


def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('nama', '').strip()
        nim = request.POST.get('nim', '').strip().upper()

        participant = Participant.objects.filter(nim=nim).first()
        if participant and participant.name.casefold() == name.casefold():
            request.session['loading_allowed'] = True
            request.session['participant_name'] = participant.name
            request.session['department'] = participant.department
            return redirect('announcements:loading')

        return render(
            request,
            'announcements/index.html',
            {
                'invalid_login': True,
                'submitted_name': name,
                'submitted_nim': nim,
            },
        )

    return render(request, 'announcements/index.html')


def loading_page(request):
    if not request.session.get('loading_allowed'):
        return redirect('announcements:login')

    return render(request, 'announcements/loading.html')


def back_to_login(request):
    request.session.flush()
    return redirect('announcements:login')


def department_page(request):
    if not request.session.get('loading_allowed'):
        return redirect('announcements:login')

    dept_key = request.session.get('department', 'hrd')
    return render_department(request, dept_key)


def department_internal_page(request):
    if not request.session.get('loading_allowed'):
        return redirect('announcements:login')

    return render_department(request, 'internal')


def department_external_page(request):
    if not request.session.get('loading_allowed'):
        return redirect('announcements:login')

    return render_department(request, 'external')
