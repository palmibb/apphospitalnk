<template>
  <nav>
    <h1>Mi Aplicacion de Capa de presentación</h1>
    <button v-if="is_auth">Home</button>
    <button v-if="is_auth" v-on:click="LogOut">LogOut</button>
    <button v-if="!is_auth" v-on:click="loadLogIn">Login</button>
    <button v-if="!is_auth" v-on:click="loadSignUp">Registrar Usuario</button>
  </nav>

  <div class="principal">
    <router-view v-on:completedLogIn="completedLogIn" v-on:completedSignUp="completedSignUp">

    </router-view>

  </div>

  <footer class="footer">
    <span>
      Derechos Reservados a Equipo 9 grupo 57/58.
    </span>
  </footer>
</template>

<script>
import { tsImportEqualsDeclaration } from '@babel/types'

export default {
  name: 'App',

  data: function () {
    return {
      is_auth: false
    }
  },
  methods: {
    verifyAuth: function () {

      this.is_auth = localStorage.getItem('isAuth') || false;
      if (this.is_auth == false) {
        this.$router.push({ name: "logIn" })
      } else {
        this.$router.push({ name: "home" })
      }
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" })
    },
    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Ingresaste correctamente a la aplicación");
      this.verifyAuth();
    },
    completedSignUp: function (data) {

    },
    logOut: function () {
      localStorage.clear()
      alert("Sesión cerrada con éxito");
      this.verifyAuth();
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" })
    }

  },
  created: function () {
    this.verifyAuth()
  }
}

</script>

<style>
.principal {
  min-height: calc(100vh - 120px);
}

.footer {
  background-color: #f6f6fa;
  font-size: 12pt;
  padding: 12px 24px;
  font-family: Arial;
}
</style>
