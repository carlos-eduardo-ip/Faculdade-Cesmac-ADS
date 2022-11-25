package Exercicios;

import java.util.Scanner;

public class Problema_salario {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        Pessoa pessoa1 = new Pessoa();
        Pessoa pessoa2 = new Pessoa();

        System.out.print("Digite o nome da primeira pessoa: ");
        pessoa1.nome = input.nextLine();

        System.out.print("Digite o salario da primeira pessoa: ");
        pessoa1.salario = input.nextDouble();

        System.out.print("Digite uma idade: ");
        pessoa1.idade = input.nextInt();

        System.out.print("Digite um sexo (F/M): ");
        pessoa1.genero = input.next().charAt(0);

        System.out.print("Digite o nome da segunda pessoa: ");
        input.nextLine();
        pessoa2.nome = input.nextLine();

        System.out.print("Digite o salario da segunda pessoa: ");
        pessoa2.salario = input.nextDouble();

        System.out.print("Digite uma idade: ");
        pessoa2.idade = input.nextInt();

        System.out.print("Digite um sexo (F/M): ");
        pessoa2.genero = input.next().charAt(0);

        pessoa1.apresentar();
        pessoa2.apresentar();

        input.close();
    }
}
