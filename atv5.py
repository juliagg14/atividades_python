
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))


velocidade_internet_mbps = float(input("Digite a velocidade do link de internet em Mbps: "))


velocidade_internet_mbps_para_mbps = velocidade_internet_mbps / 8  # 1 Byte = 8 bits


tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps_para_mbps

tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")
