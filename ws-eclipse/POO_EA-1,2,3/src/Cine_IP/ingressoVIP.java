package Cine_IP;

public class ingressoVIP extends Ingresso{
    private double ingressosVIP = 64;
    private int totalIngressos;

    private void setTotalIngressos(int totalIngresso) {
        this.totalIngressos = totalIngresso;
    }

    public void selecaoFilmesVIP(boolean filmes){
        cliente.getfilmes(filmes);
        System.out.print("Selecione o filme pela númeração dele: ");
        setNumfilme(ler.nextInt());

        cliente.getsessoes();
        System.out.print("Agora escolha o número da sessão: ");
        setNumsessoes(ler.nextInt());

        System.out.print("\nAgora vamos escolher a quantidade de ingressos :D\n");
        System.out.print("\nDigite a quantidade ingressos VIP: ");
        setTotalIngressos(ler.nextInt());
    }



    @Override
    public void acessoCliente() {

        System.out.println("\nResumo do pedido: ");
        System.out.println("\nFilme escolhido: ");
        cliente.getfilme(Numfilme);
        System.out.println("\nA sua sessão será a " + getsessao(Numsessoes));
        System.out.println("Lanchonete: Você possui acesso liberado da lanchonete!");
        System.out.println("Valor total a ser pago: R$ " + String.format("%.2f", totalIngressos*ingressosVIP));
    }
}
