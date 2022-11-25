package Exercicios;

class Pessoa {
    String nome;
    int idade;
    char genero;
    double salario, altura;
    void apresentar(){
        System.out.println("Nome : "+ nome);
        System.out.println("Salario : "+ String.format("%.2f", salario));
        System.out.println("Idade: "+ idade);
        System.out.println("Sexo: "+ genero);
    }


}
