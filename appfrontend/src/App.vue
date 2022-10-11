<template>
  <nav>
    <h1>Mi Aplicacion de Capa de presentación</h1>
  </nav>
  
  <div class="principal">

  </div>
  
  <footer>
    <span>
      Derechos Reservados a Equipo 9 grupo 57/58.
    </span>
  </footer>
  
  <router-view/>
</template>

<script>
  import { tsImportEqualsDeclaration} from '@babel/types'

export default{
  name:'App',
  data: function(){
    return{

    }
  },
  methods:{

  },
  created: function(){
    
  }
}

</script>

<style>
  .principal{
    min-height: calc( 100vh - 120px );
  }

</style>
