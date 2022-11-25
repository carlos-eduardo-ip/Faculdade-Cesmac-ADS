package Exercicios;

import java.util.ArrayList;
import java.util.Scanner;

public class Problama_soma_vetor {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar? ");
        int numeros = input.nextInt();

        double soma = 0;
        ArrayList<Double> lista = new ArrayList<>();
        for (int i = 0; i < numeros; i++) {
            System.out.print("Digite um número: ");
            lista.add(input.nextDouble());
            soma += lista.get(i);
        }

        System.out.print("Valores: ");
        for (int i = 0; i < lista.size(); i++) {
            System.out.print(lista.get(i)+" ");
        }
        System.out.print("\nSoma = "+soma);
        System.out.print("\nMedia = "+(soma/lista.size()));
    }
}
