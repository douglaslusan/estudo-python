import Class as cls



conta1 = cls.Conta('douglas', 1)
conta2 = cls.Conta('Aline', 2)

conta1.Depositar(2000.00)
conta2.Depositar(2000.00)

print(conta1.Saldo())
print(conta2.Saldo())

conta2.Transferencia(conta1, 500)

print(conta1.Saldo())
print(conta2.Saldo())




