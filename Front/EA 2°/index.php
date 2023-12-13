<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2ª Experiência de Aprendizagem</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <div class="login-box">
        <form action="" method="post">
            <h2>Faça o Login</h2>
            <div class="input-box">
                <span class="icon"><ion-icon name="person-circle"></ion-icon></span>
                <input type="email" name = "email"required>
                <label>E-mail</label>
            </div>
            <div class="input-box">
                <span class="icon"><ion-icon name="eye" id="olho"></ion-icon></ion-icon></span>
                <input type="password" id="password" name="password" required>
                <label>Senha</label>
            </div>
            <div class="button login">
                <button type="submit" name="login">Entrar</button>
            </div>
        </form>
        <form action="" method="post">
            <h2>Inscreva-se</h2>
            <div class="input-box">
                <span class="icon"><ion-icon name="person-circle"></ion-icon></span>
                <input type="text" name = "usuario"required>
                <label>Nome</label>
            </div>
            <div class="input-box">
                <span class="icon"><ion-icon name="person-circle"></ion-icon></span>
                <input type="email" name = "email"required>
                <label>E-mail</label>
            </div>
            <div class="input-box">
                <span class="icon" id="olho1"><ion-icon name="eye"></ion-icon></span>
                <input type="password" id="password1" name="password" required>
                <label>Senha</label>
            </div>
            <div class="button cadastro">
                <button type="submit" name="cadastro">Cadastre-se</button>
            </div>
        </form>
    </div>

    <script src="./js/Function.js"></script>

    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
</body>
</html>


<?php 

    session_start();    

    if (isset($_POST['email'], $_POST['password'])) {
        if ($_POST['email']=='teste@teste.com' && $_POST['password'] == 123) {
            $_SESSION['email'] = $_POST['email'];
            header('Location: painel.php');
        }
    }

    if (isset($_GET['erro'])) {
        echo "<div id='alert'>
        <span class='closebtn' onclick='closeFunction();'>&times;</span> 
        <strong>É necessário logar para acessar o sistema!</strong>
        </div>";
    }
?>