<template>
    <div class="card-container">
      <div v-for="producto in productos" :key="producto.id" class="card" @click="seleccionarProducto(producto.id)">
        <div class="card-body">
          <img src="../assets/logo.png" class="imagenProd" alt="">
          <h5 class="card-title">{{ producto.name }}</h5>
          <p class="card-text">Categoria: {{ producto.categoria.name }}</p>
          <p class="card-text">Marca: {{ producto.marca }}</p>
          <p class="card-text">Stock: {{ producto.stock }}</p>
          <p class="card-text">
          Precio en CLP: {{
            (producto.precios[0].valor * valorDolar)
              .toLocaleString('es-ES', {
                style: 'currency',
                currency: 'CLP',
                minimumFractionDigits: 0,
                maximumFractionDigits: 0,
                useGrouping: true
              })
          }}
          </p>
          <button class="btn btn-success">Agregar</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '../axios.js';
  
  
  async function InfoApi() {
      const url = 'https://mindicador.cl/api/';
      const response = await fetch(url);
      const data = await response.json();
      const valor_dolar = data.dolar.valor;
      return valor_dolar;
  }
  
  InfoApi().then((valor) => {
      console.log(valor);
  });
  
  
  export default {
    data() {
      return {
        productos: [],
      };
    },
    created() {
      this.obtenerProductos();
      InfoApi().then((valor) => {
        this.valorDolar = valor; // Almacenar el valor del dólar en la propiedad valorDolar
      });
    },
    methods: {
      async obtenerProductos() {
    try {
      const response = await axios.get('productos/');
      console.log('Datos de productos:', response.data); // Verificar los datos recibidos
      this.productos = response.data;
    } catch (error) {
      console.error('Error al obtener los productos:', error);
    }
  },
      seleccionarProducto(id) {
        this.$emit('producto-seleccionado', id);
        
      },
    },
  };
  </script>
  
  <style scoped>
  .card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
  }
  
  .card {
    width: 350px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
    
  }
  
  .card-body {
    padding: 10px;
    
  }
  .imagenProd{
    width: 50%;
    height: 50%;
    display: flex;
    margin: auto;
  }
  p{
    margin-bottom: 0px;
  }
  
  </style>