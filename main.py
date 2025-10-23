from IPAddress import IPAddress

# 1. Obtenção de entradas e criação do objeto
try:
    ip = list(map(int, input("Digite o endereço IP (ex: 192.168.1.10): ").split('.')))
    mask = list(map(int, input("Digite a máscara de sub-rede (ex: 255.255.255.0): ").split('.')))
    
    # 2. Instanciação da classe
    address = IPAddress(ip, mask)

    # 3. Cálculo de endereços
    network_address = address.networkAddressCalculator()
    broadcast_address = address.broadcastNetworkCalculator()

    # 4. Formatação da saída
    network_str = '.'.join(map(str, network_address))
    broadcast_str = '.'.join(map(str, broadcast_address))

    # 5. Cálculo do formato CIDR
    counter = sum(bin(octet).count('1') for octet in address.mask)

    print(f"\nEndereço de rede: {network_str}/{counter}")
    print(f"Endereço de broadcast: {broadcast_str}")

    # 6. Validação do IP
    validation = address.is_valid_host(network_address, broadcast_address)
    print(f"Validação: {'Válido' if validation else 'Inválido'}")

except ValueError:
    print("Entrada inválida. Certifique-se de que os endereços estão no formato correto.")