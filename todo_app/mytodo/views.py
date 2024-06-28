from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .form import TaskForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        # 未完了のタスクを取得
        incomplete_tasks = Task.objects.filter(compile=False).order_by('start_date')
        # 完了したタスクを取得
        complete_tasks = Task.objects.filter(compile=True).order_by('start_date')
        
        context = {
            "incomplete_tasks": incomplete_tasks,
            "complete_tasks": complete_tasks
        }
        #テンプレートをレンタリング
        return render(request, "mytodo/index.html", context)
    
class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {'form' : form})
    
    def post(self, request, *args, **kwargs):
        #登録処理
        #入力データをフォームに渡す
        form = TaskForm(request.POST)
        #入力データに誤りがないかチェック
        is_valid = form.is_valid()
        
        # データが正常であれば
        if is_valid:
            #モデルに登録
            form.save()
            return redirect("/")
        
        #データが正常でなければ
        return render(request, "mytodo/add.html",{'form' : form})
    
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.compile = not task.compile
        task.save()

        return redirect('/')

class EditView(View):
    def get(self, request, task_id):
        # 編集するタスクを取得
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, "mytodo/edit.html", {'form': form, 'task': task})

    def post(self, request, task_id):
        # 編集するタスクを取得
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "mytodo/edit.html", {'form': form, 'task': task})
    
class DeleteView(View):
    def post(self, request, task_id):
        #削除するタスク所得
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')

    
        
        

#ビュークラス
index = IndexView.as_view()
add = AddView.as_view()
update_task_complete = Update_task_complete.as_view()
edit = EditView.as_view()
delete = DeleteView.as_view()