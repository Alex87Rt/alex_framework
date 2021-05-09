from alex_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


class Work:
    def __call__(self, request):
        return '200 OK', render('work.html')


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
