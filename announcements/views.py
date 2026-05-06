from django.shortcuts import redirect, render


# ── Participant roster ──────────────────────────────────────────
# Maps NIM → (name, department_key)
PARTICIPANTS = {
    'B011241001': ('Irwan',  'hrd'),
    'B011241002': ('Anam',   'internal'),
    'B011241003': ('Kifa',   'external'),
    'B011241004': ('Chris',  'apr'),
    'B011241005': ('Issa',   'tim'),
    'B011241006': ('Galuh',  'mcd'),
    'B011241007': ('Arfa',   'lrc'),
    'B011241008': ('Hagiet', 'english'),
    'B011241009': ('Qadar',  'secretariat'),
    'B011241010': ('Arga',   'funding'),
}

# ── Department metadata ─────────────────────────────────────────
# Maps department_key → presentation and letter copy
DEPARTMENTS = {
    'hrd': {
        'department_name': 'HUMAN RESOURCE DEVELOPMENT DEPARTMENT',
        'title_lines': ['HUMAN RESOURCE DEVELOPMENT', 'DEPARTMENT'],
        'quote': 'Work Hard in Silence, Let Your Succeed be Noise',
        'logo_file': 'img/logo_hrd.svg',
        'greeting_department': 'HRD',
        'welcome_department': 'HRD',
    },
    'internal': {
        'department_name': 'INTERNAL AFFAIRS DEPARTMENT',
        'title_lines': ['INTERNAL AFFAIRS DEPARTMENT'],
        'quote': 'Internal Kuat, ALSA Hebat',
        'logo_file': 'img/logo_internal.svg',
        'greeting_department': 'Internal',
        'welcome_department': 'Internal Affairs',
    },
    'external': {
        'department_name': 'EXTERNAL AFFAIRS DEPARTMENT',
        'title_lines': ['EXTERNAL AFFAIRS DEPARTMENT'],
        'quote': 'Give More Contribution, in ALSA to Relation',
        'logo_file': 'img/logo_external.svg',
        'greeting_department': 'External',
        'welcome_department': 'External',
    },
    'apr': {
        'department_name': 'ALUMNI & PUBLIC RELATION DEPARTMENT',
        'title_lines': ['ALUMNI & PUBLIC RELATION', 'DEPARTMENT'],
        'quote': 'We Build, We Connect, We Keep',
        'logo_file': 'img/logo_apr_cropped.png',
        'greeting_department': 'APR',
        'welcome_department': 'APR',
    },
    'tim': {
        'department_name': 'TECHNOLOGY, INFORMATION, MULTIMEDIA DEPARTMENT',
        'title_lines': ['TECHNOLOGY, INFORMATION,', 'MULTIMEDIA DEPARTMENT'],
        'quote': 'Alone We Can Do So Little, Together We Can Do So Much',
        'logo_file': 'img/logo_tim_cropped.png',
        'greeting_department': 'TIM',
        'welcome_department': 'TIM',
    },
    'mcd': {
        'department_name': 'MOOT COURT DEPARTMENT',
        'title_lines': ['MOOT COURT DEPARTMENT'],
        'quote': 'In Moot Court We Meet, in Moot Court We Unite!',
        'logo_file': 'img/logo_mcd_cropped.png',
        'greeting_department': 'Moot Court',
        'welcome_department': 'Moot Court',
    },
    'lrc': {
        'department_name': 'LEGAL RESEARCH & COUNSELING DEPARTMENT',
        'title_lines': ['LEGAL RESEARCH & COUNSELING', 'DEPARTMENT'],
        'quote': 'We Research, We Share',
        'logo_file': 'img/logo_lrc_cropped.png',
        'greeting_department': 'LRC',
        'welcome_department': 'LRC',
    },
    'english': {
        'department_name': 'ENGLISH DEPARTMENT',
        'title_lines': ['ENGLISH DEPARTMENT'],
        'quote': 'In ALSA We Trust, In English We Crush, English Awesome!',
        'logo_file': 'img/logo_english_cropped.png',
        'greeting_department': 'English',
        'welcome_department': 'English',
    },
    'secretariat': {
        'department_name': 'SECRETARIAT DEPARTMENT',
        'title_lines': ['SECRETARIAT DEPARTMENT'],
        'quote': 'There is No Place Like Home, and Home is Secretariat',
        'logo_file': 'img/logo_secretariat_cropped.png',
        'greeting_department': 'Secretariat',
        'welcome_department': 'Secretariat',
    },
    'funding': {
        'department_name': 'FUNDING DEPARTMENT',
        'title_lines': ['FUNDING DEPARTMENT'],
        'quote': 'Money is Not Everything, But Everything Needs Money',
        'logo_file': 'img/logo_funding_cropped.png',
        'greeting_department': 'Funding',
        'welcome_department': 'Funding',
    },
}


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

        participant = PARTICIPANTS.get(nim)
        if participant and participant[0] == name:
            request.session['loading_allowed'] = True
            request.session['participant_name'] = name
            request.session['department'] = participant[1]
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
