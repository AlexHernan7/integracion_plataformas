<template>
    <div v-if="producto">
      <h2>Detalle del Producto</h2>
      <p><strong>Nombre:</strong> {{ producto.name }}</p>
      <p><strong>Descripción:</strong> {{ producto.descripcion }}</p>
      <!-- Agrega más detalles según sea necesario -->
    </div>
  </template>
  
  <script>
  import axios from '../axios.js';
  
  export default {
    props: ['productoId'],
    data() {
      return {
        producto: null,
      };
    },
    watch: {
      productoId: 'fetchProducto',
    },
    created() {
      this.fetchProducto();
    },
    methods: {
      async fetchProducto() {
        try {
          const response = await axios.get(`productos/${this.productoId}/`);
          this.producto = response.data;
        } catch (error) {
          console.error('Error al obtener el producto:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos para el componente DetalleProducto */
  </style>
  