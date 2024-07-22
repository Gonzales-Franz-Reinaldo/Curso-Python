public class CuentaBancaria {
    private String titular;
    private double saldo;

    public CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
            System.out.println("Depósito exitoso. Nuevo saldo: " + saldo);
        } else {
            System.out.println("Error: La cantidad a depositar debe ser mayor que cero.");
        }
    }

    public void retirar(double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            System.out.println("Retiro exitoso. Nuevo saldo: " + saldo);
        } else {
            System.out.println("Error: Cantidad no válida o fondos insuficientes.");
        }
    }

    public void consultarSaldo() {
        System.out.println("Saldo actual: " + saldo);
    }

    public void transferir(CuentaBancaria cuentaDestino, double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            cuentaDestino.depositar(cantidad);
            System.out.println("Transferencia exitosa. Nuevo saldo: " + saldo);
        } else {
            System.out.println("Error: Cantidad no válida o fondos insuficientes para transferir.");
        }
    }

    public void realizarPago(String concepto, double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            System.out.println("Pago de " + concepto + " realizado. Nuevo saldo: " + saldo);
        } else {
            System.out.println("Error: Cantidad no válida o fondos insuficientes para realizar el pago.");
        }
    }

    public static void main(String[] args) {
        // Crear una cuenta bancaria con un saldo inicial de 1000
        CuentaBancaria cuenta = new CuentaBancaria("Juan Perez", 1000.0);

        // Operaciones de prueba
        cuenta.depositar(500.0);
        cuenta.retirar(200.0);
        cuenta.consultarSaldo();

        // Crear otra cuenta bancaria
        CuentaBancaria cuentaDestino = new CuentaBancaria("Maria Gonzalez", 500.0);

        // Transferir 300 de una cuenta a otra
        cuenta.transferir(cuentaDestino, 300.0);

        // Realizar un pago desde la primera cuenta
        cuenta.realizarPago("Factura de electricidad", 50.0);
    }
}
