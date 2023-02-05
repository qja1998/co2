from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

next_id = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is...'},
    {'id':2, 'title':'view', 'body':'Veiw is...'},
    {'id':3, 'title':'model', 'body':'Model is...'},
]

def html_template(article, id=None):
    global topics
    context_ui = ''
    if id != None:
        context_ui = f'''
            <li>
                <form action='/delete/' method='post'>
                    <input type='hidden' name='id' value={id}>
                    <input type='submit' value='delete'>
                </form>
            </li>
        '''
    ol = ''
    for topic in topics:
        ol += f"<li><a href='/read/{topic['id']}'>{topic['title']}<a/></li>"
    return f'''
    <html>
    <body>
        <h1><a href='/'>Django practice</a></h1>
        <ol>
            {ol}
        </ol>
        {article}
        <ul>
            <li><a href='/create/'>create</a></li>
            {context_ui}
        </ul>
    </body>
    </html>
    '''

# Create your views here.
# client로 데이터를 전송하기 위한 함수 작성
def index(request): # 첫 번째 인자는 요청과 관련된 여러 정보를 받아야 함
    article = '''
    <h2>Welcome</h2>
    Hello, django
    '''
    return HttpResponse(html_template(article)) # http로 응답할 것임

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f"<h2>{topic['title']}</h2>{topic['body']}"
    return HttpResponse(html_template(article, id))

@csrf_exempt
def create(request):
    if request.method == 'GET':
        article = '''
        <form action='/create/' method='post'>
            <p><input type='text' name='title' placeholder='title'></p>
            <p><textarea name='body' placeholder='body'></textarea></p>
            <p><input type='submit'></p>
        </form>
        '''
        return HttpResponse(html_template(article))
    elif request.method == 'POST':
        global next_id
        title = request.POST['title']
        body = request.POST['body']
        new_topic = {'id':next_id, 'title':title, 'body':body}
        url = f'/read/{next_id}'
        topics.append(new_topic)
        next_id += 1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        new_topics = []
        for topic in topics:
            if topic['id'] != int(id):
                new_topics.append(topic)
        topics = new_topics
        return redirect('/')