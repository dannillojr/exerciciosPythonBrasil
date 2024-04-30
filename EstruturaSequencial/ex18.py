arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))
internet_mbps = float(input("Digite a velocidade da Internet em Mbps: "))

mbps_por_segundo = internet_mbps / 8
mb_por_segundo = mbps_por_segundo * 1024

tempo_download_segundos = arquivo_mb / mb_por_segundo

tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")
