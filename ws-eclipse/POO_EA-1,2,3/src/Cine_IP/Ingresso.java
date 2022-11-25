package Cine_IP;

public class Ingresso implements Lanchonete {

    private static double ingressosMeia = 16;
    private static double  ingressosInteiro = 32;

    public void setingressosMeia(int Ingressos){
        ingressosMeia *= Ingressos;
    }    public void setingressosInteiro(int Ingressos){
        ingressosInteiro *= Ingressos;
    }

    @Override
    public void acessoCliente() {
        System.out.println("Lanchonete: Seu ingresso não da acesso a lanchonete");
        System.out.println("Valor total a ser pago: R$ " + String.format("%.2f", ingressosInteiro + ingressosMeia));
    }
}
