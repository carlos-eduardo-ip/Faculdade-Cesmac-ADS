package Exercicios;

import java.util.Scanner;

public class Problema_crescente {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite dois números: ");
        int x = input.nextInt();
        int y = input.nextInt();

        while (x != y){
            if (x < y) {
                System.out.println("CRESCENTE!");
            } else {
                System.out.println("DECRESCENTE!");
            }
            System.out.print("Digite outros dois números: ");
             x = input.nextInt();
             y = input.nextInt();
        }
    }
}
