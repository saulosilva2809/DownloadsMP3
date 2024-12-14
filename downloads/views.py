from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdicionarMusicaForm
from .models import Musica
import pafy
import yt_dlp as youtube_dl
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def baixar_musica(request):
    if request.method == 'POST':
        form = AdicionarMusicaForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            nome_arquivo = form.cleaned_data['nome_arquivo']
            form.save()
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f'Musicas/musica_{nome_arquivo}.%(ext)s'
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messages.success(request, f'O download da música {nome_arquivo} ocorreu com sucesso!')
            return redirect('baixar_musica')
        else:
            messages.warning(request, 'Erro ao fazer o download')
            return redirect('baixar_musica')

    else:
        form = AdicionarMusicaForm()
    return render(request, 'baixar_musica.html', {'form': form})
