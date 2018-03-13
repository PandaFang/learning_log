from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
from learning_logs.models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        form = TopicForm()
    else:
        form  = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return HttpResponseRedirect('/topics/')

    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''添加新日记的页面'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()
            return redirect('/topic/' + str(topic.id))

    context = {'form':form, 'topic':topic}

    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('/topic/' + str(topic.id))
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'learning_logs/edit_entry.html', context)