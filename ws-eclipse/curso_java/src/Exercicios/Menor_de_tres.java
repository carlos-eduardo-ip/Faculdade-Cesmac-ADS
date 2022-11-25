package Exercicios;

import java.util.Scanner;

public class Menor_de_tres {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int menor;
        System.out.print("Primeiro Valor: ");
        int primeiro_valor = input.nextInt();

        System.out.print("Segundo valor: ");
        int segundo_valor = input.nextInt();

        System.out.print("Terceiro valor: ");
        int terceiro_valor = input.nextInt();

        if (primeiro_valor < segundo_valor) {
            menor = primeiro_valor;
        } else if (segundo_valor < terceiro_valor) {
            menor = segundo_valor;
        }else {
            menor = terceiro_valor;
        }

        System.out.print("Menor valor = "+ menor);
    }
}
