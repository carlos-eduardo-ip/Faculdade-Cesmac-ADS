package Cine_IP;

import java.util.Scanner;

public class MenuController {

    static Scanner ler = new Scanner(System.in);
    private static String Nome;

    public static void tela_Menu() {

        System.out.println("\nMenu Principal:");
        System.out.println("[1] - Ver filmes 2D em cartaz");
        System.out.println("[2] - Ver filmes 3D em cartaz");
        System.out.println("[3] - Comprar ingressos");
        System.out.println("[4] - Sair");
        System.out.print("Selecione a opção Desejada pelo número: ");
    }

    public static void tela_CompraDeIngresso() {
        Ingresso cliente;

        System.out.print("\nQual o tipo de ingresso que você deseja adquirir:\n [1] - VIP\n [2] - Comum\n Opção: ");
        int selecaoIngresso = ler.nextInt();


        if (selecaoIngresso == 1) {

            cliente = new ingressoVIP();
            ((ingressoVIP) cliente).selecaoFilmesVIP(true);

        }else{

            cliente = new Ingresso();
            cliente.selecaoFilmes2D(false);

        }

        cliente.acessoCliente();

    }

    public static void main(String[] args) {

        System.out.println("Seja Bem Vindo ao Cine IP!\n");
        System.out.print("Antes de tudo, vamos nos apresentar\n" + "Eu me chamo Bot IP e qual é o seu nome?  ");
        Nome = ler.nextLine();


        int opcao_Menu;
        do {

            tela_Menu();
            opcao_Menu = ler.nextInt();
            switch (opcao_Menu) {

                case 1:
                    Filmes.getfilmes(false);
                    try {Thread.currentThread().sleep(2000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    System.out.println("Voltaremos ao Menu em instantes.");
                    try {Thread.currentThread().sleep(1000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    System.out.println("Mais 1 segundo, assim você consegue escolher o seu filme.");
                    try {Thread.currentThread().sleep(1000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    break;
                case 2:
                    Filmes.getfilmes(true);
                    try {Thread.currentThread().sleep(2000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    System.out.println("Voltaremos ao Menu em instantes.");
                    try {Thread.currentThread().sleep(1000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    System.out.println("Mais 1 segundo, assim você consegue escolher o seu filme.");
                    try {Thread.currentThread().sleep(1000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    break;
                case 3:
                    tela_CompraDeIngresso();
                    try {Thread.currentThread().sleep(2000);} catch (InterruptedException e) {throw new RuntimeException(e);}
                    opcao_Menu = 4;
                    break;
                case 4:
                    break;
                default:
                    System.err.println("Essa opção não é válida, vamos tentar novamente :D");
            }
        } while (opcao_Menu != 4);
    }
}
