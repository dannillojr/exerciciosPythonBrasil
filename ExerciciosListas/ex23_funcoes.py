def calcular_byte_para_megabyte(bytes):
    megabytes = bytes / (1024 ** 2)

    return megabytes

def calcular_percentual(valor_unitario, valor_total):
    porcentual = (valor_unitario/valor_total) * 100
    return porcentual