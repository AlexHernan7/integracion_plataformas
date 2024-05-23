<template>
    <div>
      <h1>Lista de Productos</h1>
      <ul>
        <li v-for="producto in productos" :key="producto.id">{{ producto.nombre }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from '../axios.js'; // Importa la configuración de Axios
  
  export default {
    data() {
      return {
        productos: [],
      };
    },
    created() {
      this.obtenerProductos();
    },
    methods: {
      async obtenerProductos() {
        try {
          const response = await axios.get('productos/');
          this.productos = response.data;
        } catch (error) {
          console.error('Error al obtener los productos:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Agrega estilos aquí si es necesario */
  </style>