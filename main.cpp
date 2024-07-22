#include <iostream>
#include <string>

class CuentaBancaria {
private:
    std::string titular;
    double saldo;

public:
    CuentaBancaria(const std::string& titular, double saldoInicial) : titular(titular), saldo(saldoInicial) {}

    void depositar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
            std::cout << "Depósito exitoso. Nuevo saldo: " << saldo << std::endl;
        } else {
            std::cout << "Error: La cantidad a depositar debe ser mayor que cero." << std::endl;
        }
    }

    void retirar(double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            std::cout << "Retiro exitoso. Nuevo saldo: " << saldo << std::endl;
        } else {
            std::cout << "Error: Cantidad no válida o fondos insuficientes." << std::endl;
        }
    }

    void consultarSaldo() const {
        std::cout << "Saldo actual: " << saldo << std::endl;
    }

    void transferir(CuentaBancaria& cuentaDestino, double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            cuentaDestino.depositar(cantidad);
            std::cout << "Transferencia exitosa. Nuevo saldo: " << saldo << std::endl;
        } else {
            std::cout << "Error: Cantidad no válida o fondos insuficientes para transferir." << std::endl;
        }
    }

    void realizarPago(const std::string& concepto, double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            std::cout << "Pago de " << concepto << " realizado. Nuevo saldo: " << saldo << std::endl;
        } else {
            std::cout << "Error: Cantidad no válida o fondos insuficientes para realizar el pago." << std::endl;
        }
    }
};

int main() {
    // Crear una cuenta bancaria con un saldo inicial de 1000
    CuentaBancaria cuenta("Juan Perez", 1000.0);

    // Operaciones de prueba
    cuenta.depositar(500.0);
    cuenta.retirar(200.0);
    cuenta.consultarSaldo();

    // Crear otra cuenta bancaria
    CuentaBancaria cuentaDestino("Maria Gonzalez", 500.0);

    // Transferir 300 de una cuenta a otra
    cuenta.transferir(cuentaDestino, 300.0);

    // Realizar un pago desde la primera cuenta
    cuenta.realizarPago("Factura de electricidad", 50.0);

    return 0;
}
