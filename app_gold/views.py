from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random 	
# def index(request):
#     return render(request, 'index.html')

# Create your views here.

def begin_game(request):
    if 'gold' not in request.session:  #si no se hay variable de sesión se crea una
        request.session['gold'] = 0
        request.session['activities'] = "¡ Begin the Game !" + "\n"
        request.session['activities'] = ""
        # print(f"Inicio de Juego!!------{request.session['gold']} --------------")

    if request.session['gold'] < 0: #si el oro es menor que 0 se ha acabado el juego y se esconden los forms para evitar seguir jugando
        request.session['activities'] += (f"<div class='gameover'> You lose -------------GAME OVER------------- </div>")

        context = {'unhide_playagain': 'yes', 'unhide_reset': 'none'}
        return render(request, 'index.html' , context)

    context = {'unhide_playagain': 'none', 'unhide_reset': 'yes'}
    return render(request, 'index.html' , context) # si existe sesión y el oro es mayor o igual a 0 se sigue jugando


def process_money(request):
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")  
    
    if request.POST['site'] == "farm": # se se va a la granja
        print("farm")
        numero =  random.randint(10, 20) #probabilidad de ganar oro
        request.session['gold'] += numero
        request.session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the Farm! ({str(time)})</div>")

    if request.POST['site'] == "cave": # se se va a la cueva
        print("cave") 
        numero =  random.randint(5, 10)  #probabilidad de ganar oro
        request.session['gold'] += numero 
        request.session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the Cave! ({str(time)})</div>")

    if request.POST['site'] == "house": # se se va a la casa
        print("house") 
        numero =  random.randint(2, 5) #probabilidad de ganar oro
        request.session['gold'] += numero
        request.session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the House! ({str(time)})</div>")

    if request.POST['site'] == "casino": # se se va al casino
        print("casino")  
        numero =  random.randint(-50, 50) #probabilidad de ganar o perder oro
        request.session['gold'] += numero
        if numero<0: #si pierde oro
            request.session['activities'] += (f"<div class='red'>Entered a casino and lost {str(numero)} golds... Ouch..  ({str(time)})</div>")
        else: #si gana oro
            request.session['activities'] += (f"<div class='green'>Earned {str(numero)} gold from the Casino! ({str(time)})</div>")

    print(request.POST)
    print("*"*20)
  
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')