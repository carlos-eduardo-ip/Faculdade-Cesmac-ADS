package Exercicios;

import java.util.Scanner;

public class Problema_Aprovado {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Quantos Alunos serão digitados? ");
        int numeros = input.nextInt();

        String[] nomes = new String[numeros];
        double [] semestr1 = new double[numeros];
        double [] semestr2 = new double[numeros];

        for (int i = 0; i < numeros; i++) {
            System.out.print("Digite o nome do " + (i + 1) + "° aluno: ");
            input.nextLine();
            nomes[i] = input.nextLine();
            System.out.print("Nota do primeiro semestre: ");
            semestr1[i] = input.nextDouble();
            System.out.print("Nota do segundo semestre: ");
            semestr2[i] = input.nextDouble();
        }
        System.out.println("Alunos aprovados: ");

        for (int j = 0; j < numeros; j++) {
            if (((semestr1[j]+semestr2[j]) / 2) >= 6){
                System.out.println(nomes[j]);
            }
        }
    }
}
