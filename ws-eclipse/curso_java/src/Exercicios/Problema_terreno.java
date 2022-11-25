package Exercicios;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Problema_terreno {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.print("Digite a largura do terreno: ");
        double largura = leitor.nextDouble();

        System.out.print("Digite o comprimento do terreno: ");
        double comprimento = leitor.nextDouble();

        System.out.print("Digite o valor do metro quadrado: ");
        double valor_do_metro_quadrado = leitor.nextDouble();

        double area_terreno = largura * comprimento;
        System.out.println("Area do Terreno: "+ String.format("%.2f", area_terreno));

        double preco_do_terreno = area_terreno * valor_do_metro_quadrado;
        System.out.println("Preço do terreno: "+String.format("%.2f", preco_do_terreno));

    }
}
