package Exercicios;

import java.util.ArrayList;
import java.util.Scanner;

public class Problema_negativo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar? ");
        int numeros = input.nextInt();

        ArrayList<Integer> lista = new ArrayList<>();

        for (int i = 0; i < numeros; i++) {
            System.out.print("Digite um número: ");
            lista.add(input.nextInt());

            }
        System.out.println("Numeros negativos: ");
        for (int j = 0; j < lista.size(); j++) {
            if (lista.get(j) < 0) {
                System.out.println(lista.get(j));
            }
        }
        }
    }
