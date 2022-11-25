package Exercicios;

import java.util.Scanner;


public class Countdown_time {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite o tempo a ser cronometrado em segundos: ");
        int tempo = input.nextInt();

        try {
            for (int i = 0; i < tempo; i++) {
                int segundos = i % 60;
                int minutos = (i / 60) % 60;
                int horas = i / 3600;

                Thread.sleep(1000);

                System.out.println(String.format("%02d:%02d:%02d", horas, minutos, segundos));


            }
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
