import sys
from django import forms
from django.shortcuts import render
from django.http import HttpRequest as hr


class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(min_value=1, max_value=10)


tasks = []
status = False
msg = ""
title = "Tasks List"
# Create your views here.
def index(request):
    return render(
        request,
        "tasks/index.html",
        {"tasks": tasks, "title": title, "count": len(tasks)},
    )


def add(request):
    global status, msg
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            if len(tasks) > 0:
                status = True
                msg = "posted successfully!"
        else:
            msg = "Error!! Please try again!!!"
            return render(request, "", {"form": form, "status": False, "message": msg})
    return render(
        request,
        "tasks/add.html",
        {
            "title": title,
            "sub_title": "Add Task",
            "count": len(tasks),
            "status": status,
            "message": msg,
            "form": NewTasksForm(),
        },
    )
