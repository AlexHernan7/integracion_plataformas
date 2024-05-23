<template>
    <div style="padding-bottom: 100px;">
      <ListaProductos :productos="productos" @producto-seleccionado="handleProductoSeleccionado" style="padding-top: 50px;"/>
    </div>
</template>
  
<script>
 
import ListaProductos from '../components/ListaProductos';
import axios from 'axios';
export default {
  components: {
    ListaProductos 
  },
  data() {
    return {
      productos: [] 
    };
  },
  created() {
    this.obtenerProductos();
  },
  
  methods: {
    async obtenerProductos() {
      try {
        const response = await axios.get('/api/productos');
        this.productos = response.data;
      } catch (error) {
        console.error('Error al obtener los productos:', error);
      }
    }
  }
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
  width: 30%;
  height: 30%;
  display: flex;
  margin: auto;
}
p{
  margin-bottom: 0px;
}

</style>