<template>
    <h1>Contacto</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="nombre_completo">Nombre Completo:</label>
        <input type="text" id="nombre_completo" v-model="nombre_completo" />
      </div>
      <div>
        <label for="motivo">Motivo:</label>
        <select id="motivo" v-model="motivo">
          <option value="felicitacion">Felicitación</option>
          <option value="reclamo">Reclamo</option>
          <option value="sugerencia">Sugerencia</option>
        </select>
      </div>
      <div>
        <label for="mensaje">Mensaje:</label>
        <textarea id="mensaje" v-model="mensaje"></textarea>
      </div>
      <button type="submit">Enviar</button>
    </form>
  </template>

<script>
import axios from 'axios';
export default {
    name: 'MensajeriaTienda',
    data(){
        return{
            nombre_completo:'',
            motivo: 'Felicitación',
            mensaje:'',
        };
    },
    methods: {
        async submitForm(){
            const payload = {
                nombre_completo: this.nombre_completo,
                motivo: this.motivo,
                mensaje: this.mensaje
            };
            try {
                const response = await axios.post('http://localhost:8000/api/contacto/', payload);
                console.log('Mensaje Enviado: ', response.data);
                this.nombre_completo = '';
                this.motivo = 'felicitaciones';
                this.mensaje = '';
                alert('Felicitaciones, tu mensaje fue enviado');
            }catch (error){
                console.error('Error al guardar el contacto: ', error);
                alert('Hubo un error al enviar el contacto');
                this.nombre_completo = '';
                this.motivo = 'felicitaciones';
                this.mensaje = '';
            }
        }
    }
};
</script>