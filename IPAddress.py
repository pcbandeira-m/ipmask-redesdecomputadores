class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask
    
   # CONVERSÃO DE INTEIRO PARA BINÁRIO
    def intForBin(self, ip):
        binaryIPV4 = []
        intBinaryIPV4 = []

        for octet in ip:
            binary = bin(octet)
            cleanedBinary = binary[2:]
            completedBinary = cleanedBinary.zfill(8)

            binaryIPV4.append(completedBinary)
        
        for binaries in binaryIPV4:
            binToInteger = int(binaries, 2)

            intBinaryIPV4.append(binToInteger)
            
        return intBinaryIPV4 # lista de inteiros

    # MÁSCARA INVERTIDA
    # Modificação: Remove os parâmetros 'mask'
    def invertedMask(self):
        invertedMask = []
        inversionFactor = 255  # 0b11111111 em decimal

        for i in range(4):
            xor = inversionFactor ^ self.mask[i]
            invertedMask.append(xor)

        return invertedMask

    # CÁLCULO DO ENDEREÇO DE REDE
    # Modificação: Remove os parâmetros 'ip' e 'mask'
    def networkAddressCalculator(self):
        networkAddress = []

        for i in range(4):
            # Usa self.ip e self.mask
            andResult = self.ip[i] & self.mask[i]
            networkAddress.append(andResult)

        return networkAddress

    # CÁLCULO DO ENDEREÇO DE BROADCAST
    # Modificação: Remove os parâmetros 'ip' e 'mask'
    def broadcastNetworkCalculator(self):
        # Usa o método interno da classe, referenciando-o com 'self'
        newMask = self.invertedMask()
        broadcastAddress = []

        for i in range(4):
            # Usa self.ip
            orResult = self.ip[i] | newMask[i]
            broadcastAddress.append(orResult)
        return broadcastAddress


    def is_valid_host(self, network_address, broadcast_address):
        # Esta lógica está incorreta para listas. A forma correta é comparar octeto por octeto.
        # Mas para fins de demonstração, vamos seguir uma lógica que funcione com listas.
        
        # O IP é válido se for maior ou igual ao endereço de rede
        # E menor ou igual ao endereço de broadcast.
        is_greater_equal_network = all(self.ip[i] >= network_address[i] for i in range(4))
        is_less_equal_broadcast = all(self.ip[i] <= broadcast_address[i] for i in range(4))
        
        return is_greater_equal_network and is_less_equal_broadcast