from django.shortcuts import render

features_list = [
        {
            'name': 'Keep track',
            'description': 'Keep track of your refuels and see how much you have spent on fuel.',
            'icon': 'bi bi-database'
        },
        {
            'name': 'Statistics',
            'description': 'See your refuel statistics in a graph.',
            'icon': 'bi bi-graph-up'
        },
        {
            'name': 'Compare',
            'description': 'Compare your refuels to others.',
            'icon': 'bi bi-people'
        },
        {
            'name': 'Share',
            'description': 'Share your refuels with others.',
            'icon': 'bi bi-share'
        },
        {
            'name': 'Export',
            'description': 'Export your refuels to a file.',
            'icon': 'bi bi-file-earmark-arrow-down'
        },
        {
            'name': 'Import',
            'description': 'Import your refuels from a file.',
            'icon': 'bi bi-file-earmark-arrow-up'
        },
    ]

def index(request):
    context = {
        'features': features_list
    }

    return render(request, 'index.html' , context=context)

def features(request):
    context = {
        'features': features_list
    }

    return render(request, 'features.html', context=context)