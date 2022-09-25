<template>
    <h1>Formulario de Login.</h1>
    <form v-on:submit.prevent="processLogInUser">
        <input type="text" v-model="user.username" placeholder="Ingrese el Nombre del Usuario: ">
        <br>
        <input type="password" v-model="user.password" placeholder="Ingrese la Contraseña: ">
        <br>
        <button type="submit">Ingresar</button>
    </form>

</template>

<script>
import axion from 'axios';

export default {

    name: "LogIn",

    data: function () {
        return {
            user: {
                username: "",
                password: ""
            }
        }
    },
    methods:{
        processLogInUser: function(){
            axios.post("url login",
            this.user,
            {headers:{}}
            )
            .then(
                (result)=>{
                    let dataLogin = {
                        username:this.user.username,
                        toke_acces: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit('completedLogIn',dataLogin);
                }
            )
            .catch((error)=>{
                if(error.response.status == "401"){
                    alert("! Error 401:: Usuario y/o Contraseña Incorrectos!.");
                }
            });
        }

    }
}
</script>

<style>

</style>