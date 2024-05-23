<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar navbar-dark bg-dark">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">Ferremas</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/productos">Productos</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/mensajeria">Contacto</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" aria-disabled="true">Nosotros</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view></router-view>
    
    <footer class="main-footer text-center fixed-bottom bg-light py-3">
    <strong>Copyright &copy; 2020-2024 Ferremas.</strong><br>
    Todos los derechos reservados.
</footer>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {

  }
}
</script>


<style>



</style>