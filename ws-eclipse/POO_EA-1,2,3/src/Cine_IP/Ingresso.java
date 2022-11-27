package Cine_IP;

import java.util.Scanner;

public class Ingresso implements Lanchonete {
    Scanner ler = new Scanner(System.in);

    protected int Numfilme;
    protected int Numsessoes;
    private static double ingressosMeia = 16;
    private static double  ingressosInteiro = 32;

    Filmes cliente = new Filmes();

    public void selecaoFilmes2D(boolean filmes){
        cliente.getfilmes(filmes);

        System.out.print("Selecione o filme pela númeração dele: ");
        setNumfilme(ler.nextInt());

        cliente.getsessoes();
        System.out.print("Agora escolha o número da sessão: ");
        setNumsessoes(ler.nextInt());

        System.out.print("\nAgora vamos escolher a quantidade de ingressos :D\n");
        System.out.println("Sendo inteiro R$ 32 e meia R$ 16");
        System.out.print("\nDigite a quantidade ingressos inteiro: ");
        setingressosInteiro(ler.nextInt());

        System.out.print("Digite a quantidade ingressos meia: ");
        setingressosMeia(ler.nextInt());

    }

    protected void setNumsessoes(int Numsessoe) {
        this.Numsessoes = Numsessoe;
    }

    public static String getsessao(int Numsessoes){
        return Filmes.sessoes[Numsessoes];
    }

    public void setNumfilme(int Numfilmes) {
        this.Numfilme = Numfilmes;
    }

    public void setingressosMeia(int Ingressos){
        ingressosMeia *= Ingressos;
    }    public void setingressosInteiro(int Ingressos){
        ingressosInteiro *= Ingressos;
    }

    @Override
    public void acessoCliente() {
        System.out.println("\nResumo do pedido: ");
        System.out.println("\nFilme escolhido: ");
        cliente.getfilme(Numfilme);
        System.out.println("\nA sua sessão será a " + getsessao(Numsessoes));
        System.out.println("Lanchonete: Seu ingresso não da acesso a lanchonete");
        System.out.println("Valor total a ser pago: R$ " + String.format("%.2f", ingressosInteiro + ingressosMeia));
    }
}
