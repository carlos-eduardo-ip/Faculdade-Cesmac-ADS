package Cine_IP;

public class ingressoVIP extends Ingresso implements Lanchonete {

    private static int totalIngressos;

    public static void setTotalIngressos(int totalIngresso) {
        totalIngressos = totalIngresso;
    }

    @Override
    public void acessoCliente() {
        System.out.println("Lanchonete: Você possui acesso liberado da lanchonete!");
        double ingressosVIP = 64;
        System.out.println("Valor total a ser pago: R$ " + String.format("%.2f", totalIngressos*ingressosVIP));
    }
}
