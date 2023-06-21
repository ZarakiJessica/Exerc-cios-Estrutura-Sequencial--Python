#Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe
# o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_internet_mbps = float(input("Digite a velocidade de um link de interner em Mbps: "))

tamanho_arquivo_bits = tamanho_arquivo_mb * 8 * 1024 * 1024  # Convertendo para bits
tempo_download_segundos = tamanho_arquivo_bits / (velocidade_internet_mbps * 1024 * 1024)
# Convertendo para Megabits

tempo_download_minutos = tempo_download_segundos / 60

print("Tempo aproximado de download:", tempo_download_minutos, "minutos")