<template>
    <span>Bienvenido Sr(a): {{username}}</span>
</template>

<script>
    export default {
        name:"Home",
        data:function(){
            return{
                username: localStorage.getItem('username')||"none"
            }
        }
    }
</script>