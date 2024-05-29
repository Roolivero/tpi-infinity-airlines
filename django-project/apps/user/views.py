from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from rest_framework.generics import GenericAPIView
from .forms import UserForm
from .manager import UserManager

# class RegisterUserView(GenericAPIView):
#     serializer_class=UserRegisterSerializer

#     def post(self, request):
#         user_data=request.data
#         serializer=self.serializer_class(data=user_data)

#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             user=serializer.data
#             send_code_to_user(user['email'])
#             print(user)
#             return Response({
#                 'data': user,
#                 'message': f'hi, thanks for singing up'

#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserView:    
    def register_user(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                UserManager.create_user(request.data["email"], request.data["first_name"], request.data["last_name"], request.data["dni"], request.data["password"])
                messages.success(request, 'User registered successfully!')
                return redirect(reverse('register'))
        else:
            form = UserForm()
        return render(request, 'login.html', {'form': form})

#    def login_user(request):
#         if request.method == 'POST':
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email=email, password=password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse('search_fligth'))
#             else:
#                 messages.error(request, 'Invalid username or password')
#         return render(request, 'login.html')
        
