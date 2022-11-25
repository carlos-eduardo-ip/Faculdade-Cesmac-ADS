package Cine_IP;

public class Filmes{
    private static boolean filme3D;
    private static int Numfilme;
    private static int Numsessoes;

    private static String[][] filmes = {
                                 {"Nome: Adão Negro - 3D","Dirigido por Jaume Collet-Serra","Dotado dos poderes onipotentes dos deuses, Teth Adam está preso por 5.000 anos, passando de homem, mito, lenda: Adão Negro. Agora livre, um vingativo Adão Negro exerce seu senso único de justiça, nascido da raiva, mais uma vez...","Gênero: Ação - Aventura.","Duração: 125 min."},
                                 {"Nome: Harry Potter e a Câmara Secreta - 3D","Dirigido por Chris Columbus","Descrição: De férias na casa de seus tios Dursley, Harry Potter recebe a inesperada visita de Dobby, um elfo doméstico, que veio avisá-lo para não retornar à Escola de Magia de Hogwarts, pois lá correrá um grande perigo...","Gênero: Ação - Aventura - Fantasia.","Duração: 160 min."},
                                 {"Nome: Pantera Negra: Wakanda Para Sempre - 3D","Dirigido por Ryan Coogler","Descrição: A Rainha Ramonda, Shuri, M’Baku, Okoye e as Dora Milaje, lutam para proteger sua nação contra as potências mundiais intervenientes \nlogo após a morte do Rei T’Challa. Enquanto os Wakandanos se esforçam para aceitar este próximo capítulo, os heróis devem se unir com a ajuda \nda veterana guerreira Nakia e Everett Ross e forjar um novo caminho para o reino de Wakanda.","Gênero: Ação - Aventura","Duração: 161 min."},
                                 {"Nome: One Piece Film: Red","Dirigido por Gorô Taniguchi","Descrição: Luffy e sua equipe assistem a um show onde a cantora Uta não é outra senão a filha de Shanks.","Gênero: Animação - Aventura", "Duração: 115 min."},
                                 {"Nome: A Luz do Demônio","Dirigido por  Daniel Stamm","Descrição: Com relatos de possessões demoníacas alcançando números sem precedentes em todo o mundo, o Vaticano abre escolas para exorcismos em seis países, \nincluindo os Estados Unidos. A freira Ann acredita devotamente que realizar exorcismos é o seu chamado...","Gênero: Suspense - Terror.","Duração: 93 min."},
                                 {"Nome: Bardo, Falsa Crônica de Algumas Verdades","Dirigido por Alejandro Iñárritu","Descrição: BARDO acompanha um renomado jornalista e documentarista que, durante uma crise existencial, retorna à sua cidade natal,\nonde precisa se reconectar com sua família, memórias e sua própria identidade.","Gênero: Drama.","Duração: 159 min."}};

    public static void getfilmes(boolean tipoDoFilme) {
        System.out.println("\nEsses são os filmes que estão em cartaz: \n");
        filme3D = tipoDoFilme;

        if(filme3D == false) {
            for (int i = 0; i < 6; i++) {
                for (int j = 3; j < 6; j++) {
                    if (i == 0)
                        System.out.println("[" + (j+1) + "] - " + filmes[j][0].substring(6));
                }
            }
        }else{
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    if (i == 0)
                        System.out.println("[" + (j+1) + "] - " + filmes[j][0].substring(6));
                }
            }
        }
    }

    private static String[] sessoes = {"\nSessões disponível: \n", "Sala [01] - 18:30", "Sala [02] - 19:30", "Sala [03] - 20:30", "Sala [04] - 21:30","Sala [05] - 21:35"};


    public static void getsessoes() {
        for (int i = 0; i < sessoes.length; i++) {
            System.out.println(sessoes[i]);
        }
    }

    public static void setNumsessoes(int Numsessoe) {
        Numsessoes = Numsessoe;
    }

    public static String getsessao(){
        return sessoes[Numsessoes];
    }

    public static void getfilme() {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 5; j++) {
                if (i == 0)
                    System.out.println(filmes[Numfilme -1][j]);
            }
        }
    }

    public static void setNumfilme(int Numfilmes) {
        Numfilme = Numfilmes;
    }
}
