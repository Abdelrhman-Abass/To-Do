from http.client import responses
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.http import Http404
from django.http.response import JsonResponse

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response 
from rest_framework import generics, mixins, viewsets
from .serializers import *

from django.views.generic.list import ListView
from django.views.generic.edit import  CreateView ,DeleteView ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import *
from .forms import AddForm


""" API sections """

class ALLTaskList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        guests = Task.objects.all()
        serializer = TaskSerializer(guests, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )          

class  UserTasks(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, username):
        try:
            return Task.objects.filter(user__username=username)
        except KeyError:
            raise Http404
    def get(self, request, username):
        guest = self.get_object(username)
        serializer = TaskSerializer(guest,many = True)
        return Response(serializer.data)

# class LoginView(TokenObtainPairView):
# 	"""
# 	Login View with jWt token authentication
# 	"""
# 	serializer_class = MyTokenObtainPairSerializer        


class TaskOperations(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get_object(self, pk):
        try:
            return Task.objects.filter(pk=pk)
        except KeyError:
            raise Http404
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = TaskSerializer(guest,many = True)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = TaskSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class AddBookView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = AddForm
    template_name = 'Home/add.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBookView, self).form_valid(form)



class Tasks(LoginRequiredMixin , ListView):
    model = Task
    template_name = 'Home/tasks.html'

    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(task_name__contains=search_input)

        context['search_input'] = search_input

        return context
        
class Done_Tasks(Tasks):
    template_name = 'Home/done.html'



class TaskUpdate(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = Task
    fields = ['task_name', 'status', 'discription','deadline']
    template_name = 'Home/update.html'
    # success_url = reverse_lazy('tasks')
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('edit', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user



class DeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    template_name = 'Home/delete.html'
    

    success_url = reverse_lazy('tasks')
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user    



class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        tasks = Task.objects.filter(user=user).order_by('-deadline')

        

        context = {
            'user': user,
            'profile': profile,
            'tasks': tasks,
        }

        return render(request, 'Home/profile.html', context)



class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth', 'picture']
    template_name = 'Home/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user        




 
